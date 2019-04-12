class Validator:
    @staticmethod
    def validate_fields(fist_name, last_name, user_name, password):

        result = 'Congratulation!! Your account is successful'
        if fist_name == '':
            result = 'Error!! the First Name is required'
        elif last_name == '':
            result = 'Error!! the Last Name is required'
        elif user_name == '':
            result = 'Error!! the User Name is required'
        elif password == '':
            result = 'Error!! the Password is required'

        return result
