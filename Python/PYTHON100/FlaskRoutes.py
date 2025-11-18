from flask import Flask
app = Flask(__name__)

@app.route("/")           
def home():
    return "This is Home"

@app.route("/about")      
def about():
    return "This is About page"

@app.route("/contact")   
def contact():
    return "This is Contact page"

if __name__ == "__main__":
    app.run(debug=True)
