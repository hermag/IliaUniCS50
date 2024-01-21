from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True #This line allows you to refresh the flaskapp right after updating the html content

@app.route('/')
def root():
    # Render the HTML template
    return render_template('index.html')

@app.route('/home')
def home():
    # Render the HTML template
    return render_template('home.html')

@app.route('/contact')
def contact():
    # Render the HTML template
    return render_template('contact.html')

@app.route('/recipes')
def recipes():
    # Render the HTML template
    return render_template('recipes.html')

if __name__ == '__main__':
    app.run(debug=True)