import time
import traceback
import requests
from functions import get_input
from functions import generate_output
import constants as c
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
    response = requests.post(c.new_distributor, distributor)
    generate_output(response)


def update_distributor():
    print("Update information of a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"]),
        'name': get_input("Name: ", []),
        'distributor_type': get_input("Type: ", []),
        'address': get_input("Address: ", []),
        'city': get_input("City: ", []),
        'phone_number': get_input("Contact number: ", []),
        'contact_person': get_input("Contact person: ", []),
        'contact_email': get_input("Contact email: ", []),
        'periodicity': get_input("Periodicity: ", [])
    }
    response = requests.patch(c.update_distributor, distributor)
    generate_output(response)


def delete_distributor():
    print("Delete a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"])
    }
    response = requests.delete(c.base_url)  # generate URL here
    generate_output(response)


def new_order():
    print("Add a new order:")
    pub_type = get_input("What do you want to order? (Enter 1 for Books, 2 for Periodicals): ", ["null", "1_2"])
    choice = "yes"
    orders = []
    if pub_type == "Books":
        while str.lower(choice) in yes:
            pub_details = {
                'book_id': get_input("Book ID: ", ["null"]),
                'edition': get_input("Edition: ", ["null", "int"]),
                'quantity': get_input("Quantity: ", ["null", "int"])
            }
            orders.append(pub_details)
            choice = input("Add more books? (Y/N): ")

    else:
        while str.lower(choice) in yes:
            pub_details = {
                'periodical_id': get_input("Periodical ID: ", ["null"]),
                'issue': get_input("Issue: ", ["null", "int"]),
                'quantity': get_input("Quantity: ", ["null", "int"])
            }
            orders.append(pub_details)
            choice = input("Add more periodicals? (Y/N): ")
    response = requests.post(c.new_order, orders)
    generate_output(response)


def bill_distributor():
    print("Generate bills for a distributor:")
    distributor = {
        'distributor_id': get_input("Distributor ID: ", ["null"])
    }
    response = requests.post(c.new_bill, distributor)
    generate_output(response)


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
    print("Select an operation from the list (Enter 0 to exit):\n"
          "1. Enter new distributor\n"
          "2. Update distributor information\n"
          "3. Delete distributor\n"
          "4. Input order from a distributor\n"
          "5. Bill distributor\n")

    while True:
        operation = input("Enter your choice: ")
        try:
            operation = int(operation)
            if operation == 0:
                return
            if operation < MIN_OP or operation > MAX_OP:
                raise ValueError
            run_operation(operation)
            return
        except Exception as e:
            traceback.print_exc()
            time.sleep(1)
            continue