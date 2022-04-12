from dateutil.parser import parse


def get_input(prompt, conditions):  # TODO: Stack breaks after few returns - fix it
    print("Inside get input")
    ip_string = input(prompt)

    if "null" in conditions:
        if len(ip_string) == 0:
            print("Input cannot be null. Please re-enter")
            ip_string = get_input(prompt, conditions)

    if ("date" in conditions) and len(ip_string) > 0:
        # TODO: Date checking not working
        print("Goes here")
        print(ip_string)
        print(parse(ip_string))
        if not bool(parse(ip_string)):
            print("Date is not in correct format. Please re-enter")
            ip_string = get_input(prompt, conditions)

    if ("int" in conditions) and len(ip_string) > 0:
        try:
            ip_string = int(ip_string)
        except:
            print("Input is not an integer. Please re-enter")
            ip_string = get_input(prompt, conditions)

    return ip_string


def generate_output(html_response):
    status_code = html_response.status_code
    if status_code == 200:
        print(html_response.text)
    elif status_code == 404:
        print("404: Page not found. Please check API destination")
    else:
        print(f"Function returned with status code {status_code}")
