from flask import Flask,render_template,jsonify

app = Flask(__name__)
data =[
    {'title':'Commander'},
    {'title':'Weaponist'},
    {'title':'Buster'}
]
@app.route("/")
def home():
    return render_template('home.html',data=data)

@app.route("/api/data")
def api():
    return jsonify(data)

if __name__=="__main__":
    app.run(
            host='0.0.0.0', 
            debug=True,
            )