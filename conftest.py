from zipfile import ZipFile

import pytest

from config import FILES
from path_config import get_path_to_file, ARCHIVE_PATH


@pytest.fixture(scope="session", autouse=True)
def create_zip_archive():
    with ZipFile(ARCHIVE_PATH, "w") as archive:
        for file in FILES:
            archive.write(get_path_to_file(file), arcname=file)


def _open_file_from_archive(archive, file):
    with ZipFile(archive) as arch:
        return arch.open(file)


@pytest.fixture()
def open_file_from_archive():
    return _open_file_from_archive
