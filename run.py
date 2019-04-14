#!/usr/bin/env python3.6
from user import User
import random
import string


def create_user(username,account_name,password):
        '''
        function to create new user
        '''
        new_user = User(username,account_name,password)
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

    return User.find_by_username(username)


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
    print("Welcome to PASSWORD LOCKER application. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')


    while True:
        print("Use these short codes : cu - create a new user,  li - login, du - display users, fu -find a user, ex -exit the user list ")
        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print("Username")
            username = input()

            print("Account Name ie Instergram, Facebook, Twitter")
            account_name = input()

            print("put Password or Leave blank for our application to generate password for you")
            password = input()

            if password == "":
                password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

            save_user(create_user(username,account_name,password))
            print('\n')
            print(f"New User {username} {account_name} {password} created")
            print('\n')


        elif short_code == 'li':
            print("Login")

            print("Enter username")
            username = input()

            print("Account Name")
            account_name = input()

            print("Enter password")
            password = input()

            for users in display_users():
                if username == users.username and account_name == users.account_name and password == users.password:
                    print("Logged in")
                    break
                else:
                    print("There is no such user")
                    break





        elif short_code == 'du':
            if display_users():
                print("Here is a list of all users we have in our application")
                print('\n')


                for users in display_users():
                    print(f"{users.username} {users.account_name} {users.password}")
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any users saved yet. Please save then check again later")
                print('\n')


        elif short_code == 'fu':
            print("Please enter the user you want to search for")

            search_user = input()
            if check_existing_users(search_user):
                search_user = find_user(search_user)
                print(f"{search_user.username} {search_user.account_name} {search_user.password}")


            else:
                print("The user you searched for does not exist please try again later")

        elif short_code == "ex":
            print("Thank you for using our application hope you enjoyed.")
            break

        else:
            print("I really didn't get that. Please use the short codes")





if __name__ == '__main__':

    main()
