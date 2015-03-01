import os,json
from flask import Flask, render_template, request

app = Flask(__name__)

def compensation(x):
    if x <= 0.5:
        return x
    return 66.86823338 * 1.04081939 ** x - 67.19686994

@app.route("/")
def calcualte():
    time = request.args.get('time', None)
    if time:
        try:
            time = float(time)
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
