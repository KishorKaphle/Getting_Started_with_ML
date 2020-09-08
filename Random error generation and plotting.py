from random import  random
count = 0
result_array = [0]
error_array = [0]
while count<100:
    a = 1
    b = 1
    summation = a+b+random()
    result_array.insert (count, summation)
   # print(f' Sum with error value is {summation} ')
    error = summation-(a+b)
    error_array.insert(count, error)
    #print ('error in summation is :', error)
    count+=1
print( 'result array is: ', result_array)


print( 'error array is', error_array)
import matplotlib.pyplot as plt
plt.plot (result_array, 'r')
plt.plot (error_array, 'b')
plt.show()

