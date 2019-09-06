import pyperclip
class Store:
    '''
    class that will generate accounts that a user has stored.
    '''

    def __init__(self,account,user_name,email,password):

        '''
        This _init_ method will help us define our object properties.
        '''
        self.account = account
        self.user_name = user_name
        self.email = email
        self.password = password

    account_info = [] #an array that will contain the users informations

    # def savinga_contes(self):

    #     '''
    #     saving_contes method to save user objects into account_info
    #     '''

    #     Store.account_info.append(self)

    # def deletinga_conte(self):
    #     '''
    #     this method deletes a saved account from the list
    #     '''
    #     Store.account_info.remove(self)

    # @classmethod
    # def findinga_by_user_name(cls,user_name):
    #     '''
    #     this method enters a user_name and returns the account information.
    #     '''
    #     for contes in cls.account_info:
    #         if contes.user_name == user_name:
    #             return contes

    # @classmethod
    # def conte_existing(cls,user_name):
    #     '''
    #     this method checks if the account exists from the list.
    #     '''
    #     for contes in cls.account_info:
    #         if contes.user_name == user_name:
    #             return True

    #     return False
    
    # @classmethod
    # def copy_email(cls,email):
    #     found_user = cls.find_by_email(email)
    #     pyperclip.copy(found_user.email)
    
