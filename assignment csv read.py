from pandas import read_csv as rd
from matplotlib import pyplot as plt

data = rd('company_sales_data.csv')
print(data.head())

# Plot the graph of face cream
plt.plot(data['month_number'], data['facecream'], 'o:r')
plt.plot(data['facewash'], 'o:r')
plt.plot(data['moisturizer'], 'o:r')
plt.title('Sales of Cream in Different Months: ')
plt.xlabel('Month')
plt.ylabel('Facecream')
plt.show()

# Scatter of Face wash
plt.scatter(data['month_number'], data['facewash'], c='green')
plt.title('Sales of Facewash in Different Months: ')
plt.xlabel('Months')
plt.ylabel('Facewash')
plt.grid(True)
plt.show()

# Histo Graph of Moisturizer
plt.hist(data['moisturizer'])
plt.title('Sales of Moisturizer: ')
plt.show()

# Pie Char of profit:
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData = [data['facecream'].sum(), data['facewash'].sum(), data['toothpaste'].sum(),
             data['bathingsoap'].sum(), data['shampoo'].sum(), data['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()
