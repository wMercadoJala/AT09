import re
import datetime


class Validfields:

    @staticmethod
    def is_valid_email(email):
        if len(email) > 7:
            if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) is not None:
                return True
        return False

    @staticmethod
    def is_number(value):
        try:
            val = int(value)
        except ValueError:
            return False
        return True

    @staticmethod
    def is_valid_date(month, day, year):
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        nr_month = months.index(month)+1

        try:
            date = datetime.datetime(int(year), int(nr_month), int(day))
            current_date = datetime.datetime.now()
            if date > current_date:
                return False
        except ValueError:
            return False
        return True



    @staticmethod
    def perform_validated(first, last, user_name, pws, confirm_pws, month, day, year, gender, country_code, phone_number,
                      current_mail):
        results = 'successful'
        if first == '':
            results = 'Missing first name'
        elif last == '':
            results = 'Missing last name'
        elif user_name == '':
            results = 'Missing user name'
        elif pws == '':
            results = 'Missing password'
        elif confirm_pws == '':
            results = 'Missing password confirmation'
        elif pws != confirm_pws:
            results = 'Password confirmation does not match password'
        elif month == '':
            results = 'failed'
        elif day == '':
            results = 'failed'
        elif year == '':
            results = 'failed'
        elif Validfields.is_valid_date(month, day, year) is False:
            results = 'invalid birthday date'
        elif gender == '':
            results = 'failed'
        elif country_code == '':
            results = 'Missing select country code'
        elif phone_number == '':
            results = 'failed'
        elif Validfields.is_number(phone_number) is False:
            results = 'Phone number should be a number'
        elif current_mail == '':
            results = 'failed'
        elif Validfields.is_valid_email(current_mail) is False:
            results = 'invalid email'

        return results

