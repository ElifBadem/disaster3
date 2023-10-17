from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Merhaba, Azure Web App üzerinde çalýþan Flask uygulamasýna hoþ geldiniz!'

if __name__ == '__main__':
    app.run(debug=True)
