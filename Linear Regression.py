# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:22:49 2023

@author: qkswl
"""

import random
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'x':[1,2,3,4,5], 'y':[1.5,2.5,4,5,7]})
learningrate = 0.001 #learningrate

#Initialize slope and intercept to random number
a = random.random()
b = random.random()

epochs = 500 #Number of iterations

n= len(data.x) #Number of input values for averaging
mse_list = []

colors = ['red', 'yellow', 'cyan', 'magenta', 'green'] 
#Change color for each line when outputting the graph

#Scatterplot
plt.figure(figsize=(10,10))
plt.grid(True)
plt.scatter(data.x,data.y)
#iterations
for i in range(epochs):
    #2 of the numerator is omitted because you need to modify the learning rate
    cost_a = sum(-data.x*(data.y-(a*data.x+b)))//n
    cost_b = sum(-(data.y-(a*data.x+b)))/n
    #Save values to mse list
    mse = sum(data.y - (data.x*a+b)) **2/n
    mse_list.append(mse)
    if i % (epochs /5) == 0:
        print(f'a:{a:.2f}, b:{b:.2f}, mes:{mse_list[len(mse_list)-1]:.2f}')
        data['res'] = a*data.x+b
        lbl = 'epoch{i:>5} : mse{mse:.3f}'.format(i=i, mse=mse)
        plt.plot(data.x, data.res, linestyle ='dashed', color=colors.pop(), label=lbl)
        #Graduemt Descent Algorithm
    a= a-learningrate*cost_a
    b= b-learningrate*cost_b
plt.legend()
plt.show()
    













