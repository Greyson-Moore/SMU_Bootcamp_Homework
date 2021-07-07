import os
import csv

csvPath = os.path.join("Resources","election_data.csv")

row = []
county = []
candidate = []
allList = []
voteTotal = 0

with open(csvPath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    csvHeader = next(csvReader)
    for row in csvReader:
        #voterID.append(row[0])
        #county.append(row[1])
        candidate.append(row[2])
        allList.append(row)
        voteTotal += 1

uniqueSet = set(candidate)
candidateUnique = list(uniqueSet)

candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate4 = 0

for i in range((len(candidate))):
    if candidateUnique[0] == candidate[i]:
        candidate1 += 1
    elif candidateUnique[1] == candidate[i]:
        candidate2 += 1 
    elif candidateUnique[2] == candidate[i]:
        candidate3 += 1
    elif candidateUnique[3] == candidate[i]:
        candidate4 += 1 


print("Election Results")
print("-------------------------")
print(f"Total Votes: {voteTotal}")
print("-------------------------")

print(f"{candidateUnique[0]}: {(round(((candidate1/voteTotal) * 100),3))}% ({candidate1})")
print(f"{candidateUnique[1]}: {(round(((candidate2/voteTotal) * 100),3))}% ({candidate2})")
print(f"{candidateUnique[2]}: {(round(((candidate3/voteTotal) * 100),3))}% ({candidate3})")
print(f"{candidateUnique[3]}: {(round(((candidate4/voteTotal) * 100),3))}% ({candidate4})")

winner = max(candidate1,candidate2,candidate3,candidate4)
print("-------------------------")

if winner == candidate1:
    print(f"Winner: {candidateUnique[0]}")
elif winner == candidate2:
    print(f"Winner: {candidateUnique[1]}")
elif winner == candidate3:
    print(f"Winner: {candidateUnique[2]}")
elif winner == candidate4:
    print(f"Winner: {candidateUnique[3]}")

print("-------------------------")

with open('results.txt','w') as writer:
    writer.write("Election Results\n")
    writer.write("-------------------------\n")
    writer.write(f"Total Votes: {voteTotal}\n")
    writer.write("-------------------------\n")

    writer.write(f"{candidateUnique[0]}: {(round(((candidate1/voteTotal) * 100),3))}% ({candidate1})\n")
    writer.write(f"{candidateUnique[1]}: {(round(((candidate2/voteTotal) * 100),3))}% ({candidate2})\n")
    writer.write(f"{candidateUnique[2]}: {(round(((candidate3/voteTotal) * 100),3))}% ({candidate3})\n")
    writer.write(f"{candidateUnique[3]}: {(round(((candidate4/voteTotal) * 100),3))}% ({candidate4})\n")

    winner = max(candidate1,candidate2,candidate3,candidate4)
    writer.write("-------------------------\n")

    if winner == candidate1:
        writer.write(f"Winner: {candidateUnique[0]}\n")
    elif winner == candidate2:
        writer.write(f"Winner: {candidateUnique[1]}\n")
    elif winner == candidate3:
        writer.write(f"Winner: {candidateUnique[2]}\n")
    elif winner == candidate4:
        writer.write(f"Winner: {candidateUnique[3]}\n")

    writer.write("-------------------------")