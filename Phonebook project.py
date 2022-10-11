 # Registration step

confirm=input("Do you have an account in phonebook y/n?")
if confirm=='y':
    step1=input(print("please enter username"))
    step2=input(print("enter password"))
else:
    registration=input("Please complete your registration and tap enter")
    level1=input("Enter email")
    level2=input("Enter password")

# Next step:

contact={}
def display_contact():
    print("Name\t\tContact name")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1.Add new contact \n 2. search contact \n 3.read contact \n 4.update contact\n 5.delete contact \n 6.Exit\n Enter your choice"))
    if choice==1:
        name = input("enter the contact name")
        phone = input("Enter the mobile number")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter the contact name")
        if search_name in contact:
           print(search_name,"'s contact name is ",contact[search_name])
        else:
            print("name is not found in the coontact book")
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact() 
    elif choice==4:
        update_contact = input("Enter the contact to be edited")
        if update_contact in contact:
            phone=input("Enter mobile number")
            contact[update_contact]=phone
            print("Contact updated")
            display_contact() 
        else:
            print("Name is not found in the contact book")
    elif choice==5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
            dislpay_contact() 
        else:
            print("Name is not found in the contact book")
    else:
        break               




