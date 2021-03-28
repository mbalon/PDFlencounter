from PyPDF2 import PdfFileReader
from reportlab.lib.units import mm
from typing import List
import math

size_dict_box = {"A4": 0, "A3": 0, "A2": 0, "A1": 0, "A0": 0,
                 "B2": 0, "B1": 0, "B0": 0, "297": 0, "420": 0,
                 "610": 0, "707": 0, "841": 0, "914": 0, "1070": 0}


def get_page_size(path):
    with open(path, 'rb') as file:
        pdf = PdfFileReader(file)
        page = pdf.getPage(0)
        return page["/MediaBox"][2:4]


def convert_size_to_mm(pt_size: List):
    return [round(float(size)/mm, 2) for size in pt_size]


def change_size_list_to_main_key(mm_size: List):
    small_size = min(mm_size)
    big_size = max(mm_size)
    if 206 < small_size < 214:
        if 293 < big_size < 301:
            return "A4"
    if small_size < 301:
        if 416 < big_size < 424 and 291 < small_size:
            return "A3"
        else:
            return "297"
    if small_size < 424:
        if 590 < big_size < 600 and 414 < small_size:
            return "A2"
        else:
            return "420"
    if small_size < 505:
        if 703 < big_size < 712 and 494 < small_size:
            return "B2"
    if small_size < 600:
        if 836 < big_size < 845 and 589 < small_size:
            return "A1"
        else:
            return "610"
    if 605 < small_size < 614:
        return "610"
    if small_size < 712:
        if 997 < big_size < 1004 and 701 < small_size:
            return "B1"
        else:
            return "707"
    if small_size < 845:
        if 1185 < big_size < 1194 and 835 < small_size:
            return "A0"
        else:
            return "841"
    if small_size < 918:
        return "914"
    if small_size < 1005:
        if 1408 < big_size < 1420 and 994 < small_size:
            return "B0"
        else:
            return "1070"
    if small_size < 1075:
        return "1070"
    else:
        return "key not found"


def assign_to_size(size_key: str, mm_size: List):
    dict_keys = size_dict_box.keys()
    if size_key == "key not found":
        return
    if size_key in dict_keys:
        if size_key in ["A4", "A3", "A2", "A1", "A0", "B2", "B1", "B0"]:
            size_dict_box[size_key] += 1
        else:
            size_dict_box[size_key] += max(mm_size)






