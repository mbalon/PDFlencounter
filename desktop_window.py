from tkinter import *
from tkinter import filedialog
from main import count_in_dir, size_dict_box


root = Tk()


def askDir():
    dirname = filedialog.askdirectory()
    entry_box.insert(END, dirname)


def compute():
    path = entry_box.get()
    count_in_dir(path)
    A4.set(size_dict_box["A4"])
    print(size_dict_box)


label_info_box = Label(root, text="Wskaż ścieżkę do folderu")
entry_box = Entry(root, width=50, borderwidth=5)
search_button = Button(text="...", command=askDir)
frame = Frame(root, bd=5, height=60, width=60)
compute_button = Button(text="Przelicz", padx=20, command=compute)
clear_button = Button(text="Wyczyść tabelę")

label_format = Label(root, text="Formaty ISO [szt.]")
label_rolls = Label(root, text="Szerokość rolki [m]")

A4 = StringVar()
A4.set("0")

label_A4 = Label(root, text="A4 - ")
label_A4_value = Label(root, textvariable=A4)
label_A3 = Label(root, text="A3 - ")
label_A3_value = Label(root, text=size_dict_box["A3"])
label_A2 = Label(root, text="A2 - ")
label_A2_value = Label(root, text=size_dict_box["A2"])
label_A1 = Label(root, text="A1 - ")
label_A1_value = Label(root, text=size_dict_box["A1"])
label_A0 = Label(root, text="A0 - ")
label_A0_value = Label(root, text=size_dict_box["A0"])
label_B2 = Label(root, text="B2 - ")
label_B2_value = Label(root, text=size_dict_box["B2"])
label_B1 = Label(root, text="B1 - ")
label_B1_value = Label(root, text=size_dict_box["B1"])
label_B0 = Label(root, text="B0 - ")
label_B0_value = Label(root, text=size_dict_box["B0"])

label_297 = Label(root, text="297 - ")
label_297_value = Label(root, text=size_dict_box["297"])
label_420 = Label(root, text="420 - ")
label_420_value = Label(root, text=size_dict_box["420"])
label_610 = Label(root, text="610 - ")
label_610_value = Label(root, text=size_dict_box["610"])
label_710 = Label(root, text="710 - ")
label_710_value = Label(root, text=size_dict_box["707"])
label_841 = Label(root, text="841 - ")
label_841_value = Label(root, text=size_dict_box["841"])
label_914 = Label(root, text="914 - ")
label_914_value = Label(root, text=size_dict_box["914"])
label_1070 = Label(root, text="1070 - ")
label_1070_value = Label(root, text=size_dict_box["1070"])

label_info_box.grid(row=0, column=0, sticky=W)
entry_box.grid(row=1, column=0, columnspan=2)
search_button.grid(row=1, column=2, columnspan=1)
frame.grid(row=2, column=0, rowspan=9, columnspan=2)
compute_button.grid(row=1, column=4)
clear_button.grid(row=2, column=4)

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
