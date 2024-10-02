from flask import Flask, render_template, jsonify
app = Flask(__name__)
import datetime

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def print_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('time.html', time=current_time)
@app.route('/get_time')
def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'time': current_time})
app.run(host='0.0.0.0',
        port=8080,
        debug=True)
