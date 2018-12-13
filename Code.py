import numpy as np

def sigmoid(x):
    """ evaluating sigmoid at x"""
    return 1/(1+np.exp(-x))
    
def sigmoid_prime(x):
    """ evaluating the derivate of sigmoid at x"""
    return x*(1-x)

#input data (10 numbers)
### add a lot more cases to get more accurate

test_1= [1,1,1,1,1,1,1,1,1,1]   #answer =1
test_2= [0,0,0,0,0,0,0,0,0,0]   #answer =0 
test_3= [1,0,1,0,1,0,1,0,1,0]   #answer =1
test_4= [1,1,0,0,1,1,0,0,1,1]   #answer =0
test_5= [0,0,1,1,0,0,1,1,0,0]   #answer =1
test_6= [0,1,0,1,0,1,0,1,0,1]   #answer =0
test_7= [1,1,0,1,0,1,0,1,0,1]   #answer =0
test_8= [0,0,1,0,1,0,1,0,1,0]   #answer =1
test_9= [0,0,0,1,1,1,0,0,0,1]   #answer =1
test_10= [1,1,1,0,0,0,1,1,1,0]  #answer =0

#output data (11th number that the computer guesses)

y = np.array([[1,0,1,0,1,0,0,1,1,0]]).T
#print(y)

x= np.array([ test_1,test_2,test_3,test_4,test_5,
              test_6,test_7,test_8,test_9,test_10 ] )
#print(x)

np.random.seed(2222)

weights = np.random.random((10,1))


for i in range(100000):
    var_a= x
    var_b= sigmoid(np.dot(var_a,weights))
    var_b_error= y - var_b
    var_b_delta = var_b_error * sigmoid_prime(var_b)
    weights += np.dot(var_a.T,var_b_delta)
    

#print("output after training:")
#print(var_b)

your_test= []
while len(your_test) < 10:
    your_number = int(input("Please enter either 0 or 1: "))
    your_test.extend([your_number])
    #print(your_test)

x= np.array([ test_1,test_2,test_3,test_4,test_5,
              test_6,test_7,test_8,test_9,test_10,your_test ] )


    
z=sigmoid(np.dot(x,weights))
q = z[-1]
if 1-q < .05 :
    q= 1
elif q<.05 :
    q=0
else:
    print("idk kev")

print("The next number you were thinking of was ")

print(q)

