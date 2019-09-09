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
            print(f"New account {email} ceated")
            print('\n')

        elif short == 'lg':
            print("Enter your email")

            shakisha = input()
            if find_existing_user(shakisha):
                search = find_user(shakisha)

                print(f"")


if __name__ == '__main__':
        main()



