#!/usr/bin/env python3.5
import os
import time
from datetime import datetime

"""The purpose of the script is to generate a report of when was the time a DPR was updated."""

monthDict = {"1":"Jan", "2":"Feb", "3":"Mar", "4":"Apr", "5":"May", "6":"Jun", "7":"Jul", "8":"Aug", "9":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"}
todayMonth = datetime.now().month
todayMonth = monthDict[str(todayMonth)]
todayDate = str(datetime.now().day)
if len(todayDate) == 1:
    todayDate = "0" + todayDate


fileList = []
timeList = []
employeeCount = 0

catchFileList = []
catchTimeList = []

path = r"Z:\DPR\2017"  # Path to the DPR folder
dirs = os.listdir(path)
for folder in dirs:  # For every DPR in the folder extract last modified time
    folderpath = path + "\\" + str(folder)
    if os.path.isdir(folderpath):
        employeeCount += 1
        files = os.listdir(folderpath)
        for file in files:
            if str(file)[0] != "~" and "DPR_2017" in str(file):
                fileList.append(file)
                filepath = folderpath + "\\" + str(file)
                catchTime = time.ctime(os.stat(filepath).st_mtime)
                # When the date is in single digit
                if catchTime[8] == " ":
                    catchTime = catchTime[:8] + "0" + catchTime[9:]
                    catchTime = catchTime.replace(" ", ",")
                    timeList.append(catchTime)
                    day = catchTime[8:10]
                    month = catchTime[4:7]
                    if day != todayDate or  month != todayMonth:
                        catchFileList.append(str(file))
                        catchTimeList.append(catchTime)

                # when the date is not in single digit
                elif catchTime[8] != " ":
                    catchTime = catchTime.replace(" ", ",")
                    timeList.append(catchTime)
                    day = catchTime[8:10]
                    month = catchTime[4:7]
                    if day != todayDate or month != todayMonth:
                        catchFileList.append(str(file))
                        catchTimeList.append(catchTime)


result = dict(zip(fileList, timeList))
keyList = result.keys()
keyList = sorted(keyList)

catchResult = dict(zip(catchFileList, catchTimeList))
catchKeyList = catchResult.keys()
catchKeyList = sorted(catchKeyList)

# Error Report
if employeeCount == len(keyList):
    endLine = "All employees are accounted for"
else:
    endLine = "Someone has more than one copy of DPRs"

# Take user input
name = input("Please type your user name: ")

# Path of Report file to be created
try:
    csvPath = r"C:\Users\{}\Desktop\DPR Update Status.csv".format(name)
    f = open(csvPath, "w")
    # Header for the file
    updateTime = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    f.write("This is an auto generated DPR update report. It shows when was a DPR last updated." + "\n")
    f.write("This report was last generated on " + updateTime + "\n")
    f.write(endLine + "\n")
    f.write("Developed By : MSA R & D" + "\n")
    f.write("\n")
    # DPR report
    for key in keyList:
        line = key + "," + result[key]
        f.write(line + "\n")
    f.write("\n")
    f.write("*******************************************************" + "\n")
    f.write("\n")
    f.write("An Email to be sent to following people \n")
    f.write("\n")
    for key in catchKeyList:
        line = key + "," + catchResult[key]
        f.write(line + "\n")
    f.close()
    print("File written successfully! Yeah!")
except Exception as e:
    print("\n" + "Something is wrong! File was not written!" + "\n" + str(e))
