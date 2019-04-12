class Datos:

    list_date = ["Carlos", "Villca", "carlitos.vil005@gmail.com", "car123", "august", "08", "1999", "female", "+591" , 78345290, "carl.viii01@gmail.com"]

    @staticmethod
    def required_data(first, last, user, password):
        if first == "" or first == " ":
            return "fail"
        elif last == "" or first == " ":
            return "fail"
        elif user == "" or first == " ":
            return "fail"
        elif password == "" or first == " ":
            return "fail"
        if user == Datos.list_date[2]:
            return "Exist that User"
        return "Successfully"

    # @staticmethod
    # def perform_data(first, last, user, password, month, day, year, country_code, gender, phone, current_email):
    #     if user == Datos.list_datos[2]:
    #         return "user existent"
    #     return "pass"
    #
    #
