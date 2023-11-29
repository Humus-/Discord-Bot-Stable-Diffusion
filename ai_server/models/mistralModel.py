class MistralModel(Model):
	def __init__(self, q):
		"""
		q - Quantization bits to be used, eg: 32 bit, 16 bit, 8 bit, 4 bit
		"""
		Model.__init__(self)
		self.name = 'Mistral'
		self.description = 'Mistral model for chat LLM'
		self.