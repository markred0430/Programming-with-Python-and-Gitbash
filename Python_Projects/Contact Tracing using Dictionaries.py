# Display a menu
Contact_Tracing = {}
while True:
    print("                             This is Basic Contact Tracing Form ")
    print("=====================================================")
    print("                                        Options: ")
    print("=====================================================")
    print("     1 -> Add an item.")
    print("=====================================================")
    print("     2 -> Search.")
    print("=====================================================")
    print("     3 -> Exit (y/n)")
    print("=====================================================")
    print()
    # Allow the user to select item in the menu.
    selection = int(input("Select what you want to do: \n"))
    print()
    # Perform the selected option
    # Option1
    if selection == 1:
        Full_Name = str(input("Full Name: "))
        Age = str(input("Age: "))
        Address = str(input("Address: "))
        Phone_num = str(input("Phone Number: "))
        print("Saved!")
        print()
        inputs = {
            "Name": Full_Name,
            "Age": Age,
            "Address": Address,
            "Phone": Phone_num
            }
        Contact_Tracing[Full_Name] = inputs
    # Option2
    if selection == 2:
        Search = str(input("Do you want to search informations? \n Just type full name. \n"))
        if Search in Contact_Tracing:
            for key in Contact_Tracing[Search]:
                print(key, ":", Contact_Tracing[Search][key])
                print("=====================================================")
            print()
        else:
            print("No Record.")
        print()
    # Option3
    if selection == 3:
        Exit = input("Do you want to fill out another?(Y/N)")
        if Exit == 'N':
            break

