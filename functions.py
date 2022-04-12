from dateutil.parser import parse

## TODO: Stack breaks after few returns - fix it
def get_input(prompt, conditions):
    print("Inside get input")
    ip_string = input(prompt)

    if "null" in conditions:
        if len(ip_string) == 0:
            print("Input cannot be null. Please re-enter")
            ip_string = get_input(prompt, conditions)

    if ("date" in conditions) and len(ip_string) > 0:
        ## TODO: Date checking not working
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
