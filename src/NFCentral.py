'''
Created on Apr 10, 2015

@author: sdejonckheere
'''

class Users(object):

    registered_users = []

    def add_user(self,  channel, method, properties, body):
        data = body.split('@')
        if data[0] in self.registered_users:
            print data[0] + "-> Already registered"
            return False
        self.registered_users.append(data[0])
        print data[0] + "-> Registered"
        return True        

    def remove_user(self, channel, method, properties, body):
        data = body.split('@')
        if data[0] in self.registered_users:
            self.registered_users.remove(data[0])
            print data[0] + "-> Unregistered"
            return True
        print data[0] + "-> Already registered"
        return False

    def get_users(self):
        return self.registered_users
    
    def __init__(self):
        registered_users = []
    