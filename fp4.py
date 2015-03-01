import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html",
                           shown="hidden")

def compensation(x):
    return 66.86823338 * 1.04081939 ** x - 67.19686994

@app.route("/calculate")
def calcualte():
    if request.args['time']:
        try:
            time = float(request.args['time'])
            return render_template('index.html',
                                   before=time,
                                   time=compensation(time),
                                   shown="visible")
        except:
            return "couldn't understand your time, try again in seconds"
    else:
        return render_template("index.html",
                               shown="hidden")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
