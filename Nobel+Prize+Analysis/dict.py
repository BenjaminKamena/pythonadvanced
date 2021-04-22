import random

account_details_container = {}
def init():
    print("Welcome to Bank NAMX")

    has_account = int(input("Do you have an account with us? \n1. YES \n2. NO"))

    if has_account == 1:
        login()

    elif has_account == 2:
        register()

    else:
        print("You have selected an invalid option")


def register():
    print("<<< Please register >>>")

    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create your password \n")

    account_number = account_number_generator()
    user_details = [first_name, last_name, email, password]

    account_details_container[account_number] = user_details

    print("Congratulations " + first_name + " " + last_name)
    print("Your account has been created successfully.")
    print("Below are your login details. Please keep them safe.")
    print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Account number: {}".format(account_number))
    print("Password: " + password)
    print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")

    login()


def login():
    print("<<<>>> Please login <<<>>>")

    login_attempt_counter = 0
    login_attempt_limit = 3

    while login_attempt_counter < login_attempt_limit:
        entered_account_number = input("Enter your account number: \n")
        entered_password = input("Enter your password: \n")
        login_attempt_counter += 1

        for entered_account_number, entered_password in account_details_container.items():
            if (entered_account_number in account_details_container.keys()):
                if (entered_password in account_details_container.values()):
                    print("login successful")
                    break
                else:
                    print("Account number or pasword not found. Please try again.")
            else:
                print("Too many attempts. Try again after some time.")


def account_number_generator():
    return random.randrange(1111111111, 9999999999)


init()
