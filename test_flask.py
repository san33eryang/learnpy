
from flask import  Flask

app = Flask(__name__)
num = 0

@app.route('/')
def index():
    global num
    num += 1
    return '<h1>Hello Little Sheep!!! - ' + str(num)+'</h1>'

if __name__ == '__main__':
    app.run(debug=True)