import pprint
import google.generativeai as palm
import numpy as np

np.random.seed(0)
palm.configure(api_key='AIzaSyDgb2t4I4GfTwjMqmPngSDpIMOvjq9H63w')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

random_numbers = []
while len(random_numbers) < 10000:
    prompt = """
    Generate 10,000 uniformly distributed random numbers between 0 and 1. Previous numbers should have no influence on future numbers: """
    # add 20 random numbers between 0 and 1
    for i in range(20):
        prompt += str(np.random.rand()) + " "

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
        random_numbers += [float(num) for num in completion.result.split()[:-1]]
    except:
        continue
    print(len(random_numbers))

random_numbers = random_numbers[:10000]

# save the random numbers to a file
with open('random_numbers.txt', 'w') as f:
    for num in random_numbers:
        f.write(str(num) + '\n')

# plot the distribution of the random numbers
import matplotlib.pyplot as plt

plt.hist(random_numbers, bins=100)
plt.show()
