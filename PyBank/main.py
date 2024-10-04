# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
changes = []
net = []
months = []
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
avg_change = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total
        months.append(row[0])
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net.append(int(row[1]))

# Calculate the average net change across the months
for i in range(1,len(net)):
    change = net[i] - net[i-1]
    changes.append(change)

    # Calculate the greatest increase in profits (month and amount)
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_month = months[i]

    # Calculate the greatest decrease in losses (month and amount)
    if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_month = months[i]

avg_change = round(sum(changes) / len(changes), 2)

# Generate the output summary
printout = [
          "Financial Analysis",
          "",
          "-----------------------------",
          "",
          f"Total Months: {total_months}",
          "",
          f"Total: ${total_net}",
          "", 
          f"Average Change: ${avg_change}",
          "", 
          f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})",
          "",
          f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"
        ]

output = "\n".join(printout)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
