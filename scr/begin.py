# Import prerequisite libraries
import os
import openai

# Setting the API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Perform tasks using OpenAI API
client = openai.OpenAI()  # Create an OpenAI client
client.models.list()  # List available models
teste