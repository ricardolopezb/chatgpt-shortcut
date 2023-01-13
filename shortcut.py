import openai
from dotenv import dotenv_values

config_vars = dotenv_values('.env')

openai.api_key = config_vars["API_KEY"]

while True:
    prompt = input("Input your prompt: ")
    if (prompt == 'exit') or (prompt == 'Exit'):
        exit()
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
    print(response.choices[0].text + "\n")