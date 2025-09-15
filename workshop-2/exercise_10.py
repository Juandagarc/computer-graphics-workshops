# Exercise 10: Phone Book Management
# Objective: Develop a program that allows managing a phone book

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None):
        """Adds a new contact to the phone book"""
        if name in self.contacts:
            return False, f"Contact '{name}' already exists"

        self.contacts[name] = {
            'phone': phone,
            'email': email
        }
        return True, f"Contact '{name}' added successfully"

    def search_contact(self, name):
        """Searches for a contact by name"""
        if name in self.contacts:
            return True, self.contacts[name]
        return False, f"Contact '{name}' not found"

    def delete_contact(self, name):
        """Deletes a contact from the phone book"""
        if name in self.contacts:
            del self.contacts[name]
            return True, f"Contact '{name}' deleted successfully"
        return False, f"Contact '{name}' not found"

    def update_contact(self, name, phone=None, email=None):
        """Updates information of an existing contact"""
        if name not in self.contacts:
            return False, f"Contact '{name}' not found"

        if phone:
            self.contacts[name]['phone'] = phone
        if email is not None:
            self.contacts[name]['email'] = email

        return True, f"Contact '{name}' updated successfully"

    def show_all_contacts(self):
        """Shows all contacts in the phone book"""
        if not self.contacts:
            return "Phone book is empty"

        result = "=== PHONE BOOK ===\n"
        for name, info in sorted(self.contacts.items()):
            result += f"\nName: {name}\n"
            result += f"Phone: {info['phone']}\n"
            if info['email']:
                result += f"Email: {info['email']}\n"
            result += "-" * 30 + "\n"

        return result

    def search_by_phone(self, phone):
        """Searches for a contact by phone number"""
        for name, info in self.contacts.items():
            if info['phone'] == phone:
                return True, (name, info)
        return False, f"No contact found with phone '{phone}'"

    def count_contacts(self):
        """Returns the total number of contacts"""
        return len(self.contacts)

    def export_contacts(self):
        """Exports all contacts as a list of dictionaries"""
        contacts_list = []
        for name, info in self.contacts.items():
            contact = {
                'name': name,
                'phone': info['phone'],
                'email': info['email']
            }
            contacts_list.append(contact)
        return contacts_list

def phone_book_exercise():
    """Phone book management demonstration exercise"""
    print("=== PHONE BOOK MANAGEMENT ===\n")

    phone_book = PhoneBook()

    print("1. Adding contacts:")
    sample_contacts = [
        ("John Doe", "555-1234", "john@email.com"),
        ("Mary Smith", "555-5678", "mary@email.com"),
        ("Carlos Lopez", "555-9012", None),
        ("Anna Martinez", "555-3456", "anna@email.com"),
        ("Peter Rodriguez", "555-7890", "peter@email.com")
    ]

    for name, phone, email in sample_contacts:
        success, message = phone_book.add_contact(name, phone, email)
        print(f"   {message}")

    print(f"\nTotal contacts: {phone_book.count_contacts()}")

    print("\n2. Showing all contacts:")
    print(phone_book.show_all_contacts())

    print("3. Searching for specific contact:")
    success, result = phone_book.search_contact("Mary Smith")
    if success:
        print(f"   Found - Phone: {result['phone']}, Email: {result['email']}")
    else:
        print(f"   {result}")

    print("\n4. Searching by phone number:")
    success, result = phone_book.search_by_phone("555-9012")
    if success:
        name, info = result
        print(f"   Found - Name: {name}, Email: {info['email'] or 'Not available'}")
    else:
        print(f"   {result}")

    print("\n5. Updating contact:")
    success, message = phone_book.update_contact("Carlos Lopez", email="carlos@email.com")
    print(f"   {message}")

    success, result = phone_book.search_contact("Carlos Lopez")
    if success:
        print(f"   Verification - Email updated: {result['email']}")

    print("\n6. Trying to add duplicate contact:")
    success, message = phone_book.add_contact("John Doe", "555-0000", "new@email.com")
    print(f"   {message}")

    print("\n7. Deleting contact:")
    success, message = phone_book.delete_contact("Peter Rodriguez")
    print(f"   {message}")
    print(f"   Remaining contacts: {phone_book.count_contacts()}")

    print("\n8. Exporting contacts:")
    exported_contacts = phone_book.export_contacts()
    print("   Exported contacts:")
    for contact in exported_contacts:
        print(f"   - {contact['name']}: {contact['phone']}")

def interactive_phone_book_menu():
    """Interactive menu for managing the phone book"""
    phone_book = PhoneBook()

    while True:
        print("\n=== PHONE BOOK MENU ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Show all contacts")
        print("6. Export contacts")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email (optional): ").strip() or None
            success, message = phone_book.add_contact(name, phone, email)
            print(message)

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            success, result = phone_book.search_contact(name)
            if success:
                print(f"Phone: {result['phone']}")
                if result['email']:
                    print(f"Email: {result['email']}")
            else:
                print(result)

        elif choice == "3":
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone (leave empty to keep current): ").strip() or None
            email = input("Enter new email (leave empty to keep current): ").strip()
            if email == "":
                email = None
            success, message = phone_book.update_contact(name, phone, email)
            print(message)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            success, message = phone_book.delete_contact(name)
            print(message)

        elif choice == "5":
            print(phone_book.show_all_contacts())

        elif choice == "6":
            contacts = phone_book.export_contacts()
            for contact in contacts:
                print(f"{contact['name']}: {contact['phone']}")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
