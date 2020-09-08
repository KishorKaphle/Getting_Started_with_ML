#A simple ML algorithm to find the linear regression of a given data sets
# This program first generates testing data by the use of random function then with the help of that data it generate the linear regression of the training sets thereby finally testing the model with the validation data sets
import random
maxvar= 200
#lets choose the total number of data set available and assign it to total
total = 100
i = 0
X = []
Y = []
Z = []
fun = []
while i < 100:
    x = random.randint (0, maxvar)
    y = random.randint (0, maxvar)
    z = random.randint (0, maxvar)
    f = 10*x + 11*y + 12*z
    #print (x, y, z) # for testing the random number generation
    X.append (x)
    Y.append (y)
    Z.append (z)
    fun.append (f)
    #print (X, Y, Z) # for validation
    i+=1
#print (len(X))
#print ("total data", X)
#Now, it's time to create training data and testing data; training data will be 80% of total data sets and remaining 20% will be used in testing

def train (array):
    j=0
    array1 =[]
    for i in array:
        if j < 80:
            array1.append(i)
        j+=1
    print (array1)
    print (len(array1)) # for cross-checking the division of training set
    return array1
#another method of extracting validation data from the main data pool
def valid (array):
    array1 = array [60:80]
    #print(array1)
    #print (len(array1)) # for cross-checking the division of training set
    return array1
Xtrain = train(X)
Xvalid = valid (X)

Ytrain = train(Y)
Yvalid = valid (Y)

Ztrain = train(Z)
Zvalid = valid (Z)

Ftrain = train(fun)
Fvalid = valid (fun)
print ('train data: ', Xtrain, Ytrain, Ztrain, Ftrain)
print ("validation data: ", Xvalid, Yvalid, Zvalid, Fvalid)










