import unittest

from password import Ingufuri # importing the Ingufuri class

class TestIngufuri(unittest.TestCase):

    '''
    This class defines test cases for the Ingufuri class behaviours

    Args:
        unittest.TestCase: TestCase class helps create test cases
    '''

    def setUp(self):
        '''
        this method is for running before each test case.
        '''

        self.new_account = Ingufuri("Brenda Mwiza","brenda@ms.com","123456789") #user object

    def test_init(self):
        '''
        this is to test if the object is properly initialised.
        '''
        self.assertEqual(self.new_account.full_name,"Brenda Mwiza")
        self.assertEqual(self.new_account.email,"brenda@ms.com")
        self.assertEqual(self.new_account.password,"123456789")

    def test_save_account(self):
        '''
        this test case is for testing if the user-account object is added. 
        '''
        self.new_account.save_account()
        self.assertEqual(len(Ingufuri.user_info),1)

    def tearDown(self):
        '''
        method that refleshes after every test case has run.
        '''
        Ingufuri.user_info = []

    def test_save_many_accounts(self):
        '''
        this method checks if many accounts can be saved.
        '''
        self.new_account.save_account()
        test_account = Ingufuri("Muka","muka@gmail.com","12345")
        test_account.save_account()
        self.assertEqual(len(Ingufuri.user_info),2)

    def test_delete_account(self):
        '''
        this method tests if we can remove an account from the list.
        '''
        self.new_account.save_account()
        test_account = Ingufuri("Muka","muka@gmail.com","12345")
        test_account.save_account()
        self.new_account.delete_account() # for deleting a user object
        self.assertEqual(len(Ingufuri.user_info),1)


if __name__ == '__main__':
        unittest.main()
