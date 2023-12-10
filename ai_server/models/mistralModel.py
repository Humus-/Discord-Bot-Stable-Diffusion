from .model import Model
from ctransformers import AutoModelForCausalLM

class MistralModel(Model):
	def __init__(self, q):
		"""
		q - Quantization bits to be used, eg: 32 bit, 16 bit, 8 bit, 4 bit
		"""
		super().__init__()

		self.name = 'Mistral'
		self.description = 'Mistral model for chat LLM'
		self.modelNamespace = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
		self.modelFile = "mistral-7b-instruct-v0.1.Q3_K_L.gguf"
		# TODO make the quantization configurable

	def setup_model(self):
		print(f'inited model')

		# config = {'temperature':0.00, 'context_length':4000,}
		# self.model_obj = CTransformers(model='TheBloke/Mistral-7B-codealpaca-lora-GGUF',
		#								model_type='mistral',
		#								config=config,,
		#								#stream=True,
		#								callbacks=[async_handler]
		#								)

		self.model_obj = AutoModelForCausalLM.from_pretrained(self.modelNamespace,
			model_file=self.modelFile,
			model_type="mistral",
			gpu_layers=50)

	def inference(self, prompt):
		# prompt = PromptTemplate.from_template("You are a gamer, respond to the following : {query}")
		# chain = LLMChain(llm = self.model_obh, prompt = prompt)

		# return Response(chain.run(query))



		result = {
			"response": 'No response',
			"other_details": 'None',
			'bot_name': "Mistral"
		}
		if self.isInited():
			result['response'] = self.model_obj(prompt)

		return result
