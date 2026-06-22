import matplotlib.pyplot as plt

# Number of carbons in the first 10 linear alkanes
carbons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Corresponding boiling points (°C)
boiling_points = [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7, 98.4, 125.6, 150.8, 174.1]

# Create scatter plot
plt.plot(carbons, boiling_points, linestyle='-')
plt.scatter(carbons, boiling_points)

# Add title and axis labels
plt.title("Boiling Point vs. Number of Carbons for Linear Alkanes")
plt.xlabel("Number of Carbons")
plt.ylabel("Boiling Point (°C)")

# Set y-axis tick marks every 25 °C
plt.yticks(range(-175, 201, 25))

# Display the plot
plt.show()