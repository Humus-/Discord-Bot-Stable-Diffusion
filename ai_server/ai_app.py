import os
from flask import Flask, render_template, request
from flask import send_file
from flask import Response

from models.mistralModel import MistralModel

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
		shouldTryInitChatModel = force or not (self.chat_model and self.chat_model.isInited())
		if MODEL_FALGS[FLAG_CHAT] and shouldTryInitChatModel:
			print(f'intit now: {self.chat_model}')
			if self.chat_model:
				print(f'None?: {self.chat_model}')
				self.chat_model.cleanup()

			self.chat_model = MistralModel(q = 4)
			self.chat_model.setup_model()
			
			# start_chat_model()

		# create it fresh, or if force is true, then we need to reinit
		shouldTryInitImageModel = force or not (self.image_model and self.image_model.isInited())
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

	if app.chat_model:
		message = app.chat_model.inference(query)
		print(f'message: {message}')
		return message

	message = "Yo boi, how you doing? Looks like my synthetic brain is not active yet."
	return {
		"bot_name": 'Admin',
		"response": 'This service is not loaded on the current server.'
	}


@app.route('/img_chat', methods=['POST', 'GET'])
def image_chat():
	# TODO: Auth
	if not MODEL_FALGS[FLAG_IMAGE]:
		message = "This service is not loaded on the current server."

		response_payload = {
			"bot_name": 'Admin',
			"message": message
		}
		return Response(response_payload, status = 200, mimetype = 'application/json')


	return send_file('../stable-diffusion-images-generation.png')  # mimetype='image/gif'

		return Response(response_payload, status = 200, mimetype = 'application/json')


	return send_file('../stable-diffusion-images-generation.png')  # mimetype='image/gif'

	# if request.method == 'POST':
	# 	content = request.values

	# 	query = content.get('query', default = '')
	# 	# TODO: Handle blank
	# 	return {
	# 		"image": "asdf"
	# 	}

if __name__ == '__main__':
	app.run()
