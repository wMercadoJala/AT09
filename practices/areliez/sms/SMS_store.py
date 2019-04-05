import datetime


class SMS_store:

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = []
        has_been_viewed = False
        message.append(has_been_viewed)
        time = time_arrived
        message.append(time)
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
        unread_messages_indexes = []
        index = 0
        for message in self.messages:
            if message[0] is False:
                unread_messages_indexes.append(index)
                index += 1
            else:
                continue
        return unread_messages_indexes

    def get_message(self, i):
        if i < len(self.messages):
            message = self.messages[i]
        else:
            message = "The message with this index doesn't exist"
        return message

    def delete(self, i):
        if i < len(self.messages):
            message = self.messages[i]
            self.messages.remove(message)
            print("The message was deleted")
        else:
            print("The message with this index doesn't exist")

    def clear(self):
        for message in self.messages:
            self.messages.remove(message)
            continue
        print("All messages was removed")


my_store = SMS_store()
my_store.add_new_arrival("70376674", datetime.datetime.now().strftime('%H:%M:%S'), "hola mundo")
my_store.add_new_arrival("70376674", datetime.datetime.now().strftime('%H:%M:%S'), "hola kathy")

print(my_store.messages)
print(my_store.message_count())
print(my_store.get_unread_indexes())
print(my_store.get_message(1))
my_store.delete(1)
print(my_store.message_count())

my_store.add_new_arrival("70376674",  datetime.datetime.now().strftime('%H:%M:%S'), "hola mundo2")

print(my_store.message_count())
my_store.clear()
print(my_store.message_count())
