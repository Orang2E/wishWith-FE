from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("review_detail.html")
@app.route('/name')
def name():
	return "My name is yejin!"
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)