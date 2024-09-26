import numpy as np 
import pandas as pd
from plotnine import ggplot, geom_point, aes, geom_boxplot, geom_bar, geom_density,guides,labs, xlab, ylab
#Task 1
#1
#x = income, y= life expectancy, bubble size represents population size, color = world region, the data is 2010

#2
q1= pd.read_csv("/Users/alexandra/Desktop/GSB_544/Week 1/Lab_1/Data_Lab1/q1data (1).csv")
#subset only 2010 data
q1 = q1[q1['year']==2010]
(ggplot(q1, 
aes(x = "income",
  y = "life_exp",
  size = "population",
  color= "four_regions"
  ))
+ geom_point()
)

#4
(ggplot(q1, 
aes(x = "income", 
    size = "population", 
    color = "four_regions"
))
+ geom_density(alpha=0.5)
)

#I created a density plot. It is not representative for the y variable, life expectancy. The graph is hard to read. 


#Task 2 
#1
#x= exports of gdp , y= imports of gdp, bubble size = energy use, color = world regions, data = 1997
q2= pd.read_csv("/Users/alexandra/Desktop/GSB_544/Week 1/Lab_1/Data_Lab1/q2data.csv")

#subset only 1997 data
q2 = q2[q2['year']==1997]
q2= q2.dropna()

(ggplot(q2, 
aes(x = "exports",
  y = "imports",
  size = "energy",
  color= "four_regions"
  ))
+ geom_point(alpha=.5)
+ xlab("Exports (% of GDP)")
+ ylab("Exports (% of GDP)")
+guides(size=False)
+labs(title = 'Imports vs Exports as Percentage of GDP by Region',
size='Energy Use', 
color='Region'))


#4

#Task3
#1
#x= Individual internet users , y= gdp/capita, bubble size = income, color = world regions, data = 2001
q3= pd.read_csv("/Users/alexandra/Desktop/GSB_544/Week 1/Lab_1/Data_Lab1/q3data.csv")

#subset only 1997 data
q3 = q3[q3['year']==2001]
q3= q3.dropna()

(ggplot(q3, 
aes(x = "internet_users",
  y = "gdp",
  size = "income",
  color= "four_regions"
  ))
+ geom_point(alpha=.5)
+ ylab("GDP/capita")
+ xlab("Individuals using the internet")
+guides(size=False)
+labs(title = 'Imports vs Exports as Percentage of GDP by Region',
size='income', 
color='Region'))

# testing