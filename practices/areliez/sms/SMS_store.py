import datetime


class SMS_store:
    """
    SMS store
    """

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """
        This adds new SMS.
        :param from_number: number phone.
        :param time_arrived: time of message sent.
        :param text_of_SMS: text og message.
        :return:
        """
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
        """
        This counts the messages.
        :return: The cant of messages.
        """
        return len(self.messages)

    def get_unread_indexes(self):
        """
        Get the messages indexes that wasn't read.
        :return: Index list.
        """
        unread_messages_indexes = []
        index = 0
        for message in self.messages:
            if message[0] is False:
                unread_messages_indexes.append(index)
                index += 1
            else:
                continue
        return unread_messages_indexes

    def get_message(self, index):
        """
        Get the a message by index.
        :param index: of the message.
        :return: A message.
        """
        if index < len(self.messages):
            message = self.messages[index]
        else:
            message = "The message with this index doesn't exist"
        return message

    def delete(self, index):
        """
        Print a message for a message deleted by index,
        :param index: of the message.
        :return: a message if te message was deleted or not.
        """
        if index < len(self.messages):
            message = self.messages[index]
            self.messages.remove(message)
            print("The message was deleted")
        else:
            print("The message with this index doesn't exist")

    def clear(self):
        """
        Remove all message from store.
        :return: Print a message
        """
        while len(self.messages) > 0:
            self.messages.remove(self.messages[0])
        print("All messages was removed")


my_store = SMS_store()
my_store.add_new_arrival("77777777", datetime.datetime.now().strftime('%H:%M:%S'), "hello")
my_store.add_new_arrival("77776674", datetime.datetime.now().strftime('%H:%M:%S'), "Hi")

print(my_store.messages)
print(my_store.message_count())
print(my_store.get_unread_indexes())
print(my_store.get_message(1))

my_store.delete(1)
print(my_store.message_count())

my_store.add_new_arrival("77774444",  datetime.datetime.now().strftime('%H:%M:%S'), "Hello friend")
print(my_store.message_count())

my_store.clear()
print(my_store.message_count())
