# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:02:21 2020

@author: Sahil Phalle"""
import pandas as pd
import matplotlib.pyplot as plt
pd.read_csv("general_data.csv")
dataset=pd.read_csv("general_data.csv")
dataset.head()

dataset.columns
dataset.duplicated()
dataset1=dataset[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()
dataset1
dataset2=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].describe()
dataset2
plt.boxplot(dataset["MonthlyIncome"])
plt.scatter(dataset["MonthlyIncome"],dataset["PercentSalaryHike"])
