# Display a menu
Contact_Tracing = {}
while True:
    print("Menu: ")
    print("1 -> Add an item.")
    print("2 -> Search.")
    print("3 -> Exit (y/n)")
    # Allow the user to select item in the menu.
    selection = int(input("Select what you want to do: \n"))
    # Perform the selected option
    # Option1
    if selection == 1:
        Full_Name = str(input("Full Name: "))
        Age = str(input("Age: "))
        Address = str(input("Address: "))
        Phone_num = str(input("Phone Number: "))
        print("Saved!")
        inputs = {
            "Name": Full_Name,
            "Age": Age,
            "Address": Address,
            "Phone": Phone_num
            }
        print("Menu: ")
        print("1 -> Add an item.")
        print("2 -> Search.")
        print("3 -> Exit (y/n)")
        selection = int(input("Select what you want to do: \n"))
        Contact_Tracing[Full_Name] = inputs
    # Option2
    if selection == 2:
        Search = str(input("Do you want to search informations? \n Just type full name."))
        if Search in Contact_Tracing:
            for key in Contact_Tracing[Search]:
                print(key, ":", Contact_Tracing[Search][key])
        else:
            print("No Record.")
        print()
        print("Menu: ")
        print("1 -> Add an item.")
        print("2 -> Search.")
        print("3 -> Exit (y/n)")
    # Option3
    if selection == 3:
        Exit = input("Do you want to fill out another?(Y/N)")
        if Exit == 'N':
            break


