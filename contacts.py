"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""
class ContactBook:
    def __init__(self):
        
        self.contacts = {}

    def add_contact(self, name, phone_number):
        """Add a new contact to the book."""
        if name in self.contacts:
            print(f"Contact '{name}' already exists. Updating number...")
        self.contacts[name] = phone_number

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        """Search for a contact by name."""
        return self.contacts.get(name, f"Contact '{name}' not found.")

    def show_all_contacts(self):
        
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("---- All Contacts ----")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")



book = ContactBook()
book.add_contact("Amos", "08012345678")
book.add_contact("Bawa", "07098765432")

print(book.search_contact("Amos")) 

book.show_all_contacts()

book.delete_contact("Bawa")
book.show_all_contacts()
