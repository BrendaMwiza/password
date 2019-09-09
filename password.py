import pyperclip
class Ingufuri:
    '''
    class that will generate new user-names,emails and passwords
    '''

    def __init__(self,full_name,email,password):

        '''
        This _init_ method will help us define our object properties.
        '''

        self.full_name = full_name
        self.email = email
        self.password = password

    user_info = [] #an array that will contain the users informations

    def save_account(self):

        '''
        save_user method to save user objects into user_info
        '''

        Ingufuri.user_info.append(self)

    def delete_account(self):
        '''
        this method deletes a saved user account from the list
        '''
        Ingufuri.user_info.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        this method enters an email and returns the user information.
        '''
        for account in cls.user_info:
            if account.email == email:
                return account

    @classmethod
    def account_exists(cls,email):
        '''
        this method checks if the user exists from the list.
        '''
        for account in cls.user_info:
            if account.email == email:
                return True

        return False

    @classmethod
    def login(cls,emails,modepass):
        for users in cls.user_info:
            if users.email == emails and users.password == modepass:
                return True
        return False
    
    @classmethod
    def copy_email(cls,email):
        found_user = cls.find_by_email(email)
        pyperclip.copy(found_user.email)
