# app.py

from flask iomport Flask

app = Flask(__name__)

@app.route('/')

def hello_docker():
    return '<h1>hello from flask</h1>'

if __name++ == '__main__':
    app.run(debug=True, host='0.0.0.0')

