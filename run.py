from user import User


def create_user(username,password):
    '''
    function to create new user
    '''
     new_user = User(users,password)
     return new_user



def save_user(user):
    '''
    fuction to save user
    '''
    user.save_user()


def del_user(user):
    '''
    funtion to delete a user
    '''
    user.delete_user()

def find_user(number):
    '''
    function that finds user by number and returns the user
    '''

    return User.find_by_number(number)


def check_existing_users(number):
    '''
    function that cheks if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_users():
    '''
    function that returns all the saved users
    '''
    return User.display_users()
