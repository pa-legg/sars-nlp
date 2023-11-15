#GPU usage
from gpt4all import GPT4All

model_names = ['gpt4all-13b-snoozy-q4_0.gguf', 'mistral-7b-openorca.Q4_0.gguf', 'wizardlm-13b-v1.2.Q4_0.gguf', 'nous-hermes-llama2-13b.Q4_0.gguf', 'gpt4all-falcon-q4_0.gguf', 'orca-mini-3b-gguf2-q4_0.gguf']
print(model_names)

model = GPT4All(model_names[5], device='gpu')
print ('Using model: ', model_names[5])

output = model.generate("The capital of France is ", max_tokens=3)
print(output)

while True:
    question = input('# ')
    if question == "exit":
        break
    else:
        output = model.generate(question, max_tokens=100)
        print ('> '  + output)
    