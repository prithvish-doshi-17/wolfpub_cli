import time
import traceback
import requests
from functions import get_input
from functions import generate_output
import production
import constants as c
MIN_OP = 1
MAX_OP = 8


def enter_new_publication():
    print("Enter publication information:")
    pub_type = get_input("Is it a book or a periodical? Enter 1 for book, 2 for periodical: ", ["null", "1_2"])
    if pub_type == "1":
        production.add_edition()
    else:
        production.add_issue()


def update_publication():
    print("Enter publication information to be updated:")
    publication_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'title': get_input("Title: ", []),
        'topic': get_input("Topic: ", []),
        'publication_date': get_input("Publication Date (MM/DD/YYYY): ", ["date"]),
        'price': get_input("Price: ", [])
    }
    url = str(c.update_publication).replace("<publication_id>", str(publication_details["publication_id"]))
    response = requests.put(url, publication_details)
    generate_output(response)


def assign_editors():
    print("Assign editor(s) to a publication:")
    publication_id = get_input("Publication ID: ", ["null"])
    editors = get_input("Add number of editors: ", ["null", "int"])
    for i in range(editors):
        editor_details = {
            'publication_id': publication_id,
            'editor': get_input("Editor ID:", ["null"])
        }
        url = str(c.update_publication).replace("<publication_id>", str(editor_details["publication_id"]))
        response = requests.post(url, editor_details)  # Double checks here - calls API for one editor at a time,
                                                       # handler handles max 5. Can remove one of these
        generate_output(response)


def view_publications():
    print("View publications related to an author/editor:")
    employee_details = {
        'employee_id': get_input("Employee ID:", ["null"])
    }
    url = str(c.view_publication).replace("<employee_id>", str(employee_details["employee_id"]))
    response = requests.put(url, employee_details)
    generate_output(response)


def add_article():
    print("Add article to a periodical:")
    article_details = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        'creation_date': get_input("Creation Date (MM/DD/YYYY): ", ["date"]),
        'article_title': get_input("Article Title: ", []),
        'topic': get_input("Topic: ", []),
        'text': get_input("Text: ", [])
    }
    url = str(c.add_article).replace("<publication_id>", str(article_details["publication_id"]))
    response = requests.post(url, article_details)
    generate_output(response)


def delete_article():
    print("Delete article from a periodical:")
    article_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'article_id': get_input("Article ID: ", ["null"])
    }
    url = str(c.delete_article).replace("<publication_id>", str(article_details["publication_id"]))
    url = url.replace("<article_id>", str(article_details["article_id"]))
    response = requests.delete(url)
    generate_output(response)


def add_chapter():
    print("Add chapter to a book:")
    chapter_details = {
        "publication_id": get_input("Publication ID: ", ["null"]),
        'chapter_title': get_input("Title: ", []),
        'chapter_text': get_input("Text: ", [])
    }
    url = str(c.add_article).replace("<publication_id>", str(chapter_details["publication_id"]))
    response = requests.post(url, chapter_details)
    generate_output(response)


def delete_chapter():
    print("Delete article from a periodical:")
    chapter_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'chapter_id': get_input("Chapter ID: ", ["null"])
    }
    url = str(c.delete_chapter).replace("<publication_id>", str(chapter_details["publication_id"]))
    url = url.replace("<chapter_id>", str(chapter_details["chapter_id"]))
    response = requests.delete(url)
    generate_output(response)


def run_operation(operation):
    if operation == 1:
        enter_new_publication()
    elif operation == 2:
        update_publication()
    elif operation == 3:
        assign_editors()
    elif operation == 4:
        view_publications()
    elif operation == 5:
        add_article()
    elif operation == 6:
        delete_article()
    elif operation == 7:
        add_chapter()
    elif operation == 8:
        delete_chapter()


def operations():
    print("Select an operation from the list (Enter 0 to exit):\n"
          "1. Enter new publication\n"
          "2. Update a publication\n"
          "3. Assign editor(s) to publication\n"
          "4. View publications related to any editor\n"
          "5. Add article to a periodical\n"
          "6. Delete article from a periodical\n"
          "7. Add chapter to a book\n"
          "8. Delete chapter from a book\n")

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
