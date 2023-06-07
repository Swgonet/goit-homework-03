contacts = {}

def input_error(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except IndexError:
            print("Please enter norm number")
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
    return inner

@input_error
def add_contact(press_str):
    press_str = press_str.split()
    contacts.update({press_str[1]: press_str[2]})

@input_error
def change_contact(press_str):
    press_str = press_str.split()
    contacts[press_str[1]] = press_str[2]

@input_error
def phone_contact(press_str):
    press_str = press_str.split()
    print(contacts[press_str[1]])

def show_all_contacts():
    for k,v in contacts.items():
        print(k, v)

def main():
    while True:
        press_str = input()
        press_str = press_str.lower()
        if press_str == 'hello':
            print("How can I help you?")        
        if 'add' in press_str:
            add_contact(press_str)    
        if "change" in press_str:
            change_contact(press_str)
        if "phone" in press_str:
            phone_contact(press_str)    
        if "show all" in press_str:
            show_all_contacts()    
        if press_str == 'close' or press_str == 'goode bye' or press_str == 'exit':
            return "Good bye!"
      
print(main())
