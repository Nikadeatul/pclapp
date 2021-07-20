from flask import Flask,render_template,request

app = Flask(__name__)

app.route("/")
def home():
    return render_template("home.html")

app.route("/booked",methods=["GET","POST"])
def book():
    if (request.method=="GET"):
        return render_template("home.html")
    elif (request.method=="POST"):
        source=request.form["deptj"]
        dest=request.form["retj"]
        jdate=request.form["date"]
        rdate=request.form["retd"]
        return render_template("book.html")



if __name__ == "__main__":
    app.run(debug=True, port=5000)

