import csv
import os
# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")

# Declaring Variables
total_months = 0
net_total = 0
current_change = 0
prv_change = 0 
change_list = []
avrg_change = 0 
change_month = []
change_list = []
gi = ["", 0]
gd = ["", 999999]



# Open the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    # Read the header row
    header = next(reader)
    #print(header)
    first_row = next(reader)
    total_months += 1
    prv_change = int(first_row[1])

    for row in reader:
        # Calcualte the total months 
        total_months = total_months +1
        # Calcualte the net total from profit/losses
        net_total = net_total + int(row[1])
        # Calcualte the total change with the previous change to get average change
        current_change = int(row[1]) - prv_change
        prv_change = int(row[1])
        change_list += [current_change]
        change_month += [row[1]]

        # The greatest increase in profits (date and amount) over the entire period
        if current_change>gi[1]:
            gi[1] = current_change
            gi[0] = row[0]

        # The greatest decrease in profits (date and amount) over the entire period
        if current_change<gd[1]:
            gd[1] = current_change
            gd[0] = row[0]
    avrg_change = sum(change_list)/len(change_list)

    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months {total_months}")
    print(f"Total ${net_total}")
    print(f"Average Change ${avrg_change:.2f}")
    print(f"Greatest Increase in Profits: {gi[0]} (${gi[1]})")
    print(f"Greatest Decrease in Profits: {gd[0]} (${gd[1]})")
    
    with open("Resources/analysis.txt","w") as file:
        file.write("Financial Analysis")
        file.write("----------------------------")
        file.write(f"Total Months ${total_months}")
        file.write(f"Total {net_total}")
        file.write(f"Average Change ${avrg_change:.2f}")
        file.write(f"Greatest Increase in Profits: {gi[0]} (${gi[1]})")
        file.write(f"Greatest Decrease in Profits: {gd[0]} (${gd[1]})")
        

