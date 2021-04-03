# In summary, the required conversions are as follows:
# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into MM/DD/YYYY format.
#  The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.

import os
import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


PyBoss_csv=os.path.join("Resources","Employee_data.csv")
file_to_output = os.path.join("Resources", "New_Employee_data.csv")
# "analysis/employee_data_reformatted2.csv"


Id=[]
First_name=[]
Last_name=[]
DOB=[]
SSN=[]
State=[]

with open(PyBoss_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    PyBoss_header=next(csvreader)

    for row in csvreader:
        Id.append(row[0])

        name=row[1].split()
        First_name.append(name[0])
        Last_name.append(name[1])

        yyyy_DOB=row[2].split('-')[0]
        mm_DOB=row[2].split('-')[1]
        dd_DOB=row[2].split('-')[2]
        DOB.append(dd_DOB+"/"+mm_DOB+"/"+yyyy_DOB)

        SSN.append('***-**-'+ row[3][-4:])

        State.append(us_state_abbrev[row[4]])


print(len(Id))
New_csv = zip(Id, First_name, Last_name, DOB, SSN, State)


with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(New_csv)