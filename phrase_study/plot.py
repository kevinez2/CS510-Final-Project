import matplotlib.pyplot as plt
import numpy as np

# Read the random numbers from the file
phrases_count = {}
with open('phrases0.8.txt', 'r') as f:
    for line in f:
        phrase = line.strip()
        if phrase in phrases_count:
            phrases_count[phrase] += 1
        else:
            phrases_count[phrase] = 1

# Set the size of the figure
# plt.figure(figsize=(10, 6), dpi=400)  # Larger figure size

# Plot the histogram of the random numbers

phrases = ["os", "torch", "numpy", "kubernetes"]
counts = []
for phrase in phrases:
    counts.append(phrases_count[phrase])
plt.bar(phrases, counts, color='blue', alpha=0.7, label='Phrases')

# Add a theoretical uniform distribution for comparison
# plt.plot([0, 1], [1, 1], 'r-', linewidth=2, label='Uniform Distribution')

# Enhance the plot
# plt.title('Distribution of Random Numbers')
# plt.xlabel('Value')

# Save and show the plot
plt.savefig('phrases0.8.png')
plt.show()
