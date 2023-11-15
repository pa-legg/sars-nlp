#GPU usage
from gpt4all import GPT4All
from datetime import datetime

from termcolor import colored

model_names = ['gpt4all-13b-snoozy-q4_0.gguf', 'mistral-7b-openorca.Q4_0.gguf', 'wizardlm-13b-v1.2.Q4_0.gguf', 'nous-hermes-llama2-13b.Q4_0.gguf', 'gpt4all-falcon-q4_0.gguf', 'orca-mini-3b-gguf2-q4_0.gguf']
#print(model_names)

selected_model = model_names[1]

prompt_colour = 'green'
response_colour = 'magenta'

model = GPT4All(selected_model, device='gpu')
print ('Using model: ', selected_model)

glossary_codes = [
'XXS99XX:Request for a defence under POCA (consent)',
'XXGVTXX:Requiring a defence under POCA (consent) if the value of the suspected money laundering falls below a value of £3,000',
'XXPRFXX:Relates to person(s) providing professional services or specialist knowledge that wittingly or unwittingly facilitates money laundering',
'XXTBMLXX:Trade-based money laundering (TBML)',
'XXPROPXX:Relates to purchases and rental of real estate property',
'XXVAXX:Virtual assets',
'XXMLTMXX:Money laundering through markets',
'XXSNEXX:Money laundering linked to sanctioned entities',
#'XXSATXX:HMRC Self-Assessment Tax Refund system',
#'XXGPSXX:Government Priority Schemes',
#'XXCVDXX:General code',
'XXTEOSXX:Tax evasion offshore',
'XXTEUKXX:Tax evasion UK-based',
#'XXF1XX:Proceeds from benefit fraud',
'XXF2XX:Excise evasion (duty on alcohol, tobacco, fuel etc.)',
'XXF3XX:Corporate tax evasion (tax evasion by businesses, corporations)',
'XXF4XX:Personal tax evasion (tax evasion by individuals e.g. income tax)',
'XXF5XX:VAT fraud e.g. carousel, Missing Trader Intra-Community (MTIC) fraud',
#'XXF9XX:Frauds against private sector',
'XXD7XX:International Politically Exposed Persons (PEPs)',
'XXD8XX:UK Domestic Politically Exposed Persons (PEPs)',
'XXD9XX:Bribery and corruption',
#'XXV2XX:Risk to vulnerable adults',
#'XXV3XX:Risk to children – particularly including sexual abuse and exploitation',
#'XXILTXX:Illegal lotteries',
'XXFIREXX:Firearms',
'XXDRUXX:Illegal supply of drugs',
#'XXOICXX:Organised immigration crime',
'XXMSHTXX:Modern slavery/human trafficking',
#'XXPCPXX:Counter-proliferation',
#'XXVICTXX:Where the purpose of the activity is to return money to a victim of crime'
]

conversation_history = './history/conversation_history_' + str(datetime.now()) + '.txt'

system_template = 'A conversation between a user interested in classifying Suspicious Activity Reports against their glossary codes and an artificial intelligence assistant that understands about Suspicious Activity Reports and the possible glossary codes that are available.'
#system_template = 'A chat between a curious user and an artificial intelligence assistant.'
prompt_template = '### Human: {0}\n### Assistant: '


with model.chat_session(system_template, prompt_template):
    message = "The UK Financial Intelligence Unit (UKFIU), a part of the National Crime Agency, publish the Suspicious Activity Report (SAR) Glossary Codes and Reporting Routes. I will go on to inform you of different codes related to different types of criminal activity."
    print (colored(message, prompt_colour))
    output = model.generate(message, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
    print (colored('>>> '  + output, response_colour))
    
    for i in range(len(glossary_codes)):
        statement = glossary_codes[i].split(':')
        
        message = 'Here is some new information. The glossary code ' + statement[0] + ' relates to ' + statement[1] + '.'
        print (colored(message, prompt_colour))
        output = model.generate(message, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
        print (colored('>>> '  + output, response_colour))
    
    with open(conversation_history, "w") as myfile:
        myfile.write("#####")
        
    while True:
        question_input = input('# ')
        if question_input == "exit":
            print (colored('>>> Bye for now', response_colour))
            break
        else:
            print (colored(question_input, prompt_colour))
            output = model.generate(question_input, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
            print (colored('>>> '  + output, response_colour))
            with open(conversation_history, "a") as myfile:
                myfile.write("#" + question_input + '\n >' + output + '\n')
