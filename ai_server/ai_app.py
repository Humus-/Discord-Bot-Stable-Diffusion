import os
from flask import Flask, render_template, request
from flask import Response
from ctransformers import AutoModelForCausalLM
import torch


ENV = 'dev'

# gonna make the flags as a config parameter later. Maybe even a pub sub thing for the server
FLAG_CHAT = 'chat'
FLAG_IMAGE = 'image'
MODEL_FALGS = {
	FLAG_CHAT: True,
	FLAG_IMAGE: False
}

llm_obj = None
stable_diffusion_base_obj = None
stable_diffusion_refiner_obj = None

def start_models(self, force = False):
	# should we create it fresh, or if force is true, then we need to reinit
	if MODEL_FALGS[FLAG_CHAT]:
		start_chat_model()
	else:
		start_stable_diffusion()

def start_chat_model():
	global llm_obj

	# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
	llm_obj = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
		model_file="mistral-7b-instruct-v0.1.Q3_K_L.gguf",
		model_type="mistral",
		gpu_layers=50)

def start_stable_diffusion():
	from diffusers import DiffusionPipeline

	global stable_diffusion_base_obj
	global stable_diffusion_refiner_obj
	stable_diffusion_base_obj = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
		torch_dtype=torch.float16,
		use_safetensors=True,
		variant="fp16")
	stable_diffusion_base_obj.to("cuda")

	stable_diffusion_refiner_obj = DiffusionPipeline.from_pretrained(
		"stabilityai/stable-diffusion-xl-refiner-1.0",
		text_encoder_2=stable_diffusion_base_obj.text_encoder_2,
		vae=stable_diffusion_base_obj.vae,
		torch_dtype=torch.float16,
		use_safetensors=True,
		variant="fp16",
	)

	stable_diffusion_refiner_obj.to("cuda")


# run after flask startup but before first request.
class ModelRunnerFlask(Flask):
	def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
		if not (app.debug or os.environ.get("FLASK_ENV") == "development") or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
		# if os.getenv('WERKZEUG_RUN_MAIN') == 'true':
		# the app could reload, but this won't be executed again
			with self.app_context():
				# TODO: make this multi threaded?
				self.logger.info("Loading the model")
				start_models(force = False)

		super(ModelRunnerFlask, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

app = ModelRunnerFlask(__name__)

# might need this to add bigger model later.
if ENV == 'dev':
	app.debug = True
	print('In dev section')
else:
	app.debug = False


@app.route('/')
def index():
	return "Yep. I'm alive"

@app.route('/text_chat', methods=['POST', 'GET'])
def text_chat():
	# TODO: Auth
	if request.method == 'POST':
		pass

	if not MODEL_FALGS[FLAG_CHAT]:
		message = "This service is not loaded on the current server."
		return {
		"bot_name": 'Admin',
		"message": message
	}

	print(f'values: {request.values}, args:{request.args}')
	content = request.values

	query = content.get('query', default = '')
	# TODO: handle blank
	# "List the top 20 most famous presidents of the United states."
	print(f'query: {query}')
	message = "Yo boi, how you doing? Looks like my synthetic brain is not active yet."
	bot_name = "None"
	if llm_obj:
		bot_name = llm_obj.model_type
		message = llm_obj(query)
		print(f'message: {message}')
	# return render_template('insert_success.html', message='Application Rejected!')
	return {
		"bot_name": bot_name,
		"message": message
	}


@app.route('/img_chat', methods=['POST'])
def image_chat():
	# TODO: Auth
	if request.method == 'POST':
		content = request.values

		query = content.get('query', default = '')
		# TODO: Handle blank
		return {
			"image": "asdf"
		}

if __name__ == '__main__':
	app.run()



# !pip install diffusers -qq
# !pip install invisible_watermark transformers accelerate safetensors -qq

# from diffusers import DiffusionPipeline
# import torch
# base = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
#                                          torch_dtype=torch.float16,
#                                          use_safetensors=True,
#                                          variant="fp16")
# base.to("cuda")


# refiner = DiffusionPipeline.from_pretrained(
#     "stabilityai/stable-diffusion-xl-refiner-1.0",
#     text_encoder_2=base.text_encoder_2,
#     vae=base.vae,
#     torch_dtype=torch.float16,
#     use_safetensors=True,
#     variant="fp16",
# )

# refiner.to("cuda")


# n_steps = 40
# high_noise_frac = 0.8

# prompt = "A majestic lion jumping from a big stone at night"

# # run both experts
# image = base(
#     prompt=prompt,
#     num_inference_steps=n_steps,
#     denoising_end=high_noise_frac,
#     output_type="latent",
# ).images

# # image = image[0]

# image = refiner(
#     prompt=prompt,
#     num_inference_steps=n_steps,
#     denoising_start=high_noise_frac,
#     image=image,
# ).images[0]

# image