def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No contact found."
        except IndexError:
            return "Enter username."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(username, contacts):
    if username in contacts:
        return f"Showing contact info for {username}: {contacts[username]}"
    else:
        return f"No contact found with username {username}"


@input_error
def phone_contact(args, contacts):
    username = args[0]
    if username in contacts:
        return f"Calling a phone number for {username}: {contacts[username]}"
    else:
        return f"No contact found with username {username}"


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(*args, contacts))
            
        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        
        elif command == "phone":
            print(phone_contact(args, contacts))


        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()