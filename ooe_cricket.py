import random

def wicket(ba,bo):
    return ba==bo

def bat():
    bo=random.randint(1,6)
    while True:
        try:
            ba=int(input("enter the no for batting(0-6):"))
            if ba<=6 and ba>=0:
                print("computer's number:",bo)
                break
            print("entered no is invalid, enter again")
        except ValueError:
            print("enter a valid number")
    return ba,bo

def csc(ball,i,u="computer",plr=0,cor=0,w=0):
    if i==1:
        print(u,"has taken",plr,"runs/",w,",",ball,"balls("+str(ball//6)+"."+str(ball%6)+")")
    elif i==2:
        print("computer has taken",cor,"runs/",w,",",ball,"balls("+str(ball//6)+"."+str(ball%6)+")")

def bowl():
    ba=random.randint(0,6)
    while True:
        try:
            bo=int(input("enter the no for balling(1-6):"))
            if bo>0 and bo<=6:
                print("computer's no:",ba)
                break
            print("entered no is invalid,enter again")
        except ValueError:
            print("enter a valid number")
    return ba,bo

def out():
    wime=["bowled out","stumped","catch out","LBW","run out"]
    print("out!!")
    wm=random.choice(wime)
    print("method of dismissal:",wm)

def sbat():
    global result
    i=1
    w1,w2=0,0
    plrs,cors=0,0
    print(uid,"will bat first")
    for a in range(1,7):
        print("teh ball no:",a)
        ba,bo=bat()
        if wicket(ba,bo):
            w1+=1
            out()
            csc(u=uid,plr=plrs,ball=a,i=i,w=w1)
            if w1==2:
                print("all out!!") 
                break
        else:
            plrs+=ba
            csc(u=uid,plr=plrs,ball=a,i=i,w=w1)
    print("SCORE:\n "+uid+":",plrs,",",str(a//6)+"."+str(a%6))
    print("computer needs",plrs+1,"runs to win")
    x=str(str(a//6)+"."+str(a%6))
    i=2
    print("computer is about to bat")
    for a in range(1,7):
        print("teh ball no:",a)
        ba,bo=bowl()
        if wicket(ba,bo):
            w2+=1
            out()
            csc(u=uid,cor=cors,ball=a,i=i,w=w2)
            if w2==2:
                print("all out!!")
                break
        else:
            cors+=ba
            csc(u=uid,cor=cors,ball=a,i=i,w=w2)
            if cors>plrs:
                break
            print("computer needs",plrs-cors+1,"runs to win in",6-a,"balls")
    y=str(str(a//6)+"."+str(a%6))
    if plrs>cors:
        print(uid+" beat the computer in super over!!")
    elif plrs<cors:
        print("computer beat "+uid+" in super over")
    else:
        print("game ended in a super over, game will go into super over again")
        return True

def sbowl():
    i=2
    w1,w2=0,0
    plrs,cors=0,0
    print("computer will bat first")
    for a in range(1,7):
        print("teh ball no:",a)
        ba,bo=bowl()
        if wicket(ba,bo):
            w2+=1
            out()
            csc(u=uid,cor=cors,ball=a,i=i,w=w2)
            if w2==2:
                print("all out!!")
                break
        else:
            cors+=ba
            csc(u=uid,cor=cors,ball=a,i=i,w=w2)
    print("SCORE:\n computer:",cors,",",str(a//6)+"."+str(a%6))
    print(uid+" needs",cors+1,"runs to win")
    x=str(str(a//6)+"."+str(a%6))
    i=1
    print(uid+" is about to bat")
    for a in range(1,7):
        print("teh ball no:",a)
        ba,bo=bat()
        if wicket(ba,bo):
            w1+=1
            out()
            csc(u=uid,plr=plrs,ball=a,i=i,w=w1)
            if w1==2:
                print("all out!!") 
                break
        else:
            plrs+=ba
            csc(u=uid,plr=plrs,ball=a,i=i,w=w1)
            if plrs>cors:
                break
            print(uid+" needs",cors-plrs+1,"runs to win in",6-a,"balls")
    y=str(str(a//6)+"."+str(a%6))
    print("SCORE:\n computer:",cors,"/",w2,",",y,"\n "+uid+":",plrs,"/",w1,",",x)
    if plrs>cors:
        print(uid+" beat the computer in super over!!")
    elif plrs<cors:
        print("computer beat "+uid+" in super over")
    else:
        print("game ended in a super over, game will go into super over again")
        return True
