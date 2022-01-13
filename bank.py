
# Gurman Chauhan
# First OOP project
# Jan 13, 2022

# Parent class : User
# holds details about user
# has function to show user details

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print('User Details:\n')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}') 
        print(f'Gender: {self.gender}')


# child class: account
# stores details about account balance
# allows for deposit, withdraw, viewing balance
class Account(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Withdrew ${amount}. New account balance: ${self.balance}')
        else:
            print(f'Insufficient funds. Balance available: {self.balance}')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ${amount}. New account balance: ${self.balance}')
                    
    def show_balance(self):
        print(f'Current account balance: ${self.balance}')
