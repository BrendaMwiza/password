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
        
    