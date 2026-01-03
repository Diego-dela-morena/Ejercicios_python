def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
def add_contact(contact_book):
    name = input("Add the contact name: ")
    phone = input("Add the contact phone: ")
    email = input("Add the contact email: ")
    address = input("Add the contact address: ")
    if name in contact_book.keys():
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
def view_contact(contact_book):
    name = input("Write the contact name you want to view: ")
    if name in contact_book.keys():
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
    else:
        print("Contact not found!")
def edit_contact(contact_book):
    name = input("Write the contact name you want to edit: ")
    if name not in contact_book:
        print("Contact not found!")
    else:
        phone = input("Write the new contact phone: ")
        email = input("Write the new contact email: ")
        address = input("Write the new contact address: ")
        if phone != "":
            contact_book[name]["phone"] = phone
        if email != "":
            contact_book[name]["email"] = email
        if address != "":
             contact_book[name]["address"] = address
        print("Contact updated successfully!")
def delete_contact(contact_book):
    name = input("Write the contact you want to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for name in contact_book:
            phone = contact_book[name]["phone"]
            email = contact_book[name]["email"]
            address = contact_book[name]["address"]
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print(f"Address: {address}")
            print("")
contact_book = {}
while 1 == True:
    display_menu()
    choice = int(input("Choose an option from the menu: "))
    if choice == 1:
        add_contact(contact_book)
    elif choice == 2:
        view_contact(contact_book)
    elif choice == 3:
        edit_contact(contact_book)
    elif choice == 4:
        delete_contact(contact_book)
    elif choice == 5:
        list_all_contacts(contact_book)
    elif choice == 6:
        break
    else:
        print(f"{choice} is not in the menu")