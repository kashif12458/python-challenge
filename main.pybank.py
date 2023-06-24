#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import csv

# Read the CSV file
with open(r"C:\Users\kashi\OneDrive\Desktop\PyBank\Resources\budget_data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)               #To Skip the header row
    data = list(csv_reader)

# Initialize variables
total_months = 0 
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Iterate through the data
for row in data:
    # Calculate total number of months
    total_months += 1        # counter for month

    # Calculate net total amount
    profit_loss = int(row[1])         # accessing column 1 of the data and converting the values to integer
    net_total += profit_loss          # adding each value to net total 

    # Calculate change in profit/losses
    change = profit_loss - previous_profit_loss # getting the change by subtracting the last profit/loss from new
    changes.append(change)

    # Update greatest increase and decrease
    if change > greatest_increase[1]:
        greatest_increase = [row[0], change]    # if change is greater than the greatest increase replace the greatest increase by new change and its month 
    if change < greatest_decrease[1]:
        greatest_decrease = [row[0], change]   # if change is less than the greatest decrease replace the greatest decrease by new change and its month 

    previous_profit_loss = profit_loss        

# Calculate average change
average_change = sum(changes) / len(changes)   #calculating average change

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    
    
    






