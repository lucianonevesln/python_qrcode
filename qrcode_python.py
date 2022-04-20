from flask import Flask, request, render_template
import qrcode


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def gera_qrcode():
    palavra = request.form['id_palavra']
    img = qrcode.make(palavra)
    img.save('venv/static/imagem.png')
    return render_template("index.html")


@app.route('/img', methods=['GET'])
def consulta_qrcode():
    return render_template('img.html')


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)