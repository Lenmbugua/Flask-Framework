from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Build URL dynamically
@app.route('/success/<int:score>')
def success(score):
    return render_template('index.html')

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
