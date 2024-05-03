import pprint
import google.generativeai as palm
import numpy as np
import matplotlib.pyplot as plt
import argparse
import random

def main():
    palm.configure(api_key="AIzaSyDX1QeBCJxRnQaWBxHzAW2NSIPjZDqxsP4")
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    phrases = []
    with open("phrases.txt", 'w') as f:
        while len(phrases) < 10000:
            prompt = "Randomly pick 10000 words, w, from the list of words: [\"os\", \"torch\", \"numpy\", \"kubernetes\"] to form a phrase \"import w\". Your respond should be in form of \"import w\". Previous choice should have no influence on future choices."

            response = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=0,
                max_output_tokens=800,
            )
            try:
                result = str(response.result)
                result = result.replace("import", "")
                print(result)
                result = result.split()
                
                phrases += result[:-1]
            except:
                continue
        for phrase in phrases:
            f.write(phrase + "\n")

if __name__ == "__main__":
    main()
