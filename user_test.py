import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:

       unittest.TestCase: TestCase class that helps in creating test cases
   '''


def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_user = User("vanmo9", "mohassan")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username, "vanmo9")
        self.assertEqual(self.new_user.password, "mohassan")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved in to the contact list

        '''

    self.new_user.save_user()
    self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''

    self.new_user.save_user()
    test_user = User("Test", "user", "911mo", "911mo")
    test_user.save_user()
    self.assertEqual(len(User.user_list), 2)

    def tearDown(self):
        '''
        tearDown method  does clean up after test case has run.
        '''

        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "911mo", "911mo")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","911mo","911mo")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_number(self):
        '''
        this is to check if we can find user by a number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","911mo","911mo")
        test_user.save_user()

        found_user = User.find_by_number("911mo")


        self.assertEqual(found_user.email,test_user.email)


        
