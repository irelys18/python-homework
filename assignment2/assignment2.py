# Task 2
import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    employees = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)

            employees["fields"] = next(reader)

            for row in reader:
                rows.append(row)

            employees["rows"] = rows

        return employees
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )

        print("An exception occured.")
        print(f"Exception type: {type(e).__name__}")

        message = str(e)
        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")
        exit()

# Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employees = read_employees()
employee_id_column = column_index("employee_id")

print(employees)

# Task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

# Task 5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))

    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(
        filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"])
    )
    return matches

# Task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )

    return employees["rows"]

# Task 8
def employee_dict(row):
    employee = {}

    for index in range(len(employees["fields"])):
        if index != employee_id_column:
            employee[employees["fields"][index]] = row[index]

    return employee

# Task 9
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

employees = read_employees()
employee_id_column = column_index("employee_id")

all_employees = all_employees_dict()

print(all_employees)

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Thank you CTD!")

print(custom_module.secret)

# Task 12
def read_csv_file(filename):
    data = {}
    rows = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        data["fields"] = next(reader)

        for row in reader:
            rows.append(tuple(row))

            data["rows"] = rows
            
        return data
    
def read_minutes():
    minutes1 = read_csv_file("../csv/minutes1.csv")
    minutes2 = read_csv_file("../csv/minutes2.csv")

    return minutes1, minutes2

employees = read_employees()
employee_id_column = column_index("employee_id")

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

# Task 13
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    minutes_set = minutes1_set.union(minutes2_set)

    return minutes_set

minutes_set = create_minutes_set()

print(minutes_set)

# Task 14
def create_minutes_list():
    minutes_list = list(minutes_set)

    minutes_list = list(
        map(
            lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    sorted_list = list(
        map(
            lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
            minutes_list
        )
    )

    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])
                        
        writer.writerows(sorted_list)

    return sorted_list

sorted_minutes = write_sorted_list()
print(sorted_minutes)




