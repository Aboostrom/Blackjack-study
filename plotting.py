import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
a_list = []
b_list = []
dealer_card = "A"

with open("data.csv", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        if row[2] == "1":
            if len(a_list) > 0:
                x.append(a_list)
                y.append(b_list)
            a_list = []
            b_list = []
            a_list.append(float(row[2]))
            b_list.append(float(row[0]))
        else:
            a_list.append(float(row[2]))
            b_list.append(float(row[0]))

plt.figure(1)
plt.xticks(np.arange(0, 22, step=1))
color = ["r", "b", "g", "c", "m", "y", "k"]
for i in range(len(x)):
    plt.plot(x[i], y[i], "o", label=f"{i + 1}")
plt.xlabel("Minimum to stay")
plt.ylabel("Success rate")
plt.title("Blackjack graph data")
plt.legend()
# plt.figure(2)
# plt.subplot(121)
# plt.xticks(np.arange(0, 22, step=1))
# plt.bar(x, y)
# plt.title("Dealer shows A")
# plt.subplot(122)
# plt.xticks(np.arange(0, 22, step=1))
# plt.bar(x2, y2)
# plt.title("Dealer shows 2")
plt.show()
