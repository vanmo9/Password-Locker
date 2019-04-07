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


def main():
    print("Welcome. What is your name?")
           user_name = input()

    print(f"Hello {user_name}. What would you like?")
    print('\n')


    while True:
             print("Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")
