import random
uid=input("enter your name/gamer name:")
ch="X"
def toss(tc,sel):
    while True:
        if tc.upper() in ("ODD","EVEN"):
            break
        print("player has entered",tc,"instead of instructed value")
        tc=input("enter odd or even:")
    coch=random.randint(0,5)
    while True:
        try:
            if sel<6 and sel>=0:
                break
            print("entered no is invalid, enter again")
            sel=int(input("enter the number(0-5):"))
        except ValueError:
            print("enter a valid number")
            
    print("computer's no:",coch)
    ooe=(coch+sel)%2
    print("the result:",coch+sel)
    res= (tc.upper()=="ODD" and ooe!=0) or (tc.upper()=="EVEN" and ooe==0)
    return res

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
    print("SCORE:\n "+uid+":",plrs,"/",w1,",",x,"\n computer:",cors,"/",w2,",",y)
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

#football
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
def fsc(plgo,cogo,nog,nogc=9):
    print("SCORE:\n "+uid+":",plgo,"\n computer:",cogo,"\n goal chances remaining:",nogc-nog)
def football(i,nogc=9,plgo=0,cogo=0):
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
                print("savedd by "+uid)
                fsc(plgo=plgo,cogo=cogo,nog=nog,nogc=nogc)
        else:
            if inter(p=plno,c=cono):
                i+=1
                nop=0
                if bwi(i=i):
                    print("intersepted by "+uid)
                else:
                    print("intersepted by teh computer")
            else:
                nop+=1
                if bwi(i=i):
                    print(uid+" pass no:",nop)
                    if nop==3:
                        nog+=1
                        print("goal chance for "+uid)
                        g=plgc()
                        nop,i=0,1
                        if g:
                            print("gooaaal! for "+uid)
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

def cpen():
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
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=plgc()
        if g:
            pll[_]="X"
            print("scored by "+uid)
            plp+=1
        else:
            pll[_]="O"
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uid,"won")
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
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=plgc()
        if g:
            pll.append("X")
            print("scored by "+uid)
            plp+=1
        else:
            pll.append("O")
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uid,"won")
    elif plp<cop:
        print("computer won")
    print("SCORE: \n computer:",coge,"\n "+uid+":",plge)
    print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))

def ppen():
    plp,cop=0,0
    pll=["_","_","_","_","_"]
    col=["_","_","_","_","_"]
    for _ in range(5):
        g=plgc()
        if g:
            pll[_]="X"
            print("scored by "+uid)
            plp+=1
        else:
            pll[_]="O"
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=cogc()
        if g:
            col[_]="X"
            print("scored by teh computer")
            cop+=1
        else:
            col[_]="O"
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uid,"won")
    elif plp<cop:
        print("computer won")
    while plp==cop:
        _+=1
        g=plgc()
        if g:
            pll.append("X")
            print("scored by "+uid)
            plp+=1
        else:
            pll.append("O")
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
        g=cogc()
        if g:
            col.append("X")
            print("scored by teh computer")
            cop+=1
        else:
            col.append("O")
            print("penalty missed")
        print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))
    if plp>cop:
        print(uid,"won")
    elif plp<cop:
        print("computer won")
    print("SCORE: \n computer:",coge,"\n "+uid+":",plge)
    print("score:\n"+uid+":",plp,":"," ".join(pll),"\ncomputer:",cop,":"," ".join(col))

    
#baseball
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

while ch in "xX":
    print("enter:\n 1: cricket \n 2: football \n 3: baseball")
    while True:
        try:
            ch2=int(input("enter the choice:"))
            if ch2 in (1,2,3):
                break
            print("entered no is invalid, enter again")
        except ValueError:
            print("enter a valid no")
    tc=input("enter odd or even:")
    
    while True:
        if tc.upper() in ("ODD","EVEN"):
            break
        print("invalid choice entered")
        tc=input("enter odd or even:")
    while True:
        try:
            sel=int(input("enter the number(0-5):"))
            if sel<6 and sel>=0:
                break
            print("invalid no entered")
        except ValueError:
            print("invalid no entered")
    
    #player chose cricket
    if ch2==1:
        if toss(tc=tc,sel=sel):#player won toss
            
            while True:
                try:
                    chn=int(input("enter 1: to bat, 2: to bowl:"))
                    if chn in (1,2):
                        break
                    print("entered no is invalid, enter again")
                    
                except ValueError:
                    print("enter a valid number")
            if chn==1:#player chose to bat
                i,w=1,0
                plr=0
                ball=0
                print("the ",uid," chose to bat first")
                while True:
                    ba,bo=bat()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(u=uid,plr=plr,ball=ball,i=i,w=w)
                        print("computer requires ",plr+1,"runs to win")
                        break
                    else:
                        plr+=ba
                        csc(u=uid,plr=plr,ball=ball,i=i,w=w)
                print("SCORE:\n "+uid+":",plr,",",str(ball//6)+"."+str(ball%6))
                x=str(str(ball//6)+"."+str(ball%6))
                cor,ball,i,w=0,0,2,0
                print("computer about to bat")
                while True:
                    ba,bo=bowl()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(cor=cor,i=i,ball=ball,w=w)
                        if cor<plr:
                            print("computer lost the game")
                            print(uid,"beat the computer by",plr-cor,"runs")
                        break
                        
                    else:
                        cor+=ba
                        csc(cor=cor,i=i,ball=ball,w=w)
                        if cor>plr:
                            print("computer beat",uid)
                            break
                        print(uid+" needs",plr-cor+1,"runs to win")
                y=str(ball//6)+"."+str(ball%6)
                print("SCORE:\n "+uid+":",plr,",",x,"\n computer:",cor,",",y)
                if cor==plr:
                    print("game is a tie, it will head into super over")
                    while sbowl():
                        pass
                    
            else:#player chose to ball 
                w,cor,ball,i=0,0,0,2
                print(uid,"chose to ball first")
                print("computer about to bat")
                while True:
                    ba,bo=bowl()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(cor=cor,i=i,ball=ball,w=w)
                        print(uid," requires ",cor+1,"runs to win")
                        break
                    else:
                        cor+=ba
                        csc(cor=cor,ball=ball,i=i,w=w)
                print("SCORE:\n computer:",cor,",",str(ball//6)+"."+str(ball%6))
                x=str(str(ball//6)+"."+str(ball%6))
                plr,ball,i,w=0,0,1,0
                print(uid,"about to bat")
                while True:
                    ba,bo=bat()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(plr=plr,i=i,ball=ball,w=w)
                        if plr<cor:
                            print(uid+" lost the game")
                            print("the computer beat",uid," by",cor-plr,"runs")
                        break
                    else:
                        plr+=ba
                        csc(plr=plr,i=i,ball=ball,w=w)
                        if plr>cor:
                            print(uid+"beat the computer")
                            break
                        print(uid+" needs",cor-plr+1,"runs to win")
                y=str(ball//6)+"."+str(ball%6)
                print("SCORE:\n computer:",cor,",",x,"\n "+uid+":",plr,",",y)
                if plr==cor:
                    print("game is a tie, it will head into super over")
                    while sbat():
                        pass

        else:#player lost the toss
            coto=random.choice(["BA","BO"])
            if coto=="BO":#teh computer chose to ball
                i=1
                plr=0
                ball=0
                w=0
                print("the computer chose to ball first")
                while True:
                    ba,bo=bat()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(u=uid,plr=plr,ball=ball,i=i,w=w)
                        print("computer requires ",plr+1,"runs to win")
                        break
                    else:
                        plr+=ba
                        csc(u=uid,plr=plr,ball=ball,i=i,w=w)
                print("SCORE:\n "+uid+":",plr,",",str(ball//6)+"."+str(ball%6))
                x=str(str(ball//6)+"."+str(ball%6))
                cor,ball,i,w=0,0,2,0
                print("computer about to bat")
                while True:
                    ba,bo=bowl()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(cor=cor,i=i,ball=ball,w=w)
                        if cor<plr:
                            print("computer lost the game")
                            print(uid,"beat the computer by",plr-cor,"runs")
                        break
                    else:
                        cor+=ba
                        csc(cor=cor,i=i,ball=ball,w=w)
                        if cor>plr:
                            print("computer beat",uid)
                            break
                        print(uid+" needs",plr-cor+1,"runs to win")
                y=str(ball//6)+"."+str(ball%6)
                print("SCORE:\n "+uid+":",plr,",",x,"\n computer:",cor,",",y)
                if plr==cor:
                    print("game is a tie, it will head into super over")
                    while sbowl():
                        pass
            else:#teh computer chose to bat
                cor,ball,i,w=0,0,2,0
                print("computer about to bat")
                while True:
                    ba,bo=bowl()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(cor=cor,i=i,ball=ball,w=w)
                        print(uid," requires ",cor+1,"runs to win")
                        break
                    else:
                        cor+=ba
                        csc(cor=cor,ball=ball,i=i)
                print("SCORE:\n computer:",cor,",",str(ball//6)+"."+str(ball%6))
                x=str(str(ball//6)+"."+str(ball%6))
                plr,ball,i,w=0,0,1,0
                print(uid,"about to bat")
                while True:
                    ba,bo=bat()
                    ball+=1
                    if wicket(ba,bo):
                        w+=1
                        out()
                        csc(plr=plr,i=i,ball=ball,w=w)
                        if plr<cor:
                            print(uid+" lost the game")
                            print("the computer beat",uid," by",cor-plr,"runs")
                        break
                    else:
                        plr+=ba
                        csc(plr=plr,i=i,ball=ball,w=w)
                        if plr>cor:
                            print(uid+" beat the computer")
                            break
                        print(uid+" needs",cor-plr+1,"runs to win")
                y=str(ball//6)+"."+str(ball%6)
                print("SCORE:\n computer:",cor,",",x,"\n "+uid+":",plr,",",y)
                if plr==cor:
                    print("game is a tie, it will head into super over")
                    while sbat():
                        pass
    elif ch2==2:
        print(uid+" chose football")
        print("3 consequtive passes(1-3) result in goal chance")
        print("there will be nine goal chances in total")
        print("entering invalid nos result in goal chance for teh computer")
        print("the nos for goal chance will be (4-6)")
        if toss(tc=tc,sel=sel):
            print(uid+" won the toss")
            print("enter: \n 1:touch\n 2:post")
            while True:
                try:
                    chn=int(input("enter teh choice:"))
                    if chn in [1,2]:
                        break
                    print("enter a valid choice")
                except ValueError:
                    print("enter a valid choice")
            if chn==1:
                print(uid+" chose touch")
                i=0
                plgo,cogo=football(i=i)
                print("SCORE: \n computer:",cogo,"\n "+uid+":",plgo)
                if plgo>cogo:
                    print(uid+" won teh game")
                elif plgo<cogo:
                    print("teh computer won teh game")
                else:
                    print("game is a draw")
                    print("game will head into extra time(3 more goal chances)")
                    i=1
                    plge,coge=football(i=i,nogc=3,plgo=plgo,cogo=cogo)
                    if plge>coge:
                        print(uid+" won the game after extra time")
                    elif plge<coge:
                        print("computer won the game after extra time")
                    else:
                        print("the game is a draw after extra time, the game will be decided on penalties")
                        ppen()
            else:
                print(uid+" chose post")
                nog=0
                i=1
                nop=0
                plgo,cogo=football(i=i)
                print("SCORE: \n computer:",cogo,"\n "+uid+":",plgo)
                if plgo>cogo:
                    print(uid+" won teh game")
                elif plgo<cogo:
                    print("teh computer won teh game")
                else:
                    print("game is a draw")
                    print("game will head into extra time(3 more goal chances)")
                    i=0
                    plge,coge=football(i=i,nogc=3,plgo=plgo,cogo=cogo)
                    if plge>coge:
                        print(uid+" won the game after extra time")
                    elif plge<coge:
                        print("computer won the game after extra time")
                    else:
                        print("the game is a draw after extra time, the game will be decided on penalties")
                        cpen()   

        

        else:
            print("teh computer won the toss")
            coch=random.choice(["TO","PO"])
            if coch=="PO":
                print("teh computer chose post")
                nog=0
                i=0
                nop=0
                plgo,cogo=football(i=i)
                print("SCORE: \n computer:",cogo,"\n "+uid+":",plgo)
                if plgo>cogo:
                    print(uid+" won teh game")
                elif plgo<cogo:
                    print("teh computer won teh game")
                else:
                    print("game is a draw")
                    print("game will head into extra time(3 more goal chances)")
                    i=1
                    plge,coge=football(i=i,nogc=3,plgo=plgo,cogo=cogo)
                    if plge>coge:
                        print(uid+" won the game after extra time")
                    elif plge<coge:
                        print("computer won the game after extra time")
                    else:
                        print("the game is a draw after extra time, the game will be decided on penalties")
                        ppen()
            else:
                print("teh computer chose touch")
                nog=0
                i=1
                nop=0
                plgo,cogo=football(i=i)
                print("SCORE: \n computer:",cogo,"\n "+uid+":",plgo)
                if plgo>cogo:
                    print(uid+" won teh game")
                elif plgo<cogo:
                    print("teh computer won teh game")
                else:
                    print("game is a draw")
                    print("game will head into extra time(3 more goal chances)")
                    i=0
                    plgo,cogo=football(i=i,nogc=3,plgo=plgo,cogo=cogo)
                    if plgo>cogo:
                        print(uid+" won the game after extra time")
                    elif plgo<cogo:
                        print("computer won the game after extra time")
                    else:
                        print("the game is a draw after extra time, the game will be decided on penalties")
                        cpen()
    elif ch2==3:
        print(uid+"chose baseball")
        print("there will be 7 balls")
        print("adjacent nos will result in a strike(will not count to the 7 balls)")
        print("same nos result in a homerun(7 runs!)")
        print("other nos will result in runs added to the runs scored")
        if toss(tc=tc,sel=sel):#uid won the toss
            print("enter:\n 1:to bat\n 2:to ball")
            while True:
                try:
                    chn=int(input("enter the choice:"))
                    if chn in [1,2]:
                        break
                    print("enter a valid choice")
                except ValueError:
                    print("enter a valid choice")
            if chn==1:
                plr=0
                i=0
                st=0
                hr1=0
                bn=0
                while True:
                    ba,bo=bbat()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr1+=1
                            plr+=7
                            print("homerun","!"*hr1)
                        else:
                            plr+=ba
                        print(uid+" has taken",plr,"runs")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for"+uid)
                        break
                print(uid+" took",plr,"runs, teh computer requires",plr+1,"runs to win")
                print("teh computer is about to bat")
                bn,st,cor,hr2=0,0,0,0
                while True:
                    ba,bo=bbowl()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr2+=1
                            cor+=7
                            print("homerun","!"*hr2)
                        else:
                            cor+=ba
                        print("teh computer has taken",cor,"runs, they need",plr-cor+1,"runs to win")
                        if cor>plr:
                            print("teh computer beat teh "+uid+" with",7-bn,"balls remaining")
                            break
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for teh computer")
                        break
                print("SCORE:\n "+uid+":",plr,"\n computer:",cor)
                if plr>cor:
                    print(uid+" beat teh computer by",plr-cor,"runs")
                elif plr<cor:
                    print("teh computer beat "+uid)
                else:
                    print("the game is tie")
                    print("the side with more homeruns will win the game")
                    if hr1>hr2:
                        print(uid+" beat teh computer on homerun count")
                    elif hr1<hr2:
                        print("teh computer beat "+uid+" on homerun count")
                    else:
                        print("both sides have same no of homeruns")
                        print("therefore the game is a tie")
                    print("SCORE(*after homerun count rule*):\n "+uid+":",plr,"homeruns:",hr1,"\n computer:",cor,"homeruns:",hr2)

            else:
                print(uid+" decided to pitch first")
                cor,st,hr1,bn=0,0,0,0
                while True:
                    ba,bo=bbowl()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr1+=1
                            cor+=7
                            print("homerun","!"*hr1)
                        else:
                            cor+=ba
                        print("teh computer has taken",cor,"runs")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for teh computer")
                        break
                print("teh computer took",cor,"runs, "+uid+" requires",cor+1,"runs to win")
                print(uid+" is about to bat")
                bn,st,plr,hr2=0,0,0,0
                while True:
                    ba,bo=bbat()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr2+=1
                            plr+=7
                            print("homerun","!"*hr2)
                        else:
                            plr+=ba
                        
                        if plr>cor:
                            print(uid+" beat teh computer with",7-bn,"balls remaining")
                            break
                        print(uid+" has taken",plr,"runs, they need",cor-plr+1,"runs to win")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for "+uid)
                        break
                print("SCORE:\n computer:",cor,"\n "+uid+":",plr)
                if plr>cor:
                    print(uid+" beat teh computer ")
                elif plr<cor:
                    print("teh computer beat "+uid+" by",plr-cor,"runs")
                else:
                    print("the game is tie")
                    print("the side with more homeruns will win the game")
                    if hr1>hr2:
                        print("teh computer beat "+uid+" on homerun count")
                    elif hr1<hr2:
                        print(uid+" beat teh computer on homerun count")
                    else:
                        print("both sides have same no of homeruns")
                        print("therefore the game is a tie")
                    print("SCORE(*after homerun count rule*):\n computer:",cor,"homeruns:",hr1,"\n "+uid+":",plr,"homeruns:",hr2)
                    
                    
        else:
            coto=random.choice(["BA","BO"])
            if coto=="BO":
                print("computer decided to pitch first")
                plr=0
                st=0
                hr1=0
                bn=0
                while True:
                    ba,bo=bbat()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr1+=1
                            plr+=7
                            print("homerun","!"*hr1)
                        else:
                            plr+=ba
                        print(uid+" has taken",plr,"runs")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for"+uid)
                        break
                print(uid+" took",plr,"runs, teh computer requires",plr+1,"runs to win")
                print("teh computer is about to bat")
                bn,st,cor,hr2=0,0,0,0
                while True:
                    ba,bo=bbowl()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr2+=1
                            cor+=7
                            print("homerun","!"*hr2)
                        else:
                            cor+=ba
                        
                        if cor>plr:
                            print("teh computer beat teh "+uid+" with",7-bn,"balls remaining")
                            break
                        print("teh computer has taken",cor,"runs, they need",plr-cor+1,"runs to win")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for teh computer")
                        break
                print("SCORE:\n "+uid+":",plr,"\n computer:",cor)
                if plr>cor:
                    print(uid+" beat teh computer by",plr-cor,"runs")
                elif plr<cor:
                    print("teh computer beat "+uid)
                else:
                    print("the game is tie")
                    print("the side with more homeruns will win the game")
                    if hr1>hr2:
                        print(uid+" beat teh computer on homerun count")
                    elif hr1<hr2:
                        print("teh computer beat "+uid+" on homerun count")
                    else:
                        print("both sides have same no of homeruns")
                        print("therefore the game is a tie")
                    print("SCORE(*after homerun count rule*):\n "+uid+":",plr,"homeruns:",hr1,"\n computer:",cor,"homeruns:",hr2)
            else:
                print("teh computer decided to bat first")
                cor,st,hr1,bn=0,0,0,0
                while True:
                    ba,bo=bbowl()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr1+=1
                            cor+=7
                            print("homerun","!"*hr1)
                        else:
                            cor+=ba
                        print("teh computer has taken",cor,"runs")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for teh computer")
                        break
                print("teh computer took",cor,"runs, "+uid+" requires",cor+1,"runs to win")
                print(uid+" is about to bat")
                bn,st,plr,hr2=0,0,0,0
                while True:
                    ba,bo=bbat()
                    if strike(ba,bo):
                        st+=1
                        print("strike:",st,"!"*st)
                        if st==3:
                            print("strike out!!!")
                            break
                    else:
                        st=0
                        bn+=1
                        if hr(ba,bo):
                            hr2+=1
                            plr+=7
                            print("homerun","!"*hr2)
                        else:
                            plr+=ba
                        
                        if plr>cor:
                            print(uid+" beat teh computer with",7-bn,"balls remaining")
                            break
                        print(uid+" has taken",plr,"runs, they need",cor-plr+1,"runs to win")
                    print("balls remaining:",7-bn)
                    if 7-bn==0:
                        print("innings over for "+uid)
                        break
                print("SCORE:\n computer:",cor,"\n "+uid+":",plr)
                if plr>cor:
                    print(uid+" beat teh computer ")
                elif plr<cor:
                    print("teh computer beat "+uid+" by",cor-plr,"runs")
                else:
                    print("teh game is tie")
                    print("teh side with more homeruns will win teh game")
                    if hr1>hr2:
                        print("teh computer beat "+uid+" on homerun count")
                    elif hr1<hr2:
                        print(uid+" beat teh computer on homerun count")
                    else:
                        print("both sides have same no of homeruns")
                        print("therefore teh game is a tie")
                    print("SCORE(*after homerun count rule*):\n computer:",cor,"homeruns:",hr1,"\n "+uid+":",plr,"homeruns:",hr2)
            
    print("enter:\n X:to continue playing\n O:to exit")
    ch=input("enter teh choice:")
    if ch not in "Xx":
        print("thank you "+uid+" for playing the game")
        print("""
============================================
PROJECT 001

Developer:
ANACONDA

Testing:
Everyone who broke my game until it finally worked.

Special Thanks:
ABHINAV KRISHNA G
The reason why "teh" exists.
One typo in computer class...
it's still here. 😂

Started because of a bet at age 13.
Finished because I refused to lose to that bet.

============================================""")
        print("PROJECT 001")
        break

while True:
    _=input()
        
