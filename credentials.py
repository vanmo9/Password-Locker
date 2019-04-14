class creadentials:

    """
    Class that generates new instaces of creadentials.

    """
    creadentials_list = []

    def __init__(self, username, name, password):

        self.username = username
        self.name = name
        self.password = password

    def save_credentilas(self):
        '''
        save_user method saves user objects into creadentials list
        '''

        User.creadentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_user is method used to delete a saved user from the creadentials list
        '''
        User.creadentials_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        method that allows to take in a username and returns a user that matches with  that username .


        Args:
            user:username to search for
        Returns :
            users that matches the username.
        '''
        for user in cls.creadentials_list:
            if creadentials.username == username:
                return creadentials


    @classmethod
    def creadentials_exist(cls,username):
        '''
        method that cheks if a user exists from creadentials list .
        '''

        for creadentials in cls.creadentials_list:
            if creadentials.username == username:
                return True

        return False


    @classmethod
    def display_credetials(cls):
        '''
        method that returns or displays the creadentials list
        '''
        return cls.creadentials_list
