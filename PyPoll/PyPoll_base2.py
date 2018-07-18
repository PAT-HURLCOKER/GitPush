#1.	The total number of votes cast  
#2.	A complete list of candidates who received votes
#3.	The percentage of votes each candidate won
#4.	The total number of votes each candidate won
#5.	The winner of the election based on popular vote.
#ccchttps://www.bing.com/videos/search?q=sentdex+csv+for+python&&view=detail&mid=C3404523D984B678D643C3404523D984B678D643&&FORM=VRDGAR


# Data is in election_data.csv which has three columns:  Voter_ID, County, and Candidate

import pandas as pd

# Path identified to load the file
data_file = "Resources/election_data.csv"

# Method to read a data frame
election_data_df = pd.read_csv(data_file)
election_data_df
Total_votes = election_data_df["Voter_ID"].count()
print(f"Total votes: {Total_votes}")

# My Count of Election Results:  Total_votes = 1048575

Candidates_List = election_data_df["Candidate"].unique().tolist()
Candidates_List

# My Count of Election Candidates ['Khan', 'Correy', 'Li', "O'Tooley"]

Votes_counted_for_each_candidate = election_data_df["Candidate"].value_counts()
Votes_counted_for_each_candidate

#   Khan        661583
#   Correy      209046
#   Li          146360
#   O'Tooley     31586
#   Name: Candidate, dtype: int64

# For each candidate in the Candidate List:
# Display the number of Votes_received_for_each_candidate[candidate]/total_vote)
# Print out results

largest_num_of_votes = 0
print("Election Results")
print("-------------------------")
print(f"Total votes: {Total_votes}")
print("-------------------------")

# For each candidate
# Display the number of votes and the percent of total votes
for candidate in Candidates_List:
  num_of_votes = Votes_received_for_each_candidate[candidate]
  percent_of_votes = (num_of_votes/Total_votes) * 100
  # determine the winner by determining which candidate has the largest number of votes
  if num_of_votes > largest_num_of_votes:
      largest_num_of_votes = num_of_votes
        # create and set a winner variable equal to this candidate
        # for the candidate with the most vote
      winner = candidate
   # Pad the results with 2 decimal place:.2f
  print(f"{candidate}: {percent_of_votes:.2f}% ({num_of_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#  My 
#Election Results
# -------------------------
# Total votes: 1048575
# -------------------------
# Khan: 63.09% (661583)
# Correy: 19.94% (209046)
# Li: 13.96% (146360)
# O'Tooley: 3.01% (31586)
# -------------------------
# Winner: Khan
# -------------------------