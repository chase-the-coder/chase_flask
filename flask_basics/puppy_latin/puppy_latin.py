from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> write the puppy name to be translated into latin.</h1>'


@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1] == 'y':
        puppy_name_list = list(name.capitalize())
        puppy_name_list.pop()
        return '<h1>Your name is {}</h1>'.format(''.join(puppy_name_list) +
                                                 'iful')
    else:
        return '<h1>Your name is {}</h1>'.format(name.capitalize() + 'y')


if __name__ == '__main__':
    app.run()