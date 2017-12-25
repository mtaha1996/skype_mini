# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template
from flask_sse import sse
from channel import channel

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
app.register_blueprint(channel, url_prefix='/channel')


@app.route("/")
def page():
    return render_template("login.html")


@app.route("/create/<Cid>")
def create_page(Cid):
    return render_template("create.html", name=Cid)


@app.route("/join/<Cid>")
def join_page(Cid):
    return render_template("join.html", name=Cid)

