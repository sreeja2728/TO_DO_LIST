contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n📘 Contact List:")
        for name, details in contacts.items():
            print(f"{name} - {details['Phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() == name.lower() or search == details["Phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave field empty to keep existing value.")
        phone = input("Enter new phone number: ") or contacts[name]["Phone"]
        email = input("Enter new email: ") or contacts[name]["Email"]
        address = input("Enter new address: ") or contacts[name]["Address"]
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Thank you for using Contact Manager!")
            break
        else:
            print("Invalid choice! Please enter 1-6.")

main()
