from flask import Flask,render_template

app = Flask(__name__)
data =[
    {'title':'Commander'},
    {'title':'Weaponist'},
    {'title':'Buster'}
]
@app.route("/")
def home():
    return render_template('home.html',data=data)

if __name__=="__main__":
    app.run(
            host='0.0.0.0', 
            debug=True,
            )