#Create a contact book

contact_book = {
    "John": {
        "Full Name": "John Henry",
        "Phone": ["123", "456"],
        "Email": ["john@gmail.com", "john.work@live.com"],
        "Address": "Hanoi",
        "Note": "This is John",
        "Tag": ["friend", 'work']
    },
    "Rossa": {
        "Phone": ["321"],
        "Email": ["rosse@gmail.com", "rossa.work@live.com"],
        "Address": "HCM",
        "Note": "This is Rossa",
        "Tag": ['work']
    }
}
#Show menu
def show_menu():
    print('''Please select program mode:
        1) Show all contacts
        2) Add new contact
        3) Edit existing contact
        4) Delete existing contact
        5) Search contact by name
        6) Search contact by tag
        7) Thoat chuong trinh
          ''')
#Select program mode
def get_choice():
    return input("Please select mode: ")

#define function to show all contacts
def show_all_contact(contact):
    print(contact)
#define function to add new contact
def add_new_contact(contact):
    fields = [
        {
            "name": "Name",
            "loop": False,
            "display_text": "Please input contact name: "
        },
        {
            "name": "Phone",
            "loop": True,
            "display_text": "Please input phone number (multiple number allowed, stop if it's blank): "
        },
        {
            "name": "Email",
            "loop": True,
            "display_text": "Please input email (multiple email allowed, stop if it's blank): "
        },
        {
            "name": "Address",
            "loop": False,
            "display_text": "Please input address: "
        },
        {
            "name": "Note",
            "loop": False,
            "display_text": "Note: "
        },
        {
            "name": "Tag",
            "loop": True,
            "display_text": "Please input tag (multiple email allowed, stop if it's blank): "
        }
    ]
    new_contact = {}
    for field in fields:
        if field["loop"]:
            value_list = []
            print(field["display_text"])
            while True:
                value = input()
                if value == "":
                    break
                value_list.append(value)
            new_contact.update({field["name"]: value_list})
        else:
            value = input(field["display_text"])
            new_contact.update({field["name"]: value})
    name = new_contact["Name"]
    del new_contact["Name"]
    contact.update({name: new_contact})
    return contact

#Remove contact
def remove_contact(contact):
    contact_remove = input("Please input contact name that you want to delete:")
    if contact_remove in contact_book.keys():
        del contact_book[contact_remove]
    return contact

#Edit existing contact:
def edit_contact(contact):
    print("Current contacts in book:")
    print(contact.keys())
    while True:
        contact_edit = input("Please input contact name that you want to edit:")
        if contact_edit in contact.keys():
            print("Which parameter do you want to change?")
            print(contact[contact_edit].keys())
            edit_parameter = input("Please input information that you want to change:")
            if edit_parameter in contact[contact_edit].keys():
                value_change = input("Please input new value:")
                contact[contact_edit][edit_parameter] = value_change
                break
            else:
                continue
        else:
            continue
    return contact

#Search contact by contact name
def search_by_name(contact):
    while True:
        search_name = input("Please enter contact name:")
        if search_name in contact.keys():
            print(search_name, ":", contact.get(search_name))
            break
        else:
            print(search_name, " is not in contact book. Please enter name correctly!")
            continue
#Search contact by tag
def search_by_tag(contact):
    condition = False
    while (condition == False):
        search_tag = input("Please enter tag field:")
        for key in contact_book:
            for tag in contact_book[key]["Tag"]:
                if tag == search_tag:
                    print(key, ":", contact_book.get(key))
                    condition = True


#main
while True:
    show_menu()
    user_choice = get_choice()
    print("You select mode: " + user_choice)

    if user_choice == "7":
        break
    elif user_choice == "1":
        show_all_contact(contact_book)
    elif user_choice == "2":
        contact_book = add_new_contact(contact_book)
    elif user_choice == "3":
        contact_book = edit_contact(contact_book)
    elif user_choice == "4":
        contact_book = remove_contact(contact_book)
    elif user_choice == "5":
        search_by_name(contact_book)
    elif user_choice == "6":
        search_by_tag(contact_book)
