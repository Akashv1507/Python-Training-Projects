from src.appConfig import getAppConfigDict
from src.createTbl import createTbl
from src.insertOneRecord import insertOneRecord
from src.insertMultipleRecord import  insertMultipleRecord
from src.fetchRecords import fetchRecords
from src.updateRecord import updateRecord
from src.deleteRecord import deleteRecord
from src.deleteMultipleUniqueRecord import deleteMultipleUniqueRecord

# doing CRUD operation , C=create, R= read, U=update, D= delete
appConfigDict =getAppConfigDict()

# createTbl(appConfigDict)

# val = ("one record", "BSC", "09", "A", "22")
# insertOneRecord(appConfigDict, val)

# values = [("multiple record 1", "MA", "19", "A", "322"),("multiple record 2", "BSC", "29", "B", "12")]
# insertMultipleRecord(appConfigDict, values)

# fetchRecords(appConfigDict, 25, "CE")

# updateRecord(appConfigDict, "Aman", "Msc")

# deleteRecord(appConfigDict, "Aman")

# delList =[("Akash",24),("Alisha",26),("Aman",28)]
# deleteMultipleUniqueRecord(appConfigDict, delList)




