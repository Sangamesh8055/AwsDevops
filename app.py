from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    input_value = float(request.form['input_value'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']

    # Simple unit conversion logic (you can replace this with your own logic)
    if from_unit == 'miles' and to_unit == 'kilometers':
        result = input_value * 1.60934
    elif from_unit == 'kilometers' and to_unit == 'miles':
        result = input_value / 1.60934
    else:
        result = input_value  # Default to the same value if units are not recognized

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
