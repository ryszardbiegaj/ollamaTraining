
# llm = Ollama(model="deepseek-r1:14b", base_url="http://192.168.50.74:11434")

from ollama import chat
from ollama import ChatResponse
from ollama import Client

client = Client(
    host =  'http://192.168.50.74:11434'
)
response = client.chat(model='deepseek-r1:14b', messages=[
  {
    'role': 'user',
    'content': 'Create a REST controller class in Java for a Spring Boot 3.4 application. This class should handle GET and POST requests, and include security and configuration annotations.',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
