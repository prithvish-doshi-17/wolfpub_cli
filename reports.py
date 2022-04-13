import time
import traceback
import requests
from functions import get_input
from functions import generate_output
import constants as c
MIN_OP = 1
MAX_OP = 4
yes = ["yes", "y"]


def generate_reports():
    print("Generate monthly reports:")
    # arguments for reports
    response = requests.post(c.base_url)
    generate_output(response)


def total_distributors():
    print("Calculate total distributors:")
    response = requests.get(c.base_url)
    generate_output(response)


def total_revenue():  # check dict keys
    print("Calculate total revenue:")
    filters = {
        'city': get_input("City: ", []),
        'distributor': get_input("Distributor ID:", []),
        'location': get_input("Location: ", [])
    }
    response = requests.get(c.base_url, filters)
    generate_output(response)


def total_payments():  # check dict keys
    print("Calculate total revenue:")
    filters = {
        'start_date': get_input("Start date (MM/DD/YYYY): ", ["null", "date"]),
        'end_date': get_input("End date (MM/DD/YYYY):", ["null", "date"]),
        'work_type': get_input("Work type: ", ["null"])
    }
    response = requests.get(c.base_url, filters)
    generate_output(response)


def run_operation(operation):
    if operation == 1:
        generate_reports()
    elif operation == 2:
        total_distributors()
    elif operation == 3:
        total_revenue()
    elif operation == 4:
        total_payments()


def operations():
    print("Select an operation from the list (Enter 0 to exit):\n"
          "1. Generate monthly reports\n"
          "2. Calculate total distributors\n"
          "3. Calculate total revenue\n"
          "4. Calculate total payments\n")

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