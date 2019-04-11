class Operators:
    @staticmethod
    def operators(first, second, operator):
        try:
            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/":
                result = first / second
        except ZeroDivisionError:
            result = "Divide Zero Exception message"
        return result