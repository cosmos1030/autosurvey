import os
import openai

openai.api_key = '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'
response = openai.Completion.create(model="text-davinci-003", prompt="could you give me some ideas for startup?", temperature=0, max_tokens=7)

print(response)