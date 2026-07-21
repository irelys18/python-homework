# Task 3
import csv

employees = []

with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        employees.append(row)

names = [row[0] + " " + row[1] for row in employees[1:]]

print(names)

names_with_e = [name for name in names if "e" in name]

print(names_with_e)