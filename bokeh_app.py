from flask import Flask, render_template
from bokeh.embed import server_document

application = Flask(__name__)

@application.route("/")
def index():
    # tag = server_document(url=r'/bokeh', relative_urls=True)
    tag = server_document(url='http://sise.dis.eafit.edu.co/bokeh')
    # tag = server_document(url='http://192.168.10.130:5006/bokeh')
    return render_template('index.html', tag=tag, context=Flask)

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)