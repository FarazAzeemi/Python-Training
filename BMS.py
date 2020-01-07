class AccountHolder(object):
    CNIC = ""
    Title = ""
    Gender = ""
    Age = 0

    def __init__(self, cnic=None, title=None, gender=None, age=0):
        self.CNIC = cnic
        self.Title = title
        self.Gender = gender
        self.Age = age

    def printDetails(self):
        print("Title          : " + self.Title)
        print("CNIC           :  " + self.CNIC)
        if self.Gender.upper() == 'M':
            print("Gender         : MALE")
        else:
            print("Gender         : FEMALE")
        print("Age            :  " + str(self.Age))

    def modifyAccount(self, age):
        self.Age = age


class AccountBalance(object):
    AccBalance = 0.0

    def __init__(self, accbalance=None):
        self.AccBalance = accbalance

    def addbalance(self, balance):
        self.AccBalance = self.AccBalance + balance

    def redcbalance(self, balance):
        self.AccBalance = self.AccBalance - balance

    def getbalance(self):
        return self.AccBalance

    def printDetails(self):
        print("Account Balance:  " + str(self.AccBalance))


class Account(object):
    Account_Number = 0
    Account_Type = ""
    Account_Holder = AccountHolder()
    Account_Balance = AccountBalance()
    Active = True

    def __init__(self, accnumber, acctype, cnic, title, gender, age, deposit, active):
        self.Account_Number = accnumber
        self.Account_Type = acctype
        self.Active = active
        self.Account_Holder = AccountHolder(cnic, title, gender, age)
        self.Account_Balance = AccountBalance(deposit)

    def getaccholder(self):
        return self.Account_Holder

    def addbalance(self, balance):
        self.Account_Balance.addbalance(balance)

    def redcbalance(self, balance):
        self.Account_Balance.redcbalance(balance)

    def printDetails(self):
        print("Account Number : " + str(self.Account_Number))
        if self.Account_Type.upper() == 'S':
            print("Account Type   : SAVING ACCOUNT")
        else:
            print("Account Type   : CURRENT ACCOUNT")
        if self.Active:
            print("Account Status : ACTIVE")
        else:
            print("Account Status : DORMANT/ CLOSED")
        self.Account_Holder.printDetails()
        self.Account_Balance.printDetails()

    def closeAccount(self):
        self.Active == False

    def modifyAccount(self, age, accstatus):
        if accstatus.upper() == 'A':
            self.Active = True
        else:
            self.Active = False
        self.Account_Holder.modifyAccount(age)


class BMS(object):
    def createaccount(self):
        accnumber = int(input("Please enter Account Number: "))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        acctype = input("Enter Account Type (C = Current, S = Saving): ")
        if acctype.upper() != 'C' and acctype.upper() != 'S':
            print("Invalid Account Type.")
            return

        cnic = input("Enter Account Holder CNIC: ")
        if len(cnic) != 15:
            print("Invalid CNIC.")
            return

        title = input("Enter Account Title (at least 5 characters): ")
        if len(title) < 5:
            print("Invalid Title.")
            return

        gender = input("Please provide Account Holder gender (M = Male, F = Female): ")
        if gender.upper() != 'M' and gender.upper() != 'F':
            print("Invalid gender.")
            return

        age = int(input("Please enter Account Holder age: "))
        if age < 0 or age > 100:
            print("Invalid value given.")
            return

        deposit = float(input("Please enter initial deposit: "))
        if deposit <= 0:
            print("Invalid value given.")
            return

        active = True

        return Account(accnumber, acctype.upper(), cnic.upper(), title.upper(), gender.upper(), age, deposit, active)

    def depositamount(self, accounts):
        accnumber = int(input("Please enter Account Number: "))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        amount = float(input("Please enter amount of Deposit: "))
        if amount < 0:
            print("Invalid amount given.")
            return False

        accfound = False
        for acc in accounts:
            if acc.Account_Number == accnumber:
                if not acc.Active:
                    print("Account dormant/ closed. Cannot perform operation.")
                    return

                accfound = True
                acc.addbalance(amount)
                print("New balance amount: " + str(acc.Account_Balance.getbalance()))
                break

        if not accfound:
            print("Invalid Account Number.")
            return False

    def withdrawamount(self, accounts):
        accnumber = int(input("Please enter Account Number: "))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        amount = float(input("Please enter amount to Withdraw: "))
        if amount < 0:
            print("Invalid amount given.")
            return False

        accfound = False
        for acc in accounts:
            if acc.Account_Number == accnumber:
                if not acc.Active:
                    print("Account dormant/ closed. Cannot perform operation.")
                    return False

                if amount > acc.Account_Balance.getbalance():
                    print("Amount is greater than available balance: " + str(acc.Account_Balance.getbalance()))
                    return False
                accfound = True
                acc.redcbalance(amount)
                print("New balance amount: " + str(acc.Account_Balance.getbalance()))
                break

        if not accfound:
            print("Invalid Account Number.")
            return False

        return True

    def balanceEnq(self,accounts):
        accnumber = int(input("Enter Account Number :"))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        accFound = False

        for acc in accounts:
            if acc.Account_Number == accnumber:
                if not acc.Active:
                    print("Account dormant/ closed. Cannot perform operation.")
                    return

                acc.Account_Balance.printDetails()
                accFound = True
                break

        if not accFound:
            print("Provided Account not found in database!")

    def accountholderlist(self, accounts):
        for acc in accounts:
            acc.printDetails()

    def closeaccount(self, accounts):
        accnumber = int(input("Enter Your Account Number :"))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        accFound = False
        for acc in accounts:
            if acc.Account_Number == accnumber:
                if not acc.Active:
                    print("Account dormant/ closed. Cannot perform operation.")
                    return

                accFound = True
                acc.closeAccount()

        if not accFound:
            print("Provided Account not found in database!")

    def modifyaccount(self, accounts):
        accnumber = int(input("Enter Your Account Number :"))
        if accnumber < 0 or accnumber > 1000:
            print("Invalid Account Number.")
            return

        age = int(input("Please enter Account Holder age :"))
        if age <= 0 and age > 100:
            print("Invalid value.")
            return

        status = input("Enter Account Status (A = Active, C = Closed):")
        if status.upper() != 'A' and status.upper() != 'C':
            print("Invalid Status.")
            return

        accFound = False
        for acc in accounts:
            if acc.Account_Number == accnumber:
                accFound = True
                acc.modifyAccount(age, status)

        if not accFound:
            print("Provided Account not found in database!")


    def printmenu(self):
        print("Main Menu")
        print("01. New Account")
        print("02. Deposit Amount")
        print("03. Withdraw Amount")
        print("04. Balance Enquiry")
        print("05. ALL Account Holder List")
        print("06. Close An Account")
        print("07. Modify An Account")
        print("08. Exit")


def main():
    opt = 0
    accounts = []
    bms = BMS()

    while opt < 8:
        bms.printmenu()
        opt = int(input("Select Your Option (1-8) "))
        if opt == 1:
            newaccount = bms.createaccount()
            if newaccount != None:
                accounts.append(newaccount)
        elif opt == 2:
            bms.depositamount(accounts)
        elif opt == 3:
            bms.withdrawamount(accounts)
        elif opt == 4:
            bms.balanceEnq(accounts)
        elif opt == 5:
            bms.accountholderlist(accounts)
        elif opt == 6:
            bms.closeaccount(accounts)
        elif opt == 7:
            bms.modifyaccount(accounts)


main()