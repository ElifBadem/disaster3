from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Merhaba, Azure Web App �zerinde �al��an Flask uygulamas�na ho� geldiniz!'

if __name__ == '__main__':
    app.run(debug=True)
