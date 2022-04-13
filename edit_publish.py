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
    response = requests.patch(c.update_publication, publication_details)
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
        response = requests.post(c.assign_editor, editor_details)
        generate_output(response)


def view_publications():
    print("View publications related to an editor:")
    editor_details = {
        'editor': get_input("Editor ID:", ["null"])
    }
    response = requests.get(c.view_publication, editor_details)
    generate_output(response)


def add_article():
    print("Add article to a periodical:")
    article_details = {
        "title": get_input("Title: ", ["null"]),
        "issue": get_input("Issue:", ["null"]),
        'creation_date': get_input("Creation Date (MM/DD/YYYY): ", ["date"]),
        'article_title': get_input("Article Title: ", []),
        'topic': get_input("Topic: ", []),
        'text': get_input("Text: ", [])
    }
    response = requests.post(c.add_article, article_details)
    generate_output(response)


def delete_article():
    print("Delete article from a periodical:")
    article_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'article_id': get_input("Article ID: ", ["null"])
    }
    response = requests.delete(c.base_url)  # generate URL here
    generate_output(response)


def add_chapter():
    print("Add chapter to a book:")
    chapter_details = {
        "title": get_input("Title: ", ["null"]),
        "edition": get_input("Edition:", ["null"]),
        'chapter_title': get_input("Title: ", []),
        'chapter_text': get_input("Text: ", [])
    }
    response = requests.post(c.add_chapter, chapter_details)
    generate_output(response)


def delete_chapter():
    print("Delete article from a periodical:")
    chapter_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'chapter_id': get_input("Chapter ID: ", ["null"])
    }
    response = requests.delete(c.base_url)  # generate URL here
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
