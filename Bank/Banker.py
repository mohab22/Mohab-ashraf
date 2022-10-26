from User import users_ID

Gen_pass="banker1"
class Banker:
    def __init__(self):

        self.__working_Id = ""

    def set_working_Id(self):
        while True:
            main_user_id = input("enter the user's id\t")
            if users_ID.get(main_user_id, "none") == "none":
                val = False
            else:
                val = True
            if val:
                self.__working_Id = main_user_id
                return users_ID[main_user_id]
                # this break for  the loop of checking id availability

            elif not val:
                print("The Id you entered is not available please enter again !")

    @staticmethod
    def checking_Id(check):
        if users_ID.get(check, "none") == "none":
            return False
        else:
            return True

    @staticmethod
    def set_banker_working_process_num():
        global func_process_id
        while True:
            try:
                func_process_id = int(input("choose the process\n"
                                            "1 - deposit\n"
                                            "2 - withdraw\n"
                                            "3 - Balance Inquiry\n"
                                            "4 - Account statement\n"
                                            "5 - transfer\n "
                                            ))
                if 1 <= func_process_id <= 5:
                    # to break choose process loop
                    return func_process_id

                else:
                    print("please enter a valid number")
            except ValueError:
                print("please enter a number not a letter !")

            return func_process_id

    def get_credit(self):
        return users_ID[self.__working_Id].get_credit()

    def get_id(self):
        return self.__working_Id

    def deposit(self):
        while True:
            try:
                amount_of_increment = int(input("Enter the amount\t"))
                if amount_of_increment >= 0:
                    users_ID[self.__working_Id].set_credit(amount_of_increment)
                    users_ID[self.__working_Id].adding_process(amount_of_increment)
                    break
                else:
                    print("please enter a valid number\n")

            except ValueError:
                print("please enter just numbers\n")

    def balance_enquiry(self):
        print(f"The {self.__working_Id}'s balance is {users_ID[self.__working_Id].get_credit()} EGP ")

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter the amount :\t"))
                if users_ID[self.__working_Id].get_credit() >= amount >= 0:
                    users_ID[self.__working_Id].set_credit_withdraw(amount)
                    users_ID[self.__working_Id].adding_process_withdraw(amount)
                    break
                else:
                    print("The process is rejected\n(No enough money)")
            except ValueError:
                print("please enter a valid number\n")

    def account_statement(self):
        users_ID[self.__working_Id].print_account_statement()

    def transfer(self):
        while True:
            try:
                id1 = self.get_id()
                id2 = input("Enter second user id :\t")
                val = int(input("enter the value"))
                if self.checking_Id(id1) and self.checking_Id(id2):
                    if users_ID[self.__working_Id].get_credit() >= val >= 0:
                        users_ID[self.__working_Id].set_credit_withdraw(val)
                        users_ID[self.__working_Id].adding_process_transfer(val)
                        users_ID[id2].adding_process(val)
                        users_ID[id2].set_credit(val)
                        print('the amount transferred successfully\n')
                        break
                    else:
                        print("The process is rejected\n(No enough money)")
            except ValueError:
                print("please enter vaild value\n")

    def Processing_func(self, process_id):
        if process_id == 1:
            self.deposit()
        elif process_id == 2:
            self.withdraw()
        elif process_id == 3:
            self.balance_enquiry()
        elif process_id == 4:
            self.account_statement()
        elif process_id == 5:
            self.transfer()

    @staticmethod
    def main_banker_function():
        users_password=input("Enter banker password")
        if users_password ==Gen_pass :
            continue_with_same_id = "y"
            while continue_with_same_id == "y":
                cont_banker = 'y'
                b1 = Banker()
                b1.set_working_Id()
                while cont_banker == 'y' and not cont_banker == 'n':
                    process_id = Banker.set_banker_working_process_num()
                    b1.Processing_func(process_id)
                    cont_banker = input("Do you wanna continue with this account ?(y/n)\t")
                    # to break the user or banker loop
                break
