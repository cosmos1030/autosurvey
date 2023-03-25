import os
import openai

openai.api_key = 'sk-04UZQObJaNSmYaJRt$$$$$$$$$$$$$$$$$$$o3jV'
prompt = input()
response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)

print(response)
# print(response["choices"][0]["text"])