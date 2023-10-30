from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    principal = float(request.form['principal'])
    rate = float(request.form['rate'])
    time = float(request.form['time'])
    interest_type = request.form['interest_type']

    if interest_type == 'simple':
        interest = (principal * rate * time) / 100
    elif interest_type == 'compound':
        interest = principal * (1 + rate/100)**time - principal

    return render_template('results.html', principal=principal, rate=rate, time=time, interest=interest, interest_type=interest_type)

if __name__ == '__main__':
    app.run(debug=True)
