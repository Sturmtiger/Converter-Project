from flask import Flask, render_template, request
from numeralfuncs import get_roman, get_arabic
from dboperations import db_read, db_clear


app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/get-converted-number', methods=['POST']) # конвертация числа
def convert():
    num = request.form['input'].strip()  # запрос из формы с удалением пробелов
    try:
        if num.isalpha():  # если буквы, конверт. в римские
            converted_num = get_arabic(num)
            return render_template('menu.html', num=num.upper(), conv_num=converted_num)
        elif num.isdigit():  # если число, конверт. в арабские
            converted_num = get_roman(int(num))
            return render_template('menu.html', num=num, conv_num=converted_num)
    except Exception as e:
        # print('ERROR TYPE:', e.__class__.__name__)
        msg = 'Invalid syntax!'
        return render_template('menu.html', num=num, error=msg)
    else:
        msg = 'Invalid syntax!'
        return render_template('menu.html', error=msg)

@app.route('/db-data')  # история запросов
def db_data():
    data = db_read()
    return render_template('db_data.html', data=data)

@app.route('/db-data-cleared')  # очистка истории
def db_data_cleared():
    db_clear()
    return render_template('db_data.html')


if __name__ == '__main__':
    app.run()


