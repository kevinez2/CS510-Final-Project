from scipy.stats import chisquare

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

total_count = sum(counts)

expected_frequency = total_count / len(counts)

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