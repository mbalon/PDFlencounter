from PyPDF2 import PdfFileReader
from reportlab.lib.units import mm
from typing import List
import math


def get_page_size(path):
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        page = pdf.getPage(0)
        return page["/MediaBox"][2:4]


def convert_size_to_mm(pt_size: List):
    return [round(float(size)/mm, 2) for size in pt_size]






