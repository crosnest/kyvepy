#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""Release automation script."""

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import tomli
from packaging.version import Version


ROOT = Path(__file__).parent.parent


class EnvCredentials:
    """Credentials from env variables."""

    @property
    def pypi_username(self) -> str:
        """Get PYPI username."""
        return os.environ.get("PYPI_USERNAME") or ""

    @property
    def pypi_password(self) -> str:
        """Get PYPI password."""
        return os.environ.get("PYPI_PASSWORD") or ""


class ReleaseTool:
    """Release helper tool."""

    def __init__(self, credentials: EnvCredentials) -> None:
        """Init release tool instance."""
        self._credentials = credentials

    def get_the_latest_release_version(self) -> Version:
        """Get release version from gihtub tags."""
        text = subprocess.check_output(
            "git ls-remote --tags origin", shell=True, text=True
        )
        tags = [i.split("\t")[1].strip() for i in text.splitlines()]
        tags = [
            i for i in tags if i.startswith("refs/tags/v") and not i.endswith("^{}")
        ]
        versions = [i.replace("refs/tags/v", "") for i in tags]
        return Version(versions[-1])

    def get_current_version(self) -> Version:
        """Get current code version."""
        text = (ROOT / "pyproject.toml").read_text()
        version = tomli.loads(text)["tool"]["poetry"]["version"]
        return Version(version)

    def do_we_need_to_release(self) -> bool:
        """Check is code version is newer than on github."""
        current_version = self.get_current_version()
        released_version = self.get_the_latest_release_version()
        return current_version > released_version

    def parse_history(self) -> Tuple[List, Dict]:
        """Parse HISTORY.md."""
        text = (ROOT / "HISTORY.md").read_text()
        versions = [Version(i) for i in re.findall("## ([^ \n]+)", text)]
        history = {
            Version(i[0]): i[2]
            for i in re.findall(
                r"^## ([^ ]+)\n?([^\n]+\n)?\n([^#]+)", text, re.DOTALL + re.M
            )
        }
        return versions, history

    def make_tag(self, current_version: Version) -> None:
        """Make git tag."""
        subprocess.check_call(
            f"git tag v{current_version} -m 'Release {current_version}'", shell=True
        )

    def push_tag(self, current_version) -> None:
        """Push tag to github."""
        subprocess.check_call(f"git push origin v{current_version}", shell=True)

    def make_release(self, current_version: Version, release_history: str) -> None:
        """Make release on Github."""
        subprocess.check_call(
            f"""gh release create v{current_version} --title "v{current_version}" --notes "{release_history}" """,
            shell=True,
        )

    def build_packages(self):
        """Build packages."""
        subprocess.check_call("poetry build", shell=True)

    def upload_packages(self):
        """Upload packages to PYPI."""
        result = subprocess.run(
            f"poetry publish --skip-existing --username {self._credentials.pypi_username} --password {self._credentials.pypi_password} --verbose",
            check=True,
            shell=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        if result.returncode != 0:
            raise RuntimeError("Upload pacakges failed!")

    def main(self):
        """Run release process."""
        current_version = self.get_current_version()
        latest_release_version = self.get_the_latest_release_version()

        print("Current version:", current_version)
        print("Latest release version:", latest_release_version)

        if current_version > latest_release_version:
            print("Current version is newer. good to go")
        else:
            print("Current version is not newer. exit")
            return

        _, histories = self.parse_history()
        if current_version not in histories:
            print("No history provided for release. exit")
            return

        print("\nRelease history:")
        print("-------------------")
        print(histories[current_version])
        print("-------------------")

        print("\nBuilding packages")
        self.build_packages()
        print("Packages built")

        print("\nUpload packages")
        self.upload_packages()
        print("Packages uploaded")

        print("\nMake tag")
        self.make_tag(current_version)
        print("Tag made")

        print("\nPush tag")
        self.push_tag(current_version)
        print("Tag pushed")

        print("\nMake release")
        self.make_release(current_version, release_history=histories[current_version])
        print("Release made." "")

        print("\nDONE")


if __name__ == "__main__":
    creds = EnvCredentials()
    ReleaseTool(creds).main()
