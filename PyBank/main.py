
#PyBank

# Modules
import os 
import csv

# The total number of months included in the dataset
months = 0
# The total amount of revenue gained over the entire period
revenue = 0
# The average change in revenue between months over the entire period
revenue_change = 0
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

greatest_revenue_increase = 0
greatest_revenue_decrease = 0
# revenue list
revenue_list = []
average_revenue_list = []

output_path = os.path.join('output', 'new.csv')



# Set path for file
csvpath = os.path.join("raw_data", "budget_data_1.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Skip the first row of the csv
    next(csvreader, None)
    
# Loop through file
    for row in csvreader:
        # count months
        months +=1

        # add up total revenue
        revenue = revenue + float(row[1])

        # track greatest increase /decrease in revenue (next revenue - this revenue)if greater/less than for increase/decrease
        revenue_list.append(row[1])
        


for x, y in enumerate(revenue_list,1):
    print(x,y)

    revenue_change = int(revenue_list[x+1]) - int(revenue_list[x])
    average_revenue_list.append(revenue_change)
    if revenue_change > greatest_revenue_increase:
        greatest_revenue_increase = revenue_change
    if revenue_change < greatest_revenue_decrease:
        greatest_revenue_decrease = revenue_change

average_revenue = sum(average_revenue_list) / float(len(average_revenue_list))



print(months)
print(revenue)
print(revenue_list)
print(greatest_revenue_increase)
print(greatest_revenue_decrease)
print(average_revenue)


