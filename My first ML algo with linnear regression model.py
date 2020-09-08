import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [[4], [8], [12], [16], [18]]
y = [[40000], [80000], [100000], [120000], [150000]]
plt.scatter(X, y)
plt.title ('Scatter plot of X vs y')
plt.xlabel ('X value')
plt.ylabel ('y value ')
plt.show()

model = LinearRegression()
model.fit(X,y)

#predict
rooms = 11
prediction = model.predict([[rooms]])
print ('Price prediction: ', prediction)

