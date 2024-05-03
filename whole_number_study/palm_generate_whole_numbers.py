import pprint
import google.generativeai as palm
import numpy as np
import matplotlib.pyplot as plt
import argparse
import random

def generate_numbers(api_key, prompt, output_file):
    np.random.seed(0)
    palm.configure(api_key=api_key)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)

    random_numbers = []
    while len(random_numbers) < 10000:
        #"""Generate 10,000 uniformly distributed random numbers between 0 and 1. Previous numbers should have no influence on future numbers: """
        #add 20 random numbers between 0 and 1
        for i in range(20):
            prompt += str(random.randint(0, 10000)) + " "

        # print(prompt)
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            # The maximum length of the response
            max_output_tokens=800,
        )

        # print(completion.result)
        try:
            random_numbers += [int(num) for num in completion.result.split()[:-1]]
        except:
            continue
        print(len(random_numbers))

    random_numbers = random_numbers[:10000]
    print(random_numbers)
    # save the random numbers to a file
    with open(output_file, 'w') as f:
        for num in random_numbers:
            f.write(str(num) + '\n')

def plot_distribution(random_numbers):
    # plot the distribution of the random numbers
    plt.hist(random_numbers, bins=100)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', type=str, help='Your Api Key')
    parser.add_argument('--prompt', type=str, help='Your prompt')
    parser.add_argument('--output_file', type=str, help='output file name')
    args = parser.parse_args()
    generate_numbers(args.api_key, args.prompt, args.output_file)
