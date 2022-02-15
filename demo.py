# import os
# import openai

# # Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("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")
# print("open Ai")
# response = openai.Completion.create(engine="text-davinci-001", prompt="Say this is a test", max_tokens=6)


# # openai.api_key

import openai
openai.api_key = "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"
response = openai.Completion.create(engine="text-davinci-001", prompt="Say this is a test", max_tokens=6)
# # list engines
engines = openai.Engine.list()

# # print the first engine's id
print(engines.data[0].id)

print(response)

# # create a completion
# completion = openai.Completion.create(engine="ada", prompt="Hello world")

# # print the completion
# print(completion.choices[0].text)

