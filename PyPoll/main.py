import os
import csv

total_votes = 0
candidate = []
candidate_list = []
candidate_votes = {}
winner = ""
winning_count = 0

election_data_csv = os.path.join(
    "/Users/saurin/Desktop/Resources", "election_data.csv")
file_to_output = os.path.join(
    "/Users/saurin/Desktop/bootcamp/python-challenge/PyPoll", "election_analysis.text")

with open(election_data_csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    header = next(reader)

    for row in reader:
        total_votes = total_votes+1
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate] = candidate_votes[candidate]+1

with open(file_to_output, "w") as text_file:

    election_result = (
        f"\nElection Results"f"\n------------------------"f"\nTotal Votes: {total_votes}"f"\n---------------------")
    print(election_result)
    text_file.write(election_result)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100

        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        output = (f"\n{candidate}: {vote_percentage:.3f}% ({votes})")
        print(output, end="")
        text_file.write(output)
    winner = (
        f"\n-----------------------"f"\nWinner: {winner}"f"\n-----------------------\n")
    print(winner)
    text_file.write(winner)
