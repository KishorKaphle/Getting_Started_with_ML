import pandas as pd
import plotly.express as px

df = pd.read_csv('/home/kishor/PycharmProjects/my_hello_world/Engvsfuel.csv')

print(df)
fig = px.scatter(df, x = 'ENGINESIZE', y = 'FUEL CONSUMPTION IN HIGHWAY',
                 title='Engine Size Vs Fuel Consumption in Highway',
                 color = 'FUEL CONSUMPTION IN HIGHWAY',
                 size = 'FUEL CONSUMPTION IN HIGHWAY', size_max=20)
fig.show()
