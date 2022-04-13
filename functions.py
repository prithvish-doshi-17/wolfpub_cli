from dateutil.parser import parse


def get_input(prompt, conditions):
    ip_string = input(prompt)
    flag = True
    error_message = ""

    if "null" in conditions:
        if len(ip_string) == 0:
            error_message += "Input cannot be null. "
            flag = False

    if ("date" in conditions) and len(ip_string) > 0:
        # TODO: Date checking not working
        if not bool(parse(ip_string)):
            error_message += "Date is not in correct format. "
            flag = False

    if ("int" in conditions) and len(ip_string) > 0:
        try:
            ip_string = int(ip_string)
            if ip_string < 0:
                raise ValueError
        except:
            error_message += "Input is not a positive integer. "
            flag = False

    if ("float" in conditions) and len(ip_string) > 0:
        try:
            ip_string = float(ip_string)
            if ip_string < 0:
                raise ValueError
        except:
            error_message += "Input is not a positive number. "
            flag = False

    if ("1_2" in conditions) and len(ip_string) > 0:
        if ip_string not in ["1", "2"]:
            error_message += "Input is not 1 or 2. "
            flag = False

    if not flag:
        print(error_message)
        get_input(prompt, conditions)
    else:
        return ip_string


def generate_output(html_response):
    print(html_response.text)
