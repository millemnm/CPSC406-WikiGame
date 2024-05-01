
from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=)

# Set the parameters for your conversation
# prompt = ""

# Call the OpenAI API to generate a response
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="please return this list in order of how well they relate to the topic Apples: rain, emu, joshua tree, banana, eagle, orange, fence.",
  max_tokens=1000,
  temperature=0
)

# Print the response
print(response.strip())
