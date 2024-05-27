from flask import Flask, render_template, request, redirect, url_for
# Import the Maths package here
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

result = {'result':""}

@app.route("/sum", methods=["POST"])
# @app.route("/sum")
# def sum_route():
def sum_route(num1, num2):
    # num1 = float(request.args.get('num1'))
    # num2 = float(request.args.get('num2'))
    # Write your code here
    result['result'] = str(summation(num1, num2))
    return redirect(url_for("render_index_page"))

@app.route("/sub", methods=["POST"])
def sub_route(num1, num2):
    # num1 = float(request.args.get('num1'))
    # num2 = float(request.args.get('num2'))
    # Write your code here
    result['result'] = str(subtraction(num1, num2))
    return redirect(url_for("render_index_page"))

@app.route("/mul", methods=["POST"])
def mul_route(num1, num2):
    # num1 = float(request.args.get('num1'))
    # num2 = float(request.args.get('num2'))
    # Write your code here  
    result['result'] = str(multiplication(num1, num2))
    return redirect(url_for("render_index_page"))


@app.route("/")
def render_index_page():
    # Write your code here
    return render_template("index.html", result=result['result'])

@app.errorhandler(422)
def invalid_input(error):
    return ({"message": "Invalid input parameters"}, 422)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
