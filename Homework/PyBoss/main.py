#import the modules
import os
import csv

def PyBoss (PyBosscsvpath):

    #create an array for the new employee csv
    new_employee_Data = []

    #open the csv file
    with open(PyBosscsvpath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            #Manipulating the different columns into the needed format
            emp_ID = row["Emp ID"]
            #Changing the name format
            full_name = row["Name"]
            first_name = full_name.split()[0]
            last_name = full_name.split()[1]
            #Changing the Date of Birth format
            year = row["DOB"].split("-")[0]
            month = row["DOB"].split("-")[1]
            date = row["DOB"].split("-")[2]
            DOB = f"{month}/{date}/{year}"
            #Changing Social Security Number format
            SSN = row["SSN"].split("-")[2]
            right_SSN = f"***-**-{SSN}"
            #Changing State format
            state = row["State"]
            us_state_abbrev = {
                    'Alabama': 'AL',
                    'Alaska': 'AK',
                    'Arizona': 'AZ',
                    'Arkansas': 'AR',
                    'California': 'CA',
                    'Colorado': 'CO',
                    'Connecticut': 'CT',
                    'Delaware': 'DE',
                    'Florida': 'FL',
                    'Georgia': 'GA',
                    'Hawaii': 'HI',
                    'Idaho': 'ID',
                    'Illinois': 'IL',
                    'Indiana': 'IN',
                    'Iowa': 'IA',
                    'Kansas': 'KS',
                    'Kentucky': 'KY',
                    'Louisiana': 'LA',
                    'Maine': 'ME',
                    'Maryland': 'MD',
                    'Massachusetts': 'MA',
                    'Michigan': 'MI',
                    'Minnesota': 'MN',
                    'Mississippi': 'MS',
                    'Missouri': 'MO',
                    'Montana': 'MT',
                    'Nebraska': 'NE',
                    'Nevada': 'NV',
                    'New Hampshire': 'NH',
                    'New Jersey': 'NJ',
                    'New Mexico': 'NM',
                    'New York': 'NY',
                    'North Carolina': 'NC',
                    'North Dakota': 'ND',
                    'Ohio': 'OH',
                    'Oklahoma': 'OK',
                    'Oregon': 'OR',
                    'Pennsylvania': 'PA',
                    'Rhode Island': 'RI',
                    'South Carolina': 'SC',
                    'South Dakota': 'SD',
                    'Tennessee': 'TN',
                    'Texas': 'TX',
                    'Utah': 'UT',
                    'Vermont': 'VT',
                    'Virginia': 'VA',
                    'Washington': 'WA',
                    'West Virginia': 'WV',
                    'Wisconsin': 'WI',
                    'Wyoming': 'WY'}       
            #changing the states into abbreviations
            for key, value in us_state_abbrev.items():
                if state == key:
                    state = value

            #append the array with new employee files
            new_employee_Data.append(
                {
                    "Emp ID": emp_ID,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "DOB": DOB,
                    "SSN": right_SSN,
                    "State": state
                }
            )
            
    print(new_employee_Data)

#grab the filename from the original
    _, filename = os.path.split(PyBosscsvpath)

# Write updated data to csv file
    csvpath = os.path.join("output", filename)
    with open(csvpath, "w") as csvfile:
        fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_employee_Data)
    
#find and join the path (choose one of the data sets)
PyBosscsvpath = os.path.join("raw_data", "employee_data1.csv")
PyBosscsvpath2 = os.path.join("raw_data", "employee_data2.csv")

PyBoss(PyBosscsvpath)
PyBoss(PyBosscsvpath2)
