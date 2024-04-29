#!/usr/bin/env python
# coding: utf-8

# In[1]:


def options(choice =0):
    if choice  == 0 or choice == "":
        choice = int(input("""Select one of the following :
        [1] Retrieve Data via CSV Module.
        [2] Retrieve Data via Pandas module.
        [3] Visual Data Analysis.
        [4] Exit/Back to Main Menu.
        
        Choose an option ="""))
        return choice
   
    
    elif choice ==1:
        choice = int(input("""Select one of the following :
        [1] Fetch information (Gender, Age, Marital Status, Department) based on the Employee number.
        [2] Fetch information (Department, Education level, Total Working Years, Standard Hours) associated with a particular Job Role.
        [3] Fetch information (Employee Number, Job Role, Marital Status,Hourly Rate) of employees whose standard hours are under 60, categorized by department.
        [4] Fetch data (Monthly Income,Performance Rating,Job Involvement,Job Satisfaction) based on employee number.
        [5] Exit/Back to Main Menu.
        
        Choose an option ="""))
        return choice
    
    elif choice == 2:
        choice = int(input("""Select one of the following :
        [1] Identifying the top 3 job roles with most employees hired for each role according to their education level.
        [2] Analyse the average monthly rate of employees based on particular education level. 
        [3] Analyze the average duration of employment for staff in a particular department within the organization.
        [4] Analyse average Monthly Income for each job role.
        [5] Exit/Back to Main Menu.
        
        
        Choose an option ="""))
        return choice
    
    elif choice == 3:
        choice = int(input("""Select one of the following :
        [1] Display the proportion of employees of company based on their education levels.
        [2] Display the chart to visually compare the number of employee training in specific education field.
        [3] Display the chart illustrating the variation in job satisfaction ratings across various job levels within each department.
        [4] Display the percent of the salary hike for each Job Role. 
        [5] Exit/Back to Main Menu.
   
        Choose an option ="""))
        return choice
    else:
        print("Please make a valid selection.")

