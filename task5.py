def add_contact(phone_book, name, contact):
    phone_book[name] = contact
    print(f"Contact '{name}' with number '{contact}' added successfully.")

def remove_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' removed successfully.")
    else:
        print(f"Contact '{name}' not found in the phone book.")
        
def search_contact(phone_book, name):
    if name in phone_book:
        print(f"Contact '{name}': {phone_book[name]}")
    else:
        print(f"Contact '{name}' not found in the phone book.")
        
def display_contacts(phone_book):
    if phone_book:
        for name, number in phone_book.items():
            print(f'{name}: {number}')
    else:
        print("The phone book is empty")
    
def main():
    phone_book = {}
    while True:
        try:
            print("1. Add a contact")
            print("2. Remove a contact")
            print("3. Search a contact")
            print("4. List all contacts")
            print("5. Exit the phone book")
        
            option = int(input("Please select an option: "))
        
            if option == 1:
                name = input("Please enter a name: ")
                contact = input("Please enter a phone number: ")
                add_contact(phone_book, name, contact)
            
            elif option == 2:
                name = input("Please enter a name: ")
                remove_contact(phone_book, name)
            
            elif option == 3:
                name = input("Please enter a name: ")
                search_contact(phone_book, name)
            
            elif option == 4:
                display_contacts(phone_book)
            
            elif option == 5:
                print("Exiting the phone book")
                break
            else:
                print("Incorrect option selected")
        
        except ValueError:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
