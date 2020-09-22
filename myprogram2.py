

def items_buying(order):
    global items
    items_copy={}
    items_copy.update(items)
    if order == 'y':
        n=0
        list_buying = {}
        while True:
            n += 1
            name = input(f'Enter the item {n} \"or\" enter \'n\' to finish :')
            if (name == 'n'):
                break
            elif (name not in items_copy):
                print('Enter a valid item name')
                n -= 1
                continue
            else:
                item_count = input(f'Enter the item count for item {n} :')
                if item_count.isnumeric():
                    list_buying[name] = int(item_count)
                    print('The items bought are :',*list_buying)
                    continue
                else:
                    print('Invalid Count')
                    n -= 1
        calculate_items(list_buying,items_copy)

def calculate_items(things,items_copy):
    total =0
    grand_total =0
    for keys,values in things.items():
        for original_key,original_value in items_copy.items():
            if keys == original_key:
                total += values*original_value
                grand_total += total
                print(f'item {keys} = ',total)
                total =0
    print('Total cost = ',grand_total)
    balance_amount(grand_total)

def balance_amount(final_amount):
    customer_amount = int(input('enter customer amount'))
    balance = customer_amount - final_amount
    print('Return Balance =',balance)

def add_items(adding):
    new_items = {}
    global items
    print(items)
    if adding == 'a':
        while True:
            print('Adding Items')
            key = input('Enter the item name \'or\' enter \'e\' to end :')
            if key == 'e':
                break
            else:
                value = int(input('Enter it\'s price :'))
                new_items[key]=value
                items.update(new_items)
                continue
        home()
def home():
    global items
    print('!!!!!!!!!!!!Welcome!!!!!!!!!!!!')

    enter = input('Enter \'y\' to start or \'a\' to add items to the shop :')
    if enter == 'y':
        items_buying(enter)
    elif enter == 'a':
        add_items(enter)
    else:
        home()
items = {'bread':30,'coconut':10,'flour':50,'biscuits' : 25}
home()

