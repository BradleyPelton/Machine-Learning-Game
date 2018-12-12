import numpy as np

def sigmoid(x):
    """ evaluating sigmoid at x"""
    return 1/(1+np.exp(-x))
    
def sigmoid_prime(x):
    """ evaluating the derivate of sigmoid at x"""
    return x*(1-x)

#input data 

test_1= [1,1,1,1,1,1,1,1,1,1]
test_2= [0,0,0,0,0,0,0,0,0,0]
test_3= [1,0,1,0,1,0,1,0,1,0]
test_4= [1,1,0,0,1,1,0,0,1,1]
test_5= [0,0,1,1,0,0,1,1,0,0]

x= np.array

for i in range(10000):
    
