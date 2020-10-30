import cgitb cgitb.enable()
print("Welcome to Mazebank")
print("Please select the number corresponding to your name below")
name = float(input("1. Josh, 2. Reich, 3. Natalie, 4. Jugoon:"))

josh_balance = 1242000
reich_balance = 3200000
natalie_balance = 500000
jugoon_balance = 12000000

if name == 1:
    print("Welcome back Dr. Josh!")

    pin = float(input("Please enter your 4 digit pin here:"))

    if pin == 4123:
        print("Pin Correct!")
        print("Please select what function you would like to pick")
        action = float(input("1. Transaction      2. Deposit          3. Check balance           5. Cancel:"))
        
        if action == 1:

            secondpin=float(input("For security Purposes, please enter your 4 digit pin again:"))

            if secondpin == 4123:
                print("Pin Correct")
                
                transactionamount = float(input("Please enter the amount you would like to transact:"))

                if transactionamount >= josh_balance:
                    print("The amount you entered is larger than your current balance")
                    print("Executing close program protocol")
                else:
                    josh_balance=josh_balance - transactionamount
                    print("You sucessfully transacted $" + str(transactionamount) + " and your new balance is $" + str(josh_balance - transactionamount))
        if action == 2:
            depositpin = float(input("For security purposes, please enter your 4 digit pin again:"))
            if depositpin == 4123:
                print("Pin Correct")
                josh_deposit = float(input("Please enter the amount you would like to deposit:"))
                josh_balance= josh_balance + josh_deposit
                print("You sucessfully deposited $" + str(josh_deposit) + " and your new balance is $" + str(josh_balance + josh_deposit))
        if action == 3:
            print("Your balance is $", str(josh_balance))
        if action == 5:
            print("Initiating close program protocol")

if name == 2:
    print("Welcome back Mr. Reich!")

    reich_pin = float(input("Please enter your 4 digit pin here:"))

    if reich_pin == 2254:
        print("Pin Correct!")
        print("Please select what function you would like to pick")
        reich_action = float(input("1. Transaction      2. Deposit          3. Check balance           5. Cancel:"))
        
        if reich_action == 1:

            reich_secondpin=float(input("For security Purposes, please enter your 4 digit pin again:"))

            if reich_secondpin == 2254:
                print("Pin Correct")
                
                reich_transactionamount = float(input("Please enter the amount you would like to transact:"))

                if reich_transactionamount >= reich_balance:
                    print("The amount you entered is larger than your current balance")
                    print("Executing close program protocol")
                else:
                    reich_balance=reich_balance - reich_transactionamount
                    print("You sucessfully transacted $" + str(reich_transactionamount) + " and your new balance is $" + str(reich_balance - reich_transactionamount))
        if reich_action == 2:
            reich_depositpin = float(input("For security purposes, please enter your 4 digit pin again:"))
            if reich_depositpin == 4123:
                print("Pin Correct")
                reich_deposit = float(input("Please enter the amount you would like to deposit:"))
                reich_balance= reich_balance + reich_deposit
                print("You sucessfully deposited $" + str(reich_deposit) + " and your new balance is $" + str(reich_balance + reich_deposit))
            if reich_depositpin >= 4123:
                print("Pin is incorrect, initiating close program protocol")
        if reich_action == 3:
            print("Your balance is $", str(reich_balance))
        if reich_action == 5:
            print("Initiating close program protocol")
if name == 3:
    print("Welcome back Mrs. Natalie!")

    natalie_pin = float(input("Please enter your 4 digit pin here:"))

    if natalie_pin == 4123:
        print("Pin Correct!")
        print("Please select what function you would like to pick")
        natalie_action = float(input("1. Transaction      2. Deposit          3. Check balance           5. Cancel:"))
        
        if natalie_action == 1:

            natalie_secondpin=float(input("For security Purposes, please enter your 4 digit pin again:"))

            if natalie_secondpin == 4123:
                print("Pin Correct")
                
                natalie_transactionamount = float(input("Please enter the amount you would like to transact:"))

                if natalie_transactionamount >= natalie_balance:
                    print("The amount you entered is larger than your current balance")
                    print("Executing close program protocol")
                else:
                    natalie_balance=natalie_balance - natalie_transactionamount
                    print("You sucessfully transacted $" + str(natalie_transactionamount) + " and your new balance is $" + str(natalie_balance - natalie_transactionamount))
        if natalie_action == 2:
            natalie_depositpin = float(input("For security purposes, please enter your 4 digit pin again:"))

            if natalie_depositpin == 4123:
                print("Pin Correct")
                natalie_deposit = float(input("Please enter the amount you would like to deposit:"))
                natalie_balance= natalie_balance + natalie_deposit
                print("You sucessfully deposited $" + str(natalie_deposit) + " and your new balance is $" + str(natalie_balance + natalie_deposit))
        if natalie_action == 3:
            print("Your balance is $", str(natalie_balance))
        if natalie_action ==5:
            print("Initiating close program protocol")
if name == 4:
    print("Welcome back Dr. Jugoon!")

    jugoon_pin = float(input("Please enter your 4 digit pin here:"))

    if jugoon_pin == 4123:
        print("Pin Correct!")
        print("Please select what function you would like to pick")
        jugoon_action = float(input("1. Transaction      2. Deposit          3. Check balance           5. Cancel:"))
        
        if jugoon_action == 1:

            jugoon_secondpin=float(input("For security Purposes, please enter your 4 digit pin again:"))

            if jugoon_secondpin == 4123:
                print("Pin Correct")
                
                jugoon_transactionamount = float(input("Please enter the amount you would like to transact:"))

                if jugoon_transactionamount >= jugoon_balance:
                    print("The amount you entered is larger than your current balance")
                    print("Executing close program protocol")
                else:
                    jugoon_balance=jugoon_balance - jugoon_transactionamount
                    print(jugoon_balance)
                    print("You sucessfully transacted $" + str(jugoon_transactionamount) + " and your new josh_balance is $" + str(jugoon_balance - jugoon_transactionamount))
        if jugoon_action == 2:
            jugoon_depositpin = float(input("For security purposes, please enter your 4 digit pin again:"))

            if jugoon_depositpin == 4123:
                print("Pin Correct")
                jugoon_deposit = float(input("Please enter the amount you would like to deposit:"))
                jugoon_balance= jugoon_balance + jugoon_deposit
                print("You sucessfully deposited $" + str(jugoon_deposit) + " and your new balance is $" + str(jugoon_balance + jugoon_deposit))
        if jugoon_action == 3:
            print("Your balance is $", str(josh_balance))
        if jugoon_action == 5:
            print("Initiating close program protocol")