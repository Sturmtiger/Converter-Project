from flask import Flask, render_template, request
import numeralfuncs
from dboperations import db_read
app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/get-converted-number', methods=['POST'])
def convert():
    num = request.form['number']
    try:
        if num.isalpha():  # если буквы, конверт. в римские
            converted_num = numeralfuncs.get_arabic(num)
            return render_template('menu.html', num=num.upper(), conv_num=converted_num)
        elif num.isdigit():  # если число, конверт. в арабские
            converted_num = numeralfuncs.get_roman(int(num))
            return render_template('menu.html', num=num, conv_num=converted_num)

    except Exception as e:
        print('ERROR TYPE:', e.__class__.__name__)
        msg = 'Invalid syntax!'
        return render_template('menu.html', num=num, error=msg)
    else:
        msg = 'Invalid syntax!'
        return render_template('menu.html', error=msg)

@app.route('/bd-data')  # лог запросов
def bd_data():
    data = db_read()
    return render_template('bd_data.html', data=data)

if __name__ == '__main__':
    app.run()