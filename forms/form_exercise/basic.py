from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('username')
    return render_template('report.html', username=username)


if __name__ == '__main__':
    app.run()