from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá mundoooooo!'
@app.route('/questao1')
def questao1():
    return render_template('questao1.html')

app.run(host='0.0.0.0', port=81, debug=True)