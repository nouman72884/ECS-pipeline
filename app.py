from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Say hello to Flask !--! now pipeline is aslo deployed by script >> testing for change "Date::3-3-2021" <<-! nginx is working as a reverse proxy for our app'

app.run(host='0.0.0.0', port=5000)

