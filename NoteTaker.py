#--Note Taker--
def make_notes():
    print("Make a Note:")
    BeginToType = input("Type Here: ")
    entries.append(BeginToType)
    print("Note saved to memory")
entries = []
def view_notes():
    if not entries: 
        print("\nYour notepad is empty")
    else:
        print("Your Notes")
        for note in entries: 
            print("-" + note)

if __name__ == "__main__":
        while True: 
            print("My Notes App")
            OptionOpen = print("1. View Notes")
            OptionAdd = print("2. Make a Note")
            OptionClose = print("3. Exit/Close")

            Choice = int(input("Choose an Option 1-4: "))
            if Choice == 1:
                view_notes()
            if Choice == 2:
                make_notes()
            if Choice == 3:
                confirm = input("Are you sure you want to close the application (y/n): ")
                
                if confirm.lower() == "y":
                    print("Exiting the Application")
                    break
                elif confirm.lower() == "n":
                    print("Returning to Main Menu")
                    continue
                else:
                    print("Invalid Input")