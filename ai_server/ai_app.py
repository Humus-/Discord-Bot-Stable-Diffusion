import os
from flask import Flask, render_template, request
from ctransformers import AutoModelForCausalLM


ENV = 'dev'

# gonna make the flags as a config parameter later. Maybe even a pub sub thing for the server
FLAG_CHAT = 'chat'
FLAG_IMAGE = 'image'
MODEL_FALGS = {
	FLAG_CHAT: True,
	FLAG_IMAGE: False
}

# run after flask startup but before first request.
class ModelRunnerFlask(Flask):
	def init_vars(self):
		# don't want to use constructor. In case new update adds more arguments
		self.chat_model = None
		self.image_model = None

	def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
		self.init_vars()

		if not (app.debug or os.environ.get("FLASK_ENV") == "development") or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
		# if os.getenv('WERKZEUG_RUN_MAIN') == 'true':
		# the app could reload, but this won't be executed again
			with self.app_context():
				# TODO: make this multi threaded?
				self.logger.info("Loading the model")
				# start_model()
				self.start_models(force = False)

		super(ModelRunnerFlask, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

	def start_models(self, force = False):
		# create it fresh?, or if force is true, then we need to reinit
		shouldTryInitChatModel = (self.chat_model and self.chat_model.isInited()) or force
		if MODEL_FALGS[FLAG_CHAT] and shouldTryInitChatModel:
			if self.chat_model:
				self.chat_model.cleanup()

			self.chat_model = MistralModel()
			self.chat_model.setup_model()
			
			# start_chat_model()

		# create it fresh, or if force is true, then we need to reinit
		shouldTryInitImageModel = (self.image_model and self.image_model.isInited()) or force
		if MODEL_FALGS[FLAG_IMAGE] and shouldTryInitImageModel:
			if self.image_model:
				self.image_model.cleanup()

			self.image_model = StableDiffusion()
			self.image_model.setup_model()

			# start_stable_diffusion()

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

	content = request.values

	query = content.get('query', default = '')
	# TODO: handle blank
	# eg: "List the top 20 most famous presidents of the United states."
	print(f'query: {query}')

	if self.chat_model:
		message = self.chat_model.inference()
		print(f'message: {message}')
		return message

	message = "Yo boi, how you doing? Looks like my synthetic brain is not active yet."
	return {
		"bot_name": 'Admin',
		"response": 'This service is not loaded on the current server.'
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
		return Response(response_payload, status = 200, mimetype = 'application/json')


	return send_file('../stable-diffusion-images-generation.png')  # mimetype='image/gif'

if __name__ == '__main__':
	app.run()