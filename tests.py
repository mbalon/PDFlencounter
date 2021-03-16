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
    except FileNotFoundError:
        pass


def test_get_page_size_for_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"

    output = get_page_size(path)

    assert math.isclose(output[0], 21 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 29.7 * cm, rel_tol=0.0001, abs_tol=0.0)


def test_get_page_size_for_a5():
    path = str(pathlib.Path().absolute()) + r"\A5.pdf"

    output = get_page_size(path)

    assert math.isclose(output[0], 14.8 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 21 * cm, rel_tol=0.0001, abs_tol=0.0)


def test_get_page_size_for_297_2000():
    path = str(pathlib.Path().absolute()) + r"\297.pdf"

    output = get_page_size(path)

    assert math.isclose(output[0], 29.7 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 200 * cm, rel_tol=0.0001, abs_tol=0.0)


@pytest.mark.xfail
def test_get_page_size_fail_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"

    output = get_page_size(path)

    assert math.isclose(output[0], 555 * cm, rel_tol=0.0001, abs_tol=0.0)
    assert math.isclose(output[1], 777 * cm, rel_tol=0.0001, abs_tol=0.0)
