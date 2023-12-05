class MistralModel(Model):
	def __init__(self, q):
		"""
		q - Quantization bits to be used, eg: 32 bit, 16 bit, 8 bit, 4 bit
		"""
		Model.__init__(self)
		self.name = 'Mistral'
		self.description = 'Mistral model for chat LLM'
		self.modelNamespace = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
		self.modelFile = "mistral-7b-instruct-v0.1.Q3_K_L.gguf"
		# TODO make the quantization configurable

	def setup_model(self):
		self.model_obj = AutoModelForCausalLM.from_pretrained(self.modelNamespace,
			model_file=self.modelFile,
			model_type="mistral",
			gpu_layers=50)

	def inference(self, prompt):
		result = {
			"response": 'No response'
			"other_details": 'None'
		}
		if self.isInited():
			result['response'] = self.model_obj(query)

		return result
