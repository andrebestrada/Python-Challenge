# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

PyBank_csv = os.path.join("..","Resources", "Budget_data.csv")
PyBank_csv=("Resources\Election_data.csv")

Total_Vote=0
Khan_Votes=0
Correy_Votes=0
Li_Votes=0
O_Votes=0

candidates=["Khan", "Correy", "Li", "O Tooley"]
votes_count=[0,0,0,0]


with open(PyBank_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    PyBank_header=next(csvreader)

    for row in csvreader:
        Total_Vote=Total_Vote+1

        if row[2]=="Khan":
            index=0
            Khan_Votes=Khan_Votes+1
        elif row[2]== "Correy":
            index=1
            Correy_Votes=Correy_Votes+1
        elif row[2]=="O'Tooley":
            index=2
            O_Votes=O_Votes+1    
        elif row[2]=="Li":
            index=3
            Li_Votes=Li_Votes+1

        votes_count[index] +=1


Khan_Per=Khan_Votes/Total_Vote
Correy_Per=Correy_Votes/Total_Vote
O_VPer=O_Votes/Total_Vote
Li_Per=Li_Votes/Total_Vote


if Khan_Votes>Correy_Votes and Khan_Votes>O_Votes and Khan_Votes>Li_Votes: winner="Khan"
if Correy_Votes>Khan_Votes and Correy_Votes>O_Votes and Correy_Votes>Li_Votes: winner="Correy"
if O_Votes>Khan_Votes and O_Votes>Correy_Votes and O_Votes>Li_Votes: winner="O Tonney"
if Li_Votes>Khan_Votes and Li_Votes>Correy_Votes and Li_Votes>O_Votes: winner="Li"

Khan_Per="{:.3%}".format(Khan_Per)
Correy_Per="{:.3%}".format(Correy_Per)
Li_Per="{:.3%}".format(Li_Per)
O_VPer="{:.3%}".format(O_VPer)

# PRINTING RESULTS
print("Election Results")
print("---------------------")
print(f'Total Votes: {Total_Vote}')
print("---------------------")
print(f'Khan: {Khan_Per} ({Khan_Votes})')
print(f'Correy: {Correy_Per} ({Correy_Votes})')
print(f'Li: {Li_Per} ({Li_Votes})')
print(f'O Tooley: {O_VPer} ({O_Votes})')
print("---------------------")
print(f'Winner: {winner}')
print("---------------------")

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------

