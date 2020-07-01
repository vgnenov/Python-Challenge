#Import Libraries
import os
import csv

#set the path for the csv file
csv_path = os.path.join("Resources", "Election_Results.csv")

#output file for the analysis text
output_file = "Election_Results.txt"

#open and read the csv file
with open(csv_path, "r") as in_file:
    csv_reader = csv.reader(in_file)

    csv_header = next(csv_reader)
    Votes_Total = 0
    Votes_Khan = 0
    Votes_Correy = 0 
    Votes_Li = 0
    Votes_Otooley = 0

    #calculates total number of votes for each candidate using a for loop
for row in csv_reader:
    Votes_Total += 1
    if row[2] == "Khan":
        Votes_Khan += 1
    elif (row[2] == "Correy"):
        Votes_Correy += 1
    elif (row[2] == "Li"):
        Votes_Li += 1
    elif (row[2] == "O'Tooley"):
        Votes_Otooley += 1

#calculate each's candidate percentage
Percent_K = float("{0:.3f}".format(100 * Votes_Khan/Votes_Total))
Percent_C = round(100 * Votes_Correy/Votes_Total, 3)
Percent_Li = round(100 * Votes_Li/Votes_Total, 3)
Percent_OT = round(100 * Votes_Otooley/Votes_Total, 3)

#make a dictionary of candidates with their name and their percentage of votes
candidates = {  'Khan': Percent_K,
                'Correy': Percent_C, 
                'Li': Percent_Li, 
                'OTooley': Percent_OT }

#declare winner
winner = max(candidates, key=candidates.get)

#create text file and print in terminal
with open("Election_Results.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print("Total Votes: "+ str(Votes_Total ), file = text_file)
    print("-------------------------", file = text_file)
    print("Khan: " +  str(Percent_K) +"%  (" + str(Votes_Khan )+ ")", file = text_file)
    print("Correy: " +  str(Percent_C) +"%  (" + str(Votes_Correy )+ ")", file = text_file)
    print("Li: " +  str(Percent_Li) + "%  (" + str(Votes_Li)+ ")", file = text_file)
    print("OTooley: " +  str(Percent_OT) +"%  (" + str(Votes_Otooley)+ ")", file = text_file)
    print("-------------------------", file = text_file)
    print("Winner: " + winner, file = text_file)
    print("-------------------------", file = text_file)

with open("Election_Results.txt", "r") as text_file:
    print(text_file.read())