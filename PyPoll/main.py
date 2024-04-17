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
print (f"------------------------------------")
print (f"Winner: {canidates[winner]}")

output_file = ("/Users/savirahiman/Desktop/python_challenge/python-challenge/PyPoll/analysis/Election_Analysis_Summary.txt")

with open (output_file,"w") as file: 
    file.write(f"Election Results   ")
    file.write(f"------------------------------------   ")
    file.write(f"Total Votes: {row_count}   ")
    for k in range (0,canidate_count):
     file.write(f"{canidates[k]}: {percentage[k]: .3%} ({votes[k]:})   ")
    file.write(f"------------------------------------")
    file.write(f"Winner: {canidates[winner]}")


