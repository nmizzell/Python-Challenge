import os
import csv
import locale

#for formatting numbers
locale.setlocale(locale.LC_ALL, '')

def format_as_pct(amount):
    return "{:.2%}".format(amount)

#set file path for input
dirname = os.path.dirname(__file__)
path = os.path.join(dirname,'Resources/election_data.csv')

#set file path for output
output_path = os.path.join(dirname,'Analysis.txt')

#read input file
with open(path) as csvfile:
    data = csv.reader(csvfile)

    #define variables
    candidates = dict()
    total_votes = 0

    #iterate through each row of the csv
    for index, row in enumerate(data):
        
        #store headers
        if index == 0:
            csv_header = row
        else:
            
            #If the result is None when we search for the candiate name in our dictionary, then we add the candidate name and one vote
            if candidates.get(row[2]) == None:
                candidates[row[2]] = 1
            
            #otherwise, we just add one vote to the existing candidate
            else:
                candidates[row[2]] += 1
            
            #always add one vote to the total votes, except if the row is the header col
            total_votes += 1


#formatting and output

#spacer used for visual separation of output
spacer = "---------------------------------"

#results is plit into 3 parts. The first part shows the total votes
results1 = f"""Election Results
{spacer}
Total Votes: {total_votes}
{spacer}
"""

#the second results part shows each candidate's voters and the pct of total votes for each
results2 = str()

#for this part, we kill 2 birds with 1 stone:
#1. we loop through the output dict, formatting and storing the results of each candidate
#2. we calculate the winner of the election
winner = None
winner_vote_count = 0

#loop through every candidate in the output dict
for candidate in candidates:
    
    #get the value of the dictionary that corresponds to the candidates name. this equals the vote count
    vote_count = float(candidates.get(candidate))

    #format and append the results
    results2 += f"{candidate}: {format_as_pct(vote_count / total_votes)} ({vote_count})\n"
    
    #check if the current candidate is the winner
    if vote_count > winner_vote_count:
        
        #if they are the winner, then set the winner values to their name and vote count. Otherwise, do nothing
        winner = candidate
        winner_vote_count = vote_count

#for visual appeal
results2 += spacer


#the third results part shows the winner of the election, which was calculated in the above loop
results3 = f"""
Winner: {winner}
{spacer}
"""

#Now, we combine all results parts to get a final result
results = results1+results2+results3

#print results to terminal
print(results)

#export results as txt
with open(output_path,'w') as f:
    f.write(results)
