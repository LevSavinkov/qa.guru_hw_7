import os.path

PROJECT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
TMP_PATH = os.path.join(PROJECT_DIR_PATH, "tmp")
ARCHIVE_PATH = os.path.join(TMP_PATH, "test_archive.zip")

def get_path_to_file(file: str):
    return os.path.join(TMP_PATH, file)
