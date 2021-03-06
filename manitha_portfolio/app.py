from flask import Flask, render_template, url_for

#instantiate the flask app
app = Flask(__name__,template_folder='templates')

#create each of the routes. The home page route
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

if __name__=="__main__":
	app.run(debug= True)
