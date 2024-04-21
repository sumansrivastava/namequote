from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Function to read sample meanings from the mounted file
def read_sample_meanings():
    with open('/etc/sample-meanings/sample_meanings.json') as f:
        return json.load(f)

# Load sample meanings from the mounted file
SAMPLE_MEANINGS = read_sample_meanings()

@app.route('/')
def home():
    return render_template('index_input.html')

@app.route('/meaning', methods=['POST'])
def get_meaning():
    name = request.form.get('name')
    meaning = SAMPLE_MEANINGS.get(name, f"No meaning found for {name}")
    return render_template('index_result.html', meaning=meaning, name=name)

@app.route('/reset')
def reset():
    return render_template('index_input.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
