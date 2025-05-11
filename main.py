def atm_menu():
    print("\nWelcome to the ATM!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

def main():
    pin = "1234"
    balance = 1000

    user_pin = input("Enter your PIN: ")

    if user_pin != pin:
        print("Incorrect PIN. Access Denied.")
        return

    while True:
        atm_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your current balance is ₹{balance}")
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"₹{amount} deposited successfully.")
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")

        elif choice == "4":
            current = input("Enter current PIN: ")
            if current == pin:
                new_pin = input("Enter new PIN: ")
                pin = new_pin
                print("PIN changed successfully.")
            else:
                print("Incorrect current PIN.")
        
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
