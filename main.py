import edit_publish
import production
import distribution
import reports


def get_operations(task):
    if task == 1:
        edit_publish.operations()
    elif task == 2:
        production.operations()
    elif task == 3:
        distribution.operations()
    else:
        reports.operations()


if __name__ == '__main__':
    yes = ["yes", "y"]
    no = ["no", "n"]
    choice = "yes"
    print("###### Welcome to WolfPubDB! ######\n")

    while str.lower(choice) in yes:
        print("Select a task from the list:\n"
              "1. Editing and publishing\n"
              "2. Production of a book edition or of an issue of a publication\n"
              "3. Distribution\n"
              "4. Reports\n")

        try:
            task = int(input("Enter your choice: "))
            if task < 1 or task > 4:
                raise ValueError
            get_operations(task)

            choice = input("Do you want to continue with any other task? (Y/N): ")
        except:
            print("Please enter an integer between 1 and 4\n")

    print("###### Thank you for using WolfPubDB! ######")
