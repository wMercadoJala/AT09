import datetime
import re


class SMS_store:

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, text_of_SMS):
        message = []
        time_arrived = datetime.datetime.now().strftime('%H:%M:%S')
        message.append(time_arrived)
        number_phone = from_number
        message.append(number_phone)
        text = text_of_SMS
        message.append(text)
        self.messages.append(message)

    def message_count(self):
        count = 0
        for message in self.messages:
            count += 1
        return count

    def get_unread_indexes(self):
        pass

    def get_message(self, i):
        pass

    def delete(self, i):
        pass

    def clear(self):
        pass


my_store = SMS_store()
my_store.add_new_arrival("70376674", "hola mundo")
my_store.add_new_arrival("70376674", "hola kathy")

print(my_store.messages)
print(my_store.message_count())
