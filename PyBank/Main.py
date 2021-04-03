# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

PyBank_csv = os.path.join("..","Resources", "Budget_data.csv")
PyBank_csv=("Resources\Budget_data.csv")

Total_Months=0
Total_Amount=0
Average_Change=0
Change_Sum=0
Great_Increase=0
Great_Decrease=0

Change=[]

with open(PyBank_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    PyBank_header=next(csvreader)
    last_value=867884
    
    # print(int(x))
    # value=csvreader[0]
    # first=next(PyBank_header)
    # print(first)

    for i in csvreader:
        Total_Months= Total_Months+1
        Total_Amount=Total_Amount + int(i[1])
        Change=int(i[1])-last_value
        Change_Sum=Change_Sum+Change

        if Change > Great_Increase: 
            Great_Increase=Change
            Date_Increase=i[0]            
        if Change < Great_Decrease: 
            Great_Decrease=Change
            Date_Decrease=i[0]

        # Change[rows]=int(rows[1])-int(last_value)
        # print(Change)

        last_value=int(i[1])



Average_Change=Change_Sum/(Total_Months-1)
Average_Change="{:.2f}".format(Average_Change)

# PRINTING RESULTS
print("Financial Analysis")
print("---------------------")
print(f'Total Months: {Total_Months}')
print(f'Total : {Total_Amount}')
print(f'Average Change: {Average_Change}')
print(f'Greatest Increase in Profits: {Date_Increase} ({Great_Increase})')
print(f'Greatest Decrease in Profits: {Date_Decrease} ({Great_Decrease})')

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
