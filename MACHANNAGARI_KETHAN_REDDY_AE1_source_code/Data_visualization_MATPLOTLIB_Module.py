#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import necessary python libraries
import matplotlib.pyplot as plt
import pandas as pd
import warnings


# In[ ]:


#import Panda_Data_Processing_Module file to load the dataset from task B
import Pandas_Data_Processing_Module
from Pandas_Data_Processing_Module import*


# Display the proportion of Employees of Company based on their Education Levels using Pie Chart.

# In[ ]:


def proportion_employees(D):
    education_proportion = D['Education_level'].value_counts()
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
    plt.figure(figsize=(8, 6))
    plt.pie(education_proportion, labels=education_proportion.index, autopct='%1.1f%%',colors=colors[:len(education_proportion)])
    plt.legend(education_proportion.index,title='Education Levels',bbox_to_anchor=(1, 1.5),loc='best')
    plt.title('Proportion of Employees by Education Level')
    plt.show()


# Display the Comparision of frequency of employee training in each Education Field using Bar Chart.

# In[ ]:


def frequency_of_training(D):
    plt.figure(figsize = (12,8))
    y =D['Education_Field'].value_counts()
    x = y.index
    plt.bar(x,y)
    plt.title('Bar chart Displaying the frequency of employee training in each Education field.')
    plt.xlabel('Education Field')
    plt.ylabel('Frequency of employee training')
    plt.show()


# Display the Chart to visualize how job satisfaction values varies across the various job levels in specific department, in a single chart.

# In[ ]:


def job_satisfaction_by_department(D):
    plt.figure(figsize = (12,8))
    satisfaction_department = D.groupby(['Department','Job_Level'])['Job_Satisfaction'].mean().unstack()
    satisfaction_department.plot.bar(width = 0.8)
    plt.title('Variation of Job Satisfaction in different Job Levels within the specific Department')
    plt.xlabel('Department')
    plt.ylabel('Job Satisfaction')
    plt.xticks(rotation=0)
    plt.legend(title='Job Level',bbox_to_anchor=(1.05, 1),loc='upper left')
    plt.show()


# Display the percent of the salary hike for each Job Role.

# In[ ]:


def Salary_hike_across_jobroles(D):
    plt.figure(figsize=(12, 8))
    selected_data = D[['Job_Role','Percent_Salary_Hike']]
    selected_data.boxplot(by = 'Job_Role',figsize=(12, 8))
    plt.title('Perecentage of salary hike Across Job Roles')
    plt.xlabel('Job Role')
    plt.ylabel('Percent of Salary Hike')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

