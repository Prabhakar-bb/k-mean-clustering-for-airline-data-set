Business problem
            Perform clustering (Both hierarchical and K means clustering) for the airlines data to obtain optimum number of clusters.

Inference from the data 
                Data talks about each passenger, the data include information on their mileage history with other categories  having 3999 observation
Data set size 
Data give is found to be numerical data  for which classification model  can be performed getting deeper into the data analysis and its behavior 

Exploratory data analysis 
By using summary of the data set we can find the mean, median, mode  for different  columns in the data set with this we can find how the data is  some of the variance and standard deviation of data set
> var(airline$Balance)
[1] 10155734648
> var(airline$Bonus_miles)
[1] 583269247
> var(airline$Bonus_trans)
[1] 92.23317
> var(airline$Flight_miles_12mo)
[1] 1960586
> var(airline$Days_since_enroll)
[1] 4264781 
> sd(airline$Balance)
[1] 100775.7
> sd(airline$Bonus_miles)
[1] 24150.97
> sd(airline$Bonus_trans)
[1] 9.60381
> sd(airline$Flight_miles_12mo)
[1] 1400.209
> sd(airline$Days_since_enroll)
[1] 2065.135

    

here the data of bonus miles and balance are shown above most of the data lies in the range of 0 to 50000 and both the data has outliers in the data 
> skewness(airline$Balance)
[1] 5.00231
> skewness(airline$Bonus_miles)
[1] 2.841027
> kurtosis(airline$Balance)
[1] 47.10124
> kurtosis(airline$Bonus_miles)
[1] 16.61195

  



  


In the data of day since enroll  most of the data lies normally in between 0 to 8000 and there is no outliers in the data 
> skewness(airline$Bonus_trans)
[1] 1.156928
> skewness(airline$Days_since_enroll)
[1] 0.1201285
> kurtosis(airline$Bonus_trans)
[1] 5.740805
> kurtosis(airline$Days_since_enroll)
[1] 2.032204

Bivariate analysis
  


Bivariate analysis helps to relate the variables with other variables and we can find the types of correlation 

Data modelling
In this we are normalizing the data at first and then we are performing hirerachical clustering using the method ward2 we are getting the dendogram which is shown below it helps to find the no of k value to to be used for aggregating the values 
 
by keeping k =3 we are aggregating the values 
> table(groupair)
groupair
   1    2    3 
2489 1380  130 
> aggregate(AirlinesNew[,2:12],by= list(AirlinesNew$groupair), FUN = mean)
  Group.1   Balance Qual_miles cc1_miles cc2_miles cc3_miles Bonus_miles Bonus_trans
1       1  46718.86   9.274407  1.242266  1.023303  1.000000    5037.793    7.091201
2       2 116314.45 363.839130  3.498551  1.000000  1.035507   37150.357   18.066667
3       3 134880.89 393.323077  2.430769  1.000000  1.000000   36582.169   29.338462
 
 Flight_miles_12mo Flight_trans_12 Days_since_enroll    Award?
1          221.1671       0.7002812          3772.786 0.1880273
2          377.0000       1.1500000          4696.888 0.6630435
3         5915.5231      16.6384615          4599.608 0.7538462

The values are aggregated into 3 groups as shown above we can convert the entire data into csv file by using the fuction 
write_csv(AirlinesNew, "airline.csv")
getwd()

summary
 by this we can identify that the passengers in the  group 3 has travelled more than other groups 



k mean clustering
       here we are using elbow curve to find the k value the difference is that it takes centroid point for clustering below diagram shows the elbow curve 
> table(fit$cluster)

   1    2    3    4 
 832  151 2104  912 
Group 3 is higher than other groups which means the passenger’s  in group 3 travel history is more than other groups 
 
2d representation of cluster 
 

