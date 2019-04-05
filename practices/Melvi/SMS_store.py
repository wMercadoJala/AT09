#Create a new class, SMS_store. The class will instantiate SMS_store objects,
#similar to an inbox or outbox on a cellphone.
#Write the class, create a message store object, write tests for these methods, and implement the methods.​

class SMS_store:
    def __init__(self):
        self.messages = []

    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        self.messages.append(SMS_message(0, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.messages)


    def get_unread_indexes(self):
         cont = 0
         for msg in self.messages:
             if msg.has_been_viewed == 0:
                 cont += 1
         return cont

    def get_message(self, i):
         return self.messages[i]

    def delete(self,i):
         del self.messages[i]

    def clear(self):
         self.messages.clear()

class SMS_message:
    def __init__(self,has_been_viewed,from_number, time_arrived, text_of_SMS):
         self.has_been_viewed=has_been_viewed
         self.from_number=from_number
         self.time_arrived=time_arrived
         self.text_of_SMS=text_of_SMS

if __name__ == "__main__":
    cell_phone = SMS_store()
    cell_phone.add_new_arrival(78739988, "10:30", "Te estoy esperando!")
    cell_phone.add_new_arrival(75750999, "10:35", "No te olvide recoger a Vicente.")
    print(cell_phone.message_count())
    print(cell_phone.get_unread_indexes())





