from functions import get_input
from functions import generate_output
import requests
MIN_OP = 1
MAX_OP = 5
yes = ["yes", "y"]


def enter_distributor():
    print("Enter information of a new distributor:")
    distributor = {
        'name': get_input("Name: ", ["null"]),
        'distributor_type': get_input("Type: ", []),
        'address': get_input("Address: ", []),
        'city': get_input("City: ", []),
        'phone_number': get_input("Contact number: ", []),
        'contact_person': get_input("Contact person: ", []),
        'contact_email': get_input("Contact email: ", []),
        'periodicity': get_input("Periodicity: ", [])
    }
    # call API


def update_distributor():
    print("Update information of a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"]),  # TODO: missing in DISTRIBUTOR_ARGUMENTS in serializers
        'name': get_input("Name: ", []),
        'distributor_type': get_input("Type: ", []),
        'address': get_input("Address: ", []),
        'city': get_input("City: ", []),
        'phone_number': get_input("Contact number: ", []),
        'contact_person': get_input("Contact person: ", []),
        'contact_email': get_input("Contact email: ", []),
        'periodicity': get_input("Periodicity: ", [])
    }
    # call API


def delete_distributor():
    print("Delete a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"])
    }
    # call API


def new_order():
    print("Add a new order:")
    pub_type = get_input("What do you want to order? (Books/Periodicals): ", ["null"])  # no checks here
    choice = "yes"
    orders = set()
    if pub_type == "Books":
        while str.lower(choice) in yes:
            pub_details = {
                'book_id': get_input("Book ID: ", ["null"]),
                'edition': get_input("Edition: ", ["null"]),
                'quantity': get_input("Quantity: ", ["null", "int"])
            }
            orders.add(pub_details)

    else:
        while str.lower(choice) in yes:
            pub_details = {
                'periodical_id': get_input("Periodical ID: ", ["null"]),
                'issue': get_input("Issue: ", ["null"]),
                'quantity': get_input("Quantity: ", ["null", "int"])
            }
            orders.add(pub_details)
    # call API


def bill_distributor():
    print("Generate bills for a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"])
    }
    # call API


def run_operation(operation):
    if operation == 1:
        enter_distributor()
    elif operation == 2:
        update_distributor()
    elif operation == 3:
        delete_distributor()
    elif operation == 4:
        new_order()
    elif operation == 5:
        bill_distributor()


def operations():
    print("Select an operation from the list:\n"
          "1. Enter new distributor\n"
          "2. Update distributor information\n"
          "3. Delete distributor\n"
          "4. Input order from a distributor\n"
          "5. Bill distributor\n")

    while True:
        operation = input("Enter your choice: ")
        try:
            operation = int(operation)
            if operation < MIN_OP or operation > MAX_OP:
                raise ValueError
            run_operation(operation)
            return
        except:
            continue