import csv
import io
from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl import load_workbook

from path_config import ARCHIVE_PATH


def get_file_from_archive(archive, file):
    return ZipFile(archive).open(file)


def test_csv():
    with get_file_from_archive(ARCHIVE_PATH, "test_file_csv.csv") as csv_file:
        content = csv_file.read().decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        for index, row in enumerate(reader):
            if index == 2:
                assert row[2] == "Треугольник"


def test_pdf():
    with get_file_from_archive(ARCHIVE_PATH, "Python Testing with Pytest (Brian Okken).pdf") as pdf_file:
        reader = PdfReader(pdf_file)
        assert "Simple, Rapid, Effective, and Scalable" in reader.get_page(1).extract_text()


def test_xlsx():
    with get_file_from_archive(ARCHIVE_PATH, "file_example_XLSX_50.xlsx") as xslx_file:
        workbook = load_workbook(xslx_file)
        sheet = workbook.active
        assert sheet.cell(row=2, column=3).value == "Abril"
