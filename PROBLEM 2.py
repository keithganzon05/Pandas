import pandas as pd
#Problem 2
cars = pd.read_csv('cars.csv')
#A
a = cars.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
print(a)
#B
b = cars.iloc[0,0:12]
print(b)
#C
c = cars.iloc[23,2]
print("The Camaro Z28 have",c,"cylinders")
#D
model = cars.iloc[[1,28,18],0]
cyli = cars.iloc[[1,28,18],2]
geart = cars.iloc[[1,28,18],10]
print("The models:",model,"have a number of cylinders: ")
print(cyli,"and a gear type of: ")
print(geart,"respectively.")
