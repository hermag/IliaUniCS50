from flask import Flask, request, render_template 

app = Flask(__name__) 
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST']) 
def index(): 
	if request.method == 'POST': 
		# Retrieve the text from the textarea 
		text = request.form.get('textarea') 

		# Print the text in terminal for verification 
		print(text) 

	return render_template('home.html') 


if __name__ == '__main__': 
	app.run() 
