import numpy as np 
import pandas as pd
from plotnine import ggplot, geom_point, aes, geom_boxplot, geom_bar, geom_density
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

#4
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
+ geom_point()
)
