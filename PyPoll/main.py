import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "election_data.csv")

# Declaring Variable

winner = ""
winner_votes = 0
total_votes = 0
candidates = {}


# Open the csv file.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header (row skipt the frist row)
    header = next(reader)
    #print(header)

# loop construction over the rows
    for row in reader: 
    # calculate the total votes
        total_votes = total_votes +1 
        #if name is in the dictionary  
        name = row[2]
        if name in candidates:
            candidates [name] = candidates [name] +1    
         #if the name is not in dictionary add name with the count =1
        else:
            candidates[name] = 1

with open("Resources/Election_Results.txt","w") as file:
    print("Election Results") 
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")

    # format and print txt file
    file.write("Election Results\n") 
    file.write("--------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("--------------------------------\n")

    for candidate in candidates:

        vote = candidates [candidate] 
        pct = vote / total_votes

        print(f'{candidate}: {round(pct*100,3)}% ({vote})')

        file.write(f'{candidate}: {round(pct*100,3)}% ({vote})\n')
        if vote>winner_votes:
            winner = candidate
            winner_votes = vote

    print("--------------------------------")  
    file.write("--------------------------------\n")  

    print(f"Winner: {winner}")
    file.write(f"Winner: {winner}\n")


