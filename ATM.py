print("Welcome to ATM")
print("Swipe your card")
language=input("select option for choose language \n a. Hindi \n b. English \n")
amt=7000
if language=="a":
    accttype=input("Apne account ka type chunein \n a. Savings account \n b. Salary account \n c. Fixed deposit account \n")
    if accttype=="a" or accttype=="b" or accttype=="c":
        print("Aapke account me maujuda rashi", amt,"rupay hai")
        pin=input("4 digit ka pin daalein \n")
        if len(pin)==4:
             amnt=int(input("Rashi darj karein \n"))
             if amnt<amt:
                 pass
                 opt=input("a. Widrawal \n b. Transfer \n c. Fixed diposit \n")
                 if opt=="a" or opt=="b" or opt=="c":
                     print(amt-amnt)
                 else:
                      print("Amaanya vikalp")
             else:
                  print("Aparyapt rashi")
        else:
             print("Galat pin")
    else:
          print("Kripya sahi vikalp chunein")
elif language=="b":
    accttype=input("Your account type \n a. Savings account \n b. Saraly account \n c. Fixed diposit account \n")
    if accttype=="a" or accttype=="b" or accttype=="c":
        print("Your current balance is",amt)
        pin=input("Enter your 4 digit pin\n")
        if len(pin)==4:
            amnt=int(input("Enter your amount\n"))
            if amnt<amt:
                pass
                opt=input("a. Widrawal \n b. Transfer \n c. Fixed diposit \n")
                if opt=="a" or opt=="b" or opt=="c":
                    print(amt-amnt)
                else:
                    print("Invalid option")
            else:
                print("Insufficient balance")
        else:
            print("Incorrect pin")
    else:
        print("Please choose right option")
else:
    print("Please select the right option.")