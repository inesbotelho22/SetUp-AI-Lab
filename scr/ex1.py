# Import prerequisite libraries
import os
from dotenv import find_dotenv, load_dotenv

import openai

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Setting the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

test_variable = os.getenv("teste")
print(test_variable)

# Define the user prompt message
prompt = "Hello!"
# Create a chatbot using ChatCompletion.create() function
completion = openai.ChatCompletion.create(
  # Use GPT 3.5 as the LLM
  model="gpt-3.5-turbo",
  # Pre-define conversation messages for the possible roles 
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
  ]
)
# Print the returned output from the LLM model
print(completion.choices[0].message)
