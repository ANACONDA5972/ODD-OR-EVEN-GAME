import random
def pa(i):
    p=False
    cono=random.randint(1,3)
    plno=None
    while True:
        try:
            plno=int(input("enter teh no(1-3):"))
            if plno>3 or plno<1:
                p=True
                print("invalid number entered, penalty for computer")
                break
            print("teh computer's no:",cono)
            break
        except ValueError:
            p=True
            print("invalid number entered, penalty for computer")
            break    
    return p,plno,cono
def plgc():
    g=False
    cono=random.randint(4,6)
    while True:
        try:
            plno=int(input("enter the no for attack(4-6):"))
            if plno>6 or plno<4:
                print("goal missed(entered an invalid no)")
                break
            print("computer's defence number:",cono)
            g= plno!=cono
            break
        except ValueError:
            print("goal missed(entered an invalid no)")
            break
    return g
def cogc():
    g=False
    cono=random.randint(4,6)
    while True:
        try:
            plno=int(input("enter a number for defence(4-6):"))
            print("computer's attack number:",cono)
            g= plno!=cono
            break
        except ValueError:
            g=True
            break
    return g

def inter(p,c):
    return p==c
def bwi(i):
    return i%2==0
def fsc(plgo,cogo,nog,nogc=9,uname="player"):
    print("SCORE:\n "+uname+":",plgo,"\n computer:",cogo,"\n goal chances remaining:",nogc-nog)
def football(i,nogc=9,plgo=0,cogo=0,uname="player"):
    nog=0
    nop=0
    while True:
        p,plno,cono=pa(i)
        if p:
            nog+=1
            nop,i=0,0
            g=cogc()
            if g:
                print("gooal for teh computer")
                cogo+=1
                fsc(plgo=plgo,cogo=cogo,nog=nog,nogc=nogc)
            else:
                print("savedd by "+uname)
                fsc(plgo=plgo,cogo=cogo,nog=nog,nogc=nogc)
        else:
            if inter(p=plno,c=cono):
                i+=1
                nop=0
                if bwi(i=i):
                    print("intersepted by "+uname)
                else:
                    print("intersepted by teh computer")
            else:
                nop+=1
                if bwi(i=i):
                    print(uname+" pass no:",nop)
                    if nop==3:
                        nog+=1
                        print("goal chance for "+uname)
                        g=plgc()
                        nop,i=0,1
                        if g:
                            print("gooaaal! for "+uname)
                            plgo+=1
                        else:
                            print("saved by teh keeper")
                        fsc(plgo=plgo,cogo=cogo,nog=nog,nogc=nogc)
                else:
                    print("teh computer pass no:",nop)
                    if nop==3:
                        nog+=1
                        print("goal chance for teh computer")
                        g=cogc()
                        nop,i=0,0
                        if g:
                            print("gooaal! for teh computer")
                            cogo+=1
                        else:
                            print("saved by teh keeper")
                        fsc(plgo=plgo,cogo=cogo,nog=nog,nogc=nogc)
        if nog==nogc:
            print("full time")
            break
    return plgo,cogo

def cpen(uname="player"):
    global plge
    global coge
    plp,cop=0,0
    pll=["_","_","_","_","_"]
    col=["_","_","_","_","_"]
    for _ in range(5):
        g=cogc()
        if g:
            col[_]="X"
            print("scored by teh computer")
            cop+=1
        else:
            col[_]="O"
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=plgc()
        if g:
            pll[_]="X"
            print("scored by "+uname)
            plp+=1
        else:
            pll[_]="O"
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uname,"won")
    elif plp<cop:
        print("computer won")
    while plp==cop:
        _+=1
        g=cogc()
        if g:
            col.append("X")
            print("scored by teh computer")
            cop+=1
        else:
            col.append("O")
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=plgc()
        if g:
            pll.append("X")
            print("scored by "+uname)
            plp+=1
        else:
            pll.append("O")
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uname,"won")
    elif plp<cop:
        print("computer won")
    print("SCORE: \n computer:",coge,"\n "+uname+":",plge)
    print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    sc=" computer:"+str(cop)+" "+uname+":"+str(plp)
    return sc
def ppen(uname="player"):
    global plge 
    global coge 
    plp,cop=0,0
    pll=["_","_","_","_","_"]
    col=["_","_","_","_","_"]
    for _ in range(5):
        g=plgc()
        if g:
            pll[_]="X"
            print("scored by "+uname)
            plp+=1
        else:
            pll[_]="O"
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=cogc()
        if g:
            col[_]="X"
            print("scored by teh computer")
            cop+=1
        else:
            col[_]="O"
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uname,"won")
    elif plp<cop:
        print("computer won")
    while plp==cop:
        _+=1
        g=plgc()
        if g:
            pll.append("X")
            print("scored by "+uname)
            plp+=1
        else:
            pll.append("O")
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=cogc()
        if g:
            col.append("X")
            print("scored by teh computer")
            cop+=1
        else:
            col.append("O")
            print("penalty missed")
        print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uname,"won")
    elif plp<cop:
        print("computer won")
    print("SCORE: \n computer:",coge,"\n "+uname+":",plge)
    print("score:\n"+uname+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    sc=" "+uname+":"+str(plp)+": computer:"+str(cop)
    return sc
