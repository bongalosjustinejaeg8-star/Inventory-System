
from openpyxl import load_workbook
file=load_workbook("DatabaseCap.xlsx").active
Data = {}
for item, qty in file.iter_rows(min_row=2, values_only=1):
    


