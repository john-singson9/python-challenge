#import the modules
import os
import csv

#Find and join the csv file (choose one of the data sets)
pybankcsvpath = os.path.join('/Users/johnsingson/Desktop/UTAUS201804DATA2-Class-Repository-DATA/03-Python/HOMEWORK/Instructions/PyBank/raw_data', "budget_data_1.csv")
#pybankcsvpath = os.path.join('/Users/johnsingson/Desktop/UTAUS201804DATA2-Class-Repository-DATA/03-Python/HOMEWORK/Instructions/PyBank/raw_data', "budget_data_2.csv")

#create arrays for variables
total_months = []
revenue_change = []
max_min_date = []

#create starting point for variables
total_revenue = 0
sum_average = 0
previous_revenue = 0

#open the csvfile and assign the columns
with open(pybankcsvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        months = row["Date"]
        revenue = row["Revenue"]

        #figure out total revenue
        total_revenue = total_revenue + int(revenue)

        #append the months array to figure out length
        total_months.append(months)
        max_min_date.append(months)

        #figure out the changes in revenue and put them in array
        change = int(revenue) - previous_revenue
        previous_revenue = int(revenue)
        revenue_change.append(change)

#delete the first item in the array then divide by total months to figure out the average
del revenue_change[0]
average = sum((revenue_change)) / (len(total_months) - 1)

#figure out the maximum and minimum values in the array
maximum = max(revenue_change)
minimum = min(revenue_change)

#delete the first date in the max_min array to index later
del max_min_date[0]
#use the max index to figure out the date of the maximum change
index_of_max = revenue_change.index(maximum)
maximum_date = max_min_date[index_of_max]
#use the min index to figure out the date of the minimum change
index_of_min = revenue_change.index(minimum)
minimum_date = max_min_date[index_of_min]

# Write updated data to text file (change data set name based on opened file)
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