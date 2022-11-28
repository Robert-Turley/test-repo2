from flask import Flask, render_template

app = Flask(__name__)


# FIRST METHOD
# @app.route('/info')
# @app.route('/info/<name>')
# @app.route('/info/<name>/<age>')
# def info(name="Bob", age=37):
#     return f"This is {name}'s page.  {name} is {age} years old."

# SECOND METHOD
@app.route('/')
def hello_world():
    apple = 6
    return render_template('index.html', num=apple)

# @app.route('/test')
# def test_1(name="Bob", age=37):
#     return render_template('index.html')

@app.route('/info')
def info_1(name="Bob", age=37):
    return f"This is {name}'s page.  {name} is {age} years old."

@app.route('/info/<name>')
def info_2(name, age=45):
    return f"This is {name}'s page.  {name} is {age} years old."

@app.route('/info/<name>/<int:age>')
def info_3(name, age):
    return f"This is {name}'s page.  {name} is {age} years old."

@app.route('/info/<name>/<age>')
def info_4(name, age):
    return f"This is an error page - {age} is not an integer."

@app.route('/take_action/<int:num1>/<int:num2>')
def info_5(num1, num2):
    return render_template('info_5.html', num1=num1, num2=num2)

@app.route('/list')
def some_list():
    shopping_list = ['Eggs', 'Milk', 'Bread', 'Cheese', 'Wine']
    return render_template('shopping.html', shopping_list=shopping_list)

if __name__ == "__main__":
    app.run(debug=True)