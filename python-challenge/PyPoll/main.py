import os
import csv

poll_csv = os.path.join('..', 'Resources', 'election_data copy.csv')

output_path= os.path.join('..', 'Analysis', 'Resluts.txt')


def poll_analysis(poll_data):

    total_votes = len(poll_data)

    khan_votes = 0
    correy_votes=0
    li_votes=0
    tooley_votes=0

    for i in range(total_votes):

        khan_votes= khan_votes + (poll_data[i][2].count("Khan"))
        correy_votes= correy_votes +(poll_data[i][2].count("Correy"))
        li_votes = li_votes + (poll_data[i][2].count("Li"))
        tooley_votes= tooley_votes + (poll_data[i][2].count("O'Tooley"))

    if khan_votes > (correy_votes and li_votes and tooley_votes):
            winner = "Khan"
    elif correy_votes > (khan_votes and li_votes and tooley_votes):
            winner = "Correy"
    elif li_votes > (khan_votes and correy_votes and tooley_votes):
            winner = "Li"
    elif tooley_votes >(khan_votes and correy_votes and li_votes):
            winner= "O'Tooley"

    khan_percent= round((khan_votes / total_votes) * 100, 3)
    correy_percent= round((correy_votes / total_votes) * 100, 3)
    li_percent= round((li_votes / total_votes) * 100, 3)
    tooley_percent= round((tooley_votes / total_votes) * 100, 3)

    with open (output_path, 'w') as f:
        print("Election Results", file=f)
        print("-----------------------", file = f)
        print(f"Total Votes: {total_votes}", file = f)
        print("-----------------------", file = f)
        print(f"Khan: %{khan_percent} ({khan_votes})", file = f)
        print(f"Correy: %{correy_percent}({correy_votes})", file = f)
        print(f"Li: %{li_percent} ({li_votes})", file = f)
        print(f"O'Tooley: %{tooley_percent} ({tooley_votes})", file = f)
        print("-----------------------", file = f)
        print(f"Winner: {winner}", file= f)
        print("-----------------------", file= f)

with open(poll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')

    header = next(csvreader)

    poll_data= []

    for row in csvreader:

        voter_id = int(row[0])
        county = str(row[1])
        candidate = str(row[2])

        poll_data.append([voter_id, county, candidate])

poll_analysis(poll_data)
