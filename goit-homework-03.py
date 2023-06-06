di = {'3': 45, 'didi': 123}


def input_error(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except:
            print("Try again")
        finally:
            return main()


def hello(x):
    print("How can I help you?")
    return main()

@input_error(func)
def add(x):
    add = x
    add = add.split()
    di.update({add[0]: add[1]})
    return main()

@input_error(func)
def change(x):
    key = x
    key = key.split()
    di[key[0]] = key[1]
    return main()

@input_error(func)
def phone(x):
    print(di[x])
    return main()

def show_all():
    for k,v in di.items():
        print(k, v)

def main():
    while True:
        x = input()
        x = x.lower()
        if x == 'hello':
            print(hello(x))        
        if 'add ...' in x:
            x = input()
            add(x)    
        if "change ..." in x:
            x = input()
            change(x)
        if "phone ..." in x:
            phone(x)    
        if "show all" in x:
            show_all()    
        if x == 'close' or x == 'goode bye' or x == 'exit':
            return "Good bye!"
            

print(main())