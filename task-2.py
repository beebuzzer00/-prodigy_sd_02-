contacts = {}

def add_contact():
  name = input("Enter contact name: ")
  email = input("Enter contact email: ")
  phone = input("Enter contact phone number (optional): ")
  # Add more details if needed...

  contacts[email] = {"name": name, "email": email, "phone": phone}
  # Add more details to the inner dictionary...

def display_contacts():
  for email, contact in contacts.items():
    print(f"Name: {contact['name']}, Email: {email}, Phone: {contact['phone']}")

def search_contact():
  search_term = input("Enter search term: ")
  found_contacts = []
  for email, contact in contacts.items():
    if search_term in contact["name"] or search_term in email:
      found_contacts.append(contact)

  if len(found_contacts) > 0:
    print(f"Found contacts:")
    for contact in found_contacts:
      print(f"Name: {contact['name']}, Email: {email}")
  else:
    print("No contacts found matching your search.")

# Other functions for edit and delete operations...

while True:
  choice = input(
      """
      What do you want to do?
      1. Add Contact
      2. Display Contacts
      3. Search Contact
      4. Edit Contact
      5. Delete Contact
      6. Exit

      Enter your choice: """)

  if choice == "1":
    add_contact()
  elif choice == "2":
    display_contacts()
  elif choice == "3":
    search_contact()
  # Implement functionality for other choices...
  elif choice == "6":
    break
  else:
    print("Invalid choice. Please try again.")

print("Exiting...")