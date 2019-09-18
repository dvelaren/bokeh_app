import logging
from flask import Flask, render_template
from bokeh.embed import server_document

app = Flask(__name__)

@app.route("/")
def index():
    tag = server_document(url=r'/bokeh', relative_urls=True)
    return render_template('index.html', tag=tag)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)