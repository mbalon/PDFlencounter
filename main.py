from PyPDF2 import PdfFileReader
from reportlab.lib.units import mm
from typing import List

path_name = r'C:\Users\balon\Desktop\kartkaSosin1.pdf'


def get_page_size(path):
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        page = pdf.getPage(0)
        return page["/MediaBox"][2:4]


def convert_size_to_mm(pt_size: List):
    return [float(size)/mm for size in pt_size]


page_size = get_page_size(path_name)
print(get_page_size(path_name))
print(convert_size_to_mm(page_size))
