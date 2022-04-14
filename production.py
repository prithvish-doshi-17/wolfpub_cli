import time
import traceback
import requests
from functions import get_input
from functions import generate_output
import constants as c

MIN_OP = 1
MAX_OP = 11


def add_publication():
    publication_details = {
        'title': get_input("Title: ", ["null"]),
        'topic': get_input("Topic: ", []),
        'publication_date': get_input("Publication Date (MM/DD/YYYY): ", ["date"]),
        'price': get_input("Price: ", ["float"])
    }
    return publication_details


def add_edition():
    print("Enter information of new book edition:")
    publication_details = add_publication()
    edition = {
        "isbn": get_input("ISBN: ", []),
        "creation_date": get_input("Creation Date: ", ["date"]),
    }
    publication_response = requests.post(c.new_book, publication_details)
    generate_output(publication_response)
    book_response = requests.post(c.new_book, edition)
    generate_output(book_response)


def add_issue():
    print("Enter information of new periodical issue:")
    publication_details = add_publication()
    issue = {
        "issn": get_input("ISSN: ", []),
        "periodical_type": get_input("Type (Enter 1 for Magazine, 2 for Journal): ", ["1_2"]),
    }
    if issue["periodical_type"] == 1:
        issue["periodical_type"] = "Magazine"
    else:
        issue["periodical_type"] = "Journal"
    publication_response = requests.post(c.new_periodical, publication_details)
    generate_output(publication_response)
    book_response = requests.post(c.new_periodical, issue)
    generate_output(book_response)


def update_edition():
    print("Update book edition:")
    edition = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        "isbn": get_input("ISBN: ", []),
        "creation_date": get_input("Creation Date: ", ["date"]),
        "is_available": get_input("Is it available? (1 for Yes, 2 for No): ", ["1_2"])
    }
    if edition["is_available"] == 1:
        edition["is_available"] = "Yes"
    else:
        edition["is_available"] = "No"
    url = str(c.update_publication).replace("<publication_id>", str(edition["publication_id"]))
    response = requests.put(url, edition)
    generate_output(response)


def update_issue():
    print("Update periodical issue:")
    issue = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        "issn": get_input("ISSN: ", []),
        "periodical_type": get_input("Type (Enter 1 for Magazine, 2 for Journal): ", ["1_2"]),
        "is_available": get_input("Is it available? (1 for Yes, 2 for No): ", ["1_2"])
    }
    if issue["is_available"] == 1:
        issue["is_available"] = "Yes"
    else:
        issue["is_available"] = "No"
    url = str(c.update_publication).replace("<publication_id>", str(issue["publication_id"]))
    response = requests.put(url, issue)
    generate_output(response)


def update_chapter():
    choice = get_input("Enter 1 to add new chapter, 2 to update existing chapter: ", ["null", "1_2"])
    if choice == "1":
        chapter_details = {
            "publication_id": get_input("Publication ID: ", ["null"]),
            "chapter_title": get_input("Chapter Title: ", []),
            "chapter_text": get_input("Chapter Text:", [])
        }
        url = str(c.update_chapter).replace("<publication_id>", str(chapter_details["publication_id"]))
        response = requests.put(url, chapter_details)
    else:
        chapter_details = {
            "publication_id": get_input("Publication ID: ", ["null"]),
            "chapter_id": get_input("Chapter ID:", ["null"]),
            "chapter_title": get_input("Chapter Title: ", []),
            "chapter_text": get_input("Chapter Text:", [])
        }
        url = str(c.add_chapter).replace("<publication_id>", str(chapter_details["publication_id"]))
        url = url.replace("<chapter_id>", str(chapter_details["chapter_id"]))
        response = requests.put(url, chapter_details)
    generate_output(response)


def update_article():
    choice = get_input("Enter 1 to add new article, 2 to update existing article: ", ["null", "1_2"])
    if choice == "1":
        article_details = {
            "publication_id": get_input("Publication ID: ", ["null"]),
            'creation_date': get_input("Creation Date (MM/DD/YYYY): ", ["date"]),
            'article_title': get_input("Title: ", []),
            'topic': get_input("Topic: ", []),
            'text': get_input("Text: ", [])
        }
        url = str(c.update_article).replace("<publication_id>", str(article_details["publication_id"]))
        response = requests.put(url, article_details)
    else:
        article_details = {
            "publication_id": get_input("Publication ID: ", ["null"]),
            'article_id': get_input("Article ID: ", ["null"]),
            'creation_date': get_input("Creation Date (MM/DD/YYYY): ", ["date"]),
            'article_title': get_input("Title: ", []),
            'topic': get_input("Topic: ", []),
            'text': get_input("Text: ", [])
        }
        url = str(c.add_article).replace("<publication_id>", str(article_details["publication_id"]))
        url = url.replace("<article_id>", str(article_details["article_id"]))
        response = requests.put(url, article_details)
    generate_output(response)


def update_article_text():
    print("Enter/Update article text:")
    article_text = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        'article_id': get_input("Publication ID: ", ["null"]),
        'text': get_input("Text: ", [])
    }
    url = str(c.add_article).replace("<publication_id>", str(article_text["publication_id"]))
    url = url.replace("<article_id>", str(article_text["article_id"]))
    response = requests.put(url, article_text)
    generate_output(response)


def find_book():
    print("Find book:")
    book_filter = {
        'topic': get_input("Topic: ", []),
        'date': get_input("Date: ", ["date"]),
        'author': get_input("Author's name:", [])
    }
    response = requests.get(c.get_content, book_filter)
    generate_output(response)


def find_article():
    print("Find book:")
    article_filter = {
        'topic': get_input("Topic: ", []),
        'date': get_input("Date: ", ["date"]),
        'author': get_input("Author's name:", [])
    }
    response = requests.get(c.get_content, article_filter)
    generate_output(response)


def add_payment():
    print("Add a payment for author/editor:")
    payment = {
        'emp_id': get_input("Employee ID: ", ["null"]),
        'house_id': get_input("House ID: ", ["null"]),
        'amount': get_input("Amount: ", ["null", "float"]),
        'send_date': get_input("Payment sent date: ", ["null", "date"]),
    }
    response = requests.post(c.add_salary, payment)
    generate_output(response)


def claim_payment():
    print("Claim a payment by author/editor:")
    payment = {
        'transaction_id': get_input("Transaction ID: ", ["null"]),
        'received_date': get_input("Payment claim date: ", ["null", "date"])
    }
    url = str(c.update_salary).replace("<transaction_id>", str(payment["transaction_id"]))
    response = requests.post(url, payment)
    generate_output(response)


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
        update_chapter()
    elif operation == 6:
        update_article()
    elif operation == 7:
        update_article_text()
    elif operation == 8:
        find_book()
    elif operation == 9:
        find_article()
    elif operation == 10:
        add_payment()
    elif operation == 11:
        claim_payment()


def operations():
    print("Select an operation from the list (Enter 0 to exit):\n"
          "1. Add an edition of a book\n"
          "2. Add an issue of a periodical\n"
          "3. Update book edition\n"
          "4. Update periodical issue\n"
          "5. Enter/update a chapter\n"
          "6. Enter/update an article\n"
          "7. Enter/Update text for an article\n"
          "8. Find book by topic / date / author's name\n"
          "9. Find article by topic / date / author's name\n"
          "10. Enter a payment for author / editor\n"
          "11. Claim payment by addressee\n")

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
        except Exception:
            traceback.print_exc()
            time.sleep(1)
            continue
