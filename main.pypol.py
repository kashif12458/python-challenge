#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Read the CSV file
with open(r"C:\Users\kashi\OneDrive\Desktop\PyPoll\Resources\election_data.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    data = list(csv_reader)

# Initialize variables
total_votes = 0
candidates = {}
winner = ['', 0]

# Iterate through the data
for row in data:
    # Count total number of votes
    total_votes += 1

    # Count votes for each candidate
    candidate = row[2]
    if candidate in candidates:
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1

    # Update the winner
    if candidates[candidate] > winner[1]:
        winner = [candidate, candidates[candidate]]

# Calculate the percentage of votes each candidate won
percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    percentages[candidate] = percentage

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner[0]}\n")

print(f"Results exported to {output_file}")

