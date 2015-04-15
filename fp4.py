import os,json, math
from flask import Flask, render_template, request

app = Flask(__name__)

def ilford(x):
    if x <= 0.5:
        return x
    return 66.86823338 * 1.04081939 ** x - 67.19686994

def portra(time):
    return time + (0.5167 * math.log(time) - 0.2006) * time

@app.route("/")
def calcualte():
    time = request.args.get('time', None)
    stock = request.args.get('stock', 'fp4')
    if time:
        try:
            time = float(time)
            adjusted_time = time
            if stock == 'fp4' or stock == 'hp5':
                adjusted_time = ilford(time)
            elif stock == 'portra':
                adjusted_time = portra(time)
            return render_template('index.html',
                                   before=time,
                                   time=adjusted_time,
                                   shown="visible")
        except:
            return "couldn't understand your time, try again in seconds"
    else:
        return render_template("index.html",
                               shown="hidden")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
