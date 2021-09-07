import openpyxl

Wb = openpyxl.load_workbook("2020-06-14 - STOCK UPDATE.xlsx")
print(Wb.active.title)
Users_working_sheet = input("Enter sheet Name\n")
Changed_Users_working_sheet = Wb[Users_working_sheet]
