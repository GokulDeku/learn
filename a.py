master_list = ['l1']
api_list = []

l1 = ['Home']
l2 = []
l3 = []
l4 = []

master_hash = {1: l1, 2: l2, 3: l3, 4: l4}

h = {
    'Home': 1,
    'Work': 0,
    'Others': 0
}

def show_list_items():
    print_all_list()
    list_index = int(input("Enter list number: "))
    lis = get_list(list_index)

    if lis == -1:
        return
    
    print(lis)

def add_item():
    print_all_list()
    list_index = int(input("Enter list number: "))
    lis = get_list(list_index)

    if lis == -1:
        return

    item = input("Enter item: ")
    if item not in h.keys():
        print("Invalid Item")
        return

    if item in lis:
        print(f"Item {item} already in l{list_index}")
        return
    
    
    lis.append(item)
    h[item] += 1

    print(f"Added {item} in l{list_index}")

def save():
    api_list = [
        ['Home', 1111111111],
        ['Work', 1212121212]
    ]

def populate(item_list):
    for k,v in item_list.items():
        if k != 'Others':
            if item_list[k] == 0:
                print(k)
        elif item_list[k] != 2:
            print(k)
    print("---------------------------")

def get_list(list_index):
    if list_index <= 0 and list_index >= 5:
        print("Invalid List index")

    return master_hash[list_index]

def remove_list():
    print_all_list()
    if(len(master_list) == 1):
        print("Cannot remove only one list available")
        return
    list_index = int(input("Enter List Number: "))
    master_list.remove('l' + str(list_index))
    l = get_list(list_index)
    l.clear()

def print_all_list():
    for lis in master_list:
        print(lis, end=" => ")
        lis = get_list(int(lis[-1]))
        for items in lis:
            print(items, end=", ")
        print()

def def_add_check():
    if h['Home'] <= 0:
        h['Home'] += 1
        return "Home"
    elif h['Work'] <= 0:
        h['Work'] += 1
        return "Work"
    elif h['Others'] <= 1:
        return "Others"

def add_list():
    index = len(master_list)
    if index >= 4:
        print("Can't add more than 4 list")
        return -1
    for i in range(1,5):
        t = 'l' + str(i)
        if t in master_list:
            continue
        master_list.append(t)
        lis = get_list(i)

        break
    print("List Added")

while True:
    user_choice = int(input("""Enter your choice:
        1. Add List
        2. Add Item in List
        3. Show all List and its items
        4. Modify item in List
        5. Remove List
        6. Save
    """))
    if user_choice == 1:
        add_list()
    elif user_choice == 2:
        add_item()
    elif user_choice == 3:
        print_all_list()
    elif user_choice == 4:
        print("")
    elif user_choice == 5:
        remove_list()
    elif user_choice == 6:
        save()
    else:
        print("Enter valid choice")
