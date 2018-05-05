import os
import csv

PyBosscsvpath = os.path.join("/Users/johnsingson/Desktop/UTAUS201804DATA2-Class-Repository-DATA/03-Python/HOMEWORK/Instructions/PyBoss/raw_data/employee_data2.csv")

new_employee_Data = []

with open(PyBosscsvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        #Manipulating the different columns into the needed format
        emp_ID = row["Emp ID"]
        #Changing the name format
        full_name = row["Name"]
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        #Date of Birth
        year = row["DOB"].split("-")[0]
        month = row["DOB"].split("-")[1]
        date = row["DOB"].split("-")[2]
        DOB = f"{month}/{date}/{year}"
        #Social Security Number
        SSN = row["SSN"].split("-")[2]
        right_SSN = f"***-**-{SSN}"
        #State
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

_, filename = os.path.split(PyBosscsvpath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_Data)