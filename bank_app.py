import random
import string
import json
import os
import sys
import uuid
import datetime
import time
import winsound
from datetime import date, timedelta




# A class of the client, with various methods such as seeing the current a/c balance
class Client:
    def __init__(self):
        self.client_name = ''
        self.nationality = ''
        self.date_of_birth = ''
        self.passport_number = ''
        self.account_number = ''
        self.atm_login_pin = ''
        self.password = ''
        self.current_account_balance = 0
        self.notifications = []
        self.notifications_bar = []
        self.savings_account_registered = 0
        self.savings_account = []
        self.current_account_registered = 0
        self.current_account = []

    # A method to deduct amount from the current account after a transaction has been collected
    def deduct_from_current_acc(self, amount):
        updated_list, compounded_interest_utilised = fifo_withdrawal_30_days(self.current_account, amount)
        self.current_account = updated_list
        return updated_list

    # A method to update the list of transactions in the database. It takes the new list after a deposit has been made and updates the current a/c objects
    def update_current_account_deposit(self, new_current_accounts_transactions):
        self.current_account = new_current_accounts_transactions

    def update_current_account_withdrawal(self, new_current_accounts_transactions):
        self.current_account = new_current_accounts_transactions

    def update_savings_account(self, new_savings_account_transactions):
        self.savings_account = new_savings_account_transactions

    def update_current_account(self, new_current_account_transactions):
        self.current_account += new_current_account_transactions

    def update_current_account_bal(self, new_current_account_balance):
        self.current_account_balance = new_current_account_balance

    def notification_update(self, notification):
        self.notifications.append(notification)
        self.notifications_bar.append(notification)

    def register_savings_account(self):
        self.register_savings_account = True

    # A method to create a new client
    def create_client(self):

        clear_terminal()
        BANK_NAME()
        running = True

        try:
            password_loop = True
            while running:
                token = 0
                client_name = input("Enter the name: ")
                if client_name != '':
                    token += 1
                while password_loop:
                    try:
                        date_of_birth = int(input("Enter your birth year: "))
                        if type(date_of_birth) == int:
                            token += 1
                            password_loop = False

                    except ValueError:
                        clear_terminal()
                        BANK_NAME()
                        print('Error, invalid Data type. Integers only supported. Date should be in digit format.')
                        error_message()
                        time.sleep(1)
                        clear_terminal()
                        BANK_NAME()

                # Account number Generator
                account_number = str(
                    random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(
                        string.ascii_letters) + str(random.randint(1000, 2000)))

                if account_number != 0:
                    token += 1

                passport_number = input('Enter your passport number: ')
                if passport_number != '':
                    token += 1

                nationality = input('Enter your country of residence: ')
                if nationality != '':
                    token += 1

                clear_terminal()
                BANK_NAME()

                # Password validation.
                print('\nPASSWORD SHOULD HAVE AT LEAST SIX CHARACTERS\n')
                resolved = False
                while resolved == False:
                    password = input('Enter password: ')
                    passw_conf = input('Confirm password: ')

                    # Conditional statements to validate the password, if the password registration is false, it loops until the user gets it write
                    # Also an option to exit
                    # If the passwords matches, and the length is at least 6, then the registation will be succesfull
                    password_match = False
                    if password == passw_conf:
                        password_match = True
                        if len(password) >= 6:
                            password_match = True
                            resolved = True
                            token += 1
                            continue

                    if password_match == False and len(password) >= 6:
                        clear_terminal()
                        BANK_NAME()
                        opt_selected = input('Passwords didn\'t match.\n1. Restart 2. Exit\nOptions: ')
                        if opt_selected == 1:
                            clear_terminal()
                            BANK_NAME()
                            resolved = False
                        elif opt_selected == 2:
                            clear_terminal()
                            BANK_NAME()
                            resolved = True


                    elif password_match == True and resolved == False:
                        clear_terminal()
                        BANK_NAME()
                        opt_selected = input(
                            'Your password should be at least six characters long.\n1. Restart 2. Exit\nOptions: ')
                        if opt_selected == 1:
                            clear_terminal()
                            BANK_NAME()
                            resolved = False
                        elif opt_selected == 2:
                            clear_terminal()
                            BANK_NAME()
                            resolved = True


                    elif password_match == False and resolved == False:
                        clear_terminal()
                        BANK_NAME()
                        opt_selected = input(
                            'Your password should be at least six characters long and should both match.\n1. Restart 2. Exit\nOptions: ')
                        if opt_selected == 1:
                            clear_terminal()
                            BANK_NAME()
                            resolved = False
                        elif opt_selected == 2:
                            clear_terminal()
                            BANK_NAME()
                            resolved = True

                # Conditional statement to give the user an option to confirm their details. If there is an error, they can edit
                if token == 6:
                    try:
                        clear_terminal()
                        BANK_NAME()
                        print(
                            f'1. Full name:\t{client_name}\n2. Date of birth:\t{date_of_birth}\n3. Nationality:\t{nationality}\n4. Passport Number:\t{passport_number}')
                        confirm_details = int(input('\n1. Confirm 2. Edit 3. Exit\t\nOption:\t'))
                        if confirm_details == 1:
                            clear_terminal()
                            BANK_NAME()

                            # Appending the attributes to the object

                            self.client_name = client_name
                            self.date_of_birth = date_of_birth
                            self.nationality = nationality
                            self.passport_number = passport_number
                            self.password = password
                            self.account_number = account_number

                            print('Registration In Progress ...')
                            loading_animation()
                            clear_terminal()
                            BANK_NAME()

                            print(
                                f'Thank you for registering with us.\nACCOUNT DETAILS\n1.Account Name:\t{self.client_name}\n2.Account Number:\t{self.account_number}')
                            successful_notification()
                            running = False
                            return True
                        elif confirm_details == 2:
                            clear_terminal()
                            BANK_NAME()
                            running = True
                            password_loop = True
                        elif confirm_details == 3:
                            clear_terminal()
                            BANK_NAME()
                            running = False


                    except ValueError:
                        print('Invalid input')

                else:
                    try:
                        clear_terminal()
                        BANK_NAME()
                        confirm_details_two = int(input('Registration Unsuccesful\n1. Restart 2. Exit'))
                        if confirm_details_two == 1:
                            running = True
                            clear_terminal()
                            BANK_NAME()
                            return False
                        elif confirm_details == 2:
                            clear_terminal()
                            BANK_NAME()
                            running = False
                    except ValueError:
                        print('Invalid Input')
        except ValueError:
            print("Invalid Input")


# A class of a bank
class Bank(Client):
    # A list of all the clients in the bank.
    def __init__(self):
        self.clients = []

    # A method to append a new client and append the object to the client list.
    def add_new_client(self):
        client = Client()
        client.create_client()
        if client.__getattribute__('account_number') != "":
            self.clients.append(client)

    # A method to load the database when the program starts. All the data is written to the bank_database.txt file. This method parse it and
    # appends the individual client object the client list
    def load_database(self):
        with open('bank_database.txt', 'r') as n:
            if len(n.readlines()) > 0:
                with open('bank_database.txt', 'r') as f:
                    for i, client_details in enumerate(f.readlines()):
                        client_name, account_number, current_account_balance, passport_number, nationality, date_of_birth, password, atm_login_pin, notifications, notifications_bar, savings_account, savings_account_registered, current_account, current_account_registered = client_details.rstrip().split(
                            '|')
                        notifications = json.loads(notifications)
                        notifications_bar = json.loads(notifications_bar)
                        savings_account = json.loads(savings_account)
                        current_account = json.loads(current_account)

                        client = Client()
                        self.clients.append(client)
                        self.clients[i].__setattr__('client_name', client_name)
                        self.clients[i].__setattr__('account_number', account_number)
                        self.clients[i].__setattr__('passport_number', passport_number)
                        self.clients[i].__setattr__('nationality', nationality)
                        self.clients[i].__setattr__('current_account_balance', current_account_balance)
                        self.clients[i].__setattr__('date_of_birth', date_of_birth)
                        self.clients[i].__setattr__('password', password)
                        self.clients[i].__setattr__('atm_login_pin', atm_login_pin)
                        self.clients[i].__setattr__('notifications', notifications)
                        self.clients[i].__setattr__('notifications_bar', notifications_bar)
                        self.clients[i].__setattr__('savings_account', savings_account)
                        self.clients[i].__setattr__('current_account', current_account)
                        self.clients[i].__setattr__('notifications_bar', notifications_bar)
                        self.clients[i].__setattr__('current_account_registered', current_account_registered)
                        self.clients[i].__setattr__('savings_account_registered', savings_account_registered)

    # A method to update the database and reflect the changes
    def update_database(self):
        with open('bank_database.txt', 'w') as f:
            for client in self.clients:
                client_name, account_number, current_account_balance, passport_number, nationality, date_of_birth, password, atm_login_pin, notifications, notifications_bar, savings_account, savings_account_registered, current_account, current_account_registered = client.__getattribute__(
                    'client_name'), client.__getattribute__('account_number'), client.__getattribute__(
                    'current_account_balance'), client.__getattribute__('passport_number'), client.__getattribute__(
                    'nationality'), client.__getattribute__('date_of_birth'), client.__getattribute__(
                    'password'), client.__getattribute__('atm_login_pin'), client.__getattribute__(
                    'notifications'), client.__getattribute__('notifications_bar'), client.__getattribute__(
                    'savings_account'), client.__getattribute__('savings_account_registered'), client.__getattribute__(
                    'current_account'), client.__getattribute__('current_account_registered')
                f.writelines(
                    f'{client_name}|{account_number}|{current_account_balance}|{passport_number}|{nationality}|{date_of_birth}|{password}|{atm_login_pin}|{json.dumps(notifications)}|{json.dumps(notifications_bar)}|{json.dumps(savings_account)}|{savings_account_registered}|{json.dumps(current_account)}|{current_account_registered}\n')

    # A method to login.
    def login(self):
        clear_terminal()
        BANK_NAME()
        account_number = input('Account number: ')
        password = input('Enter your password: ')
        clear_terminal()
        BANK_NAME()
        loading_animation()
        success = False
        for client in self.clients:
            if account_number == client.__getattribute__('account_number'):
                if password == client.__getattribute__('password'):
                    clear_terminal()
                    BANK_NAME()
                    print('Login Successful')
                    successful_notification()
                    time.sleep(0.6)
                    success = True
                    return account_number, success

        return success

    # A method to get the cuurent account balance
    def current_account_balance(self, acc_number):
        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                current_account_balance = float(client.__getattribute__('current_account_balance'))

        return current_account_balance

    # A method to calculate the total interest earned from the current account deposits.
    def calculate_interest_earned_current_account(self, acc_number):
        # The account number passed in as an argument is used to search for the client object
        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                user = client

        # The transactions dictionary contains all details on the transactions related to the current account
        transactions = dict(user.__getattribute__('current_account'))

        # Initiating the cumulative interest variable
        cumulated_current_account_interest = 0

        # Checking if the transaction dictionary has any ID's
        if len(list(transactions.keys())) > 0:

            # This gets the date of transaction, amount, and the interest and passes them as arguments to the coompound_interest function.
            for key in list(transactions.keys()):

                # [["2c50ecd7-378a-4942-9c35-00fa441b38ac", ["2002-09-14 19:40:28.997112", 1000, 0.01]]]
                # The above is an example of how the list are stored, however here it has been converted to a dictionary
                todays_date = datetime.datetime.now().date()
                transactions_date_string = transactions[key][
                    0]  # Accessing the date object in the dictionary and converting into a string

                # Calculation of the duration of the transaction
                duration = (abs(todays_date.year - int(transactions_date_string[0:4])) * 365) + (abs(
                    todays_date.month - int(transactions_date_string[5:7])) * 30) + abs(
                    int(todays_date.day - int(transactions_date_string[8:10])))

                # Checking if the transaction is eligible for yielding interest, 30 days and above
                if duration >= 30:
                    # converting the duration into month
                    months = duration // 30
                    # The interest is returned by the compound interest function
                    current_acc_interest = compound_interest(float(transactions[key][1]), float(transactions[key][2]),
                                                             months)
                    # It is then appended to cumulated interest variable
                    cumulated_current_account_interest += current_acc_interest

        # The result is the stored in this variable
        cumulated_current_account_interest = cumulated_current_account_interest

        return cumulated_current_account_interest

    # A current account method, with options to deposit, withdraw and check balance
    def current_account(self, acc_number):
        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                user = client

        transactions = dict(user.__getattribute__('current_account'))

        # Getting the value of interest earned by the client
        current_account_interest_receivable = self.calculate_interest_earned_current_account(acc_number)

        # Initiating the current account total, and the dictionary and list to be used within the method
        current_account_total = 0
        current_acc_transactions = {}
        current_acc_transactions_list = []

        # Appending all transactions to the current_acc_transactions
        if len(list(transactions.keys())) > 0:
            for key in list(transactions.keys()):
                todays_date = datetime.datetime.now().date()
                transactions_date_string = transactions[key][0]
                duration = (abs(todays_date.year - int(transactions_date_string[0:4])) * 365) + (abs(
                    todays_date.month - int(transactions_date_string[5:7])) * 30) + abs(
                    int(todays_date.day - int(transactions_date_string[8:10])))

                if duration >= 30:
                    months = duration // 30
                    current_acc_interest = compound_interest(float(transactions[key][1]), float(transactions[key][2]),
                                                             months)

                    current_acc_transactions.update({key: transactions[key]})
                    gross = round((current_acc_interest + float(transactions[key][1])), 2)
                    current_account_total += gross
                else:
                    current_account_total += round((transactions[key][1]), 2)
                    current_acc_transactions.update({key: transactions[key]})

            current_acc_transactions_list = list_generator(current_acc_transactions)


        user.update_current_account_bal(round(current_account_total, 2))

        # Main Loop of the current account
        main_loop_running = True
        while main_loop_running:
            current_acc_transactions_list = current_acc_transactions_list
            try:
                clear_terminal()
                BANK_NAME()

                options = int(input('1. Deposit 2. Withdraw 3. Check Balance 4. Exit:\nOptions:  '))
                phone_number_correct = False

                # Deposit
                if options == 1:
                    solved = False
                    next_level = True
                    inner_run_deposit = True
                    while inner_run_deposit:
                        while not solved:
                            try:
                                clear_terminal()
                                BANK_NAME()
                                # The amount the user wants to deposit via Momo
                                print('here')
                                money_deposit = round(float(input('Enter the amount you want to deposit via momo: ')),
                                                      2)
                                phone_number_correct = False
                                solved = False
                                next_level = True
                                inner_run_deposit = True
                                if type(money_deposit) == float:
                                    solved = True

                            except ValueError:
                                clear_terminal()
                                BANK_NAME()
                                print(
                                    'Error, invalid Data type. Integers only supported. Money should be in digit form.')
                                error_message()
                                time.sleep(1)

                        # Count is used to store the number of times has entered their number, if they do it 3 times, the menu is then terminated
                        count = 1

                        while not phone_number_correct:
                            phone_number = str(input('Enter your phone number(0781234567): '))

                            # The phone number should be 10 characters longs and should have numeric values only
                            if len(phone_number) == 10 and phone_number.isnumeric() == True:
                                phone_number_correct = True

                            # If the user gets it incorrect, the loop gives them the option to retry to enter the number.
                            else:
                                if count < 3:
                                    count += 1
                                    clear_terminal()
                                    BANK_NAME()
                                    if len(phone_number) != 10 and phone_number.isnumeric() == False:
                                        print(
                                            'Invalid Phone Number. It is not numeric, and it should be 10 numbers long.')
                                    elif phone_number.isnumeric() == False:
                                        print('Invalid Phone Number, It is not numeric.')
                                    elif len(phone_number) != 10:
                                        print('Invalid Phone Number,it should be 10 numbers long.')

                                    time.sleep(1)
                                    print(f'Trials: {count}/3')
                                else:
                                    print("Too many failed attempts")
                                    solved = False
                                    inner_run_deposit = False
                                    next_level = False


                        # If the user gets it right with their phone number, they arrive here
                        if next_level:
                            # Confirmation of details, if there is a mistake, they can rectify it.
                            try:
                                confirmation = int(input(
                                    f'Deposit Amount: ${money_deposit}\nPhone Number: +250 {phone_number[1:3]} {phone_number[3:6]} {phone_number[6:11]}\n\n1. Confirm 2. Edit 3. Exit\nOption: '))
                                if confirmation == 2:
                                    solved = False
                                    inner_run_deposit = True
                                    next_level = False
                                    phone_number_correct = True


                                clear_terminal()
                                BANK_NAME()
                            except ValueError:
                                clear_terminal()
                                BANK_NAME()
                                print('Error, invalid Data type. Integers only supported.')
                                error_message()
                                time.sleep(1)


                            # Randomly generated momo_balance
                            if confirmation == 1:
                                if money_deposit <= 100:
                                    x = float(random.randint(90, 100))
                                elif money_deposit <= 300:
                                    x = float(random.randint(250, 300))
                                elif money_deposit <= 2000:
                                    x = float(random.randint(1500, 2000))
                                elif money_deposit <= 10000:
                                    x = float(random.randint(7000, 10000))
                                elif money_deposit > 10000:
                                    x = float(random.randint(8500, 10000))
                                momo_balance = x
                                charges = 0.03
                                total = round((charges + 1) * money_deposit, 2)


                                counter_deposit = 0
                                deposited = False


                                # checking if the user entered amount is sufficient, if not they can change it or just exit and go to deposit more.
                                while not deposited:
                                    resolved_momo_bal = False
                                    if counter_deposit > 0:
                                        resolved_counter_deposit = False
                                        while not resolved_counter_deposit:
                                            clear_terminal()
                                            BANK_NAME()
                                            money_deposit = round(
                                                float(input('Enter the amount you want to deposit via momo: ')), 2)
                                            option_counter_deposit = int(input(
                                                f'\nAmount:\t${money_deposit}\n1. Confirm 2. Edit 3. Exit\nOption:  '))
                                            total = round(money_deposit * (charges + 1), 2)

                                            if option_counter_deposit == 1:
                                                resolved_counter_deposit = True

                                            elif option_counter_deposit == 2:
                                                resolved_counter_deposit = False

                                            elif option_counter_deposit == 3:
                                                inner_run_deposit = False
                                                resolved_counter_deposit = True

                                            clear_terminal()
                                            BANK_NAME()

                                    # Transaction successful

                                    if momo_balance >= total:

                                        clear_terminal()
                                        BANK_NAME()
                                        print("Transaction Successful...")
                                        successful_notification()
                                        time.sleep(1)
                                        # The interest rate for deposit
                                        interest = 0.01

                                        # for reference each transaction is given a random id, the uuid module is used to generate the unique ID.
                                        transcation_date = str(datetime.datetime.now())
                                        transcation_id = str(uuid.uuid4())

                                        # The new transaction details
                                        transaction_update = dict(
                                            [((transcation_id), [transcation_date, money_deposit, interest])])

                                        # The new transactions list. The transactions are stored in a way that allows FIFO method when withdrawings
                                        new_transactions = list(
                                            list_generator({**current_acc_transactions, **transaction_update}))

                                        # Updated Dictionary of the current account
                                        current_acc_transactions = {**current_acc_transactions, **transaction_update}

                                        # Updated total of the current account
                                        current_account_total += money_deposit

                                        # The new attributes are then appended to the client object
                                        user.update_current_account_deposit(new_transactions)
                                        user.update_current_account_bal(current_account_total)

                                        notification = f'You have successfully deposited ${money_deposit} on {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, Time: {datetime.datetime.now().hour}:{datetime.datetime.now().minute} hrs. Your new Current Account balance is ${current_account_total}'
                                        user.notification_update(notification)
                                        user.update_current_account_bal(current_account_total)

                                        self.update_database()
                                        clear_terminal()
                                        BANK_NAME()
                                        print(notification)
                                        running = True

                                        # Stopping the screen from rapidly disappearing
                                        while running:
                                            option = int(input('1. Exit\nOption:  '))
                                            if option == 1:
                                                deposited = True
                                                inner_run_deposit = False
                                                running = False

                                    # Insufficient Balance
                                    elif momo_balance < total:
                                        clear_terminal()
                                        BANK_NAME()
                                        deposited = False
                                        print(
                                            f'Transaction Error: Insufficient Balance.\nAvailable Balance: ${momo_balance}\nCharges: ${round(float(momo_balance * 0.03), 2)}\nMaximum you can send is ${round(momo_balance - (momo_balance * 0.03/1.03), 2)}')
                                        counter_deposit += 1

                                        try:
                                            while not resolved_momo_bal:
                                                option = int(input('1. Restart 2. Exit\nOption: '))
                                                if option == 1:
                                                    deposited = False
                                                    resolved_momo_bal = True
                                                if option == 2:
                                                    deposited = True
                                                    inner_run_deposit = False
                                                    phone_number_correct = True
                                                    main_loop_running = False
                                                    resolved_momo_bal = True

                                        except ValueError:
                                            clear_terminal()
                                            BANK_NAME()
                                            print('Invalid Data type: Integers only')
                                            error_message()
                                            time.sleep(1)


                            elif confirmation == 3:
                                break



                # Withdrawal
                elif options == 2:

                    inner_run_two = True
                    while inner_run_two:
                        clear_terminal()
                        BANK_NAME()

                        amount = float(input('Enter the withdrawal amount: '))
                        clear_terminal()
                        BANK_NAME()
                        loading_animation()

                        # If the withdrawal amount is greater than the current account total, the transaction proceeds
                        if amount <= current_account_total and amount != 0:

                            clear_terminal()
                            BANK_NAME()
                            print("Transaction Successful...")
                            successful_notification()
                            time.sleep(1)

                            # Fifo Function
                            updated_list, compounded_interest_utilised = fifo_withdrawal_30_days(
                                current_acc_transactions_list, amount)

                            if round(compounded_interest_utilised, 2) <= 0.01:
                                current_acc_transactions_list.pop(0)
                            # The Fifo withdrawal function allows to deduct amount in a First In, First out fashion, taking into account the interest
                            # earned
                            # [['825bbeb0-c307-4c08-a228-45e8ee7107c3', ['2021-11-12', 1000.0, 0.10 ]], ['75edc713-335b-4236-944f-f7027d54de42', ['2021-11-12', 100.0, 0.10]]]
                            # For the above two transactions, the first transaction is one month old and it yas yield a an interest of $100.
                            # The amounts which are on [0][1][1] are immutable
                            # Let's say the user wants to withdraw $1200. The function first realises that on the first transaction, the balance is $1000, but the compounded interest
                            # is $100, making the balance $1100. It subtracts that $1100 from the $1000 balance, pop the list and proceeds to the next. The next list is not eligible to
                            # earn interest, so it just subtract the $100 and an empty list is left.
                            # The function returns an updated list: [], compound interest utilised: $200.

                            current_acc_transactions_list = updated_list
                            compounded_interest_utilised = round(compounded_interest_utilised, 2)

                                

                            # The interest receivable is updated by subtracting the utlised amount.
                            current_account_interest_receivable -= compounded_interest_utilised
                            user.update_current_account_withdrawal(updated_list)

                            new_current_acc_bank_bal = current_account_total - amount
                            current_account_total -= amount
                            current_account_total = round(current_account_total, 2)

                            user.update_current_account_bal(new_current_acc_bank_bal)
                            withdrawal_notification = f'You have successfully withdrawn ${amount} and you earned a total of ${compounded_interest_utilised} in interest. Withdrawable amount is ${round((current_account_total), 2)}\n Current A/C Balance: ${current_account_total} '
                            user.notification_update(withdrawal_notification)

                            self.update_database()

                            try:
                                unresolved = True
                                while unresolved:
                                    clear_terminal()
                                    BANK_NAME()
                                    print(withdrawal_notification)
                                    option = int(input('1. Exit\nOption:  '))
                                    if option == 1:
                                        unresolved = False
                                        inner_run_two = False
                            except ValueError:
                                clear_terminal()
                                BANK_NAME()
                                print('Invalid Data type: Integers only')
                                error_message()
                                time.sleep(1)



                        else:
                            unresolved = True
                            while unresolved:
                                clear_terminal()
                                BANK_NAME()
                                maximum_not_0 = f'The amount of money you can withdraw is: {current_account_total}'
                                maximum_0 = f'Deposit money into your current account to start transacting.'
                                print(
                                    f'Insufficient Balance. {maximum_not_0 if current_account_total > 0 else maximum_0}.')
                                decision = int(input('1.Exit\nOption: '))
                                if decision == 1:
                                    inner_run_two = False
                                    unresolved = False
                                else:
                                    unresolved = True

                elif options == 3:
                    clear_terminal()
                    BANK_NAME()
                    print(
                        f'1. Current A/C balance: ${current_account_total}\n2. Total Interest earned: {round(abs(current_account_interest_receivable), 2)}\n')
                    loop = True
                    try:
                        while loop:
                            option = int(input('1. Exit\nOption:  '))
                            if option == 1:
                                loop = False
                    except ValueError:
                        clear_terminal()
                        BANK_NAME()
                        print('Invalid Data type: Integers only')
                        error_message()
                        time.sleep(1)

                elif options == 4:
                    main_loop_running = False
            except  ValueError:
                pass

    # Savings Account Method
    def savings_account(self, acc_number):
        clear_terminal()
        BANK_NAME()
        loading_animation()

        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                user = client
                client_ref = self.clients.index(client)

        # Checking if the user has registered for a current account and giving the option to register one
        register_status = int(user.__getattribute__('savings_account_registered'))
        while register_status != 1:
            option = int(input("You have not registered for the Savings Accounts\n1. Activate 2. Exit\nOption:  "))
            if option == 1:
                clear_terminal()
                BANK_NAME()
                loading_animation()
                print('Registratition in Progress ...')
                clear_terminal()
                BANK_NAME()
                self.clients[client_ref].__setattr__('savings_account_registered', 1)
                notification = f'You have successfully opened a Savings Account. Deposit and earn 3% interest.'
                user.notification_update(notification)
                clear_terminal()
                BANK_NAME()
                print(notification)
                successful_notification()
                register_status = 1
                self.update_database()

            elif option == 2:
                break

        savings_account_transactions_interest_receivable = {}
        savings_account_transactions_no_interest_receivable = {}

        savings_account_withdrawable_amount = 0
        savings_account_balance = 0
        interest_receivable = 0
        if int(user.__getattribute__('savings_account_registered')) > 0:
            transactions = dict(user.__getattribute__('savings_account'))

            if len(list(transactions.keys())) > 0:
                for key in list(transactions.keys()):
                    todays_date = datetime.datetime.now().date()
                    transactions_date_string = transactions[key][0]
                    duration = (abs(todays_date.year - int(transactions_date_string[0:4])) * 365) + (abs(
                        todays_date.month - int(transactions_date_string[5:7])) * 30) + abs(
                        int(todays_date.day - int(transactions_date_string[8:10])))

                    if duration >= 180:
                        months = duration // 30
                        trans_interest_receivable = compound_interest(float(transactions[key][1]),
                                                                      float(transactions[key][2]), months)


                        gross = round(transactions[key][1] + trans_interest_receivable,2)
                        savings_account_withdrawable_amount += round(gross, 2)
                        interest_receivable += round(trans_interest_receivable, 2)

                        savings_account_transactions_interest_receivable.update({key: transactions[key]})


                    else:
                        savings_account_transactions_no_interest_receivable.update({key: transactions[key]})

                    savings_account_balance += transactions[key][1]

        savings_account_interest_eligible_transactions = list(
            list_generator(savings_account_transactions_interest_receivable))

        savings_account_total = round(savings_account_balance + interest_receivable,2)
        savings_account_interest_ineligible_transactions = list(
            list_generator(savings_account_transactions_no_interest_receivable))

        savings_account_withdrawable_amount_ = round(savings_account_withdrawable_amount, 2)

        current_account_balance = float(user.__getattribute__(
            'current_account_balance')) + self.calculate_interest_earned_current_account(acc_number)

        compounded_interest_utilised = 0
        main_loop_running = True
        while main_loop_running:
            interest_receivable = round(interest_receivable, 2)
            try:

                clear_terminal()
                BANK_NAME()
                options = int(input('1. Deposit 2. Withdraw 3. Balance. 4 Exit\nOptions: '))
                clear_terminal()
                if options == 1:
                    inner_run = True
                    while inner_run:
                        clear_terminal()
                        BANK_NAME()
                        amount = round(float(input("Enter the amount you want to credit into your savings a/c: ")),
                                       2)

                        clear_terminal()
                        BANK_NAME()
                        confirmation = int(
                            input(f'Deposit Amount: ${amount}\n1. Confirm 2. Edit 3. Exit\nOption: '))

                        # Deposit
                        if confirmation == 1:
                            if current_account_balance - amount >= 0:
                                clear_terminal()
                                BANK_NAME()
                                print("Transaction Successful...")
                                successful_notification()
                                time.sleep(1)

                                transactions = dict(client.__getattribute__('savings_account'))
                                interest = 0.03

                                withdrawal_transcation_date = str(datetime.datetime.now())
                                transcation_id = str(uuid.uuid4())
                                transaction_update = dict(
                                    [((transcation_id), [withdrawal_transcation_date, amount, interest])])

                                new_current_account_balance = round(current_account_balance - amount, 2)

                                updated_list = list(list_generator({**transactions, **transaction_update}))

                                new_current_account_balance_transactions = user.deduct_from_current_acc(amount)

                                user.update_current_account(new_current_account_balance_transactions)
                                user.update_current_account_bal(new_current_account_balance)
                                user.update_savings_account(updated_list)
                                savings_account_total += round(amount, 2)

                                notification = f'You have successfully transferred ${amount} to your savings account on {datetime.datetime.now().date()}. The money is withdrawable on {datetime.datetime.now().date() + timedelta(days=180)}.\nThe savings account balance is ${round(savings_account_total, 2)}\nCurrent A/C balance is ${new_current_account_balance}'
                                user.notification_update(notification)
                                user.update_current_account(new_current_account_balance_transactions)

                                self.update_database()
                                unresolved = True
                                while unresolved:
                                    clear_terminal()
                                    BANK_NAME()
                                    print(notification)
                                    option = int(input('1. Exit\nOption:  '))
                                    if option == 1:
                                        unresolved = False
                                        inner_run = False

                            else:
                                clear_terminal()
                                BANK_NAME()
                                unresolved = True
                                while unresolved:
                                    clear_terminal()
                                    BANK_NAME()
                                    option = int(input((
                                        f'You have insufficient funds.\nCurrent A/C Balance: ${current_account_balance}.\n\n1. Exit\nOption:  ')))
                                    if option == 1:
                                        inner_run = False
                                        unresolved = False
                                    else:
                                        unresolved = True

                        elif confirmation == 2:
                            inner_run = True
                        elif confirmation == 3:
                            inner_run = False

                elif options == 2:
                    inner_run_two = True
                    while inner_run_two:
                        clear_terminal()
                        BANK_NAME()

                        withdrawal_amount = round(float(input('Enter the withdrawal amount: ')),2)
                        clear_terminal()
                        BANK_NAME()
                        loading_animation()

                        if withdrawal_amount <= savings_account_withdrawable_amount and withdrawal_amount != 0.0:
                            clear_terminal()

                            successful_notification()
                            time.sleep(1)

                            current_account_balance = float(user.__getattribute__('current_account_balance'))


                            updated_list, compounded_interest_utilised = fifo_withdrawal_180_days(
                                savings_account_interest_eligible_transactions, withdrawal_amount)



                            if round(compounded_interest_utilised, 2) < 0.01:
                                updated_list.pop(0)
                            interest_receivable -= compounded_interest_utilised

                            interest_receivable = round(interest_receivable, 2)


                            savings_account_transactions = savings_account_interest_eligible_transactions + savings_account_interest_ineligible_transactions

                            withdrawal_transaction_date = str(datetime.datetime.now().date())
                            withdrawal_transaction_id = str(uuid.uuid4())
                            transaction_update = dict(
                                [((withdrawal_transaction_id), [withdrawal_transaction_date, withdrawal_amount, 0.01])])

                            transaction_update = list_generator(transaction_update)

                            savings_account_total -= round(withdrawal_amount, 2)

                            savings_account_withdrawable_amount_ -= round(withdrawal_amount, 2)
                            print(savings_account_withdrawable_amount_)
                            savings_account_withdrawable_amount_ = round(savings_account_withdrawable_amount_, 2)


                            savings_account_total = round(savings_account_total, 2)
                            current_account_balance += round(withdrawal_amount, 2)
                            user.update_current_account_bal(current_account_balance)
                            user.update_current_account(transaction_update)
                            user.update_savings_account(savings_account_transactions)

                            savings_withdrawal_notification = f'You have successfully withdrawn ${withdrawal_amount} and you earned a total of ${compounded_interest_utilised} in interest. Withdrawable amount is ${round((savings_account_withdrawable_amount_), 2)}\n Savings A/C Balance: ${savings_account_total} '
                            user.notification_update(savings_withdrawal_notification)

                            self.update_database()
                            unresolved = True
                            while unresolved:
                                clear_terminal()
                                BANK_NAME()
                                print(savings_withdrawal_notification)
                                option = int(input('1. Exit\nOption:  '))
                                if option == 1:
                                    unresolved = False
                                    inner_run_two = False



                        else:
                            unresolved = True
                            while unresolved:
                                clear_terminal()
                                BANK_NAME()
                                max_not_0 = f'Insufficient Balance. The amount of money you can withdraw is: ${savings_account_withdrawable_amount_}.'
                                max_0 = f'Insufficient Balance. Save more to withdraw.'
                                print(f'{max_0 if savings_account_withdrawable_amount_ <=0 else max_not_0 }')
                                decision = int(input('1.Exit\nOption: '))
                                if decision == 1:
                                    inner_run_two = False
                                    unresolved = False
                                else:
                                    unresolved = True


                elif options == 3:
                    inner_run_three = True
                    while inner_run_three:
                        clear_terminal()
                        BANK_NAME()
                        optionchosen = int(input(
                            f'1. The total Redeemable amount: ${round(savings_account_withdrawable_amount_, 2)}.\n2. Total interest earnings: ${abs(round((interest_receivable),2))} .\n3. The savings account balance is ${round(savings_account_total, 2)}.\n\n1.Exit\nOption: '))
                        if optionchosen == 1:
                            inner_run_three = False

                elif options == 4:
                    main_loop_running = False
                    break



            except ValueError:
                print('Invalid input')

    # A Method to check the total current a/c balance
    def check_balance(self, acc_number):
        clear_terminal()
        BANK_NAME()
        loading_animation()
        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                user = client
        current_account_balance = round(float(user.__getattribute__(
            'current_account_balance')), 2)
        print(
            f'1. Current A/C Balance:\t${current_account_balance}\n2. Total Interest Receivable: {round(float(self.calculate_interest_earned_current_account(acc_number)),2)}')

    # A Method to transfer money to another client
    def transfer_money(self, acc_number):
        clear_terminal()
        BANK_NAME()
        loading_animation()
        exit_loop = False
        while not exit_loop:

            try:
                amount_of_transfer = 0
                resolved = False
                recipient_details_true = False
                while not resolved:
                    clear_terminal()
                    BANK_NAME()
                    recipient_full_name = input('Recipient Full Account Name: ')
                    recipient_account_number = input('Recipient Account Number: ')
                    amount_of_transfer = round(float(input('Enter the amount: ')),2)
                    clear_terminal()
                    BANK_NAME()

                    for client in self.clients:
                        if client.__getattribute__('account_number') == acc_number:
                            sender = client
                        elif client.__getattribute__('account_number') == recipient_account_number:
                            if client.__getattribute__('client_name').upper() == recipient_full_name.upper():
                                recipient = client
                                recipient_details_true = True
                            else:
                                recipient_details_true = False

                    if recipient_details_true:
                        sender_current_account_balance = round(
                            float(sender.__getattribute__('current_account_balance')), 2)
                        sender_current_account_transactions = sender.__getattribute__('current_account')
                        recipient_current_account_transactions = recipient.__getattribute__("current_account")

                        bank_charges = 0.05
                        government_tax = 0.01

                        transfer_aggregate_cost = round(amount_of_transfer + (bank_charges * amount_of_transfer) + (
                                government_tax * amount_of_transfer), 2)

                        option_details_loop = True
                        while option_details_loop:
                            clear_terminal()
                            BANK_NAME()
                            print(
                                f'Confirm receiver details:\n\n1. Full Name:\t{recipient_full_name}\n2. Account Number:\t{recipient_account_number}\n3. Amount\t${amount_of_transfer}')
                            try:
                                confirm_details = int(input('\n1. Confirm 2. Edit 3. Exit \nOption: '))

                                if confirm_details == 1:
                                    transaction_validation_start = True
                                    option_details_loop = False
                                    option = confirm_details


                                elif confirm_details == 2:
                                    transaction_validation_start = False
                                    option_details_loop = False


                                elif confirm_details == 3:
                                    resolved = True
                                    exit_loop = True
                                    option_details_loop = False
                                    break


                            except ValueError:
                                clear_terminal()
                                BANK_NAME()
                                print('Invalid Data type: Integers only')
                                error_message()
                                time.sleep(1)

                        if exit_loop:
                            break




                        transaction_counter = 0

                        while transaction_validation_start:
                            if option == 1:
                                clear_terminal()
                                BANK_NAME()
                                print(f'Proccessing Transaction')
                                loading_animation()

                                if recipient_details_true:
                                    clear_terminal()
                                    BANK_NAME()
                                    if transaction_counter > 0:
                                        transaction_counter_loop = True
                                        while transaction_counter_loop:
                                            updated_amount = float(input('Enter the new amount: '))
                                            confirm_loop = True
                                            while confirm_loop:
                                                try:
                                                    clear_terminal()
                                                    BANK_NAME()
                                                    print(
                                                        f'Confirm receiver details:\n\n1. Full Name:\t{recipient_full_name}\n2. Account Number:\t{recipient_account_number}\n3. Amount\t${updated_amount}')
                                                    confirm_details = int(
                                                        input('\n1. Confirm 2. Edit 3. Exit \nOption: '))
                                                    if confirm_details == 1:
                                                        amount_of_transfer = round(updated_amount, 2)
                                                        transfer_aggregate_cost = round(
                                                            amount_of_transfer + (bank_charges * amount_of_transfer) + (
                                                                        government_tax * amount_of_transfer), 2)
                                                        confirm_loop = False
                                                        transaction_counter_loop = False

                                                    elif confirm_details == 2:
                                                        confirm_loop = False


                                                    elif confirm_details == 3:
                                                        transaction_counter = False
                                                        resolved = True
                                                        exit_loop = True

                                                except ValueError:
                                                    clear_terminal()
                                                    BANK_NAME()
                                                    print('Invalid Data type: Integers only')
                                                    error_message()
                                                    time.sleep(1)

                                    if sender_current_account_balance >= transfer_aggregate_cost:
                                        clear_terminal()
                                        BANK_NAME()
                                        print("Transaction Successful...")
                                        successful_notification()
                                        time.sleep(1)

                                        transfer_transaction_date = str(datetime.datetime.now().date())
                                        withdrawal_transaction_id = str(uuid.uuid4())
                                        sender_transaction_update = dict([((withdrawal_transaction_id),
                                                                           [transfer_transaction_date,
                                                                            amount_of_transfer,
                                                                            0.01])])

                                        updated_list, compound_interest_utilised = fifo_withdrawal_30_days(
                                            sender_current_account_transactions, transfer_aggregate_cost)

                                        recipient_current_account_transactions = {
                                            **dict(recipient_current_account_transactions), **sender_transaction_update}

                                        recipient.current_account = list_generator(recipient_current_account_transactions)

                                        sender_new_balance = round(
                                            sender_current_account_balance - transfer_aggregate_cost, 2)

                                        recipient_old_balance = round(float(recipient.__getattribute__(
                                            'current_account_balance')), 2)
                                        recipient_new_balance = round(float(recipient_old_balance) + float(amount_of_transfer), 2)

                                        sender.update_current_account_bal(sender_new_balance)
                                        recipient.update_current_account_bal(recipient_new_balance)

                                        clear_terminal()
                                        BANK_NAME()
                                        sender_notifications = f'You have successfully sent ${amount_of_transfer} to {recipient_full_name}, on {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, Time: {datetime.datetime.now().hour}:{datetime.datetime.now().minute} hrs. Your Current Account balance is ${sender_new_balance}. \nINTEREST RECEIVABLE UTLISED: {round(compound_interest_utilised, 2)}'
                                        sender.notification_update(sender_notifications)

                                        receiver_notifications = f'You have successfully received ${amount_of_transfer} from {sender.__getattribute__("client_name")}, on {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}, Time: {datetime.datetime.now().hour}:{datetime.datetime.now().minute} hrs. Your new bank balance is ${recipient_new_balance}'
                                        recipient.notification_update(receiver_notifications)
                                        self.update_database()

                                        print(sender_notifications)
                                        unresolved = True
                                        while unresolved:
                                            try:
                                                option = int(input('1. Exit\n Options: '))
                                                transaction_validation_start = False
                                                resolved = True
                                                exit_loop = True
                                                unresolved = False

                                            except ValueError:
                                                clear_terminal()
                                                BANK_NAME()
                                                print('Invalid Data type: Integers only')
                                                error_message()
                                                time.sleep(1)


                                    else:
                                        loop_inside = True
                                        while loop_inside:
                                            try:
                                                clear_terminal()
                                                BANK_NAME()

                                                # Variables of storing messages, to be displayed depending on the balance of the client

                                                maximum_0 = f'Deposiit money to start making transactions.'
                                                # A calculation of the maximum balance amount a user can send
                                                maximum_not_0 = f'the maximum amount you can send ${round(sender_current_account_balance * (1 - (6 / 106)), 2)}'  # A calculation of the maximum balance amount a user can send
                                                max_amount = round(sender_current_account_balance * (1 - (6 / 106)), 2)

                                                # A ternary to change the message depending on the balance of the client
                                                option = int(input(
                                                    f'Insufficient Balance, {maximum_not_0 if max_amount > 0 else maximum_0}\n {"1. Exit" if max_amount <= 0 else "1. Edit 2. Exit"}\nOption: '))

                                                if max_amount > 0:
                                                    if option == 1:
                                                        transaction_counter += 1
                                                        transaction_validation_start = True
                                                        loop_inside = False
                                                    elif option == 2:
                                                        exit_loop = True
                                                        transaction_validation_start = False
                                                        resolved = True
                                                        loop_inside = False

                                                elif max_amount <= 0:
                                                    if option == 1:
                                                        exit_loop = True
                                                        transaction_validation_start = False
                                                        resolved = True
                                                        loop_inside = False


                                            except ValueError:
                                                clear_terminal()
                                                BANK_NAME()
                                                print('Invalid Data type: Integers only')
                                                error_message()
                                                time.sleep(1)

                                else:
                                    clear_terminal()
                                    BANK_NAME()
                                    resolved_inside = False
                                    while not resolved_inside:
                                        try:
                                            option = int(input('1. Edit 2. Exit\nOption: '))
                                            if option == 1:
                                                resolved_inside = True
                                                resolved = False
                                            elif option == 2:
                                                resolved_inside = True
                                                exit_loop = True
                                        except ValueError:
                                            clear_terminal()
                                            BANK_NAME()
                                            print('Invalid Data type: Integers only')
                                            error_message()
                                            time.sleep(1)

                            elif option == 2:
                                resolved = False

                            elif option == 3:
                                exit_loop = True

                    else:
                        clear_terminal()
                        BANK_NAME()
                        else_loop = True
                        while else_loop:
                            try:
                                else_loop_option = int(
                                    input('RECEPIENT DETAILS ARE NOT CORRECT.\n\n1. Edit 2. Exit\nOption: '))

                                if else_loop_option == 1:
                                    else_loop = False
                                elif 2:
                                    else_loop = False
                                    resolved = True
                                    exit_loop = True

                            except ValueError:
                                clear_terminal()
                                BANK_NAME()
                                print('Invalid Data type: Integers only')
                                error_message()
                                time.sleep(1)



            except ValueError:
                clear_terminal()
                BANK_NAME()
                print('Error, Input: Invalid Datatype')
                error_message()
                time.sleep(2)

    # A method to view notifications
    def view_notification(self, acc_number):

        clear_terminal()
        BANK_NAME()
        loading_animation()

        resolved = False
        while not resolved:
            for client in self.clients:
                if client.__getattribute__('account_number') == acc_number:
                    reference_number = self.clients.index(client)
                    client_notifications = client.__getattribute__('notifications')
                    client_notifications = list(client_notifications)
                    client_notifications.reverse()
                    user = client

            self.clients[reference_number].__setattr__('notifications_bar', [])

            for index, notification in enumerate(client_notifications):
                index += 1
                print(f'{index}.\t {notification}', end="\n")

            unresolved = True
            while unresolved:
                number_of_notifications = len(client_notifications)
                if number_of_notifications == 0:
                    check_notifications(client_notifications)

                option = int(input('\n1. Delete All \t2. Exit the screen\nOption:\t'))
                if option == 1:
                    clear_terminal()
                    BANK_NAME()
                    self.clients[reference_number].__setattr__('notifications', [])
                    client_notifications.clear()
                    self.update_database()



                elif option == 2:
                    resolved = True
                    break

    def notification_bar(self, acc_number):
        for client in self.clients:
            if client.__getattribute__('account_number') == acc_number:
                notification_bar_ = client.__getattribute__('notifications_bar')
                notification_bar_ = list(notification_bar_)
                break

        number_of_notifications = len(notification_bar_)
        return number_of_notifications


bank = Bank()
bank.load_database()

# A function to clear the terminal
clear_terminal = lambda: os.system('cls')


# A function to notify a succesful login or transaction.
def successful_notification(notification=True):
    if os.path.isfile('./assets/successful.wav'):
        if notification:
            winsound.PlaySound('./assets/successful.wav', winsound.SND_ALIAS)


# A function to make a sound when there is an error
def error_message(notification=True):
    if os.path.isfile('./assets/unsuccessful.wav'):
        if notification:
            winsound.PlaySound('./assets/unsuccessful.wav', winsound.SND_ALIAS)


# A function to convert a dictionary into this list [['assdads'], [2021/12/3, 20, 0.01]]], the format we use.
def list_generator(dict):
    new_list = []
    for i, key in enumerate(list(dict.keys())):
        new_list.append([(key), (dict[key])])
    return new_list


# A compound interest calculator
def compound_interest(principle, rate, time):
    # Calculates compound interest
    CI = principle * pow(1 + rate, time) - principle
    return CI


# A function to display the name of the bank
def BANK_NAME():
    print(f'DANGOTE BANK LIMITED\n')


# A function to check if they are any notifications to displayed
def check_notifications(notif):
    if len(notif) == 0:
        print('No Notifications.')


# A function to animate loading
def loading_animation():
    animation = "|/-\\"
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


# A function to calculate interest receivable
def compound_interest_30_days(list_n1):
    todays_date = datetime.datetime.now().date()

    transactions_date_string = list_n1[0][1][0]
    principle = list_n1[0][1][1]
    rate = list_n1[0][1][2]

    duration = (abs(int(todays_date.year) - int(transactions_date_string[0:4])) * 365) + (abs(
        todays_date.month - int(transactions_date_string[5:7])) * 30) + abs(
        int(todays_date.day - int(transactions_date_string[8:10])))

    if duration >= 30:

        duration //= 30
        CI = principle * pow(1 + rate, duration) - principle

        return True, CI
    else:
        CI = 0
        return False, CI

# A function to calculate interest receivable
def compound_interest_180_days(list_n1):
    todays_date = datetime.datetime.now().date()

    transactions_date_string = list_n1[0][1][0]
    principle = list_n1[0][1][1]
    rate = list_n1[0][1][2]

    duration = (abs(int(todays_date.year) - int(transactions_date_string[0:4])) * 365) + (abs(
        todays_date.month - int(transactions_date_string[5:7])) * 30) + abs(
        int(todays_date.day - int(transactions_date_string[8:10])))

    if duration >= 180:

        duration //= 30
        CI = principle * pow(1 + rate, duration) - principle

        return True, CI
    else:
        CI = 0
        return False, CI

# A fifo function to return a list of transactions
def fifo_withdrawal_30_days(transactions, user_input_):
    user_input = user_input_
    utilised = 0

    while user_input != 0:
        if len(transactions) == 0 or user_input == 0:
            break

        compounded, compound_interest_earned = compound_interest_30_days(transactions)

        immutable = transactions[0][1][1]

        immutable_compounded = compound_interest_earned + immutable
        print(immutable_compounded)
        interest_rate = float(compound_interest_earned / immutable)

        if compounded:

            if user_input <= immutable_compounded:
                if user_input - immutable_compounded == 0:
                    utilised += round(compound_interest_earned, 2)
                    transactions.pop(0)
                    user_input = 0

                else:
                    utilised += interest_rate / (interest_rate + 1) * user_input

                    new = immutable_compounded - user_input
                    transactions[0][1][1] = new - (new * (interest_rate / (interest_rate + 1)))
                    user_input = 0


            else:
                if user_input - immutable_compounded == 0:
                    utilised += round(compound_interest_earned)
                    transactions.pop(0)
                    user_input = 0

                else:
                    utilised += immutable_compounded - immutable
                    transactions.pop(0)
                    user_input -= immutable_compounded

        else:

            if user_input <= immutable:
                if user_input - immutable == 0:
                    transactions.pop(0)
                    user_input = 0

                else:
                    transactions[0][1][1] = round(immutable - user_input, 2)
                    user_input = 0

            else:

                if user_input - immutable == 0:
                    transactions.pop(0)
                    user_input = 0

                else:
                    transactions.pop(0)
                    user_input -= immutable

    return transactions, utilised


def fifo_withdrawal_180_days(transactions, user_input_):
    user_input = user_input_
    utilised = 0

    while user_input != 0:
        if len(transactions) == 0 or user_input == 0:
            break

        compounded, compound_interest_earned = compound_interest_180_days(transactions)

        immutable = transactions[0][1][1]

        immutable_compounded = compound_interest_earned + immutable
        print(immutable_compounded)
        interest_rate = float(compound_interest_earned / immutable)

        if compounded:

            if user_input <= immutable_compounded:
                if user_input - immutable_compounded == 0:
                    utilised += round(compound_interest_earned, 2)
                    transactions.pop(0)
                    user_input = 0

                else:
                    utilised += interest_rate / (interest_rate + 1) * user_input

                    new = immutable_compounded - user_input
                    transactions[0][1][1] = new - (new * (interest_rate / (interest_rate + 1)))
                    user_input = 0


            else:
                if user_input - immutable_compounded == 0:
                    utilised += round(compound_interest_earned)
                    transactions.pop(0)
                    user_input = 0

                else:
                    utilised += immutable_compounded - immutable
                    transactions.pop(0)
                    user_input -= immutable_compounded

        else:

            if user_input <= immutable:
                if user_input - immutable == 0:
                    transactions.pop(0)
                    user_input = 0

                else:
                    transactions[0][1][1] = round(immutable - user_input, 2)
                    user_input = 0

            else:

                if user_input - immutable == 0:
                    transactions.pop(0)
                    user_input = 0

                else:
                    transactions.pop(0)
                    user_input -= immutable

    return transactions, utilised


# A funtion for aunthetication
def user_aunthecation():
    run = True
    while run:
        try:
            clear_terminal()
            BANK_NAME()
            option_chosen_one = int(input('1. Login\n2. Register\nOption:\t'))
            if option_chosen_one == 1:
                result = bank.login()
                if result is not False:
                    account_number, aunth = result
                    run = False
                    return account_number, aunth;


                elif result is False:
                    clear_terminal()
                    BANK_NAME()
                    option = int(input('\nWrong Credentials\n1. Try Again\nOption:\t'))
                    if option == 1:
                        run = True



            elif option_chosen_one == 2:
                bank.add_new_client()
                bank.update_database()
                option = int(input('1. Exit\nOption:\t'))
                if option == 1:
                    run = True


        except ValueError:
            clear_terminal()
            BANK_NAME()
            print('Error, invalid Data type. Integers only supported.')
            error_message()
            time.sleep(1)


# Values returned after an authentication
acc_number, authorization = user_aunthecation()


def terminal(acc_num_terminal, auth):
    if auth:
        run_terminal = True
        while run_terminal:
            clear_terminal()
            BANK_NAME()
            dictionary_prompts = {
                1: '1. View Balance',
                2: '2. Send Money',
                3: '3. Current Account',
                4: '4. Savings Account',
                5: '5. Notifications',
                6: '6. Exit'
            }

            for i, value in enumerate(list(dictionary_prompts.values())):
                if i == 4:
                    print(f'{value}\t[{bank.notification_bar(acc_num_terminal)}]')
                else:
                    print(value)
            try:
                option_selected = int(input('Select an option: '))

                if option_selected == 1:
                    clear_terminal()
                    BANK_NAME()
                    bank.check_balance(acc_num_terminal)
                    option_prompt1 = int(input('\n1. Exit\nOption:\t'))
                    if option_prompt1 == 1:
                        continue

                elif option_selected == 2:
                    clear_terminal()
                    BANK_NAME()
                    bank.transfer_money(acc_num_terminal)
                    bank.update_database()

                if option_selected == 3:
                    clear_terminal()
                    BANK_NAME()
                    bank.current_account(acc_num_terminal)
                    bank.update_database()

                if option_selected == 4:
                    clear_terminal()
                    BANK_NAME()
                    bank.savings_account(acc_num_terminal)

                if option_selected == 5:
                    clear_terminal()
                    BANK_NAME()
                    option_prompt1 = bank.view_notification(acc_num_terminal)
                    bank.update_database()
                    if option_prompt1 == True:
                        continue

                if option_selected == 6:
                    clear_terminal()
                    BANK_NAME()
                    option_prompt1 = int(input('\nAre you sure you want to Quite?\n1. YES\t2.NO\nOption:\t'))
                    if option_prompt1 == 1:
                        clear_terminal()
                        BANK_NAME()
                        print(f"\n\nThank you for using Dangote Bank.\n\n\nKaspaGOAT Systems\n{date.today().year}\n©")
                        time.sleep(3)
                        run_terminal = False
                    elif option_prompt1 == 2:
                        run_terminal = True

            except ValueError:
                clear_terminal()
                BANK_NAME()
                print('Error, invalid Data type. Integers only supported.')
                error_message()
                time.sleep(1)


#Function To start the terminal prompts
terminal(acc_number, authorization)


