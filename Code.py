import numpy as np

def sigmoid(x):
    """ evaluating sigmoid at x"""
    return 1/(1+np.exp(-x))
    
def sigmoid_prime(x):
    """ evaluating the derivate of sigmoid at x"""
    return x*(1-x)
