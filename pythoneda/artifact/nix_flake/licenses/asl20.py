"""
pythoneda/artifact/nix_flake/licenses/asl20.py

This file defines the Asl20 class.

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
from pythoneda.shared.nix_flake import License


class Asl20(License):

    """
    Represents the Apache Software license, 2.0

    Class name: Asl20

    Responsibilities:
        - Provide information about the ASL 2.0 license.

    Collaborators:
        - None
    """
    def __init__(self, copyrightYear: int, copyrightHolder: str, url: str):
        """
        Creates a new Asl20 instance.
        :param copyrightYear: The copyright year.
        :type copyrightYear: int
        :param copyrightHolder: The copyright holder.
        :type copyrightHolder: str
        :param url: The project url.
        :type url: str
        """
        super().__init__(
            f""" Apache License 2.0

 Copyright (C) {copyrightYear} {copyrightHolder} {url}

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
""",
        )

    @classmethod
    def id(self) -> str:
        """
        Retrieves the id of the license.
        :return: Such id.
        :rtype: str
        """
        return "asl20"
