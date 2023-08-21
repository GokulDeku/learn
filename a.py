master_list = []
api_list = []

l1 = []
l2 = []
l3 = []
l4 = []

master_hash = {1: l1, 2: l2, 3: l3, 4: l4}

h = {
    'Home': 0,
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

def show_item_dropdown(lis_item):
    print("Dropdown List:")
    for k,v in h.items():
        if k == lis_item:
            print(k)
            continue
        elif k == 'Home' and v == 0:
            print("Home")
        elif k == 'Work' and v == 0:
            print("Work")
        elif k == 'Others' and v <= 1:
            print("Others")

def modify_item():
    print_all_list()
    list_index = int(input("Enter list number: "))
    lis = get_list(list_index)

    if lis == -1:
        return
    
    lis_item = lis[0]

    h[lis_item] -= 1

    show_item_dropdown(lis_item)

    item = input("Enter item: ")
    if item not in h.keys():
        print("Invalid Item")
        return
    
    num = int(input("Enter number: "))

    lis[0] = item

    if len(lis) == 1:
        lis.append(num)
    else:
        lis[1] = num
    
    h[item] += 1

    print(f"Added {item} in l{list_index}")

def get_api_data():
    api_list = [
        ['Home', 1111111111],
        ['Work', 1212121212]
    ]

    n = len(api_list)

    for i in range(n):
        item = api_list[i][0]
        num = api_list[i][1]
        h[item] += 1
        master_list.append('l' + str(i+1))
        lis = get_list(i+1)
        lis.extend([item, num])

def get_list(list_index):
    if list_index <= 0 and list_index >= 5:
        print("Invalid List index")

    return master_hash[list_index]

def remove_list():
    print_all_list()
    if(len(master_list) <= 1):
        print("Cannot remove only one list available")
        return
    list_index = int(input("Enter List Number: "))
    master_list.remove('l' + str(list_index))
    l = get_list(list_index)
    print(h)
    h[l[0]] -= 1
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
        h['Others'] += 1
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
        item = def_add_check()
        lis.append(item)
        break
    print("List Added")

while True:
    user_choice = int(input("""Enter your choice:
        1. Add List
        2. Modify item in List
        3. Show all List and its items
        4. Remove List
        5. Get api Data
    """))
    if user_choice == 1:
        add_list()
    elif user_choice == 2:
        modify_item()
    elif user_choice == 3:
        print_all_list()
    elif user_choice == 4:
        remove_list()
    elif user_choice == 5:
        get_api_data()
    else:
        print("Enter valid choice")