import os
import csv

count=0
candidate=[]
candidate_vote={}


csvpath = os.path.join("..","election_data.csv")

print("Election Results")
print("----------------------------------------")

with open (csvpath,newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
#Use next command to skip the first line, which is the header.  
    csv_header=next(csvreader)
    #print(csv_header)


    for row in csvreader:
        count+=1

        if row[2] not in candidate:
            candidate.append(row[2])  #To add elements into an empty list. 
            candidate_vote[row[2]]=1  #To add elements into an empty dictionary. I want row[2] to be my dictionary keys, the vote counts be my dictionary value. 
            
        else:
            candidate_vote[row[2]]+=1 
        
 #Up to now, we have a complete dictionary called candidate_vote which specific each candidate and their votes.          

print(f"Total votes :{count}")
print("---------------------------------------")

#Finding the most vote count in the dictionary. 
max_value=max(candidate_vote.values())
#print(max_value)


#Iterate through this dictionary candidate_vote. Candidate key is the key of dictionary and respective_count is the value.
for candidate_key,respective_count in candidate_vote.items():   
    percentage =round(float(candidate_vote[candidate_key])/float(count)*100,2)
    
    print(f"{candidate_key} : {percentage}% ({candidate_vote[candidate_key]})")
    if respective_count==max_value:
        Winner=candidate_key  #save the winner name in a new variable called "Winner" because we don't want to print winner name each time we iterate. 


print("---------------------------------------")
print(f"The winner: {Winner}")









