import matplotlib.pyplot as plt

x_values = range(1, 101)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.axis([0, 110, 0, 11000])

plt.savefig('squares_plot.jpg', bbox_inches='tight')
plt.show()
