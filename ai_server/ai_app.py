import os
from flask import Flask, render_template, request
from ctransformers import AutoModelForCausalLM


ENV = 'dev'

llm_obj = None
# gonna make the flags as a config parameter later. Maybe even a pub sub thing for the server
FLAG_CHAT = 'chat'
FLAG_IMAGE = 'image'
MODEL_FALGS = {
	FLAG_CHAT: True,
	FLAG_IMAGE: False
}

def start_model():
	# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
	global llm_obj
	llm_obj = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
		model_file="mistral-7b-instruct-v0.1.Q3_K_L.gguf",
		model_type="mistral",
		gpu_layers=50)


# run after flask startup but before first request.
class ModelRunnerFlask(Flask):
	def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
		if not (app.debug or os.environ.get("FLASK_ENV") == "development") or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
		# if os.getenv('WERKZEUG_RUN_MAIN') == 'true':
		# the app could reload, but this won't be executed again
			with self.app_context():
				# TODO: make this multi threaded?
				self.logger.info("Loading the model")
				start_model()

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