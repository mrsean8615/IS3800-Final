from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    title = 'IS3800 Final Project'
    return render_template('index.html', title = title)

if __name__ == "__main__":
    app.run(debug=True)
