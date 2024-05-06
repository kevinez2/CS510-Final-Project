import numpy as np
from scipy.stats import kstest, randint, chisquare
import argparse
import matplotlib.pyplot as plt
import numpy as np
import random


def zhang_test(data, a, b):
    """
    Performs Zhang's test for uniformity of discrete data.
    
    Args:
        data (numpy.ndarray): The dataset of discrete values.
        a (int): The lower bound of the discrete uniform distribution.
        b (int): The upper bound of the discrete uniform distribution.
        
    Returns:
        float: The test statistic.
        float: The p-value.
    """
    n = len(data)
    data_sorted = np.sort(data)
    
    # Compute spacings between consecutive order statistics
    spacings = np.diff(np.concatenate(([a], data_sorted, [b])))
    
    # Compute the test statistic
    test_statistic = n * (max(spacings) - min(spacings))
    
    # Compute the p-value using Monte Carlo simulation
    num_simulations = 10000
    simulated_statistics = np.zeros(num_simulations)
    for i in range(num_simulations):
        simulated_data = randint.rvs(a, b + 1, size=n)
        simulated_data_sorted = np.sort(simulated_data)
        simulated_spacings = np.diff(np.concatenate(([a], simulated_data_sorted, [b])))
        simulated_statistics[i] = n * (max(simulated_spacings) - min(simulated_spacings))
    
    p_value = np.mean(simulated_statistics >= test_statistic)
    
    return test_statistic, p_value

# Read the text file and convert the contents to a NumPy array
def ks_analysis(random_numbers: str):
    iter_list = list(zip(random_numbers.split(","), [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]))
    for value in iter_list:
        random_number_file = value[0]
        temp = value[1]
        with open(random_number_file, 'r') as file:
            data = np.array([int(line.strip()) for line in file])

        a, b = 0, 10000  # Range: [0, 10000]
        num_bins = b - a + 1  # Number of possible values

        # Count the occurrences of each value
        counts, bins = np.histogram(data, bins=num_bins, range=(a - 0.5, b + 0.5))

        # Compute the expected counts for a discrete uniform distribution
        expected_counts = len(data) / num_bins * np.ones(num_bins)

        # Conduct the chi-squared goodness-of-fit test
        test_statistic, p_value = chisquare(counts, f_exp=expected_counts)
        print("Temp:", temp)
        print("********************************************************")
        # Print the results
        print(f"Chi-Squared Test Statistic: {test_statistic:.4f}")
        print(f"p-value: {p_value:.4f}")
        print("********************************************************")
        # Interpret the results
        alpha = 0.05  # Significance level
        if p_value < alpha:
            print("The data does not follow a discrete uniform distribution.")
        else:
            print("The data follows a discrete uniform distribution.")
        print("********************************************************")
        # Compute the Kolmogorov-Smirnov statistic and p-value
        statistic, p_value = kstest(data, 'uniform', args=[a, b])
        # Print the results
        print("********************************************************")
        print(f"KS's Statistic: {statistic:.4f}")
        print(f"p-value: {p_value:.4f}")
        print("********************************************************")
        # Interpret the results
        alpha = 0.05  # Significance level
        if p_value < alpha:
            print("The data does not follow a uniform distribution.")
        else:
            print("The data follows a uniform distribution.")
        print("********************************************************\n")

def plot_distribution(random_numbers):
    # plot the distribution of the random numbers
    for temp, random_number_file in enumerate(random_numbers.split(","), start=0):
        with open(random_number_file, 'r') as file:
            data = np.array([int(line.strip()) for line in file])
            plt.figure()
            plt.hist(data, bins=1000)
            plt.title('Distribution of Random Numbers')
            plt.xlim(0, 10000)
            plt.xlabel('Value')
            plt.ylabel('Frequency')
            plt.savefig(f'/Users/admin/Documents/UIUC/CS 588/CS510-Final-Project/whole_number_study/Results/whole_numbers_{str(temp)}.png', dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_files', type=str, help='input file name')
    args = parser.parse_args()
    plot_distribution(args.input_files)
    #ks_analysis(args.input_files)