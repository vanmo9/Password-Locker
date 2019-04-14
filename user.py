class User:

    """
    Class that generates new instaces of users.

    """
    user_list = []

    def __init__(self, username, account_name, password):

        self.username = username
        self.account_name = account_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user is method used to delete a saved user from the user list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        method that allows to take in a username and returns a user that matches with  that username .


        Args:
            user:username to search for
        Returns :
            users that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user


    @classmethod
    def user_exist(cls,username):
        '''
        method that cheks if a user exists from user list .
        '''

        for user in cls.user_list:
            if user.username == username:
                return True

        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns or displays the user list
        '''
        return cls.user_list
