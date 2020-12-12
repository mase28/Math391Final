from flask import Flask, render_template, request
from euclideanAlgorithm import euclidean_gaus, euclidean_int, bezout, print_html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/integer", methods=["POST", "GET"])
def integer():
    if request.method == "POST":
        a = request.form["first"]
        b = request.form["second"]
        ret = euclidean_int(int(a), int(b))
        bez = bezout(ret)
        print_html(ret, bez)
        return render_template("output.html")
    else:
        return render_template("integer.html")

@app.route("/guassian", methods=["POST", "GET"])
def gaussian():
    if request.method == "POST":
        a_real = int(request.form["first_real"])
        a_imag = int(request.form["first_imag"])
        b_real = int(request.form["second_real"])
        b_imag = int(request.form["second_imag"])
        ret = euclidean_gaus(complex(a_real, a_imag), complex(b_real, b_imag))
        bez = bezout(ret)
        print_html(ret, bez)
        return render_template("output.html")
    else:
        return render_template("gaussian.html")

if __name__ == "__main__":
    app.run(debug=True)