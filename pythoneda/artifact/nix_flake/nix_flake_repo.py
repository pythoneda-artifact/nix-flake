# vim: set fileencoding=utf-8
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
from pythoneda.shared import Repo
from pythoneda.shared.code_requests import CodeExecutionNixFlake, CodeRequest
from pythoneda.shared.code_requests.jupyterlab import JupyterlabCodeRequestNixFlake
from pythoneda.shared.nix_flake import (
    FlakeUtilsNixFlake,
    NixFlake,
    NixFlakeSpec,
    NixosNixFlake,
    PythonedaSharedPythonedaBannerNixFlake,
    PythonedaSharedPythonedaDomainNixFlake,
)
from typing import Dict, List


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
        super().__init__(NixFlake)

    def default_latest_flakes(self) -> List:
        """
        Retrieves the latest Nix flakes for the default packages.
        :return: The Nix flakes for NixOS, FlakeUtils, pythoneda-shared-pythoneda/banner
        and pythoneda-shared-pythoneda/domain.
        :rtype: List[pythoneda.shared.nix_flake.NixFlake]
        """
        return [
            self.latest_Nixos(),
            self.latest_FlakeUtils(),
            self.latest_PythonedaSharedPythonedaBanner(),
            self.latest_PythonedaSharedPythonedaDomain(),
        ]

    def latest_Cachetools(self) -> NixFlake:
        """
        Retrieves the latest Nix flake for grpcio.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Cachetools_version(self.latest_Cachetools_version())

    @abc.abstractmethod
    def latest_Cachetools_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for grpcio.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Cachetools_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for cachetools.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_DbusNext(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for dbus-next.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_DbusNext_version(self.latest_DbusNext_version())

    @abc.abstractmethod
    def latest_DbusNext_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for dbus-next.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_DbusNext_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for dbus-next.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Dulwich(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for dulwich.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Dulwich_version(self.latest_Dulwich_version())

    @abc.abstractmethod
    def latest_Dulwich_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for dulwich.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Dulwich_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for dulwich.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    @abc.abstractmethod
    def latest_code_execution(self, codeRequest: CodeRequest) -> CodeExecutionNixFlake:
        """
        Retrieves the latest version of the nix flake for executing code.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :return: Such flake.
        :rtype: pythoneda.shared.code_requests.CodeExecutionNixFlake
        """
        pass

    def latest_FlakeUtils(self) -> FlakeUtilsNixFlake:
        """
        Retrieves the latest version of the Nix flake for FlakeUtils.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.FlakeUtilsNixFlake
        """
        return self.find_FlakeUtils_version(self.latest_FlakeUtils_version())

    @abc.abstractmethod
    def latest_FlakeUtils_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for FlakeUtils.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_FlakeUtils_version(self, version: str) -> str:
        """
        Retrieves a specific version of the Nix flake for FlakeUtils.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.FlakeUtilsNixFlake
        """
        pass

    def latest_GitPython(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for GitPython.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_GitPython_version(self.latest_GitPython_version())

    @abc.abstractmethod
    def latest_GitPython_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for GitPython.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_GitPython_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for GitPython.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Grpcio(self) -> NixFlake:
        """
        Retrieves the latest Nix flake for grpcio.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Grpcio_version(self.latest_Grpcio_version())

    @abc.abstractmethod
    def latest_Grpcio_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for grpcio.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Grpcio_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for grpcio.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Joblib(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for Joblib.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Joblib_version(self.latest_Joblib_version())

    @abc.abstractmethod
    def latest_Joblib_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for Joblib.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Joblib_version(self, version: str) -> str:
        """
        Retrieves a specific version of the Nix flake for Joblib.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    @abc.abstractmethod
    def latest_Jupyterlab_for_code_requests(
        self, codeRequest: CodeRequest
    ) -> JupyterlabCodeRequestNixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :return: Such flake.
        :rtype: pythoneda.shared.code_requests.jupyter.JupyterlabCodeRequestNixFlake
        """
        pass

    def latest_Jupyterlab(self) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Jupyterlab_version(self.latest_Jupyterlab_version())

    @abc.abstractmethod
    def latest_Jupyterlab_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for Jupyterlab.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Jupyterlab_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_Nbformat(self) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for nbformat.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Nbformat_version(self.latest_Nbformat_version())

    @abc.abstractmethod
    def latest_Nbformat_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for nbformat.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Nbformat_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for nbformat.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_Nixos(self) -> NixosNixFlake:
        """
        Retrieves the latest version of the NixOS flake.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Nixos_version(self.latest_Nixos_version())

    @abc.abstractmethod
    def latest_Nixos_version(self) -> str:
        """
        Retrieves the version of the latest NixOS flake.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Nixos_version(self, version: str) -> NixosNixFlake:
        """
        Retrieves a specific version of the NixOS flake.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_Paramiko(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for paramiko.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Paramiko_version(self.latest_Paramiko_version())

    @abc.abstractmethod
    def latest_Paramiko_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for paramiko.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Paramiko_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for paramiko.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactCodeRequestApplication(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/code-request-application
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactCodeRequestApplication_version(
            self.latest_PythonedaArtifactCodeRequestApplication_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactCodeRequestApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/code-request-application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactCodeRequestApplication_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/code-request-application
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactCodeRequestInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/code-request-infrastructure
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactCodeRequestInfrastructure_version(
            self.latest_PythonedaArtifactCodeRequestInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactCodeRequestInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/code-request-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactCodeRequestInfrastructure_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/code-request-infrastructure
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactGit(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/git
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactGit_version(
            self.latest_PythonedaActifactGit_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactGit_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/git.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactGit_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/git
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactGitApplication(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/git-application
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactGitApplication_version(
            self.latest_PythonedaActifactGitApplication_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactGitApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/git-application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactGitApplication_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/git-application
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactGitInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/git-infrastructure
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactGitInfrastructure_version(
            self.latest_PythonedaActifactGitInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactGitInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/git-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactGitInfrastructure_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/git-infrastructure
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactNixFlake(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/nix-flake
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactNixFlake_version(
            self.latest_PythonedaActifactNixFlake_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactNixFlake_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/nix-flake.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactNixFlake_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/nix-flake
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactNixFlakeApplication(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/nix-flake-application
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactNixFlakeApplication_version(
            self.latest_PythonedaActifactNixFlakeApplication_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactNixFlakeApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/nix-flake-application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactNixFlakeApplication_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/nix-flake-application
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaArtifactNixFlakeInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-artifact/nix-flake-infrastructure
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaArtifactNixFlakeInfrastructure_version(
            self.latest_PythonedaActifactNixFlakeInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaArtifactNixFlakeInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-artifact/nix-flake-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaArtifactNixFlakeInfrastructure_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-artifact/nix-flake-infrastructure
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaRealmRydnrApplication(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-realm-rydnr/application.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaRealmRydnrApplication_version(
            self.latest_PythonedaRealmRydnrApplication_version()
        )

    @abc.abstractmethod
    def latest_PythonedaRealmRydnrApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-realm-rydnr/application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaRealmRydnrApplication_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-realm-rydnr/application
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaRealmRydnrInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-realm-rydnr/infrastructure.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaRealmRydnrInfrastructure_version(
            self.latest_PythonedaRealmRydnrInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaRealmRydnrInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-realm-rydnr/infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaRealmRydnrInfrastructure_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-realm-rydnr/infrastructure
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaRealmRydnrRealm(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-realm-rydnr/realm.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaRealmRydnrRealm_version(
            self.latest_PythonedaRealmRydnrRealm_version()
        )

    @abc.abstractmethod
    def latest_PythonedaRealmRydnrRealm_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-realm-rydnr/realm.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaRealmRydnrRealm_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-realm-rydnr/realm
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedArtifactChangesEvents(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-artifact-changes/events.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedArtifactChangesEvents_version(
            self.latest_PythonedaSharedArtifactChangesEvents_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesEvents_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/events.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesEvents_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-artifact-changes/events.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedArtifactChangesEventsInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-artifact-changes/events-infrastructure.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedArtifactChangesEventsInfrastructure_version(
            self.latest_PythonedaSharedArtifactChangesEventsInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesEventsInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/events-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesEventsInfrastructure_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-artifact-changes/events-infrastructure.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedArtifactChangesShared(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-artifact-changes/shared.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedArtifactChangesShared_version(
            self.latest_PythonedaSharedArtifactChangesShared_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesShared_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-artifact-changes/shared.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedCodeRequestsEvents(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-code-requests/events.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedCodeRequestsEvents_version(
            self.latest_PythonedaSharedCodeRequestsEvents_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsEvents_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/events.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsEvents_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/events.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedCodeRequestsEventsInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-code-requests/events-infrastructure.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedCodeRequestsEventsInfrastructure_version(
            self.latest_PythonedaSharedCodeRequestsEventsInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsEventsInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/events-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsEventsInfrastructure_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/events-infrastructure.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedCodeRequestsJupyterlab(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-code-requests/jupyterlab.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedCodeRequestsJupyterlab_version(
            self.latest_PythonedaSharedCodeRequestsJupyterlab_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsJupyterlab_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/jupyterlab.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsJupyterlab_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/jupyterlab.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedCodeRequestsShared(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-code-requests/shared.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedCodeRequestsShared_version(
            self.latest_PythonedaSharedCodeRequestsShared_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsShared_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/shared.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedGitShared(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-git/shared.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedGitShared_version(
            self.latest_PythonedaSharedGitShared_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedGitShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-git/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedGitShared_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-git/shared.
        :param version: The version.
        :type version: str
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedNixFlakeShared(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-nix-flake/shared.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedGitShared_version(
            self.latest_PythonedaSharedGitShared_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedNixFlakeShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-nix-flake/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedNixFlakeShared_version(self, version: str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-nix-flake/shared.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaApplication(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-pythoneda/application.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedPythonedaApplication_version(
            self.latest_PythonedaSharedPythonedaApplication_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-pythoneda/application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaApplication_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-pythoneda/application.
        :param version: The version.
        :type version: str
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaBanner(
        self,
    ) -> PythonedaSharedPythonedaBannerNixFlake:
        """
        Retrieves the latest version of the Nix flake for PythonEDA banner.
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        return self.find_PythonedaSharedPythonedaBanner_version(
            self.latest_PythonedaSharedPythonedaBanner_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaBanner_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for PythonEDA banner.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaBanner_version(
        self, version: str
    ) -> PythonedaSharedPythonedaBannerNixFlake:
        """
        Retrieves a specific version of the Nix flake for PythonEDA banner.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaDomain(
        self,
    ) -> PythonedaSharedPythonedaDomainNixFlake:
        """
        Retrieves the latest version of the Nix flake for PythonEDA domain.
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaDomainNixFlake
        """
        return self.find_PythonedaSharedPythonedaDomain_version(
            self.latest_PythonedaSharedPythonedaDomain_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaDomain_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for PythonEDA domain.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaDomain_version(
        self, version: str
    ) -> PythonedaSharedPythonedaDomainNixFlake:
        """
        Retrieves a specific version of the Nix flake for PythonEDA domain.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaDomainNixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-pythoneda/infrastructure.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedPythonedaInfrastructure_version(
            self.latest_PythonedaSharedPythonedaInfrastructure_version()
        )

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-pythoneda/infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaInfrastructure_version(
        self, version: str
    ) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-pythoneda/infrastructure.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_Requests(self) -> NixFlake:
        """
        Retrieves the latest Nix flake for requests.
        :return: Such version.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Requests_version(self.latest_Requests_version())

    @abc.abstractmethod
    def latest_Requests_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for requests.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Requests_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for requests.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Semver(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for semver.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Semver_version(self.latest_Semver_version())

    @abc.abstractmethod
    def latest_Semver_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for semver.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Semver_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for semver.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Stringtemplate3(self) -> NixFlake:
        """
        Retrieves the latest Nix flake for stringtemplate3.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Stringtemplate3_version(self.latest_Stringtemplate3_version())

    @abc.abstractmethod
    def latest_Stringtemplate3_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for stringtemplate3.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Stringtemplate3_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for stringtemplate3.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    def latest_Unidiff(self) -> NixFlake:
        """
        Retrieves the latest Nix flake for unidiff.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_Unidiff_version(self.latest_Unidiff_version())

    @abc.abstractmethod
    def latest_Unidiff_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for unidiff.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Unidiff_version(self, version: str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for unidiff.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.NixFlake
        """
        pass

    @abc.abstractmethod
    def resolve(self, spec: NixFlakeSpec) -> NixFlake:
        """
        Resolves given specification.
        :return: A compatible Nix flake, or None if none found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def find_by_id(self, idValue: str) -> NixFlake:
        """
        Retrieves a flake by its id.
        :param idValue: The id.
        :type idValue: str
        """
        raise NotImplementedError("Not used for NixFlakes")

    def find_by_pk(self, idValue: str) -> NixFlake:
        """
        Retrieves a flake by its id.
        :param idValue: The id.
        :type idValue: str
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def find_by_attribute(self, attributeName: str, attributeValue: str):
        """
        Retrieves the flakes matching given attribute criteria.
        :param attributeName: The name of the attribute.
        :type attributeName: str
        :param attributeValue: The name of the attribute.
        :type attributeValue: str
        :return: The instances of the EntityClass matching given criteria, or an empty list if none found.
        :rtype: List[pythoneda.Entity]
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def filter(self, dictionary: Dict):
        """
        Retrieves the entities matching given criteria.
        :param dictionary: The filter.
        :type dictionary: Dict
        :return: The instances of the EntityClass matching given criteria, or an empty list if none found.
        :rtype: List[pythoneda.Entity]
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def insert(self, item):
        """
        Persists a new Entity.
        :param item: The entity.
        :type item: pythoneda.Entity
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def update(self, item):
        """
        Updates an existing Entity.
        :param item: The entity.
        :type item: pythoneda.Entity
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def delete(self, idValue: str):
        """
        Deletes an existing Entity.
        :param idValue: The identifier of the entity.
        :type idValue: pythoneda.Entity
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def list(self) -> List:
        """
        Retrieves all entities.
        :return: The list of all entities.
        :rtype: List[Entity]
        """
        raise NotImplementedError("Operation not available for NixFlakes")
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
