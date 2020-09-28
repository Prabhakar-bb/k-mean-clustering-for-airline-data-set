#importing the dataset
flight = pd.read_excel('C:/Users/prabhakar/Desktop/data sets/hierarchical c/EastWestAirlines.xlsx', sheet_name = "data")

#exploratory data analysis
flight.describe()

#variance
flight.var()

#standard deviation
flight.std()

#third moment
flight.skew()

#fourth moment
flight.kurt()

# graphical representation
#histogram
import matplotlib.pyplot as plt
plt.hist(flight.Balance)
plt.hist(flight.Bonus_miles)
plt.hist(flight.Flight_miles_12mo)
plt.hist(flight.Days_since_enroll)

#boxplot
plt.boxplot(flight.Balance)
plt.boxplot(flight.Bonus_miles)
plt.boxplot(flight.Flight_miles_12mo)
plt.boxplot(flight.Days_since_enroll)

#co relation
flight.corr()


#bivaraiate analysis
import seaborn as sns
sns.pairplot(flight)
#The pairplot shows that the data is not linear and KNN can be applied to get nearest neighbors and classify the glass types


#drop id
flight = flight.drop(["ID#"], axis=1)

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

# Normalized data frame (considering the numerical part of data)
flightnorm = norm_func(flight)
flightnorm.describe()

#dendrogram 
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 

z1 = linkage(flightnorm, method = "complete", metric = "euclidean")

# Dendrogram
plt.figure(figsize=(15, 8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z1, leaf_rotation = 0, leaf_font_size = 10)
plt.show()


# Now applying AgglomerativeClustering choosing 5 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering

complete = AgglomerativeClustering(n_clusters = 4, linkage = 'complete', affinity = "euclidean").fit(flightnorm) 
complete.labels_

cluster_labels = pd.Series(complete.labels_)
flight['clust'] = cluster_labels # creating a new column and assigning it to new column 


# Aggregate mean of each cluster
flight.groupby(flight.clust).mean()

# creating a csv file 
flight.to_csv("flight.csv", encoding = "utf-8")
import os
os.getcwd()




#kmean clustering
flight1 = pd.read_excel('C:/Users/prabhakar/Desktop/data sets/hierarchical c/EastWestAirlines.xlsx', sheet_name = "data")
#drop id
flight1 = flight1.drop(["ID#"], axis=1)
# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)
# Normalized data frame (considering the numerical part of data)
flight1norm = norm_func(flight1)

#kmean
from sklearn.cluster import	KMeans
TWSS = []
k = list(range(1, 8))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(flight1norm)
    TWSS.append(kmeans.inertia_)
    
TWSS

# Scree plot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

# Selecting 4 clusters 
model1 = KMeans(n_clusters = 4)
model1.fit(flight1)

model1.labels_ # getting the labels of clusters assigned to each row 
labels = pd.Series(model1.labels_)  # converting numpy array into pandas series object 
flight1['clust'] = labels # creating a  new column and assigning it to new column 

#aggreate the values
flight1.groupby(flight1.clust).mean()

#saving into csv file
flight1.to_csv("Kmeanflight.csv", encoding = "utf-8")
import os
os.getcwd()
