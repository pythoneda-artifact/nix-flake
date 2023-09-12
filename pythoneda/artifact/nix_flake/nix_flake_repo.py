"""
pythoneda/artifact/nix_flake/nix_flake_repo.py

This file defines the NixFlakeRepo class.

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
import abc
from pythoneda import Repo
from pythoneda.shared.nix_flake import NixFlake

class NixFlakeRepo(Repo, abc.ABC):

    """
    A repository for nix flakes.

    Class name: NixFlakeRepo

    Responsibilities:
        - Retrieves nix flakes based on certain criteria.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new NixFlakeRepo instance.
        """
        super().__init__()

    @abc.abstractmethod
    def latest_pythoneda_shared_pythoneda_domain(self):
        """
        Retrieves the latest version of the Nix flake for PythonEDA domain.
        :return: Such input.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaDomainNixFlake
        """
        pass

    @abc.abstractmethod
    def latest_pythoneda_shared_pythoneda_banner(self):
        """
        Retrieves the latest version of the Nix flake for PythonEDA banner.
        :return: Such input.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        pass

    @abc.abstractmethod
    def latest_Nixos(self):
        """
        Retrieves the latest version of the Nix flake for NixOS's nixpkgs.
        :return: Such input.
        :rtype: pythoneda.artifact.nix_flake.NixosNixFlake
        """
        pass

    @abc.abstractmethod
    def latest_FlakeUtils(self):
        """
        Retrieves the latest version of the Nix flake for FlakeUtils.
        :return: Such input.
        :rtype: pythoneda.artifact.nix_flake.FlakeUtilsNixFlake
        """
        pass

    @abc.abstractmethod
    def latest_Jupyterlab(self):
        """
        Retrieves the latest version of the Nix flake for Jupyterlab.
        :return: Such input.
        :rtype: pythoneda.artifact.nix_flake.jupyter.JupyterlabNixFlake
        """
        pass

    @abc.abstractmethod
    def resolve(self, spec:NixFlakeSpec) -> NixFlake:
        """
        Resolves given specification.
        :return: A compatible Nix flake, or None if none found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass
