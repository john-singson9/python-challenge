#do the modules
import os
import csv

#Find and join the csv file
pybankcsvpath = os.path.join('/Users/johnsingson/Desktop/UTAUS201804DATA2-Class-Repository-DATA/03-Python/HOMEWORK/Instructions/PyBank/raw_data', "budget_data_1.csv")
#pybankcsvpath = os.path.join('/Users/johnsingson/Desktop/UTAUS201804DATA2-Class-Repository-DATA/03-Python/HOMEWORK/Instructions/PyBank/raw_data', "budget_data_2.csv")

#open the csv file
total_months = []
revenue_change = []
total_revenue = 0
sum_average = 0
previous_revenue = 0
max_min_date = []

with open(pybankcsvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        months = row["Date"]
        revenue = row["Revenue"]
        total_revenue = total_revenue + int(revenue)
        total_months.append(months)
        max_min_date.append(months)

        change = int(revenue) - previous_revenue
        previous_revenue = int(revenue)
        revenue_change.append(change)

print(total_revenue)
print(len(total_months))
del revenue_change[0]
print(revenue_change)

average = sum((revenue_change)) / (len(total_months) - 1)
print(average)

del max_min_date[0]
maximum = max(revenue_change)
minimum = min(revenue_change)
print(maximum)
print(minimum)

index_of_max = revenue_change.index(maximum)
maximum_date = max_min_date[index_of_max]
print(maximum_date)

index_of_min = revenue_change.index(minimum)
minimum_date = max_min_date[index_of_min]
print(minimum_date)

# Write updated data to text file
output_path = os.path.join("data_set1.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write("Total Months:" + str(len(total_months)) + "\n")
    output_file.write("Total Revenue: $" + str(total_revenue) + "\n")
    output_file.write("Average Revenue Change: $" + str(average) + "\n")
    output_file.write("Greatest Increase in Revenue: " + maximum_date + "($" + str(maximum) + ")" + "\n")
    output_file.write("Greatest Decrease in Revenue: " + minimum_date + "($" + str(minimum) + ")" + "\n")
    output_file.close()