# python-challenge
Module 3 Challenge - PyBank : create a Python script that analyzes the records to calculate a list of values as well as PyPoll : create a Python script that analyzes the votes and calculates a list of values.
#PyBank lines 4-66 PyPoll lines 69-125
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join ("/Users/savirahiman/desktop/python_challenge/python-challenge/PyBank/Resources/budget_data.csv")

# Declare variables
total_months = []
total_profits = []
profit_changes = []


# Open the csv file
with open(csvpath) as csvfile:
csvreader = csv.reader (csvfile, delimiter= ",")
csv_reader = next(csvreader)

# Use loop to go through each row in the data set
for row in csvreader:

# Total number of months & profit/loss in data set
total_months.append(row[0])
total_profits.append(int (row[1]))

# Use loop to go throgh the profits to get the monthly change
for i in range (len(total_profits)-1):
profit_changes.append(total_profits[i+1]-total_profits[i])

# Get the min & max of the profit changes
max_increase = max(profit_changes) 
max_decrease = min(profit_changes) 

# Find the month that is represented by the min & max of the profit changes by using the index function
max_increase_month = profit_changes.index(max(profit_changes)) + 1
max_decrease_month = profit_changes.index(min(profit_changes)) + 1

#Print Statements
output = (f"Finanial Analysis\n"
f"----------------------------------------------\n"
f"Total Months: {len(total_months)}\n"
f"Total: ${sum(total_profits)}\n"
f"Average Change: ${round(sum(profit_changes)/len(profit_changes),2)}\n"
f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})\n"
f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})"
)
print (output )


# text files
output_file = ("/Users/savirahiman/Desktop/python_challenge/python-challenge/PyBank/analysis/Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:

file.write(f"Finanial Analysis")
file.write(f"----------------------------------------------")
file.write(f"Total Months: {len(total_months)} ")
file.write(f"Total: ${sum(total_profits)} ")

file.write(f"Average Change: ${round(sum(profit_changes)/len(profit_changes),2)} ")

file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))}) ")

file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))}) ")

#PyPoll lines 69-125
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join ("/Users/savirahiman/desktop/python_challenge/python-challenge/PyPoll/Resources/election_data.csv")



# Open the csv file
with open(csvpath) as csvfile:
csvreader = csv.reader (csvfile, delimiter= ",")
csv_reader = next(csvreader)
data = list(csvreader)
row_count = len(data)


# Create a list of canidates 
canidates = list()
tally = list()

# Use loop to go through each row of the data with array
for i in range (0,row_count):
canidate_name = data[i][2]
tally.append(canidate_name)
if canidate_name not in canidates: 
canidates.append(canidate_name)
canidate_count = len(canidates)


# Use another loop to go create a list of votes by canidates 
votes = list()
percentage = list()
for j in range (0, canidate_count):
name = canidates[j]
votes.append(tally.count(name))
votecount_per_canidate = votes[j]/row_count
percentage.append(votecount_per_canidate)
winner = votes.index(max(votes))



# Print Statements 
print (f"Election Results")
print (f"------------------------------------")
print (f"Total Votes: {row_count}")
print (f"------------------------------------")
for k in range (0,canidate_count):
print(f"{canidates[k]}: {percentage[k]: .3%} ({votes[k]:})")

output_file = ("/Users/savirahiman/Desktop/python_challenge/python-challenge/PyPoll/analysis/Election_Analysis_Summary.txt")

with open (output_file,"w") as file: 
file.write(f"Election Results ")
file.write(f"------------------------------------ ")
file.write(f"Total Votes: {row_count} ")
for k in range (0,canidate_count):
file.write(f"{canidates[k]}: {percentage[k]: .3%} ({votes[k]:}) ")