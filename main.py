from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""
    
    filename = input("Enter the CSV file name:/n").strip()

    encrypt_passwords_in_file(filename)

    while True:
        option = input("options: (1) Change Password, (2) Add Password, (3) Quit:/n").strip()

        if option == "1":
            entry = input("Enter the website and the new password:\n").strip().split()
            if len(entry) < 2:
                print("Input is in the wrong format!")
                continue

            website, new_password = entry[0], entry[1]
            if len(new_password) < 12:
                print("Password is too short!")
                continue

            success = change_password(filename, website, new_password)
            if success:
                print("Password changed.")
            else:
                print("Website not found! Operation failed.")

        elif option == "2":

            entry = input("Enter the website, username, and password:\n").strip().split()
            if len(entry) < 3:
                print("Input is in the wrong format!")
                continue
            
            website, username, password = entry[0], entry[1], entry[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, password)
        
        elif option == "3":
            break
        else:
            print("Invalid option! selected!")


if __name__ == "__main__":
    main()1
