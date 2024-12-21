from flask import Flask,render_template,jsonify
from database import load_data,load_job
app = Flask(__name__)

@app.route("/")
def home():
    data = load_data()
    return render_template('home.html',data=data)

@app.route("/api/data")
def api():
    return jsonify(load_data())

@app.route("/api/data/<id>")
def job(id):
    job = load_job(id)
    if not job == []:
        return jsonify(job)
    else:
        return jsonify('invalid id')

        

if __name__=="__main__":
    app.run(
            host='0.0.0.0', 
            debug=True,
            )