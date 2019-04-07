class User:
    """
    Class that generates new instaces of usersself.

    """
    user_list = []

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method is to delete a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_number(cls, number):
        '''
        method that allowto take in a number and returns a user that matches that number .


        Args:
            number:Phone number to search for
        Returns :
            User of persons that matches the number.
        '''
        for user in cls.user_list:
            if user.phone_number == number:
                return user


    @classmethod
    def user_exist(cls,number):
        '''
        method that cheks if a user exists from user list .
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
