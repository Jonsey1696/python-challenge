import os
import csv

budget_csv= os.path.join("..", "Resources", "budget_data copy.csv")

output_path= os.path.join("..", "Analysis", "Results.txt")


def budget_analysis(budget_data):

    total_months= len(budget_data)
    total_profit=0
    change=0
    daily_change = []

    for i in range(total_months):
        
        total_profit = total_profit + budget_data[i][1]

        if i < (total_months - 1):
            change = (budget_data[i][1] - budget_data[i+1][1])
            total_change= change + (budget_data[i][1] - budget_data[i+1][1])
            average_change = round(total_change/(total_months - 1), 2)
            daily_change.append(change)
            great_inc= max(daily_change)
            great_dec= min(daily_change)

            
    with open (output_path, "w") as f:
        print("Financial Analysis", file=f)
        print("------------------------------", file = f)
        print(f"Total Months: {total_months}", file = f)
        print(f"Total: ${total_profit}", file = f)
        print(f"Average Change: ${float(average_change)}", file = f)
        print(f"Greatest Increase in Profits: {great_inc}", file = f)
        print(f"Greatest Decrease in Profits: {great_dec}", file = f)


with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    budget_data= []

    for row in csvreader:
        month = str(row[0])
        profit_loss= int(row[1])

        budget_data.append([month, profit_loss])



budget_analysis(budget_data)
