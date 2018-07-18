#The task is to create a Python script that analyzes the records to calculate each of the following:
#  1.	The total number of months included in the dataset
#  2.	The total net amount of "Profit/Losses" over the entire period
#  3.	The average change in "Profit/Losses" between months over the entire period
#  4.	The greatest increase in profits (date and amount) over the entire period
#  5.	The greatest decrease in losses (date and amount) over the entire period

#Data is found in budget_data.csv file and it has two columns of data called:  
#Date and Revenue  (you must determine the Profit/Losses), this is incorrect instruction

import os
import csv

#set path for CSV file to be used
csvpath = "Resources/budget_data.csv"

# Lists to store data
Date = []
Revenue = []
Month_Cnt = 1
Net_Change = []
Change_value = []
Average_Change =[]
Month_GIncrease = []
Month_GDecrease = []
a = 0
b = 0


'''
# empty list
print(list())

# date string
DateString = 'Date'
print(list(DateString))
'''
# Open the CSV to read in the data
with open(csvpath, newline="") as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
        print(row)

        # 2. Determine the total net amount of "Profit/Losses" over the entire period and find
        # 1. Determine the total number of months included in the dataset
        
    a = row[1]
    if b == 0:
        break
    else:
        c = ((a - b) * -1)
        print(row)
    