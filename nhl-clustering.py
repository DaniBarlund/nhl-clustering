#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


# In[2]:


#Read data
df = pd.read_excel("nhl-standings.xlsx")
display(df)


# In[3]:


# Set Team as index
df = df.set_index("Team")
display(df)


# In[4]:


# Remove variables which are not dependent on the number of games played
df = df.drop(["Season", "GP", "W", "L", "T", "OT", "P", "RW", "ROW", "S/O Win", "GF", "GA"],axis=1)
display(df)


# In[5]:


# Calculate inertias to find value for k
inertias = []
for i in range(1,10):
    kmeans = KMeans(n_clusters=i, n_init=10)
    kmeans.fit(df)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10),inertias, marker='o')
plt.xlabel("Value of k")
plt.ylabel("Inertia")
plt.show()


# In[6]:


#Select k=4 and insert into df
k=4
kmeans = KMeans(n_clusters=k, n_init=10)
kmeans.fit(df)

df.insert(0,"Cluster", kmeans.labels_, True)

display(df)


# In[7]:


#Plot index to cluster
plt.scatter(range(0,len(df.index)), df["Cluster"])
plt.xlabel("rank")
plt.ylabel("Cluster")
plt.title("Cluster based on the rank in standings")
plt.show()


# In[8]:


#Findest nearest neigbours for each team and insert into dataframe
neighbors = NearestNeighbors(n_neighbors=2, algorithm="auto").fit(df)
distances, indices = neighbors.kneighbors(df)
closest = []
closestDistance = []


for value in indices:
    closest.append(value[1])

for dist in distances:
    closestDistance.append(dist[1])
    

# Find team name for each index
closestName=[]
names = list(df.index)
for value in closest:
    name = names[value]
    closestName.append(name)

df.insert(1,"Closest team", closestName, True)
df.insert(2,"Closest Distance",closestDistance,True)

display(df)


# In[9]:


grouped = df.groupby("Cluster")
groupedMean = grouped.mean()


# In[10]:


#Find the cluster and the teams with the highest average amount of goals for and against in a game
totalGoals = groupedMean["GF/GP"]+groupedMean["GA/GP"]

#plot the goals for each cluster
plt.scatter(groupedMean.index, totalGoals)
plt.xlabel("Cluster")
plt.ylabel("Avg goals")
plt.ylim(5,7)
plt.show()


# In[11]:


max = 0
cluster=0
for c in groupedMean.index:
    value = totalGoals[c]
    if value > max:
        max = value
        cluster = c

print(f"Cluster {cluster} has average of {max:.1f} goals for and against per game")

display(df.loc[df["Cluster"]==cluster])


# In[ ]:




