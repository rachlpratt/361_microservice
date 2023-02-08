from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)


@app.route('/due/<due_date>', methods=['GET'])
def generate_message(due_date):
    # Get integer values for month, day, year
    month = int(due_date[:2])
    day = int(due_date[3:5])
    year = int(due_date[6:])

    # Get today's date and format due_date
    today = date.today()
    new_due_date = date(year, month, day)

    # Calculate number of days between today and due_date
    diff = new_due_date - today
    days = diff.days

    # Get return message based on difference between today and due_date
    match days:
        case 0:
            message = 'today'
        case -1:
            message = '1 day ago'
        case 1:
            message = 'in 1 day'
        case 7:
            message = 'in 1 week'
        case -7:
            message = '1 week ago'
        case -14 | -21:
            message = f'{int(days / -7)} weeks ago'
        case 14 | 21:
            message = f'in {int(days / 7)} weeks'
        case _ if -1 > days > -21:
            message = f'{days * -1} days ago'
        case _ if 1 < days < 21:
            message = f'in {days} days'
        case _ if days < -21:
            message = f'{days * -1} days ago'
        case _:
            message = f'{due_date}'
    return jsonify(message=message)


if __name__ == '__main__':
    app.run(port=8080)
