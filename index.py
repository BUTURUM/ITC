from time import sleep
from user import User
from dialog import *
from random import randrange

def authUser():
    print('please type your user info')
    user = User(noemtry('type username: ', warn='username cannot be empty string')); status = user.status
    if status:
        if singOut(user): exit()
    else:
        if status is None:
            if not singUp(user):
                print('Program cannot work with out your user auth'); return authUser()
        else:
            singIn(user)
    return user
def authOpponent():
    print('please type your opponent info')
    user = User(noemtry('type username: ', warn='username cannot be empty string')); status = user.status
    if not status:
        if status is None:
            if not singUp(user):
                print('Program cannot work with out your opponent auth'); return authOpponent()
        else:
            singIn(user)
    return user

user = authUser(); opponent = authOpponent()

def throw(user: User):
    d1 = randrange(1, 6, 1); d2 = randrange(1, 6, 1); amount = d1 + d2
    print('player {0} throw dice: {1} + {2} = {3}'.format(user.username, d1, d2, amount))
    if amount % 2:
        amount -= 5; print('minus 5 points - not event amount')
    else:
        amount += 10; print('plus 10 points - event amount')
    user.score += amount
def results(user: User):
    print('{0} has {1} points'.format(user.username, user.score))
rounds = 0
while True:
    if rounds >= 4:
        if user.score == opponent.score:
            continue
        print('\n')
        results(user); results(opponent)
        print('\n')
        if user.score > opponent.score:
            print('{0} win with {1} points'.format(user.username, user.score))
        else:
            print('{0} win with {1} points'.format(opponent.username, opponent.score))
        break
    print('\nround {0}: '.format(rounds + 1))
    throw(user); throw(opponent)
    rounds += 1
    sleep(1.5)