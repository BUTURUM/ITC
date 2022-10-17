from user import User

def confirm(msg, agree='y'):
    return input(msg).lower() == agree
def noemtry(msg, warn=None):
    while True:
        value = input(msg)
        if value:
            return value
        if type(warn) == str: print(warn)