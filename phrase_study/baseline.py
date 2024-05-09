import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

counts = [0, 0, 0, 0]
for i in range(10000):
    random_number = np.random.randint(0, 4)
    counts[random_number] += 1

phrases = ["os", "torch", "numpy", "kubernetes"]

plt.bar(phrases, counts, color='blue', alpha=0.7, label='Phrases')
plt.savefig('phrases_baseline.png')

expected_frequency = 10000 / len(counts)

chi_square_stat, p_value = chisquare(counts, f_exp=expected_frequency)

degrees_of_freedom = len(counts) - 1
critical_value = 7.815

print("Chi-Square Statistic:", chi_square_stat)
print("p-value:", p_value)
print("Degrees of Freedom:", degrees_of_freedom)
print("Critical Value (a=0.05):", critical_value)

# Compare chi-square statistic with critical value
if chi_square_stat > critical_value:
    print("Reject null hypothesis: Counts are not uniformly distributed.")
else:
    print("Fail to reject null hypothesis: Counts are uniformly distributed.")