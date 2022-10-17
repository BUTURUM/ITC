from user import User
import dialog

def authPlayer():
    print('please type info about you account')
    user = User(dialog.noemtry('type username: ', warn='username cannot be empty string'))
    if user.registered:
        if dialog.confirm('This user already registered. Do you want sing out? y/n '):
            user.singOut(); exit()
        return user
    if not user.exists:
        if dialog.confirm('this user not exist. Do you want to register? y/n '):
            user.create(dialog.noemtry('type password: ', warn='password cannot be empty string'))
        else:
            print('you have to have account to use this program.'); exit()
        return user
    while True:
        if user.check(dialog.noemtry('type password: ', warn='password cannot be empty string')):
            user.singIn(); break
        print('wrong password. try other.'); continue
    return user

def authOpponent():
    print('please type info about you opponent account')
    user = User(dialog.noemtry('type username: ', warn='username cannot be empty string'))
    if not user.exists:
        print('this user do not exists. Try another.'); return authOpponent()
    if not user.registered:
        while True:
            if user.check(dialog.noemtry('type password: ', warn='password cannot be empty string')): break
    return user
    
player = authPlayer(); opponent = authOpponent()