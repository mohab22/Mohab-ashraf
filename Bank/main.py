from Banker import Banker
from User import User
print("Welcome to Our bank\n")
while True:
    user_or_banker = input("please choose are you ...?\n"+" 1 - User\n"+ " 2 - Banker\n"+" 3 - Exit\n")
    if user_or_banker == "1":
        User.main_user_function()
    elif user_or_banker == "2":
        Banker.main_banker_function()
    else:
        break
