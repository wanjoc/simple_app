import os

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    hostname = os.environ.get('HOSTNAME', 'localhost')
    port = int(os.environ.get('PORT', 8080))
    debug = bool(os.environ.get('DEBUG', True))
    app.run(host=hostname, port=port, debug=debug)

