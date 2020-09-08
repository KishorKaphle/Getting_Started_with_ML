import numpy as np
import matplotlib.pyplot as plt

X = [1, 5, 8, 10, 14, 18, 21, 24, 29, 30]
Y = [1, 1, 10, 20, 45, 75, 90, 110, 129, 134]

# Train Algorithm (Polynomial)
degree = 2
poly_fit = np.poly1d(np.polyfit(X,Y, degree))

# Plot data
xx = np.linspace(0, 30, 150)
plt.plot(xx, poly_fit(xx), c='r',linestyle='-')
plt.title('Polynomial')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0, 30, 0, 150])
plt.grid(True)
plt.scatter(X, Y, c='g')
plt.show()

# Predict price
print( poly_fit(14) )