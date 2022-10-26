import datetime


def checking_Id(check):
    if users_ID.get(check, "none") == "none":
        return False
    else:
        return True


class User:

    def __init__(self, Id="0", credit=0):
        self.__Id = Id
        self.__password = ""
        self.__credit = credit
        self.__statement = {}

    def set_Id(self, Id):
        self.__Id = Id
        return self.__Id

    def set_password(self, password):
        self.__password = password
        return self.__password

    def set_credit(self, credit):
        self.__credit += credit
        return self.__credit

    def set_credit_withdraw(self, credit):
        self.__credit -= credit
        return self.__credit

    def get_password(self):
        return self.__password

    def get_credit(self):
        return self.__credit

    def get_id(self):
        return self.__Id

    def adding_process(self, amount):
        self.__statement[amount] = (datetime.datetime.now(), "deposit")

    def adding_process_withdraw(self, amount):
        self.__statement[amount] = (datetime.datetime.now(), "withdraw")

    def adding_process_transfer(self, amount):
        self.__statement[amount] = (datetime.datetime.now(), "Transfer")

    def print_account_statement(self):
        for child in self.__statement:
            print(f"Type : {self.__statement[child][1]}\tvalue : {child}\tTime : {self.__statement[child][0]} ")

    def sign_in(self):
        while True:
            username = input("Enter your user name : \t")
            password = input("Enter your password :\t")
            if checking_Id(username):
                if users_ID[username].get_password() == password:
                    self.__Id = username
                    return True

                else:
                    print("Users or password are incorrect")
            else:
                print("there is no user with this name please sign up\n")
                return False

    @staticmethod
    def pick_num():
        while True:
            try:
                while True:
                    choice = int(input("1-withdraw\n2-Balance Inquiry\n3-Account statement\n4-transfer\n"))
                    if 4 >= choice >= 1:
                        return choice
                    else:
                        print("enter a valid number\n")
            except ValueError:
                print("please enter number not letter !!\n")

    @staticmethod
    def sign_up():
        username = input("enter your user\t")
        if checking_Id(username):
            print("this username already taken try again\n")
        else:
            password = input("Enter your password\n\t(it should contain 6 letters al least)\n")
            if len(password) >= 6:
                tempU = User(username, 0)
                tempU.set_password(password)
                users_ID[username] = tempU
                print("signed up successfully\n")

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter the amount :\t"))
                if users_ID[self.__Id].get_credit() >= amount >= 0:
                    users_ID[self.__Id].set_credit_withdraw(amount)
                    users_ID[self.__Id].adding_process_withdraw(amount)
                    break
                else:
                    print("The process is rejected\n(No enough money)")
            except ValueError:
                print("please enter a valid number\n")

    def account_statement(self):
        users_ID[self.__Id].print_account_statement()

    def transfer(self):
        while True:
            try:
                id1 = self.__Id
                id2 = input("Enter second user id :\t")
                val = int(input("enter the value"))
                if checking_Id(id1) and checking_Id(id2):
                    if users_ID[self.__Id].get_credit() >= val >= 0:
                        users_ID[self.__Id].set_credit_withdraw(val)
                        users_ID[self.__Id].adding_process_transfer(val)
                        users_ID[id2].adding_process(val)
                        users_ID[id2].set_credit(val)
                        print('the amount transferred successfully\n')
                        break
                    else:
                        print("The process is rejected\n(No enough money)")
            except ValueError:
                print("please enter valid value\n")

    def balance_enquiry(self):
        print(f"The {self.__Id}'s balance is {users_ID[self.__Id].get_credit()} EGP ")

    def Processing_func(self, num):
        if num == 1:
            self.withdraw()
        elif num == 2:
            self.balance_enquiry()
        elif num == 3:
            self.account_statement()
        elif num == 4:
            self.transfer()

    @staticmethod
    def main_user_function():
        sign_choice = input("1-sign in\n2-sign up\n")
        if sign_choice == "1":
            u1 = User()
            if u1.sign_in():
                continue_in_user = "y"
                while continue_in_user == "y":
                    num = User.pick_num()
                    u1.Processing_func(num)
                    continue_in_user = input("Do you wanna continue ?(y/n)")

        elif sign_choice == "2":
            User.sign_up()


u1 = User("1", 5000)
u1.set_password("1111")
u2 = User("22", 5000)
u2.set_password("1234")
users_ID = {
    "1": u1,
    "22": u2
}
