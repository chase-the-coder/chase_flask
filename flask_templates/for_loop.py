from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_list = list(range(1, 6))
    return render_template('for_loop.html', my_list=my_list)


if __name__ == '__main__':
    app.run(debug=True)
