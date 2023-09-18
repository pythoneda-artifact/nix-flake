"""
pythoneda/artifact/nix_flake/nix_flake_package.py

This file declares the NixFlakePackage class.

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
from .nix_flake_repo import NixFlakeRepo
from pythoneda import listen, Event, EventEmitter, EventListener, Ports
from pythoneda.shared.code_requests import CodeRequest
from pythoneda.shared.artifact_changes.events import ChangeStagingCodeDescribed, ChangeStagingCodePackaged
from pythoneda.shared.nix_flake import NixFlake

class NixFlakePackage(EventListener):
    """
    A package for NixFlakes.

    Class name: NixFlakePackage

    Responsibilities:
        - Transforms a NixFlake into a runnable package.

    Collaborators:
        - pythoneda.artifact.nix_flake.NixFlake
    """

    _singleton = None

    def __init__(self):
        """
        Creates a new NixFlakePackage instance.
        """
        super().__init__()

    @classmethod
    def instance(cls):
        """
        Retrieves the singleton instance.
        :return: Such instance.
        :rtype: pythoneda.artifact.nix_flake.NixFlakePackage
        """
        if cls._singleton is None:
            cls._singleton = cls.initialize()

        return cls._singleton

    @classmethod
    @listen(ChangeStagingCodeDescribed)
    async def listen_ChangeStagingCodeDescribed(cls, event: ChangeStagingCodeDescribed):
        """
        Gets notified of a ChangeStagingCodeDescribed event.
        :param event: The event.
        :type event: pythoneda.shared.artifact_changes.events.ChangeStagingCodeDescribed
        """
        NixFlakePackage.logger().info(f"Received {type(event)}")
        nix_flake = cls.resolve_nix_flake(event.code_request)
        result = ChangeStagingCodePackaged(nix_flake, event.id)

        NixFlakePackage.logger().info(f"Emitting {type(result)}")
        await Ports.instance().resolve(EventEmitter).emit(result)
        return result

    @classmethod
    def resolve_nix_flake(cls, codeRequest: CodeRequest) -> NixFlake:
        """
        Resolves a NixFlake based on the code request specification.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :return: A compatible NixFlake.
        :rtype: pythoneda.shared.nix_flake.NixFlake
        """
        nix_flake_repo = Ports.instance().resolve(NixFlakeRepo)
        return nix_flake_repo.resolve(codeRequest.nix_flake_spec())
