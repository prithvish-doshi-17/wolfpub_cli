from functions import get_input
MIN_OP = 1
MAX_OP = 9

def enter_new_publication():
    print("Enter publication information:")
    publication_details = {
        'title': get_input("Title: ", ["null"]),
        'topic': get_input("Topic: ", ["null"]),
        'publication_date': get_input("Publication Date (MM/DD/YYYY): ", ["null", "date"]),
        'price': get_input("Price: ", ["null", "float"])
        ## book/periodical info - where do you want it
    }
    # call API

def update_publication():
    print("Enter publication information to be updated:")
    publication_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'title': get_input("Title: ", []),
        'topic': get_input("Topic: ", []),
        'publication_date': get_input("Publication Date (MM/DD/YYYY): ", ["date"]),
        'price': get_input("Price: ", [])
    }
    # call API

def assign_editors():
    print("Assign editor(s) to a publication:")
    publication_id = get_input("Publication ID: ", ["null"])
    editors = get_input("Add number of editors: ", ["null", "int"])
    for i in range(editors):
        editor_details = {
            'publication_id': publication_id,
            'editor': get_input("Editor ID:", ["null"])
        }
        # call API


def view_publications():
    print("View publications related to an editor:")
    editor_details = {
        'editor': get_input("Editor ID:", ["null"])
    }
    # call API


def edit_toc():  ## TODO
    return 0


def add_article():
    print("Add article to a periodical:")
    article_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'creation_date': get_input("Creation Date (MM/DD/YYYY): ", ["null", "date"]),
        'title': get_input("Title: ", ["null"]),
        'topic': get_input("Topic: ", ["null"]),
        'text': get_input("Text: ", [])
        ## not adding journalist name as we are removing that attribute, could see it in serializers though
        ## TODO: Update serializers
    }
    # call API

def delete_article():
    print("Delete article from a periodical:")
    article_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'article_id': get_input("Publication ID: ", ["null"])
    }
    # call API

def add_chapter():
    print("Add article to a periodical:")
    chapter_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'chapter_title': get_input("Title: ", ["null"]),
        'chapter_text': get_input("Text: ", ["null"])
    }
    # call API

def delete_chapter():
    print("Delete article from a periodical:")
    chapter_details = {
        'publication_id': get_input("Publication ID: ", ["null"]),
        'chapter_id': get_input("Chapter ID: ", ["null"])
    }
    # call API


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
        edit_toc()
    elif operation == 6:
        add_article()
    elif operation == 7:
        delete_article()
    elif operation == 8:
        add_chapter()
    elif operation == 9:
        delete_chapter()


def operations():
    print("Select an operation from the list:\n"
          "1. Enter new publication\n"
          "2. Update a publication\n"
          "3. Assign editor(s) to publication\n"
          "4. View publications related to any editor\n"
          "5. Edit table of contents of a publication\n"  ## TODO
          "6. Add article for a periodical\n"
          "7. Delete article from a periodical\n"
          "8. Add chapter to a book\n"
          "9. Delete chapter from a book\n")

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