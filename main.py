from flask import Flask, render_template, request, redirect,session
from datetime import datetime
app = Flask(__name__)
app.secret_key="1234567890"


@app.get("/train")
def trainList():
    return render_template("base.html")

@app.get("/train/trains")
def trains():
    return render_template("trains.html")

@app.route("train/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        companyName = request.form.get("companyName")
        ownerName = request.form.get("ownerName")
        rollNumber = request.form.get("rollNumber")
        ownerEmail = request.form.get("ownerEmail")
        accessCode = request.form.get("accessCode")
        session["ownerName"]=ownerName
        session["accessCode"]=accessCode
        if "ownerName" in session and "accessCode" in session:
            return redirect("/train/trains")
    else:
        if "ownerName" in session and "accessCode" in session:
            return redirect("/train/trains")
        return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
