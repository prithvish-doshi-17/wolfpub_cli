from functions import get_input
from functions import generate_output
import requests
MIN_OP = 1
MAX_OP = 10


def add_edition():
    print("Enter information of new book edition:")
    edition = {
        "isbn": get_input("ISBN: ", ["null"]),
        "creation_date": get_input("Creation Date: ", ["null", "date"]),
        "edition": get_input("Edition: ", ["int"]),
        "book_id": get_input("Book ID: ", ["null"]),
        "is_available": True
    }
    response = requests.get()  # will add similarly in all other functions accroding to type of HTTP request
    generate_output(response)


def add_issue():
    print("Enter information of new periodical issue:")
    issue = {
        "issn": get_input("ISSN: ", ["null"]),
        "issue": get_input("Issue: ", ["int"]),
        "periodical_type": get_input("Type (Magazine/Journal): ", []), ## no checks
        "periodical_id": get_input("Periodical ID: ", ["null"]),  ## need to keep it?
        "is_available": True
    }
    # call API


def update_edition():
    print("Update book edition:")
    edition = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        "isbn": get_input("ISBN: ", []),
        "creation_date": get_input("Creation Date: ", ["date"]),
        "edition": get_input("Edition: ", ["int"]),
        "book_id": get_input("Book ID: ", []),
        "is_available": get_input("Is it available? (Y/N)", [])
    }
    # call API


def update_issue():
    print("Update periodical issue:")
    issue = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        "issn": get_input("ISSN: ", []),
        "issue": get_input("Issue: ", ["int"]),
        "periodical_type": get_input("Type (Magazine/Journal): ", []),  ## no checks
        "periodical_id": get_input("Periodical ID: ", []),
        "is_available": get_input("Is it available? (Y/N)", [])
    }
    # call API


def update_article_chapter():  # TODO
    return 0


def update_article_text():
    print("Update article text:")
    article_text = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'article_id': get_input("Publication ID: ", ["null"]),
        'text': get_input("Text: ", ["null"])
    }
    # call API


def find_book():
    print("Find book:")
    book_filter = {
        'topic': get_input("Topic: ", []),
        'date': get_input("Date: ", ["date"]),
        'author': get_input("Author's name:", [])
    }
    # call API


def find_article():
    return 0


def add_payment():
    print("Add a payment for author/editor:")
    payment = {
        'emp_id': get_input("Employee ID: ", ["null"]),
        'house_id': get_input("House ID: ", ["null"]),
        'amount': get_input("Amount: ", ["null", "float"]),
        'send_date': get_input("Payment sent date: ", ["null"]),
    }
    # call API


def claim_payment():
    print("Claim a payment by author/editor:")
    payment = {
        'transaction_id': get_input("Transaction ID: ", ["null"]),
        'received_date': get_input("Payment claim date", ["null"])
    }
    # call API


def run_operation(operation):
    if operation == 1:
        add_edition()
    elif operation == 2:
        add_issue()
    elif operation == 3:
        update_edition()
    elif operation == 4:
        update_issue()
    elif operation == 5:
        update_article_chapter()
    elif operation == 6:
        update_article_text()
    elif operation == 7:
        find_book()
    elif operation == 8:
        find_article()
    elif operation == 9:
        add_payment()
    elif operation == 10:
        claim_payment()


def operations():
    print("Select an operation from the list:\n"
          "1. Add an edition of a book\n"
          "2. Add an issue of a periodical\n"
          "3. Update book edition\n"
          "4. Update periodical issue\n"
          "5. Enter/update an article or chapter\n"  # TODO
          "6. Enter/Update text for an article\n"
          "7. Find book by topic / date / author's name\n"
          "8. Find article by..."  # TODO
          "9. Enter a payment for author / editor\n"
          "10. Claim payment by addressee\n")

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