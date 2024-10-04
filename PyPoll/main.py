# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winner_count = 0
winner = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    printout = [
                "Election Results",
                "",
                "-------------------------------",
                "",
                f"Total Votes: {total_votes}",
                "",
                "-------------------------------"
                ""
            ]

    output = "\n".join(printout)

    print(output)

    # Write the total vote count to the text file
    txt_file.write(output)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:

        # Get the vote count and calculate the percentage
        votes = candidate_votes.get(candidate)
        votes_pct = round(float(votes) / float(total_votes) * 100,3)

        # Update the winning candidate if this one has more votes
        if votes > winner_count:
            winner_count = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        vote_counts = [
                        "",
                        f"{candidate}: {votes_pct}% ({votes})",
                        "",
                    ]
                    
        # Generate and print the winning candidate summary
        output = "\n".join(vote_counts)
        print(output)
        txt_file.write(output)

    # Save the winning candidate summary to the text file
    election_winner = [
                        "",
                        "-------------------------------",
                        "",
                        f"Winner: {winner}",
                        "",
                        "-------------------------------"
                    ]
    output = "\n".join(election_winner)
    print(output)
    txt_file.write(output)