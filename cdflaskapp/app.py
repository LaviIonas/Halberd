from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    sitename =  "credibleDEV Test"
    return render_template('index.html', sitename=sitename)

if __name__ == '__main__':
    app.run()
