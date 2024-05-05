import os
import numpy as np
import matplotlib.pyplot as plt
import argparse
import google.generativeai as palm

def load_or_generate_numbers(api_key):
    np.random.seed(0)
    palm.configure(api_key=api_key)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)

    prompt = """Generate 10,000 uniformly distributed random numbers between 0 and 1. Previous numbers should have no influence on future numbers: """
    # Add 20 random numbers between 0 and 1
    for i in range(20):
        prompt += str(np.random.rand()) + " "

    temperatures = [1, 0, 0.2, 0.4, 0.6, 0.8]
    numbers_by_temperature = {}
    for temp in temperatures:
        file_path = f'random_numbers_{temp}.txt'
        if os.path.exists(file_path):
            # Load numbers from file
            with open(file_path, 'r') as f:
                random_numbers = [float(line.strip()) for line in f]
            print(f"Loaded {len(random_numbers)} numbers from {file_path}")
        else:
            # Generate numbers if file does not exist
            random_numbers = []
            while len(random_numbers) < 10000:
                completion = palm.generate_text(
                    model=model,
                    prompt=prompt,
                    temperature=temp,
                    max_output_tokens=800,
                )
                try:
                    random_numbers += [float(num) for num in completion.result.split()[:-1]]
                except:
                    continue
                print(len(random_numbers))
            print(f"Generated {len(random_numbers)} numbers at temperature {temp}")
            random_numbers = random_numbers[:10000]
            with open(file_path, 'w') as f:
                for num in random_numbers:
                    f.write(str(num) + '\n')
        numbers_by_temperature[temp] = random_numbers

    for temp, numbers in numbers_by_temperature.items():
        plot_distribution(numbers, temp)

def plot_distribution(random_numbers, temp):
    plt.figure(figsize=(10, 6))
    plt.hist(random_numbers, bins=1000, color='blue', alpha=0.7)
    plt.title(f'Distribution of Random Numbers at Temperature {temp}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(f'random_numbers_distribution_{temp}.png')  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', type=str, help='Your API Key')
    args = parser.parse_args()
    load_or_generate_numbers(args.api_key)
