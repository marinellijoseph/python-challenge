# The total number of votes cast
total_votes = 0
# A complete list of candidates who received votes
candidate_list = []
# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


# open csv
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("raw_data", "election_data_1.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the first row of the csv
    next(csvreader, None)

    # Loop through 
    for row in csvreader:
        # count votes
        total_votes +=1
        # list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            
            #loop through candidate list and make list for each candidate
        for candidate in candidate_list: 
            candidate = []

            # count votes and append voter id to candidate list
            if row[2] == candidate:
                candidate.append(row[0])
            # calculate percentage of votes per candidate
            votes = candidate.count()
            

        # winner of election

print(total_votes)
print(candidate_list)


