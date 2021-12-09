from flask import Flask,render_template
from data import Results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon',methods=['GET'])
def pokemon():
    return render_template('pokemon.html', Results=Results)


@app.route('/game',methods=['GET'])
def game():
    return render_template('game.html')

if __name__=='__main__':
    app.run(debug=True)


