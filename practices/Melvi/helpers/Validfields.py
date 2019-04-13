class Validfields:


    @staticmethod
    def perform_validated(first, last, user_name, pws, month, day, year, gender, country_code, phone_number,
                      current_mail):
        results = 'successful'
        if first == '':
            results = 'failed'
        elif last == '':
            results = 'failed'
        elif user_name == '':
            results = 'failed'
        elif pws == '':
            results = 'failed'
        elif month == '':
            results = 'failed'
        elif day == '':
            results = 'failed'
        elif year == '':
            results = 'failed'
        elif gender == '':
            results = 'failed'
        elif country_code == '':
            results = 'failed'
        elif phone_number == '':
            results = 'failed'
        elif current_mail == '':
            results = 'failed'

        return results