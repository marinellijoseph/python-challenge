
#PyBank

# import dependencies
import csv

# set variables to track our analysis
months = 0 
revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


# Set path for file
file_to_load = "raw_data/budget_data_1.csv"
file_to_output = "budget_analysis_1.txt"

# Open the CSV
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:
    
        # count months
        months +=1

        # add up total revenue
        revenue = revenue + float(row["Revenue"])
        
        #track revenue change
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = float(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# set output to print
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total Revenue: ${revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
file_to_output = "budget_analysis_1.txt"
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
