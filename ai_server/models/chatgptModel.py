from .model import Model
from openai import OpenAI

class ChatGPTModel(Model):
	def __init__(self, useRefiner = True):
		Model.__init__(self)
		self.name = 'chat-gpt'
		self.description = 'Chat GPT'
		self.model_version = "gpt-4.1"

	def setup_model(self):
		# Remember to set the open AI key before launch. 
		# TODO: Load the openAI key from config or env?
		client = OpenAI()

	def inference(self, prompt):
		response = client.responses.create(
		  model=self.model_version,
		  input=prompt
		)

		return response
