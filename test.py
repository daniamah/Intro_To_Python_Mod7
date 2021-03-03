############################################################################################################
# Title: Assignment 07
# Description: Demonstrating Error Handling, Pickling and Unpickling
#
# ChangeLog (Who,When,What)
#           DaniaM,03.02.2021,Add script for Error Handling
#           DaniaM,03.01.2021,Add script for Pickling and Unpickling
#############################################################################################################

#Demonstarting Error Handling
'''
while True:
    try:
        phone_num = input("Enter phone number: ")
        if phone_num.isalpha() or phone_num == '':
            raise Exception("You must enter only numbers.")
        #name = input("Enter contact's name: ")

#Demonstrating pickling data
file_store = ""
print("Pickling Data")
file = open("Contacts.txt", 'wb')
pickle.dump(file_store, file)
file.close()
print("Pickling Complete")

#Demonstarting unpickling data
print("Unpickling the file")
file = open("Contacts.txt", 'rb')
data = pickle.load(file)
file.close()
print("Unpickling Complete, This is your Data: ", data)
---------------------------
'''
import pickle

#defining variables
lstTable =[]
choice = ""

# Load current data

try:
    objFile = open("Contacts.txt", "rb")
    FileData = pickle.load(objFile)
    for i in FileData:
        print(i["Name"] + " | " + i["Phone Number"])
    objFile.close()
    print("Successfully loaded file")
except FileNotFoundError as e:
    print("File not found")

#demonstarting error handling
while choice != 'x':
    try:
        strname = str(input('Enter Name of contact: '))
        if strname.isnumeric() == True:
            raise Exception("Only use alphabets for name \n")

        phone = str(input('Enter phone number: '))
        if phone.isalpha() == True:
            raise Exception("Only use digits for phone \n")

        dicRow = {"Name": strname, "Phone Number": phone}
        lstTable.append(dicRow)
    except Exception as e:
        print(e)

    try:
        choice = input("Type 'x' to exit or 'c' to continue ").lower()
        if choice not in ['x', 'c']:
            raise Exception("Only use 'x' to exit or 'c' to continue \n")
    except Exception as e:
        print( e, e.__doc__)

print("Here are your tasks pre-pickled:")
for i in lstTable:
    print(i["Name"] + " | " + i["Phone Number"])

print("Pickling tasks...")
objFile = open("Contacts.txt", "wb")
pickle.dump(lstTable, objFile)
objFile.close()

print("Data Unpickled! contacts below: ")
objFile = open("Contacts.txt", "rb")
FileData = pickle.load(objFile)
for i in FileData:
    print(i["Name"] + " | " + i["Phone Number"])
objFile.close()
