from typing import List
import openpyxl


def generateAvailabilityExcel(finalOpList: List[dict], excelDumpPath:str):
    wb = openpyxl.Workbook()
    sheet = wb.active
    currRowNo =2

    #setting column name
    sheet.cell(column=1, row=1, value= "Date")
    sheet.cell(column=2, row=1, value= "District_name")
    sheet.cell(column=3, row=1, value= "block_name")
    sheet.cell(column=4, row=1, value= "Address")
    sheet.cell(column=5, row=1, value= "Fee_type")
    sheet.cell(column=6, row=1, value= "Available_capacity")
    sheet.cell(column=7, row=1, value= "Available_capacity_dose1")
    sheet.cell(column=8, row=1, value= "Available_capacity_dose2")

    for centre in finalOpList:
        sheet.cell(column=1, row=currRowNo, value= centre["date"])
        sheet.cell(column=2, row=currRowNo, value= centre["district_name"])
        sheet.cell(column=3, row=currRowNo, value= centre["block_name"])
        sheet.cell(column=4, row=currRowNo, value= centre["address"])
        sheet.cell(column=5, row=currRowNo, value= centre["fee_type"])
        sheet.cell(column=6, row=currRowNo, value= centre["available_capacity"])
        sheet.cell(column=7, row=currRowNo, value= centre["available_capacity_dose1"])
        sheet.cell(column=8, row=currRowNo, value= centre["available_capacity_dose2"])
        currRowNo = currRowNo+1
    wb.save(filename=excelDumpPath + "/demo.xlsx")