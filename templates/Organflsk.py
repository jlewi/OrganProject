from flask import Flask, render_template

app = Flask(__name__)
#import pdb; pdb.set_trace()
@app.route("/")
def home():
    return render_template("index1.html")

if __name__ == '__main__':
    app.run()