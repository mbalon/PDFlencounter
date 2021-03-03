import pytest
import os
import pathlib
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm

from main import *


@pytest.fixture(autouse=True)
def run_around_tests():
    canvas_a4 = Canvas("A4.pdf", pagesize=(21 * cm, 29.7 * cm))
    canvas_a4.drawString(72, 72, "Hello, World")
    canvas_a5 = Canvas("A5.pdf", pagesize=(14.8 * cm, 21 * cm))
    canvas_a5.drawString(72, 72, "Hello, World")
    canvas_a4.save()
    canvas_a5.save()
    yield
    try:
        os.remove("A4.pdf")
        os.remove("A5.pdf")
    except FileNotFoundError:
        pass


def test_get_page_size_for_a4():
    path = str(pathlib.Path().absolute()) + r"\A4.pdf"

    output = get_page_size(path)

    assert output == [595.2756, 841.8898]


def test_get_page_size_for_a5():
    path = str(pathlib.Path().absolute()) + r"\A5.pdf"

    output = get_page_size(path)

    assert output == [419.5276, 595.2756]



