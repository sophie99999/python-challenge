import os
import csv

count = 0
total = 0
prev_row = 0
change = 0
total_change = 0
max_increase = 0
max_decrease = 0

csvpath = os.path.join("..","budget_data.csv")


print("Financial analysis")
print("----------------------------------------------------------------------------")


with open(csvpath,newline="") as csvfile:
    
    
    csvreader = csv.reader(csvfile, delimiter=",")
 #Use next command to skip the first line, which is the header.    
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")
    
    for row in csvreader:
        count += 1
        total += int(row[1])
        #3rd question, to calcuate the average increase of profit and loss
        if (count == 1):
            prev_row = int(row[1])
            #print(prev_row)
        else: 
            change = int(row[1])-prev_row
            #print(change)
            if (change >= max_increase):
                max_increase = change
                max_month = str(row[0])
            elif (change <= max_decrease):
                max_decrease = change
                min_month = str(row[0])                  
            prev_row = int(row[1])
            #print(prev_row)
            total_change+=change
        #print(count)
    count -= 1
    average_change=total_change/count

        

            
        

print(f"Total Months:{count}")
print(f"Total profit and loss: $ {total}")
print(f"Average change is: $ {round(average_change,2)}")
print(f"Greatest Increase in Profits: {max_month} {max_increase}")
print(max_decrease)

