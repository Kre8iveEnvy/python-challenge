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
output = (f"Financial Analysis\n"
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

    file.write(f"Financial Analysis")
   
    file.write(f"----------------------------------------------")
  
    file.write(f"Total Months: {len(total_months)}   ")
 
    file.write(f"Total: ${sum(total_profits)}   ")

    file.write(f"Average Change: ${round(sum(profit_changes)/len(profit_changes),2)}   ")

    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase))})   ")

    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease))})   ")

