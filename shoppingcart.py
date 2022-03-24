from IPython.display import clear_output

def shop_cart():
    cart_dict = {}
    prompt = "What would you like to do? \n"
    prompt += "Add items to your cart(type 'add')? "
    prompt += "Delete items from your cart(type 'del')? "
    prompt += "Show your cart items(type 'show')? "
    prompt += "Checkout (type 'done')? "
    prompt += "Quit(type 'quit')? "
    
    
    name = input("What is your name: ")
    name = name.title()
    print(f"Hi {name}!")
    cart_dict[name] = []
    while True:
        
        cart_action = input(prompt)
        
        if cart_action.lower() == 'quit':
            for name, items in cart_dict.items():
                print(f"{name} you have {len(items)} item/s in your cart.")
            
            goodbye = input('Are you sure you want to quit (y/n)? ')
            clear_output()
            if goodbye.lower() == 'y':
                print(f"Goodbye {name}!")
                break 
            else:
                continue 
            
        if cart_action.lower() == 'add': 
            add = input('What items would you like to add to your cart? ')
            cart_dict[name].append(add)
            clear_output()
        
        if cart_action.lower() == 'del':
            delete = input("What items would you like to delete from your cart? ")
            cart_dict[name].remove(delete)
            clear_output()
        
        if cart_action.lower() == 'show':
            clear_output()
            for name, items in cart_dict.items():
                print(f"{name} your cart has the following items in it: ")
                for item in items:
                    print(item)

        if cart_action.lower() == 'done':
            clear_output()
            break
            
    for name, items in cart_dict.items():
        print(f"{name} your cart has {len(items)} items in it: ")
        for item in items:
            print(item)
            
        item_len = len(items)
        if item_len < 5:
            print(f"Your total is $10")

        elif item_len < 10:
            print(f"Your total is $15")
        else:
            print(f"Your total is $20")

                    



# shop_cart()
    

  
