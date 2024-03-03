from utils import input_error, parse_input

contacts = {}


@input_error
def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args):
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args):
    name = args[0]
    phone = contacts.get(name)
    if not phone:
        raise KeyError
    return phone


def show_all():
    if not contacts:
        return "No contacts found."
    return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    print("Welcome to the assistant bot! Type 'exit' or 'close' to quit.")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
