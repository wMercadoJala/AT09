class SMS_store:
    '''
    This class store all the message into an array and permit to the user to read the unread messages delete, and
    receive messages.
    '''

    list_SMS = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        '''
        Receive the messages with from number, time arrived and set False to read latter. The message are saved in an
        array.
        '''
        self.list_SMS.append([False, from_number, time_arrived, text_of_SMS])

    def message_count(self):
        '''
        Return the size of the array or the quantity of the messages.
        '''
        print("All the messages are: ", len(self.list_SMS))

    def get_unread_indexes(self):
        '''
        Return the list of the messages that are not read.
        '''
        index = 1
        print("The Unread messages are:")
        for element in self.list_SMS:
            if element[0] is False:
                print(index, element[1], element[2])
                index += 1

    def get_message(self, index):
        '''
        Return the message that the user selected, and put it in True.
        '''
        if index < len(self.list_SMS):
            self.list_SMS[index][index] = True
            print("Number:", self.list_SMS[index][1], "Time Arrived:", self.list_SMS[index][2])
            print(self.list_SMS[index][3])

    def delete(self, index):
        '''
        Delete the message that the user selected.
        '''
        if index < len(self.list_SMS):
            self.list_SMS.pop(index)
        else:
            print("Don't exist that index")

    def clear(self):
        '''
        Delete all of the list of messages.
        '''
        self.list_SMS.clear()


my_inbox = SMS_store()
my_inbox.add_new_arrival("72504487", "05:30", "Hi bro")
my_inbox.add_new_arrival("68495979", "6:00", "Come")
my_inbox.add_new_arrival("75020039", "08:15", "It is too late")
my_inbox.message_count()
my_inbox.get_unread_indexes()
my_inbox.get_message(0)
my_inbox.get_unread_indexes()
my_inbox.delete(0)
my_inbox.message_count()
my_inbox.clear()
my_inbox.message_count()
