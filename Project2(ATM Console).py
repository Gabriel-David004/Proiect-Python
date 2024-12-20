from cardHolder import cardHolder

def printMenu():
    #printare optiuni
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much money would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your money. Your balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much money would you like to withdraw: "))
        #verifica daca user-ul are bani
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance!")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go!Thank you!")
    except:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    #creare lista de pin-uri
    list_of_cardHolder = []
    list_of_cardHolder.append(cardHolder("123456789101112", 1234, "Gabriel", "John", 150.31))
    list_of_cardHolder.append(cardHolder("121110987654321", 4321, "Isac", "Maria", 500.89))
    list_of_cardHolder.append(cardHolder("729939771223244", 8819, "Lutcan", "Mihai", 67.23))
    list_of_cardHolder.append(cardHolder("928335446477122", 9184, "Cazacu", "Daniel", 899.16))
    list_of_cardHolder.append(cardHolder("991823638911029", 9119, "Popescu", "Lucian", 13.89))

    #solicitare utilizator numar debit
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            #verificare against repo
            debitMatch = [holder for holder in list_of_cardHolder if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again!")
        except:
            print("Card number not recognized. Please try again!")

    #solicitare pin
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN, try again!")
        except:
            print("Invalid PIN, try again!")

    #printare optiuni
    print("Welcome ", current_user.get_firstName())
    option = 0
    while(True): #am inlocuit cu True sau ***true
        printMenu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again!")

        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0

    print("Thank you! Have a nice day!")