from flask import Flask, render_template, request


app = Flask(__name__)

ENV = 'dev'

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
	if request.method == 'POST' or True:
		message = "Yo boi, how you doing?"
		# return render_template('insert_success.html', message='Application Rejected!')
		return {
			"bot_name": "none",
			"message": message
		}


@app.route('/img_chat', methods=['POST'])
def image_chat():
	# TODO: Auth
	if request.method == 'POST':
		# return render_template('insert_success.html', message='Application Rejected!')
		return {
			"image": "asdf"
		}


if __name__ == '__main__':
	app.run()