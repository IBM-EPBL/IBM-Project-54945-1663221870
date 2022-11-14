from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/login")
def login_page():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
