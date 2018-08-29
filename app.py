from flask import Flask, render_template, request
import numeralfuncs
app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/get-roman-number', methods=['POST'])
def get_roman():
    arabic = request.form['arabic']
    roman = numeralfuncs.get_roman(int(arabic))
    return render_template('menu.html', arabic=arabic, roman=roman)

@app.route('/get-arabic-number', methods=['POST'])
def get_arabic():
    roman = request.form['roman']
    arabic = numeralfuncs.get_arabic(roman)
    return render_template('menu.html', roman=roman, arabic=arabic)

# if __name__ == '__main__':
app.run(debug=True)