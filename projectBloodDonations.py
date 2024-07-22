#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\tahiy\Downloads\transfusion.data")
df
#R (Recency - months since last donation),
#F (Frequency - total number of donation),
#M (Monetary - total blood donated in c.c.),
#T (Time - months since first donation), and
#a binary variable representing whether he/she donated blood in March 2007 (1 yes 0 no). 


# In[2]:


df.columns
df.columns = ["Recency (months)", "Frequency (times)", "Monetary (c.c. blood)", "Time (months)", "Donated March"]


# In[3]:


df.isna().sum()


# In[4]:


stats = df[["Time (months)", "Recency (months)", "Frequency (times)"]].describe()
stats


# In[5]:


variance = df[["Time (months)", "Recency (months)", "Frequency (times)"]].var()
variance


# In[6]:


donated = df[df["Donated March"] == 1]
df[df["Donated March"] == 1][["Time (months)", "Recency (months)", "Frequency (times)"]].describe()


# In[7]:


notdonated = df[df["Donated March"] == 0]
df[df["Donated March"] == 0][["Time (months)", "Recency (months)", "Frequency (times)"]].describe()


# In[8]:


donationCounts = df["Donated March"].value_counts()

plt.pie(donationCounts, labels=["Donated", "Didn't Donate"], autopct = '%0.1f%%', colors = ["teal", "orange"])
plt.title("Donations in March 2007")
plt.show()


# In[9]:


plt.hist(donated["Frequency (times)"], bins=100, color = "teal")

plt.xlabel("Frequency (times)")
plt.ylabel("# of Donors")
plt.title("Frequency of Blood Donations for March Donators")
plt.show()


# In[10]:


plt.hist(notdonated["Frequency (times)"], bins=100, color = "orange")

plt.xlabel("Frequency (times)")
plt.ylabel("# of Donors")
plt.title("Frequency of Blood Donations for Non-March Donators")
plt.show()


# In[11]:


plt.hist(notdonated["Frequency (times)"], bins=100, color = "orange")
plt.hist(donated["Frequency (times)"], bins=100, color = "teal")

plt.xlabel("Frequency (times)")
plt.ylabel("# of Donors")
plt.title("Frequency of Blood Donations for March Donators")
plt.legend(["Didn't Donate", "Donated"])
plt.show()


# In[12]:


plt.scatter(x = donated["Recency (months)"], y = donated["Frequency (times)"], color = "teal")

plt.xlabel("Recency (months)")
plt.ylabel("Frequency (times)")

plt.title("March Donators Recency vs Frequency")
plt.show()


# In[13]:


plt.scatter(x = notdonated["Recency (months)"], y = notdonated["Frequency (times)"], color = "orange")

plt.xlabel("Recency (months)")
plt.ylabel("Frequency (times)")

plt.title("Non-March Donators Recency vs Frequency")
plt.show()


# In[14]:


plt.scatter(x = donated["Recency (months)"], y = donated["Frequency (times)"], color = "teal")
plt.scatter(x = notdonated["Recency (months)"], y = notdonated["Frequency (times)"], color = "orange", alpha = 0.20)

plt.xlabel("Recency (months)")
plt.ylabel("Frequency (times)")

plt.title("Donated vs Not Donated Recency + Frequency")
plt.legend(["Donated", "Not Donated"])
plt.show()


# In[ ]:




