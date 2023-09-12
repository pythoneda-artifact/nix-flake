"""
pythoneda/artifact/nix_flake/nix_flake_spec.py

This file defines the NixFlakeSpec class.

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
from pythoneda import primary_key_attribute, ValueObject

class NixFlakeSpec(ValueObject):

    """
    A specification for nix flakes.

    Class name: NixFlakeSpec

    Responsibilities:
        - Defines criteria for Nix flakes.

    Collaborators:
        - None
    """

    def __init__(self, name:str, url:str):
        """
        Creates a new NixFlakeSpec instance.
        """
        super().__init__()
        self._name = name
        self._url = url

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the name of the Nix flake.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def url(self) -> str:
        """
        Retrieves the url of the Nix flake.
        :return: Such url.
        :rtype: str
        """
        return self._url
