#!/usr/bin/env python
# coding: utf-8

# Function to load the data from a CSV file into memory using the CSV module

# In[ ]:


# importing python library
import csv

def data_processing_csv():
    data = []

    data_set = input("Provide Path for data :")
    
    try:
        if data_set == "":
            with open(data_set,encoding="utf8") as file_reader:
                reader = csv.reader(file_reader)
                headings = next(reader)
                for data_points in reader:
                    data.append(data_points)
            print("Data has been loaded.")
            return data
        else:
            with open(data_set) as file_reader:
                reader = csv.reader(file_reader)
                headings = next(reader)
                for data_points in reader:
                    data.append(data_points)
            print("Data has been loaded.")        
            return data
    except IOError:
        print("Not able to open file.!")
data_set =data_processing_csv()


# Function to Retrieve the Gender, Age, Marital Status, and Department based on the Employee number.

# In[ ]:


def employee_details(data_set):
    Employee_Number = input("Enter the Employee number to retrieve data : ")
    found = False
    for data in data_set:
        if data[1] == Employee_Number:
            found = True
            print(f"Gender : {data[9]}","\n",f"Age : {data[4]}","\n",f"Martial Status : {data[11]}","\n",f"Department : {data[7]}")
            break
    if not found:
        print("Employee not found")


# Function to retrieve the Department, Education level, Total Working Years, and Standard Hours
# associated based on specific Job Role.

# In[ ]:


def professional_details(data_set):
        job_role = input("Enter the job role of Employee to retrieve data : ").strip().lower()
        column_names = ["DEPARTMENT", "EDUCATION LEVEL", "TOTAL WORKING YEARS", "STANDARD HOURS"]
        print(f"[{column_names[0]:^15}|{column_names[1]:^25}|{column_names[2]:^25}|{column_names[3]:^20}]")
        print(92*'-')
        found = False
        for data in data_set:
            if data[10].lower() == job_role:
                found = True
                print(f"[{data[7]:^15}|{data[17]:^25}|{data[33]:^25}|{data[30]:^20}]")
        if not found:
            print(f"No job role found of: {job_role}, please enter a valid Job Role !")


# Function to the Retrieve the Employee Number, Job Role, Marital Status, and Hourly Rate of employees whose
# Standard Hours are less than 60 hours based on the department.

# In[ ]:


def department_details(data_set):
    department = input("Enter the Department of Employee to retrieve data : ").strip().lower()
    column_names = ["EMPLOYEE NUMBER", "JOB ROLE", "MARITAL STATUS", "HOURLY RATE"]
    print(f"[{column_names[0]:^20}|{column_names[1]:^27}|{column_names[2]:^20}|{column_names[3]:^20}]")
    print(92*'-')
    found = False
    for data in data_set:
        if data[7].lower() == department and int(data[30]) < 60:
            found = True
            print(f"[{data[1]:^20}|{data[10]:^27}|{data[11]:^20}|{data[20]:^20}]")
    if not found:
            print(f"No Department found of: {department}, please enter a valid Departmernt!")


# Function to Retrieve the Monthly Income,Performance Rating,Job Involvement,Job Satisfaction based of Employee Number.
# (specific condition )

# In[ ]:


def important_details(data_set):
    Employee_Number = input("Enter the Employee number to retrieve data : ")
    found = False
    for data in data_set:
        if data[1] == Employee_Number:
            found = True
            print(f"Monthly_Income : {data[24]}","\n",f"Performance_Rating : {data[28]}","\n",f"Job_Involvement : {data[21]}","\n",f"job_Satisfaction : {data[23]}")
            break
            
    if not found:
        print("Employee not found.")


# In[ ]:




