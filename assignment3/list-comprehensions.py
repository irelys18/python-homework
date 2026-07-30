# Task 3
import csv

with open("../csv/employees.csv", newline="") as file:
    reader = list(csv.reader(file))

names = [row[0] + " " + row[1] for row in reader[1:]]

print(names)

names_with_e = [name for name in names if "e" in name]

print(names_with_e)