# vim: set fileencoding=utf-8
"""
pythoneda/artifact/nix/flake/jupyterlab/jupyterlab_code_request_nix_flake_factory.py

This file defines the JupyterlabCodeRequestNixFlakeFactory class.

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
from pythoneda import BaseObject, Ports
from pythoneda.artifact.nix.flake import NixFlakeRepo
from pythoneda.shared.code_requests import PythonedaDependency
from pythoneda.shared.code_requests.jupyterlab import (
    JupyterlabCodeRequest,
    JupyterlabCodeRequestNixFlake,
)
from pythoneda.shared.nix.flake import NixFlakeSpec
from typing import Dict, List


class JupyterlabCodeRequestNixFlakeFactory(BaseObject):

    """
    A factory for Jupyterlab's Nix flakes.

    Class name: JupyterlabCodeRequestNixFlakeFactory

    Responsibilities:
        - Is able to build JupyterlabCodeRequestNixFlake instances.

    Collaborators:
        - pythoneda.shared.code_requests.jupyterlab.JupyterlabCodeRequestNixFlake
    """

    _singleton = None

    def __init__(self):
        """
        Creates a new JupyterlabCodeRequestNixFlake instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: Ports
        """
        if cls._singleton is None:
            cls._singleton = cls()

        return cls._singleton

    def create(self, codeRequest: JupyterlabCodeRequest, inputs: List):
        """
        Creates a new JupyterlabNixFlake instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.jupyterlab.JupyterlabCodeRequest
        :param inputs: The flake inputs.
        :type inputs: List[pythoneda.shared.nix.flake.NixFlake]
        :return: The Nix flake.
        :rtype: pythoneda.shared.nix.flake.NixFlake
        """
        return JupyterlabCodeRequestNixFlake(
            codeRequest,
            "latest",
            self.__class__.dependencies_to_inputs(inputs, codeRequest),
        )

    @classmethod
    def dependencies_to_inputs(
        cls, inputs: List, codeRequest: JupyterlabCodeRequest
    ) -> List:
        """
        Converts the dependencies of given code request to a list of NixFlake instances.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.JupyterlabCodeRequest
        :param inputs: The flake inputs.
        :type inputs: List[pythoneda.shared.nix.flake.NixFlake]
        :return: The list of NixFlake instances.
        :rtype: List[pythoneda.shared.nix.flake.NixFlake]
        """
        nix_flake_repo = Ports.instance().resolve(NixFlakeRepo)

        result = inputs
        pythonedaDependencies = [
            nix_flake_repo.latest_Nixos(),
            nix_flake_repo.latest_FlakeUtils(),
            nix_flake_repo.latest_PythonedaSharedPythonedaBanner(),
            nix_flake_repo.latest_Jupyterlab(),
        ]
        for dep in codeRequest.dependencies:
            deps = []
            if isinstance(dep, PythonedaDependency):
                deps = pythonedaDependencies
                if dep.name != "pythoneda-shared-pythoneda-domain":
                    deps.append(nix_flake_repo.latest_PythonedaSharedPythonedaDomain())
            resolved_flake = nix_flake_repo.resolve(
                NixFlakeSpec(dep.name, dep.version, dep.url)
            )
            if resolved_flake is None:
                JupyterlabCodeRequestNixFlakeFactory.logger().error(
                    f"Cannot resolve flake for {dep.name}-{dep.version}"
                )
            else:
                result.append(resolved_flake)
        return list(set(result))


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
