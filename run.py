#!/usr/bin/env python3.6

from password import Ingufuri # importing the Ingufuri class
from credentials import Store

def create_account(funame,email,password):
    '''
    this function will create a new account.
    '''
    new_user = Ingufuri(funame,email,password)
    return new_user

def save_account(user):
    '''
    this will save the user account
    '''
    user.save_account()

def delete_user(user):
    '''
    this will be used to delete user account.
    '''
    user.delete_user()

def find_user(email):
    '''
    this will find the user account by email and will return the user information.
    '''
    return Ingufuri.find_by_emai(email)

def find_existing_user(email):
    '''
    this will check if an account exists using an email and will return a boolean.
    '''
    return Ingufuri.account_exists(email)

# functions for credentials
def create_cre(user_name,email,password,account):
    '''
    this function will create a new credential.
    '''
    account_info = Store(user_name,email,password,account)
    return account_info

def save_cre(conte):
    '''
    this will save the created credential
    '''
    conte.savinga_contes()

def delete_cre(conte):
    '''
    this will be used to delete credential.
    '''
    conte.delete_cre()

def find_cre(account):
    '''
    this will find credential and display it.
    '''
    return Store.find_by_account(account)

def find_existing_cre(account):
    '''
    this will check if an account exists using an account name.
    '''
    return Store.conte_existing(account)

def display_cres():
    '''
    Function that returns all the saved contacts
    '''
    return Store.display_contes()



def main():
    print(f"Hello! great choice to our app.")
    print('\n')

    while True:
        print("use the following short codes: ca - create account, lg - login account")

        short = input().lower()
        if short == 'ca':
            print("New account")
            print("-"*12)

            print("Full name...")
            fullName = input()

            print("Email...")
            email = input()

            print("Password...")
            password = input()

            save_account(create_account(fullName,email,password)) #created and saved new account
            print('\n')
            print(f"New account {email} successfully ceated")
            print('\n')

        elif short == 'lg':
            print("Enter your email")
            shakisha = input()
            print('.' * 30)

            print ("Enter passord")
            shakisha = input()
            print('.' * 30)

            if find_existing_user(shakisha):
                search = find_user(shakisha)

            break

    while True:
        print("use the following short codes: ccr - create credential, del - delete credential, dcr - display credential")

        short = input().lower()
        if short == 'ccr':
            user_name = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            account = input("Credential: ")
            print('.' * 60)
            save_cre(create_cre(user_name,email,password,account))

            print("credential successfully created.")
            print('.' * 60)

        elif short == 'dcr':

            if display_cres():
                print("This is a list of credentials you have stored")
                print('\n')

                for conte in display_cres():
                    print(f"{conte.account} {conte.user_name} {conte.email}")
                    print('\n')
            else:
                print("You have not created no credential yet")
                print('\n')

        elif short == 'del':
            print('Enter credential you want to delete')
            see = input()
            if find_existing_cre(see):
                conte.delete_cre()
                print("credential deleted")
            else:
                print("It does not exist")


if __name__ == '__main__':
        main()



