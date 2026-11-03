import sys
from accCreation import userExist, createUser
from login import verifyUser
from addContact import addContact

def main():
    if not userExist():
        print("No users are registered with this client.")
        choice = input("Do you want to register a new user (y/n)? ").strip().lower()

        if (choice == "y"):
            if not createUser():
                sys.exit(1)
        else:
            print("Exiting SecureDrop.")
        sys.exit(0)

    aesKey = verifyUser()
    if not aesKey:
        print("Email and Password Combination Invalid.")
        sys.exit(1)

    print("Welcome to SecureDrop.")
    print('Type "help" For Commands.')

    while (True):
        command = input("secure_drop> ").strip().lower()

        if (command == "help"):
            print('"add"  -> Add a new contact')
            print('"list" -> List all online contacts')
            print('"send" -> Transfer file to contact')
            print('"exit" -> Exit SecureDrop')

        if (command == "exit"):
            sys.exit(0)

        if (command == "add"):
            addContact(aesKey)



if __name__ == "__main__":
    main()