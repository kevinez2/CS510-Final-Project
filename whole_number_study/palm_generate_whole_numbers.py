import ast
import pprint
import google.generativeai as palm
import numpy as np
import matplotlib.pyplot as plt
import argparse
import random
from google.api_core import retry

@retry.Retry()
def generate_text(*args, **kwargs):
    response = palm.generate_text(*args, **kwargs).candidates
    return [output['output'] for output in response]

def generate_numbers(api_key, prompt, output_file, temp):
    np.random.seed(0)
    palm.configure(api_key=api_key)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)
    random.seed(1234)
    for i in range(19):
            prompt += str(random.randint(0, 10000)) + ".0 "
    prompt += str(random.randint(0, 10000)) + ".0"
    random_numbers = []
    while len(random_numbers) < 10000:
        responses = generate_text(
            model=model,
            prompt=prompt,
            temperature=temp,
            # The maximum length of the response
            max_output_tokens=1024
        )
        # print(completion.result)
        for response in responses:
            try:
                random_numbers += [int(num) for num in response.replace(".0", "").split()[:-1]]
            except:
                continue
            print(len(random_numbers))

    random_numbers = random_numbers[:10000]
    # save the random numbers to a file
    with open(output_file + "_" + str(temp).replace(".", "_") + ".txt", 'w') as f:
        for num in random_numbers:
            f.write(str(num) + '\n')

def plot_distribution(random_numbers):
    # plot the distribution of the random numbers
    plt.hist(random_numbers, bins=100)
    plt.show()

def test_random_seed():
    int_list = []
    for _ in range(5):
        random.seed(1234)
        for _ in range(20):
            int_list.append(str(random.randint(0, 10000)))
    print(int_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api_key', type=str, help='Your Api Key')
    parser.add_argument('--prompt', type=str, help='Your prompt')
    parser.add_argument('--output_file', type=str, help='output file name')
    parser.add_argument('--temp', type=float, help='temperature of model')
    args = parser.parse_args()
    #test_random_seed()
    generate_numbers(args.api_key, args.prompt, args.output_file, args.temp)
