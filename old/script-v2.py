#GPU usage
from gpt4all import GPT4All

model_names = ['gpt4all-13b-snoozy-q4_0.gguf', 'mistral-7b-openorca.Q4_0.gguf', 'wizardlm-13b-v1.2.Q4_0.gguf', 'nous-hermes-llama2-13b.Q4_0.gguf', 'gpt4all-falcon-q4_0.gguf', 'orca-mini-3b-gguf2-q4_0.gguf']
print(model_names)

selected_model = model_names[1]

model = GPT4All(selected_model, device='gpu')
print ('Using model: ', selected_model)

glossary_codes = ['XXGVTXX:Requiring a defence under POCA (consent) if the value of the suspected money laundering falls below a value of £3,000',
'XXPRFXX:Professional enablers - persons providing professional services or specialist knowledge that wittingly or unwittingly facilitates money laundering.',
'XXTBMLXX:Trade-based money laundering (TBML)',
'XXPROPXX:Purchase, sale and rental of real estate property',
'XXVAXX:Virtual assets',
'XXMLTMXX:Money laundering through markets',
'XXSNEXX:Money laundering linked to sanctioned entities',
'XXSATXX:HMRC Self-Assessment Tax Refund system',
'XXGPSXX:Government Priority Schemes',
'XXCVDXX:General code',
'XXTEOSXX:Tax evasion offshore',
'XXTEUKXX:Tax evasion UK-based',
'XXF1XX:Proceeds from benefit fraud',
'XXF2XX:Excise evasion (duty on alcohol, tobacco, fuel etc.)',
'XXF3XX:Corporate tax evasion (tax evasion by businesses, corporations)',
'XXF4XX:Personal tax evasion (tax evasion by individuals e.g. income tax)',
'XXF5XX:VAT fraud e.g. carousel, Missing Trader Intra-Community (MTIC) fraud',
'XXF9XX:Frauds against private sector',
'XXD9XX:Bribery and corruption',
'XXV2XX:Risk to vulnerable adults',
'XXV3XX:Risk to children – particularly including sexual abuse and exploitation',
'XXD9XX:Bribery and corruption',
'XXILTXX:Illegal lotteries',
'XXFIREXX:Firearms',
'XXDRUXX:Illegal supply of drugs',
'XXOICXX:Organised immigration crime',
'XXMSHTXX:Modern slavery/human trafficking',
'XXPCPXX:Counter-proliferation',
'XXVICTXX:Where the purpose of the activity is to return money to a victim of crime']

for i in range(len(glossary_codes)):
    statement = glossary_codes[i].split(':')
    message = 'Here is some new information about Suspicious Activity Reports to retain. If a Suspicious Activity Report was filed, that detailed activity related to ' + statement[1] + ', then it should be classified with a glossary code of ' + statement[0] + '. If you are asked to classify a report that describes activities that relate to ' + statement[1] + ' please provide the glossary code ' + statement[0] + ' as a suitable response.'
    template = '### Human: \n' + message + '\n### Assistant: '
    output = model.generate(template, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
    print('> '  + output)
    
    
f = open("./glossary-codes.txt", "r")
finput = f.readlines()
#finput = ' '.join(finput).replace('\n',' ').replace('\t',' ')
#print (finput)
  

# importing required modules 
from PyPDF2 import PdfReader 
reader = PdfReader('glossary-codes.pdf') 
for i in range(len(reader.pages)):#
    print ("Page", i)
    page = reader.pages[i] 
    text = page.extract_text()
    input = 'Here is some new information about suspicious activity reports and the associated glossary codes: ' + text + '. No response is required, however you should retain this knowledge and use it in later questioning.'
    template = '### Human: \n' + input + '\n### Assistant: '
    output = model.generate(template, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
    print('> '  + output)

with open("conversation.txt", "w") as myfile:
    myfile.write("#####")

while True:
    question_input = input('# ')
    if question_input == "exit":
        print ("Bye for now...")
        break
    else:
        template = '### Human: \n' + question_input + '\n### Assistant: '
        output = model.generate(template, max_tokens=4096, temp=0.7, top_k=40, top_p=0.4, repeat_penalty=1.18, repeat_last_n=64)
        print ('> '  + output)
        with open("conversation.txt", "a") as myfile:
            myfile.write("#" + question_input + '\n >' + output '\n')
    