import matplotlib.pyplot as plt


year=[2000,2005,2010,2015,2020]
profit = [10000,30000,10000,50000,25000]

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(year,profit)  # Plot some data on the Axes.
plt.show()                           # Show the figure.

limit=5
for i in range (5,0,-1):
    print(i)