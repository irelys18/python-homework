
import pandas as pd 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']  
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)


#task1 with salary
task1_with_salary = task1_data_frame.copy()

task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)


#task1 older
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(task1_older)


#to CSV file
task1_older.to_csv("employees.csv", index=False)
print("DataFrame saved to employees.csv")

#Task 2
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

#JSON file
json_employees = pd.read_json("additional_employees.json")
print(json_employees) 

#Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index = True)

#Task 3
first_three = more_employees.head(3)
print(first_three)

#tail
last_two = more_employees.tail(2)
print(last_two)

#shape
employee_shape = more_employees.shape
print(employee_shape)

#info
print(more_employees.info())

#Task 4
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()

#Remove duplicates
clean_data = clean_data.drop_duplicates()
print(clean_data)

#Age to numeric
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# Salary to numeric
clean_data["Salary"]= clean_data["Salary"].replace(
    ["unknown", "n/a"], pd.NA
)

clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)

print(clean_data)

#fillna
clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())

clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())

print(clean_data)

#datetime
clean_data["Hire Date"] = clean_data["Hire Date"].str.strip()

clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"], 
    errors="coerce"
)

clean_data["Hire Date"] = clean_data["Hire Date"].fillna(
    clean_data["Hire Date"].mode()[0]
)
print(clean_data)

# strip whitespace
clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print(clean_data)

# pytest -v -x assignment4-test.py.
# python assignment4.py
