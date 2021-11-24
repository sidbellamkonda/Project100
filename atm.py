class Atm:
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        #self.atm_amount = 300
    def checkBalance(self):
        print("Your balance is: 300")
    def withdrawl(self, amount):
        new_amount = 300-amount
        print("You have withdrawn amount" + str(amount) + ". Your remaining balance is:" + str(new_amount))
def main():
    card_number = input("Insert your card number")
    pin = input("Insert your pin")
    new_user = Atm(card_number, pin)
    print("Choose your activity: ")
    print("1. Balance Inquiry")
    print("2. Withdrawl")
    activity = int(input("Enter activity number: "))
    if(activity == 1):
        new_user.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter the amount: "))
        if amount <= 300:
            new_user.withdrawl(amount)
        else:
            print("Enter a valid amount")
    else:
        print("Enter a valid number")
main()