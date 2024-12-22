from flask import Flask,render_template,jsonify,request
from database import load_data,load_job,insert_application
app = Flask(__name__)

@app.route("/")
def home():
    data = load_data()
    return render_template('home.html',data=data)

@app.route("/api/data")
def api():
    return jsonify(load_data())

@app.route("/job/<id>")
def job(id):
    job = load_job(id)
    return render_template('jobs.html',job=job)

@app.route('/job/<id>/apply', methods=['POST'])
def apply(id):
    data = request.form
    job = load_job(id)
    insert_application(id,data)
    return render_template('applied.html',job=job,data=data)
    

if __name__=="__main__":
    app.run(
            host='0.0.0.0', 
            debug=True,
            )