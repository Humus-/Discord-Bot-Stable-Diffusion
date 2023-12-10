from abc import abstractmethod
import torch

class Model:
	def __init__(self):
		self.name = 'Model'
		self.description = ''
		self.quant = 32 # default quantization
		self.model_obj = None

	# def __del__(self):
	# 	self.cleanup()

	@abstractmethod
	def setup_model(self):
		pass

	def isInited(self):
		return self.model_obj != None

	def getName(self):
		return self.name

	def getModelDetails(self):
		return {
			'name': self.name,
			'description': self.description,
			'quantization': self.quant
		}

	@abstractmethod
	def inference(self, query):
		pass

	def cleanup(self):
		del self.model_obj
		self.model_obj = None

		torch.cuda.empty_cache()