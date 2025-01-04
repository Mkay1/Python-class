card_pin = "4991"
acct_bal = 5000

print("Welcome")
def trans(t):
    pin = input("Enter Your Pin: ")
    if pin == card_pin:
        def withD():
            amt = int(input("How much would you like to withdraw: "))
            if amt <= acct_bal:
                avil_bal = acct_bal - amt
                print("...please wait...")
                print("Here is your withdrawal\nAvailable balance is $%d" % (avil_bal))   
            else:
                print("Insufficent Balance\nAvailable balance is $%d" % (acct_bal))
                withD()
        withD()
    else:
        t += 1
        if t == 3:
            print("Bye")
        else:
            print("incorrect Pin")
            trans(t)       
trans(0)




