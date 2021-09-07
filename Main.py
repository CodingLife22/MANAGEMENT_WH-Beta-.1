import openpyxl
from Dictionary import K

"""
Important comment
yellow = 2-5
green  =>5
red    =0-2

Red color code "FF240A"
Green color code "7EFF1F"
"""
SHEETNAME = "2020-06-14 - STOCK UPDATE.xlsx"
Wb = openpyxl.load_workbook(SHEETNAME)
print(Wb.sheetnames)
Need = input(
    """Enter: "packing"for Packing procisure or Enter "Value" to know value: """
)


def Value():
    pass


def packing():
    pass


# Users_working_sheet = input("Enter sheet Name\n")
# Sheet = Wb[Users_working_sheet]
# print(Sheet["C8"].value)
