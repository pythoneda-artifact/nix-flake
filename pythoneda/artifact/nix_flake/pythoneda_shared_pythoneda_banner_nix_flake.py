"""
pythoneda/artifact/nix_flake/pythoneda_shared_pythoneda_banner_nix_flake.py

This file defines the PythonedaSharedPythonedaBannerNixFlake class.

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
from .pythoneda_nix_flake import PythonedaNixFlake
from pythoneda import Ports

class PythonedaSharedPythonedaBanner(PythonedaNixFlake):

    """
    Nix flake for pythoneda-shared-pythoneda/banner.

    Class name: PythonedaSharedPythonedaBannerNixFlake

    Responsibilities:
        - Provides a way to build pythoneda-shared-pythoneda/banner.
        - Provides a way to run pythoneda-shared-pythoneda/banner.

    Collaborators:
        - pythoneda.shared.nix_flake.NixFlake
    """

    def __init__(self):
        """
        Creates a new PythonedaSharedPythonedaBannerNixFlake instance.
        :param version: The version.
        :type version: str
        """
        nix_flake_repo = Ports.instance().resolve(NixFlakeRepo)
        super().__init__(
            "pythoneda-shared-pythoneda-banner",
            version,
            f"github:pythoneda-shared-pythoneda/banner/{version}",
            [ nix_flake_repo.latest_Nixos(), nix_flake_repo.latest_FlakeUtils() ])
