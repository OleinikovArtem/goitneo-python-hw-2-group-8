contacts = {}


def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args


def add_contact(args):
    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args):
    if len(args) < 2:
        return "Please provide both name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args):
    if not args:
        return "Please provide a name."
    name = args[0]
    phone = contacts.get(name)
    return phone if phone else "Contact not found."


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
