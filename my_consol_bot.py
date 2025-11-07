# функція-декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError as err:
            return f"Error: {err}" if str(err) else "Error: Invalid value format."
        except IndexError:
            return "Error: Please enter all required arguments."
        except Exception as err:
            return f"Unexpected error: {err}"
    return inner

def parse_input(user_input):
    """Розбиває введений рядок на команду та аргументи"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """Додає новий контакт"""
    if len(args) != 2:
        raise IndexError()
    
    name, phone = args
    
    # Перевірка на коректність імені
    if not name:
        raise ValueError("Name cannot be empty")
    
    # Правильна перевірка: ім'я має містити принаймні одну літеру
    if not any(char.isalpha() for char in name):
        raise ValueError("Name should contain at least one letter")
    
    # Перевірка на коректність телефону
    if not phone.isdigit():
        raise ValueError("Phone number should contain only digits")
    if len(phone) < 5:
        raise ValueError("Phone number is too short")
    
    # Перевірка чи контакт вже існує
    if name in contacts:
        raise ValueError(f"Contact '{name}' already exists. Use 'change' command to update.")
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту"""
    if len(args) != 2:
        raise IndexError()
    
    name, new_phone = args
    
    # Перевірка на коректність телефону
    if not new_phone.isdigit():
        raise ValueError("Phone number should contain only digits")
    if len(new_phone) < 5:
        raise ValueError("Phone number is too short")
    
    if name not in contacts:
        raise KeyError()
    
    contacts[name] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """Показує номер телефону за ім'ям"""
    if len(args) != 1:
        raise IndexError()
    
    name = args[0]
    if name not in contacts:
        raise KeyError()
    
    return contacts[name]

@input_error
def show_all(contacts):
    """Показує всі контакти"""
    if not contacts:
        return "No contacts saved."
    
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

@input_error
def delete_contact(args, contacts):
    """Видаляє контакт"""
    if len(args) != 1:
        raise IndexError()
    
    name = args[0]
    if name not in contacts:
        raise KeyError()
    
    del contacts[name]
    return "Contact deleted."

def main():
    """Основна функція для управління ботом"""
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        
        # Обробка порожнього вводу
        if not user_input:
            print("Please enter a command.")
            continue
            
        try:
            command, args = parse_input(user_input)
        except ValueError as e:
            print("Error: Please enter a valid command.")
            continue
        except Exception as e:
            print(f"Unexpected error during parsing: {e}")
            continue
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command in ["hello", "hi"]:
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        elif command == "delete":
            print(delete_contact(args, contacts))
            
        else:
            print("Invalid command: Available commands: hello, add, change, phone, all, delete, close/exit")

if __name__ == "__main__":
    main()