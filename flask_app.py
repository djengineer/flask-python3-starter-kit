from flask import Flask,  render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/page1/')
def page1():
    return render_template("page1.html")

if __name__ == '__main__':
    # run flask server on this machine's local host
    # works with cloud servers
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), use_reloader=False, debug=True)