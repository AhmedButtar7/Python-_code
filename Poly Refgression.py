import numpy
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

numpy.random.seed(2)

df = pd.read_csv('random_data_Vehicles.csv')
x = df['Weight']
y = df['Wheels'] / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 9, 100)
r2 = r2_score(train_y, mymodel(train_x))

if r2 > 0.65:
    print("It is a Good Relation as R Squared Score is ", r2)
else:
    print("It is a Bad Relation as R Squared Score is ", r2)

# Plotting
plt.scatter(train_x, mymodel(train_x), c='green')
plt.plot(train_x, mymodel(train_x), linestyle='--')
plt.title('Relational Graph')
plt.xlabel('Weight')
plt.ylabel('Wheels/Weight')
plt.grid(True)
plt.show()
