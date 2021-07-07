import os
import csv

csvPath = os.path.join("Resources","budget_data.csv")

#Intialized Variables
row = []
month = []
money = []
monthTotal = 0
profitTotal = 0
totalChange = 0
increaseGreatAmount = 0
decreaseGreatAmount = 0

#CSV File Loop
with open(csvPath) as csvfile:
     csvReader = csv.reader(csvfile, delimiter=',')
     csvHeader = next(csvReader)
     for row in csvReader:
         month.append(row[0])
         money.append(row[1])
         monthTotal += 1
         profit = int(row[1])
         profitTotal += profit
#Change in Profit Loop         
for i in range(len(money) - 1):
    currentChange = int(money[i+1]) - int(money[i])
    totalChange += currentChange
    #Determine the greatest increase and decrease
    if currentChange > increaseGreatAmount:
        increaseGreatAmount = int(currentChange)
        increaseGreatMonth = month[i + 1]
    if currentChange < decreaseGreatAmount:
        decreaseGreatAmount = int(currentChange)
        decreaseGreatMonth = month[i + 1]

#Average Change Calculation
averageChange = round(totalChange / (monthTotal - 1), 2)

#Print to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthTotal}")
print(f"Total: ${profitTotal}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {increaseGreatMonth} (${increaseGreatAmount})")
print(f"Greatest Decrease in Profits: {decreaseGreatMonth} (${decreaseGreatAmount})")
print("----------------------------")

#Print to results.txt file
outPath = os.path.join("Results","results.txt")
with open(outPath,'w') as writer:

    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f"Total Months: {monthTotal}\n")
    writer.write(f"Total: ${profitTotal}\n")
    writer.write(f"Average Change: ${averageChange}\n")
    writer.write(f"Greatest Increase in Profits: {increaseGreatMonth} (${increaseGreatAmount})\n")
    writer.write(f"Greatest Decrease in Profits: {decreaseGreatMonth} (${decreaseGreatAmount})\n")
    writer.write("----------------------------\n")
