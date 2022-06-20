from tkinter import *
from tkinter import filedialog
from main import count_in_dir, size_dict_box, convert_file_to_image, count_len_in_file


root = Tk()


def askDir():
    dirname = filedialog.askdirectory()
    entry_box.insert(END, dirname)

def set_value():
    A4.set(size_dict_box["A4"])
    A3.set(size_dict_box["A3"])
    A2.set(size_dict_box["A2"])
    A1.set(size_dict_box["A1"])
    A0.set(size_dict_box["A0"])
    B2.set(size_dict_box["B2"])
    B1.set(size_dict_box["B1"])
    B0.set(size_dict_box["B0"])

    roll_297.set(size_dict_box["297"])
    roll_420.set(size_dict_box["420"])
    roll_610.set(size_dict_box["610"])
    roll_710.set(size_dict_box["707"])
    roll_841.set(size_dict_box["841"])
    roll_914.set(size_dict_box["914"])
    roll_1070.set(size_dict_box["1070"])

def compute_simple():
    path = entry_box.get()
    count_in_dir(path, count_len_in_file)
    set_value()

def compute_with_flatten():
    path = entry_box.get()
    count_in_dir(path, convert_file_to_image)
    set_value()

def checkbox_selection():
    if flat_on.get() == 1:
        compute_with_flatten()
    else:
        compute_simple()


def clear():
    for key in size_dict_box.keys():
        size_dict_box[key] = 0

    set_value()
    entry_box.delete(0, 'end')


flat_on = IntVar()
flatten_check_box = Checkbutton(root, text='Spłaszcz', variable=flat_on, onvalue=1, offvalue=0, command=checkbox_selection)
label_info_box = Label(root, text="Wskaż ścieżkę do folderu")
entry_box = Entry(root, width=50, borderwidth=5, relief='flat')
search_button = Button(text="...", command=askDir)
frame = Frame(root, bd=5, height=60, width=60)

if flat_on.get() == 1:
    compute_button = Button(text="Przelicz", padx=20, command=compute_with_flatten)
else:
    compute_button = Button(text="Przelicz", padx=20, command=compute_simple)

clear_button = Button(text="Wyczyść tabelę", command=clear)

label_format = Label(root, text="Formaty ISO [szt.]")
label_rolls = Label(root, text="Szerokość rolki [m]")

A4 = StringVar()
A4.set("0")
A3 = StringVar()
A3.set("0")
A2 = StringVar()
A2.set("0")
A1 = StringVar()
A1.set("0")
A0 = StringVar()
A0.set("0")
B2 = StringVar()
B2.set("0")
B1 = StringVar()
B1.set("0")
B0 = StringVar()
B0.set("0")

label_A4 = Label(root, text="A4 - ")
label_A4_value = Label(root, textvariable=A4)
label_A3 = Label(root, text="A3 - ")
label_A3_value = Label(root, textvariable=A3)
label_A2 = Label(root, text="A2 - ")
label_A2_value = Label(root, textvariable=A2)
label_A1 = Label(root, text="A1 - ")
label_A1_value = Label(root, textvariable=A1)
label_A0 = Label(root, text="A0 - ")
label_A0_value = Label(root, textvariable=A0)
label_B2 = Label(root, text="B2 - ")
label_B2_value = Label(root, textvariable=B2)
label_B1 = Label(root, text="B1 - ")
label_B1_value = Label(root, textvariable=B1)
label_B0 = Label(root, text="B0 - ")
label_B0_value = Label(root, textvariable=B0)

roll_297 = StringVar()
roll_297.set("0")
roll_420 = StringVar()
roll_420.set("0")
roll_610 = StringVar()
roll_610.set("0")
roll_710 = StringVar()
roll_710.set("0")
roll_841 = StringVar()
roll_841.set("0")
roll_914 = StringVar()
roll_914.set("0")
roll_1070 = StringVar()
roll_1070.set("0")

label_297 = Label(root, text="297 - ")
label_297_value = Label(root, textvariable=roll_297)
label_420 = Label(root, text="420 - ")
label_420_value = Label(root, textvariable=roll_420)
label_610 = Label(root, text="610 - ")
label_610_value = Label(root, textvariable=roll_610)
label_710 = Label(root, text="710 - ")
label_710_value = Label(root, textvariable=roll_710)
label_841 = Label(root, text="841 - ")
label_841_value = Label(root, textvariable=roll_841)
label_914 = Label(root, text="914 - ")
label_914_value = Label(root, textvariable=roll_914)
label_1070 = Label(root, text="1070 - ")
label_1070_value = Label(root, textvariable=roll_1070)

label_info_box.grid(row=0, column=0, sticky=W)
entry_box.grid(row=1, column=0, columnspan=4)
search_button.grid(row=1, column=4, columnspan=1)
frame.grid(row=2, column=0, rowspan=9, columnspan=2)
compute_button.grid(row=1, column=5)
clear_button.grid(row=2, column=5)
flatten_check_box.grid(row=3, column=5)

label_format.grid(row=2, column=0, columnspan=2)
label_A4.grid(row=3, column=0, columnspan=1)
label_A4_value.grid(row=3, column=1, columnspan=1)
label_A3.grid(row=4, column=0, columnspan=1)
label_A3_value.grid(row=4, column=1, columnspan=1)
label_A2.grid(row=5, column=0, columnspan=1)
label_A2_value.grid(row=5, column=1, columnspan=1)
label_A1.grid(row=6, column=0, columnspan=1)
label_A1_value.grid(row=6, column=1, columnspan=1)
label_A0.grid(row=7, column=0, columnspan=1)
label_A0_value.grid(row=7, column=1, columnspan=1)
label_B2.grid(row=8, column=0, columnspan=1)
label_B2_value.grid(row=8, column=1, columnspan=1)
label_B1.grid(row=9, column=0, columnspan=1)
label_B1_value.grid(row=9, column=1, columnspan=1)
label_B0.grid(row=10, column=0, columnspan=1)
label_B0_value.grid(row=10, column=1, columnspan=1)

label_rolls.grid(row=2, column=2, columnspan=2)
label_297.grid(row=3, column=2, columnspan=1)
label_297_value.grid(row=3, column=3, columnspan=1)
label_420.grid(row=4, column=2, columnspan=1)
label_420_value.grid(row=4, column=3, columnspan=1)
label_610.grid(row=5, column=2, columnspan=1)
label_610_value.grid(row=5, column=3, columnspan=1)
label_710.grid(row=6, column=2, columnspan=1)
label_710_value.grid(row=6, column=3, columnspan=1)
label_841.grid(row=7, column=2, columnspan=1)
label_841_value.grid(row=7, column=3, columnspan=1)
label_914.grid(row=8, column=2, columnspan=1)
label_914_value.grid(row=8, column=3, columnspan=1)
label_1070.grid(row=9, column=2, columnspan=1)
label_1070_value.grid(row=9, column=3, columnspan=1)

root.mainloop()
