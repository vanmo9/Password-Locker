import unittest
from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        this is Set up method to run before each test cases.
        '''
        self.new_user = User("vanmo9","instergram","mohassan")

    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "vanmo9")
        self.assertEqual(self.new_user.account_name, "instergram")
        self.assertEqual(self.new_user.password, "mohassan")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved in to the user list

        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user is to check if we can save multiple user objects to our user list
        '''

        self.new_user.save_user()
        test_user = User("vanmo9", "instergram", "mohassan")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def tearDown(self):
        '''
        tearDown method  does clean up after test case has run.
        '''

        User.user_list = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user list
        '''
        self.new_user.save_user()
        test_user = User("vanmo9", "instergram", "mohassan")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("vanmo9", "instergram", "mohassan")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_username(self):
        '''
        this is to check if we can find user by a username and display information
        '''

        self.new_user.save_user()
        test_user = User("vanmo9", "instergram", "mohassan")
        test_user.save_user()

        found_user = User.find_by_username("vanmo9")


        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        '''
        test to check if we can return aBollean when we cannot find the user
        '''

        self.new_user.save_user()
        test_user = User("vanmo9", "instergram", "mohassan")
        test_user.save_user()

        user_exists = User.user_exist("vanmo9")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)



if __name__ ==  '__main__':
    unittest.main()
