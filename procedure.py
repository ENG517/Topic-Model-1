import matplotlib.pyplot as plt


categories = ["A", "B", "C", "D", "E"]
values = [5, 10, 15, 20, 25]


plt.bar(categories, values)


plt.title("Bar Chart")

plt.xlabel("Categories")
plt.ylabel("Values")


plt.bar(categories, values, color="blue")


plt.show()