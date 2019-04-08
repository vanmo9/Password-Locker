#!/usr/bin/env python3.6
from user import User


def create_user(username,password):
        '''
        function to create new user
        '''
        new_user = User(username,password)
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

def find_user(username):
    '''
    function that finds user by username and returns the user
    '''

    return User.find_by_number(username)


def check_existing_users(username):
    '''
    function that cheks if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

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
        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print("Username")
            username = input()

            print("Password")
            password = input()


            save_user(create_user(username,password))
            print ('\n')
            print(f"New User {username} {password} created")
            print('\n')



        elif short_code == 'du':
            if display_users():
                print("Here is a list of all your users we have in our account")
                print('\n')


                for users in display_users():
                    print(f"{users.username} {users.password}")
                    print('\n')
            else:
                prin('\n')
                print("You don't seem to have any users saved yet. Please save then check again")
                print('\n')


        elif short_code == 'fu':
            print("Enter the user you want to search for")

            search_user = input()
            if check_existing_users(search_user):
                search_user = find_user(search_user)
                print(f"{search_user.username} {search_user.password}")


            else:
                print("The user you searched for does not exist please try again later")

        elif short_code == "ex":
            print("Thank you for using our application hope you enjoyed.")

        else:
            print("I really didn't get that. Please use the short codes")




if __name__ == '__main__':

    main()
