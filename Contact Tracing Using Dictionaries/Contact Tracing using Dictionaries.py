# Display a menu
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

    Contact_Tracing = {
        "Full name": {
            Full_Name
        },
        "Age": {
            Age
        },
        "Address": {
            Address
        },
        "Phone Number": {
            Phone_num
        }
    }
    for key, value in Contact_Tracing.items():
            print(key, ":", value)
# Option2
# Option3
    Exit = input("Do you want to fill out another?(Y/N)")
    if Exit == 'N':
        break


