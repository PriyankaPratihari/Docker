from pymongo import MongoClient
from script.config import DBConf
import xlsxwriter
from bson import ObjectId
MONGO_URI = DBConf.MONGO_URI
client = None
try:
    client = MongoClient(MONGO_URI)
    print("connected")
except Exception as e:
    print("default" + str(e))

# Creating database
db = client.interns_b2_23

# # Creating document
lib = db.priyanka_lib

cursor = lib.find({})
data = list(cursor)

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook('outputs.xlsx')
worksheet = workbook.add_worksheet()

# Write the header row
header = list(data[0].keys())
for col_num, field in enumerate(header):
    worksheet.write(0, col_num, field)

# Write the data rows
for row_num, row_data in enumerate(data, start=1):
    for col_num, value in enumerate(row_data.values()):
        if isinstance(value, ObjectId):
            value = str(value)  # Convert ObjectId to string
        worksheet.write(row_num, col_num, value)

# Save the workbook
workbook.close()