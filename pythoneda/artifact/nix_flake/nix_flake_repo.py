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
from pythoneda.shared.code_requests import CodeRequest
from pythoneda.shared.code_requests.jupyter import JupyterlabCodeRequestNixFlake
from pythoneda.shared.nix_flake import FlakeUtilsNixFlake, NixFlake, NixFlakeSpec, NixosNixFlake, PythonedaSharedPythonedaBannerNixFlake, PythonedaSharedPythonedaDomainNixFlake
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
        :return: The Nix flakes for NixOS, FlakeUtils, pythoneda-shared-pythoneda/banner and pythoneda-shared-pythoneda/domain.
        :rtype: List[pythoneda.shared.nix_flake.NixFlake]
        """
        return [ self.latest_Nixos(), self.latest_FlakeUtils(), self.latest_PythonedaSharedPythonedaBanner(), self.latest_PythonedaSharedPythonedaDomain() ]

    def latest_PythonedaSharedPythonedaBanner(self) -> PythonedaSharedPythonedaBannerNixFlake:
        """
        Retrieves the latest version of the Nix flake for PythonEDA banner.
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        return self.find_PythonedaSharedPythonedaBanner_version(self.latest_PythonedaSharedPythonedaBanner_version())

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaBanner_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for PythonEDA banner.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaBanner_version(self, version:str) -> PythonedaSharedPythonedaBannerNixFlake:
        """
        Retrieves a specific version of the Nix flake for PythonEDA banner.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaBannerNixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaDomain(self) -> PythonedaSharedPythonedaDomainNixFlake:
        """
        Retrieves the latest version of the Nix flake for PythonEDA domain.
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaDomainNixFlake
        """
        return self.find_PythonedaSharedPythonedaDomain_version(self.latest_PythonedaSharedPythonedaDomain_version())

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaDomain_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for PythonEDA domain.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaDomain_version(self, version:str) -> PythonedaSharedPythonedaDomainNixFlake:
        """
        Retrieves a specific version of the Nix flake for PythonEDA domain.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.PythonedaSharedPythonedaDomainNixFlake
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
    def find_Nixos_version(self, version:str) -> NixosNixFlake:
        """
        Retrieves a specific version of the NixOS flake.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_FlakeUtils(self) -> FlakeUtilsNixFlake:
        """
        Retrieves the latest version of the Nix flake for FlakeUtils.
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.FlakeUtilsNixFlake
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
    def find_FlakeUtils_version(self, version:str) -> str:
        """
        Retrieves a specific version of the Nix flake for FlakeUtils.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.FlakeUtilsNixFlake
        """
        pass

    def latest_PythonedaSharedPythonedaInfrastructure(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-pythoneda/infrastructure.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedPythonedaInfrastructure_version(self.latest_PythonedaSharedPythonedaInfrastructure_version())

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-pythoneda/infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaInfrastructure_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-pythoneda/infrastructure.
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
        return self.find_PythonedaSharedPythonedaApplication_version(self.latest_PythonedaSharedPythonedaApplication_version())

    @abc.abstractmethod
    def latest_PythonedaSharedPythonedaApplication_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-pythoneda/application.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedPythonedaApplication_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-pythoneda/application.
        :param version: The version.
        :type version: str
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_PythonedaSharedGitShared(self) -> NixFlake:
        """
        Retrieves the latest version of the Nix flake for pythoneda-shared-git/shared.
        :return: Such flake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        return self.find_PythonedaSharedGitShared_version(self.latest_PythonedaSharedGitShared_version())

    @abc.abstractmethod
    def latest_PythonedaSharedGitShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-git/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedGitShared_version(self, version:str) -> NixFlake:
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
        return self.find_PythonedaSharedGitShared_version(self.latest_PythonedaSharedGitShared_version())

    @abc.abstractmethod
    def latest_PythonedaSharedNixFlakeShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-nix-flake/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedNixFlakeShared_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-nix-flake/shared.
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
        return self.find_PythonedaSharedArtifactChangesShared_version(self.latest_PythonedaSharedArtifactChangesShared_version())

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesShared_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-artifact-changes/shared.
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
        return self.find_PythonedaSharedArtifactChangesEvents_version(self.latest_PythonedaSharedArtifactChangesEvents_version())

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesEvents_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/events.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesEvents_version(self, version:str) -> NixFlake:
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
        return self.find_PythonedaSharedArtifactChangesEventsInfrastructure_version(self.latest_PythonedaSharedArtifactChangesEventsInfrastructure_version())

    @abc.abstractmethod
    def latest_PythonedaSharedArtifactChangesEventsInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-artifact-changes/events-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedArtifactChangesEventsInfrastructure_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-artifact-changes/events-infrastructure.
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
        return self.find_PythonedaSharedCodeRequestsShared_version(self.latest_PythonedaSharedCodeRequestsShared_version())

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsShared_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/shared.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsShared_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/shared.
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
        return self.find_PythonedaSharedCodeRequestsEvents_version(self.latest_PythonedaSharedCodeRequestsEvents_version())

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsEvents_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/events.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsEvents_version(self, version:str) -> NixFlake:
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
        return self.find_PythonedaSharedCodeRequestsEventsInfrastructure_version(self.latest_PythonedaSharedCodeRequestsEventsInfrastructure_version())

    @abc.abstractmethod
    def latest_PythonedaSharedCodeRequestsEventsInfrastructure_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for pythoneda-shared-code-requests/events-infrastructure.
        :return: Such version.
        :rtype: str
        """
        pass
    
    @abc.abstractmethod
    def find_PythonedaSharedCodeRequestsEventsInfrastructure_version(self, version:str) -> NixFlake:
        """
        Retrieves a specific version of the Nix flake for pythoneda-shared-code-requests/events-infrastructure.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
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
    def find_Jupyterlab_version(self, version:str) -> NixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab.
        :param version: The version.
        :type version: str
        :return: Such flake, or None if not found.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        pass

    def latest_Jupyterlab_for_code_requests(self, codeRequest:CodeRequest) -> JupyterlabCodeRequestNixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :return: Such flake.
        :rtype: pythoneda.artifact.nix_flake.jupyter.JupyterlabCodeRequestNixFlake
        """
        return self.find_Jupyterlab_for_code_requests_version(self.latest_Jupyterlab_for_code_requests_version(), codeRequest)

    @abc.abstractmethod
    def latest_Jupyterlab_for_code_requests_version(self) -> str:
        """
        Retrieves the version of the latest Nix flake for Jupyterlab for code requests.
        :return: Such version.
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def find_Jupyterlab_for_code_requests_version(self, version:str, codeRequest:CodeRequest) -> JupyterlabCodeRequestNixFlake:
        """
        Retrieves the latest version of the nix flake for Jupyterlab for code requests.
        :param version: The version.
        :type version: str
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :return: Such flake, or None if not found.
        :rtype: pythoneda.artifact.nix_flake.jupyter.JupyterlabCodeRequsetNixFlake
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

    def find_by_id(self, id:str) -> NixFlake:
        """
        Retrieves a flake by its id.
        :param id: The id.
        :type id: str
        """
        raise NotImplementedError("Not used for NixFlakes")

    def find_by_pk(self, id:str) -> NixFlake:
        """
        Retrieves a flake by its id.
        :param id: The id.
        :type id: str
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

    def delete(self, id: str):
        """
        Deletes an existing Entity.
        :param item: The entity.
        :type item: pythoneda.Entity
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def find_by_pk(self, pk: Dict):
        """
        Retrieves an entity matching a primary key filter.
        :param pk: The primary key values.
        :type pk: str
        :return: An instance of the EntityClass type, or None if none found.
        :rtype: pythoneda.Entity
        """
        raise NotImplementedError("Operation not available for NixFlakes")

    def list(self) -> List:
        """
        Retrieves all entities.
        :return: The list of all entities.
        :rtype: List[Entity]
        """
        raise NotImplementedError("Operation not available for NixFlakes")
