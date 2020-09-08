import math as mt
arr = []
lbl = []
for i in range (-100,100):
    fun = 1 / (1 + mt.exp(-i))
    arr.append(fun)
    lbl.append(i)
    print ( fun)

import matplotlib.pyplot as plt
plt.plot(lbl, arr)
plt.title('Sigmoid Function Plot')
plt.xlabel('x')
plt.ylabel('Sigmoid Function')
plt.grid()
plt.show()
