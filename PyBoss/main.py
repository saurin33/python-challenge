import os
import csv
import datetime
file_num = 2
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
    'Wyoming': 'WY',
}
emp_id = []
dob = []
first_name = []
last_name = []
ssn = []
state = []


py_boss_csv = os.path.join("/Users/saurin/Desktop", "employee_data.csv")
# new_employee_data = []
with open(py_boss_csv, 'r')as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        emp_id.append(row['Emp ID'])
        first_name.append(row['Name'].split(" ")[0])
        last_name.append(row['Name'].split(" ")[1])
        dob.append(row['DOB'].split('-')[1] + '/' +
                   row['DOB'].split('-')[2] + '/' + row['DOB'].split('-')[0])
        ssn.append('***-**-' + row['SSN'].split('-')[2])
        state.append(us_state_abbrev[row['State']])

    new_data = zip(emp_id, first_name, last_name, dob, ssn, state)
    # print(new_data)

    output_file = os.path.join('new_emp_data' + str(file_num) + '.csv')

    with open(output_file, 'w')as csvwrite:
        new_file = csv.writer(csvwrite, delimiter=',')
        new_file.writerow(
            ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
        new_file.writerows(new_data)

    with open(output_file, 'r')as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
