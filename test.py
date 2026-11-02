from flask import Flask

app: Flask = Flask(__name__)


@app.route("/<nume>")
def user(nume: str):
    return f'Salut {nume.capitalize()}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)