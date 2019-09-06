import pyperclip
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

    def test_find_user_by_email(self):
        '''
        this method is to find the user account by email and display information.
        '''
        self.new_account.save_account()
        test_account = Ingufuri("Muka","muka@gmail.com","12345")
        test_account.save_account()

        found_user = Ingufuri.find_by_email("muka@gmail.com")

        self.assertEqual(found_user.email,test_account.email)

    def test_account_exists(self):
        '''
        this method checks if the user account exists by returning a boolean.
        '''
        self.new_account.save_account()
        test_account = Ingufuri("Muka","muka@gmail.com","12345")
        test_account.save_account()
        account_exists = Ingufuri.account_exists("muka@gmail.com")

        self.assertTrue(account_exists)

    def test_copy_email(self):
        '''
        this test confirms that an email is being copied from an account.
        '''
        self.new_account.save_account()
        Ingufuri.copy_email("brenda@ms.com")
        self.assertEqual(self.new_account.email,pyperclip.paste())

#------------------------------------------------------------------------------------------------------------------------------------
    # testing credentials in Store class

from credentials import Store # importing the Store class from credentials

class TestStore(unittest.TestCase):

    '''
    This class defines test cases for the Store class behaviours
    '''

    def setUp(self):
        '''
        this method is for running before each test case.
        '''

        self.new_conte = Store("Facebook","Black Mwiza","black@ms.com","12345") 

    def test_init(self):
        '''
        this is to test if the object is properly initialised.
        '''

        self.assertEqual(self.new_conte.account,"Facebook")
        self.assertEqual(self.new_conte.user_name,"Black Mwiza")
        self.assertEqual(self.new_conte.email,"black@ms.com")
        self.assertEqual(self.new_conte.password,"12345")
        
    def test_savinga_contes(self):
        '''
        this test case is for testing if the account_info object is added. 
        '''
        self.new_conte.savinga_contes()
        self.assertEqual(len(Store.account_info),1)

    def tearDown(self):
        '''
        method that refleshes after every test case has run.
        '''
        Store.account_info = []

    def test_savinga_many_contes(self):
        '''
        this method checks if many accounts can be saved.
        '''
        self.new_conte.savinga_contes()
        test_conte = Store("Instagram","Gasaro Wandah","nyira@gmail.com","ziraje")
        test_conte.savinga_contes()
        self.assertEqual(len(Store.account_info),2)

    def test_deletinga_conte(self):
        '''
        this method tests if we can remove an account from the list.
        '''
        self.new_conte.savinga_contes()
        test_conte = Store("Instagram","Gasaro Wandah","nyira@gmail.com","ziraje")
        test_conte.savinga_contes()
        self.new_conte.deletinga_conte() # for deleting an account object
        self.assertEqual(len(Store.account_info),1)

    def test_findinga_by_user_name(self):
        '''
        this method is to find the account by user_name and display information.
        '''
        self.new_conte.savinga_contes()
        test_conte = Store("Instagram","Gasaro Wandah","nyira@gmail.com","ziraje")
        test_conte.savinga_contes()

        found_conte = Store.findinga_by_user_name("Gasaro Wandah")

        self.assertEqual(found_conte.user_name,test_conte.user_name)

if __name__ == '__main__':
        unittest.main()
