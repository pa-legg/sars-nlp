import gpt4all
gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
#gptj = gpt4all.GPT4All("ggml-gpt4all-l13b-snoozy")
#messages = [{"role": "user", "content": "Name 3 colors"}]

message = "You are providing the script for two robots, A and B. A has a young cheeky personality whilst B is more serious and older. You should write a script for the conversation between A and B, denoting each passage of text as either spoken by A or B. The script should be about 200 words. The conversation will begin with A asking the following statement: Do you like Super Mario Bros?"
#messages = [{"role": "user", "content": message}]

#gptj.chat_completion(messages)


token = gptj.generate(message)
print (token)


#from pygpt4all import GPT4All

#model = GPT4All("../language-models/ggml-gpt4all-l13b-snoozy.bin")

#def answer(question):
#    print ("Q: ", question)
#    print ("----------")
#    for token in model.generate(question, n_threads=4):
#        print(token, end='', flush=True)