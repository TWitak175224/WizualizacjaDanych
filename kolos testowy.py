import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# z1
x = np.arange(-3, 3.01, 0.5)
plt.plot(x, (np.sin(x)) * x, color='plum')
help(plt.xlim)
plt.xlim((-3.0, 3.0))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji sin(x)*x')
plt.show()

# z.2
data = {
    'Fuel-type': ['GAS', 'DIESEL', 'GAS', 'DIESEL', 'GAS', 'GAS'],
    'Price': [22000, 25000, 18000, 27000, 21000, 22000],
    'Car model': ['OPEL', 'AUDI', 'DODGE', 'DODGE', 'BMW', 'NISSAN']
}
df = pd.DataFrame(data)
# df = pd.read_csv('automobile.csv')
audi_dodge_df = df[(df['Car model'] == 'AUDI') | (df['Car model'] == 'DODGE')]
print(audi_dodge_df)
model_price = df.groupby('Car model').sum()
model_price.drop('Fuel-type', axis=1, inplace=True)
print(model_price)

# z3
df = pd.DataFrame(data)
# df=pd.read_csv('automobile.csv')
fuel_type = df['Fuel-type'].value_counts()
fuel_type.plot(kind='pie', autopct='%1.2f%%', title='Wykres ilość aut benzynowych do diesla', legend=True, fontsize=14)
# plt.pie(fuel_type, autopct='%1.2f%%',textprops={'fontsize':14})
plt.show()
