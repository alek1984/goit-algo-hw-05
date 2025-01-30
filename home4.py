def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args[0]
    return contacts[name]

@input_error
def get_all_contacts():
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) if contacts else "No contacts found."

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command.startswith("add"):
            args = input("Enter the argument for the command: ").split()
            print(add_contact(args))
        elif command.startswith("phone"):
            args = input("Enter the argument for the command: ").split()
            print(get_phone(args))
        elif command == "all":
            print(get_all_contacts())
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()

 
 