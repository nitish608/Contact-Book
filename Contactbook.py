import pickle
import os
filename='CB.pkl'

if os.path.exists(filename):
    with open(filename,'rb') as f:
        contact=pickle.load(f)
else:
    contact={}
    
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
while True:
    
    print("----------------------------------")
    print("\t\tMenu")
    print("----------------------------------\n")
    
    choice=int(input("1.Add New Contact\n2.Search Contact\n3.Display all Contacts\n4.Edit Contact\n5.Delete Contact\n6.Exit\n\nEnter your Choice:"))
    
    if choice == 1:
        name=input("Enter the Contact Name:")
        number=input("Enter the Mobile Number:")
        contact[name]=number
        print("\n-----Contact Created Successfully-------")
        
    elif choice == 2:
        search_name=input("Enter the Contact Name:")
        
        if search_name in contact:
            print("-----Contact is Found-----")
            print("\n")
            print(search_name,"contact number is",contact[search_name])
                    
        else:
            print(search_name,"\nIs not Found")
            
    elif choice == 3:
        
        if not contact:
            print("\n-----Contact Book is Empty------")
            
        else:
            display_contact()
                        
    elif choice == 4:
        edit_contact=input("Enter the Contact Name to be Edited:")
        
        if edit_contact in contact:
            number=input("Enter the New Mobile Number:")
            contact[edit_contact]=number
            print("------Contact Updated------\n")
            display_contact()

        else:
            print(edit_contact,"-----Is not Found-----\n")
            
    elif choice == 5:
        delete_contact=input("Enter the Contact Name to be Delete:")
        
        if delete_contact in contact:
            option=input("Do you want to Delete this Contact y/n?:")
            
            if option=='y' or option=='Y':
                contact.pop(delete_contact)
                print("-----Deleted Successfully-----\n")
            display_contact()
                        
        else:
            print(delete_contact,"Is Not Found")
            
    else:
        print("THANK YOU\n")
        break
    
