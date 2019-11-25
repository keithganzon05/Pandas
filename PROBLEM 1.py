import pandas as pd
#Problem 1
cars = pd.read_csv('cars.csv')
#For first five
firstf = cars[0:5]
print(firstf)
#For last five
lastf = cars[27:32]
print(lastf)
