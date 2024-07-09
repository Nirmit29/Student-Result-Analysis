import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Expanded_data_with_more_features.csv")
print(df.head())
# from head we check what our data is saying as we have 5 rows & 15 columns,
# #also we can draw some patterns like which are the categories that are affecting the students scores
# analysing the impact
# As checked in weekly study hrs their is fault in raw data as 05 oct i.e 5 to 10 hrs
# so we have to also analyse the changes we that do in the data
# also as seen we have a column named unnamed which have some numeric value which is of no use so we can aslo drop them

print(df.describe())
#all the numeric value data we can check
#we can notice only in maths student got 0 marks
#students are strong in reading & writing but weak in maths

print(df.info())
#gives the output of datatype in the column if i need to change it
# also tells not null values

print(df.isnull().sum())
#gives the null values

#Step 1
#we can drop the unnamed column
df = df.drop("Unnamed: 0",axis = 1)
print(df.head())

#step 2
# we can correct the incorrect data as we had in weekly study hours column
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
print(df.head())

#Step 3
#for creating this visualizations or to make charts we have analyse data & distribute it.
#gender distribution
# making a count plot

plt.figure(figsize=(5,5))
ax = sns.countplot(data = df , x = "Gender")
# as we can see the values are very near by
#so we can find the exact count by creating labels
ax.bar_label(ax.containers[0])
plt.title("Gender-Distribution")
plt.show()

#from the above chart we have analysed that number of females in the data is more than the number of males

#Step 4
# by watching the data we can create a chart of how parent education is impacting students marks

gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)
# as we can see the parents having good marks in degree there childrens have also good marks,
# so we can create a heat map to represent our analysis

#step 5

plt.figure(figsize=(4,4))
sns.heatmap(gb,annot = True)
plt.title("Relation between Parents Score & Students Score")
plt.show()

# as we can see in the chart for lighter shade marks are higher & for darker shade marks are lower
#also for exact count using annot

#we can clealy say now parents having good marks in masters degree there childrens have also good marks as compared to parents in high school

#Step 6
#we can also check how the marital status of parents are afftecting their kids study

gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})

plt.figure(figsize=(4,4))
sns.heatmap(gb,annot = True)
plt.title("Relation between Parents Marital Status & Students Score")
plt.show()

# from the above chart we can say their is negligible impact of parent marital status on their kids
# from the data we have we can easily find out many relationship

#step 7
# to find out any exceptional student in marks (outlier)
#making a box plot to find out

sns.boxplot(data = df , x = "MathScore")
plt.show

sns.boxplot(data = df , x = "ReadingScore")
plt.show

sns.boxplot(data = df , x = "WritingScore")
plt.show

# we can say only in math there is a student who has 0 marks as comapred to reading & writing

# also we have etenic group so we can make a final chart to show case our analysis
# by finding out unique values

print(df["EthnicGroup"].unique())

# here we can ignore NaN value and we have other groups

#Distribution of ethnic groups
# we can find out using countplot but we should take out the percentage so for that we can make a pie chart
# for count using loc from pandas

groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
#here we found out the values that lies in Group A , SO finding out all the others too
groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
groupE = df.loc[(df["EthnicGroup"] == "group E")].count()

# so we have count of all the columns in every group but we need specific Ethnic group
# for labels creating variable l for piechart

l = ["group A","group B","group C","group D","group E"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

plt.pie([mlist],labels = l,autopct = "%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()

#from this we can Group C has highest percentage
# you can also pass legends as well as colours
# also by making count plot we can check the vales of groups & make a countplot
# we can make many analysis here too

'''
So, a final output we can say bu making relationship for the institute or any company working behind it.
'''






