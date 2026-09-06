import random
def bbat():
    bo=random.randint(1,6)
    while True:
        try:
            ba=int(input("enter the run number(0-6):"))
            if ba>=0 and ba<=6:
                print("teh computer's no:",bo)
                break
            print("entered an invalid no")
        except ValueError:
            print("enter a valid no")
    return ba,bo


def bbowl():
    ba=random.randint(0,6)
    while True:
        try:
            bo=int(input("enter the run number(1-6):"))
            if bo>=1 and bo<=6:
                print("teh computer's number:",ba)
                break
            print("entered an invalid no")
        except ValueError:
            print("enter a valid no")
    return ba,bo

def hr(ba,bo):
    return ba==bo
def strike(ba,bo):
    return ((ba-bo)**2 )== 1
