class Bank:
    def __init__(self):
        self.customer_details = []
        self.started = False
        self.amount = 1000
        self.Tranfer_amount = False

    def user_registeration(self, user_name, phone_no, password):
        amount = self.amount
        conditions = True
        if len(str(phone_no)) > 10 or len(str(phone_no)) < 10:
            print("INVALID PHONE NUMBER! PLEASE ENTER A 10 DIGIT NUMBER")
            conditions = False

        if len(password) < 5 or len(password) > 20:
            print("ENTER A PASSWORD GREATER THAN 5 AND LESS THAN 20 CHARACTER")
            conditions = False

        if conditions == True:
            print("SUCCESS! ACCOUNT CREATED")
            self.customer_details = [user_name, phone_no, password, amount]
            with open(f"{user_name}.txt", "w") as f:
                for details in self.customer_details:
                    f.write(str(details) + "\n")

    def login(self, user_name, phone_no, password):
        with open(f"{user_name}.txt", "r") as f:
            details = f.read()
            self.customer_details = details.split("\n")
            if str(phone_no) in str(self.customer_details):
                if str(password) in str(self.customer_details):
                    self.started = True

            if self.started == True:
                print(f"{user_name} LOGGED IN TO YOUR ACCOUNT")
                self.amount = int(self.customer_details[3])
                self.user_name = user_name

            else:
                print("WRONG DETAILS")

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            with open(f"{user_name}.txt", "r") as f:
                details = f.read()
                self.customer_details = details.split("\n")

            with open(f"{user_name}.txt", "w") as f:
                f.write(details.replace(str(self.customer_details[3]), str(self.amount)))

            print("SUCCESS! YOUR AMOUNT ADDED TO YOUR ACCOUNT")

        else:
            print("ENTER CORRECT VALUE OF AMOUNT")

    def Amount_transfer(self, amount, user_name, phone_no):
        with open(f"{user_name}.txt", "r") as f:
            details = f.read()
            self.customer_details = details.split("\n")
            if str(phone_no) in self.customer_details:
                self.Tranfer_amount = True

        if self.Tranfer_amount == True:
            total_cash = int(self.customer_details[3]) + amount
            left_cash = self.amount - amount
            with open(f"{user_name}.txt", "w") as f:
                f.write(details.replace(str(self.customer_details[3]), str(total_cash)))

            with open(f"{self.user_name}.txt", "r") as f:
                details_2 = f.read()
                self.customer_details = details_2.split("\n")

            with open(f"{self.user_name}.txt", "w") as f:
                f.write(details_2.replace(str(self.customer_details[3]), str(left_cash)))

            print("SUCCESSFULLY AMOUNT TRANSFERED TO", user_name, "-", phone_no)
            print("BALANCE LEFT =", left_cash)
            self.amount = left_cash

    def reset_password(self, password):
        if len(password) < 5 or len(password) > 18:
            print("ENTER A PASSWORD GREATER THAN 5 AND LESS THAN 18 CHARACTER")
        else:
            with open(f"{self.user_name}.txt", "r") as f:
                details = f.read()
                self.customer_details = details.split("\n")

            with open(f"{self.user_name}.txt", "w") as f:
                f.write(details.replace(str(self.customer_details[2]), str(password)))
            print("SUCCESS! NEW PASSWORD WAS SET")

    def reset_phone_no(self, phone_no):
        if len(str(phone_no)) > 10 or len(str(phone_no)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{self.user_name}.txt", "r") as f:
                details = f.read()
                self.customer_details = details.split("\n")

            with open(f"{self.user_name}.txt", "w") as f:
                f.write(details.replace(str(self.customer_details[1]), str(phone_no)))
            print("new Phone number set up successfully")


if __name__ == "__main__":
    DDCBANK = Bank()
    print("WELCOME TO DDC BANK")
    print("1.LOGIN TO YOUR ACCOUNT")
    print("2.CREATE AN ACCOUNT")
    user = int(input("ENTER 1 / 2 : "))

    if user == 1:
        print("TO LOGIN")
        user_name = input("ENTER USER NAME: ")
        phone_no = int(input("ENTER USER PHONE NUMBER: "))
        password = input("ENTER PASSWORD: ")
        DDCBANK.login(user_name, phone_no, password)
        while True:
            if DDCBANK.started:
                print("1.ADD AMOUNT")
                print("2.CHECK BALANCE")
                print("3.AMOUNT TRANSFER")
                print("4.EDIT YOUR PROFILE")
                print("5.LOGOUT")
                user_login = int(input())
                if user_login == 1:
                    print("YOUR BALANCE IS =", DDCBANK.amount)
                    amount = int(input("ENTER AMOUNT: "))
                    DDCBANK.deposit(amount)
                    print("\n1.BACK TO MENU")
                    print("2.LOGOUT AND EXIT")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif user_login == 2:
                    print("BALANCE =", DDCBANK.amount)
                    print("\n1.BACK TO MENU")
                    print("2.LOGOUT AND EXIT")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif user_login == 3:
                    print("BALANCE =", DDCBANK.amount)
                    amount = int(input("ENTER AMOUNT: "))
                    if amount >= 0 and amount <= DDCBANK.amount:
                        user_name = input("ENTER CUSTOMER NAME: ")
                        phone_no = input("ENTER CUSTOMER PHONE NUMBER: ")
                        DDCBANK.Amount_transfer(amount, user_name, phone_no)
                        print("\n1.BACK TO MENU")
                        print("2.LOGOUT")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("ENTER VALID AMOUNT")

                    elif amount > DDCBANK.amount:
                        print("ENOUGH BALANCE NOT AVAILABLE")

                elif user_login == 4:
                    print("1.CHANGE PASSWORD")
                    print("2.CHANGE PHONE NUMBER")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("ENTER NEW PASSWORD: ")
                        DDCBANK.reset_password(new_passwrod)
                        print("\n1.BACK TO MENU")
                        print("2.LOGOUT")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("ENTER NEW PHONE NUMBER: "))
                        DDCBANK.reset_phone_no(new_ph)
                        print("\n1.BACK TO MENU")
                        print("2.LOGOUT AND EXIT")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif user_login == 5:
                    break

    if user == 2:
        print("CREATING AN ACCOUNT")
        user_name = input("ENTER YOUR NAME: ")
        phone_no = int(input("ENTER YOUR PHONE NUMBER: "))
        password = input("ENTER PASSWORD: ")
        DDCBANK.user_registeration(user_name, phone_no, password)