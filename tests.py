import pytest
import os
import pathlib
import math
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm

from main import *


def create_test_file(name: str, width: float, height: float):
    canvas = Canvas(name, pagesize=(round(width * cm, 4), round(height * cm, 4)))
    canvas.drawString(72, 72, "Hello World")
    canvas.save()
    return canvas


@pytest.fixture(autouse=True)
def run_around_tests():
    canvas_a4 = create_test_file("A4.pdf", 21, 29.7)
    canvas_a5 = create_test_file("A5.pdf", 14.8, 21)
    canvas_297 = create_test_file("297.pdf", 29.7, 200)
    yield
    try:
        os.remove("A4.pdf")
        os.remove("A5.pdf")
        os.remove("297.pdf")
        size_dict_box = {"A4": 0, "A3": 0, "A2": 0, "A1": 0, "A0": 0,
                         "B2": 0, "B1": 0, "B0": 0, "297": 0, "420": 0,
                         "610": 0, "707": 0, "841": 0, "914": 0, "1070": 0}
    except FileNotFoundError:
        pass


def test_get_page_size_for_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        num_page = pdf.getNumPages() - 1
        output = get_page_size(pdf, num_page)

    assert math.isclose(output[0], 21 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 29.7 * cm, rel_tol=0.0001, abs_tol=0.0)


def test_get_page_size_for_a5():
    path = str(pathlib.Path().absolute()) + r"\A5.pdf"

    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        num_page = pdf.getNumPages() - 1
        output = get_page_size(pdf, num_page)

    assert math.isclose(output[0], 14.8 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 21 * cm, rel_tol=0.0001, abs_tol=0.0)


def test_get_page_size_for_297_2000():
    path = str(pathlib.Path().absolute()) + r"\297.pdf"

    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        num_page = pdf.getNumPages() - 1
        output = get_page_size(pdf, num_page)

    assert math.isclose(output[0], 29.7 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 200 * cm, rel_tol=0.0001, abs_tol=0.0)


@pytest.mark.xfail
def test_get_page_size_fail_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"

    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        num_page = pdf.getNumPages() - 1
        output = get_page_size(pdf, num_page)

    assert math.isclose(output[0], 555 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 777 * cm, rel_tol=0.0001, abs_tol=0.0)


def test_convert_size_to_mm_a4():
    size_list = [21 * cm, 29.7 * cm]
    size_list_mm = convert_size_to_mm(size_list)

    assert size_list_mm == [210, 297]


def test_convert_size_to_mm_a5():
    size_list = [14.8 * cm, 21 * cm]
    size_list_mm = convert_size_to_mm(size_list)

    assert size_list_mm == [148, 210]


@pytest.mark.xfail
def test_convert_size_to_mm_a5_fail():
    size_list = [14.8 * cm, 21 * cm]
    size_list_mm = convert_size_to_mm(size_list)

    assert size_list_mm == [568, 454]


def test_change_size_list_to_main_key_a4():
    size_list = [210, 297]

    output = change_size_list_to_main_key(size_list)

    assert output == "A4"


def test_change_size_list_to_main_key_a3():
    size_list = [297, 420]

    output = change_size_list_to_main_key(size_list)

    assert output == "A3"


def test_change_size_list_to_main_key_b2():
    size_list = [500, 707]

    output = change_size_list_to_main_key(size_list)

    assert output == "B2"


def test_change_size_list_to_main_key_297():
    size_list = [297, 707]

    output = change_size_list_to_main_key(size_list)

    assert output == "297"


def test_change_size_list_to_main_key_a1():
    size_list = [841, 594]

    output = change_size_list_to_main_key(size_list)

    assert output == "A1"


def test_change_size_list_to_main_key_610():
    size_list = [850, 606]

    output = change_size_list_to_main_key(size_list)

    assert output == "610"


def test_assign_to_size_a4():
    size_key = "A4"
    mm_size = [210, 297]

    assign_to_size(size_key, mm_size)

    assert size_dict_box["A4"] == 1


def test_assign_to_size_297():
    size_key = "297"
    mm_size = [750, 297]

    assign_to_size(size_key, mm_size)

    assert size_dict_box["297"] == 750


def test_count_len_in_file_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"

    count_len_in_file(path)

    assert size_dict_box["A4"] == 2


