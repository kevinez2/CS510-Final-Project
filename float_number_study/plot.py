import matplotlib.pyplot as plt
import numpy as np

# Read the random numbers from the file
random_numbers = []
with open('random_numbers.txt', 'r') as f:
    for line in f:
        random_numbers.append(float(line.strip()))

# Set the size of the figure
plt.figure(figsize=(10, 6), dpi=400)  # Larger figure size

# Plot the histogram of the random numbers
plt.hist(random_numbers, bins=10, density=True, alpha=1, label='Empirical Data')

# Add a theoretical uniform distribution for comparison
plt.plot([0, 1], [1, 1], 'r-', linewidth=2, label='Uniform Distribution')

# Enhance the plot
plt.title('Distribution of Random Numbers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()  # Show legend to distinguish between empirical data and uniform distribution

# Save and show the plot
plt.savefig('random_numbers.png')
plt.show()
