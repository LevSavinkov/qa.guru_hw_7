from zipfile import ZipFile

import pytest

from config import FILES
from path_config import get_path_to_file, ARCHIVE_PATH


@pytest.fixture(scope="session", autouse=True)
def create_zip_archive():
    with ZipFile(ARCHIVE_PATH, "w") as archive:
        for file in FILES:
            archive.write(get_path_to_file(file), arcname=file)
