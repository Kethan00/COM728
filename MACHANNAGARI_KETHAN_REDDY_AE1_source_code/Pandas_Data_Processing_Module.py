#!/usr/bin/env python
# coding: utf-8

# Pandas Data Processing Module

# Loads Data set using Pandas

# In[ ]:


import pandas as pd

def data_processing_pandas(df):
    try:
        data = pd.read_csv(df)
        print("Data Loaded Successfully!")
        return data
    except IOError:
        print("Unable to read/open file name or file path")
df = "HR_Metrics.csv"
D= data_processing_pandas(df)


# Function to identify the top 3 job titles with the highest number of employees recruited for each position based on their educational standard.

# In[ ]:


def top_job_roles_by_education_level(D):
    top_roles = D.groupby(['Education_level', 'Job_Role']).size().groupby(level=0, group_keys=False).nlargest(3)
    print("Top 3 job roles by education level:")
    print(top_roles)


# Function to analyse the mean of monthly rate of employees based on each education level.

# In[ ]:


def average_monthly_rate(D):
    avg_rate = D.groupby('Education_level')['Monthly_Rate'].mean()
    print("Average Monthly Rate by Education Level:")
    print(avg_rate)


# Analyse the average tenure of employment for employees in a specific department within
# the company.

# In[ ]:


def tenure_of_employment(D):
    tenure_of_employment = D.groupby('Department')['Years_At_Company'].mean()
    print("Average Tenure of employment for employees in a Each Department:")
    print(tenure_of_employment) 


# Calculating average monthly income for each job role.(Own Selected attributes)

# In[ ]:


def monthly_income(D):
    monthly_income= D.groupby('Job_Role')['Monthly_Income'].mean()
    print("Average Monthly Income Of Employee based on Specific Jobe Role:")
    print(monthly_income)

