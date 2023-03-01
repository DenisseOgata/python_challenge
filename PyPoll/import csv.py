import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")

# Declaring Variable

total_votes = 0
list_candidates =[]
perc_won_vts = 0

# Open the csv file.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header row
    header = next(reader)
    #print(header)
    first_row = next(reader)

    for row in reader
    # Calculate the total votes
    total_votes = total_votes +1
    # Set the rows for candidate names


