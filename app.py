from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

# Build URL dynamically
@app.route('/success/<int:score>')
def success(score):
    return "<html><body></body><h1>The result is passed</h1></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks are " + str(score)

# Results checker
@app.route('/results/<int:score>')
def results(score):
    result = ""
    if score < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score=score))

if __name__ == '__main__':
    app.run(debug=True)
