# from flask import Flask, render_template, request
# # import joblib

# app = Flask(__name__)

# @app.route('/')
# def base():
#     return render_template('home.html')
# @app.route('/')
# @app.route("/")
# def contact():
#   return ('contact.html')

# # @app.route('/predict')
# # def predict():
# #    return
# #     # print("hello")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/porfolio")
def porfolio():
    return render_template("porfolio.html")
if __name__  == "__main__":
    app.run(debug=True)