from user import User

def confirm(msg, agree='y'):
    return input(msg).lower() == agree
def noemtry(msg, warn=None):
    while True:
        value = input(msg)
        if value:
            return value
        if type(warn) == str: print(warn)
def singOut(user: User):
    if confirm('This user already registered. Do you want sing out? y/n '):
        user.singOut(); return True
    return False
def singUp(user: User):
    if confirm('This user is not exists. Do you want to create new? y/n '):
        user.create(noemtry('type password: ')); return True
    return False
def singIn(user: User):
    while True:
        if not user.check(noemtry('type password: ', 'password cannot be empty string')):
            user.singIn(); break
        print('wrong password. try other.')