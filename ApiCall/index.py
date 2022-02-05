from src.getVaccineAvailibilty import  getSessionsInDistrict


districtId = 395
dateStr = "06-02-2022"

sessions =getSessionsInDistrict(districtId, dateStr)
# get all the slots from all centres
for ele in sessions:
    print(ele['slots'])