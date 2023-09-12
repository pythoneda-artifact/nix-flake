"""
pythoneda/artifact/nix_flake/pythoneda_nix_flake.py

This file defines the PythonedaNixFlake class.

Copyright (C) 2023-today rydnr's pythoneda-artifact/nix-flake

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from datetime import datetime
from path import Path
from pythoneda import attribute
from .flake_utils_input import FlakeUtilsInput
from .nix_flake import NixFlake
from .nix_flake_input import NixFlakeInput
from .nixos_2305_input import Nixos2305Input
from .pythoneda_shared_pythoneda_banner_input import PythonedaSharedPythonedaBannerInput
from .pythoneda_shared_pythoneda_domain_input import PythonedaSharedPythonedaDomainInput
from typing import List

class PythonedaNixFlake(NixFlake):

    """
    Represents a Nix flake of a PythonEDA project.

    Class name: PythonedaNixFlake

    Responsibilities:
        - Model a Nix flake for PythonEDA.
        - Knows how to run itself.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """
    def __init__(
            self,
            name:str,
            version:str,
            inputs:List,
            description:str,
            homepage:str,
            archRole:str,
            pescioSpace:str,
            hexagonalLayer:str):
        """
        Creates a new NixFlake instance.
        :param name: The name of the flake.
        :type name: str
        :param version: The version of the flake.
        :type version: str
        :param inputs: The inputs.
        :type inputs: List[pythoneda.shared.nix_flake.NixFlakeInput]
        :param description: The flake description.
        :type description: str
        :param homepage: The project's homepage.
        :type homepage: str
        :param archRole: The architectural role. See pythoneda.application.ArchitecturalRole.
        :type archRole: str
        :param pescioSpace: The Pescio space. See pythoneda.application.PescioSpace.
        :type pescioSpace: str
        :param hexagonalLayer: The type of hexagonal layer. See pythoneda.application.HexagonalLayer.
        :type hexagonalLayer: str
        """
        nix_flake_repo = Ports.instance().resolve(NixFlakeRepo)
        aux_inputs = [ nix_flake_repo.latest_Nixos(), nix_flake_repo.latest_FlakeUtils(), nix_flake_repo.latest_PythonedaSharedPythonedaBanner() ]
        if name != 'pythoneda-shared-pythoneda-domain':
            aux_inputs.append(nix_flake_repo.latest_PythonedaSharedPythonedaDomain())
        super().__init__(
            name,
            version,
            list(set(inputs) | set(aux_inputs)),
            "pythoneda",
            description,
            homepage,
            "gpl3",
            [ "rydnr <github@acm-sl.org>" ],
            datetime.now().year,
            "rydnr")
        self._arch_role = archRole
        self._pescio_space = pescioSpace
        self._hexagonal_layer = hexagonalLayer

    @classmethod
    def empty(cls):
        """
        Builds an empty instance. Required for unmarshalling.
        :return: An empty instance.
        :rtype: pythoneda.ValueObject
        """
        return cls(None, None, [], None, None, None, None, None)

    @property
    @attribute
    def package_inputs(self) -> List:
        """
        Retrieves the inputs of the package.
        :return: Such collection.
        :rtype: List
        """
        return [input for input in self._inputs if not isinstance(input, Nixos2305Input) and not isinstance(input, FlakeUtilsInput) ]

    @property
    @attribute
    def arch_role(self) -> str:
        """
        Retrieves the architectural role. See pythoneda.application.ArchRole.
        :return: Such information.
        :rtype: str
        """
        return self._arch_role

    @property
    @attribute
    def pescio_space(self) -> str:
        """
        Retrieves the Pescio space. See pythoneda.application.PescioSpace.
        :return: Such information.
        :rtype: str
        """
        return self._pescio_space

    @property
    @attribute
    def hexagonal_layer(self) -> str:
        """
        Retrieves which hexagonal layer the project represents. See pythoneda.application.HexagonalLayer.
        :return: Such information.
        :rtype hexagonalLayer: str
        """
        return self._hexagonal_layer

    def generate_files(self, flakeFolder: str):
        """
        Generates the files.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.generate_flake(flakeFolder)
        self.generate_pyprojecttoml_template(flakeFolder)

    def generate_pyprojecttoml_template(self, flakeFolder:str):
        """
        Generates the pyprojecttoml.template from a template. Yes, a template generates another template.
        :param flakeFolder: The flake folder.
        :type flakeFolder: str
        """
        self.process_template(flakeFolder, "PyprojecttomlTemplate", Path(self.templates_folder()) / self.template_subfolder, "root", "pyprojecttoml.template")

    def git_add_files(self, gitAdd):
        """
        Adds the generated files to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        self.git_add_flake(gitAdd)
        self.git_add_pyprojecttoml_template(gitAdd)

    def git_add_pyprojecttoml_template(self, gitAdd):
        """
        Adds the generated pyprojecttoml.template file to git.
        :param gitAdd: The GitAdd instance.
        :type gitAdd: pythoneda.shared.git.GitAdd
        """
        gitAdd.add("pyprojecttoml.template")
