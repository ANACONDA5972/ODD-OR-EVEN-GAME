import random
from acc_sys import *
from ooe_cricket import *
from ooe_football import *
from ooe_baseball import *

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

def acc_man(uname=None,uid=None):
    if uid is None:
        p=False
    else:
        p=True
    while True:
        print("enter:\n 0:to exit and play the game\n 1:to create an account\n 2:login\n 3:display acc history\n 4:display acc data\n 5:to logout")
        print(" 6:to print all usernames and its uids")
        while True:
            try:
                chx=int(input("enter teh choice:"))
                if 0<=chx<=6:
                    break
                print("enter a valid choice")
            except ValueError:
                print("enter a valid choice")
        if chx==1:
            if uid is None:
                uname=create_acc()
            else:
                print("cannot create account while logged in")
        elif chx==2:
            if uid is not None:
                print("already logged in")
            else:
                uid,uname,p=login()
        elif chx==3:
            if uid is None:
                print("no account has been logged in")
            else:
                disp_data(uid)
        elif chx==4:
            if uid is None:
                print("no account has been logged in")
            else:
                disp_acc_data(uid)
        elif chx==5:
            if uid is None:
                print("already logged out")
            else:
                uid,uname,p=logout(uid)
        elif chx==6:
            disp_all()
            
        elif chx==0:
            break
    return uid,uname,p
create_db()
uid,uname,result=None,"player" ,""             




while True:
    print("enter:\n 1:to play\n 2:For account details\n 3:to exit")
    while True:
        try:
            chm=int(input("enter the choice:"))
            if chm in (1,2,3):
                break
            print("entered choice is invalid, enter again")
        except ValueError:
            print("enter a valid choice")
    if chm==1:
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
        def status(plr,cor):
            if plr>cor:
                return "WIN"
            elif plr==cor:
                return "DRAW"
            else:
                return "LOSS"
            
        #player chose cricket
        if ch2==1:
            result=""
            game="cricket"
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
                    print("the ",uname," chose to bat first")
                    while True:
                        ba,bo=bat()
                        ball+=1
                        if wicket(ba,bo):
                            w+=1
                            out()
                            csc(u=uname,plr=plr,ball=ball,i=i,w=w)
                            print("computer requires ",plr+1,"runs to win")
                            break
                        else:
                            plr+=ba
                            csc(u=uname,plr=plr,ball=ball,i=i,w=w)
                    print("SCORE:\n "+uname+":",plr,",",str(ball//6)+"."+str(ball%6))
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
                                print(uname,"beat the computer by",plr-cor,"runs")
                            break
                            
                        else:
                            cor+=ba
                            csc(cor=cor,i=i,ball=ball,w=w)
                            if cor>plr:
                                print("computer beat",uname)
                                break
                            print(uname+" needs",plr-cor+1,"runs to win")
                    y=str(ball//6)+"."+str(ball%6)
                    print("SCORE:\n "+uname+":",plr,",",x,"\n computer:",cor,",",y)
                    
                    if cor==plr:
                        print("game is a tie, it will head into super over")
                        while sbowl():
                            pass
                        
                else:#player chose to ball 
                    w,cor,ball,i=0,0,0,2
                    print(uname,"chose to ball first")
                    print("computer about to bat")
                    while True:
                        ba,bo=bowl()
                        ball+=1
                        if wicket(ba,bo):
                            w+=1
                            out()
                            csc(cor=cor,i=i,ball=ball,w=w)
                            print(uname," requires ",cor+1,"runs to win")
                            break
                        else:
                            cor+=ba
                            csc(cor=cor,ball=ball,i=i,w=w)
                    print("SCORE:\n computer:",cor,",",str(ball//6)+"."+str(ball%6))
                    x=str(str(ball//6)+"."+str(ball%6))
                    plr,ball,i,w=0,0,1,0
                    print(uname,"about to bat")
                    while True:
                        ba,bo=bat()
                        ball+=1
                        if wicket(ba,bo):
                            w+=1
                            out()
                            csc(plr=plr,i=i,ball=ball,w=w)
                            if plr<cor:
                                print(uname+" lost the game")
                                print("the computer beat",uname," by",cor-plr,"runs")
                            break
                        else:
                            plr+=ba
                            csc(plr=plr,i=i,ball=ball,w=w)
                            if plr>cor:
                                print(uname+"beat the computer")
                                break
                            print(uname+" needs",cor-plr+1,"runs to win")
                    y=str(ball//6)+"."+str(ball%6)
                    print("SCORE:\n computer:",cor,",",x,"\n "+uname+":",plr,",",y)
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
                            csc(u=uname,plr=plr,ball=ball,i=i,w=w)
                            print("computer requires ",plr+1,"runs to win")
                            break
                        else:
                            plr+=ba
                            csc(u=uname,plr=plr,ball=ball,i=i,w=w)
                    print("SCORE:\n "+uname+":",plr,",",str(ball//6)+"."+str(ball%6))
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
                                print(uname,"beat the computer by",plr-cor,"runs")
                            break
                        else:
                            cor+=ba
                            csc(cor=cor,i=i,ball=ball,w=w)
                            if cor>plr:
                                print("computer beat",uname)
                                break
                            print(uname+" needs",plr-cor+1,"runs to win")
                    y=str(ball//6)+"."+str(ball%6)
                    print("SCORE:\n "+uname+":",plr,",",x,"\n computer:",cor,",",y)
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
                            print(uname," requires ",cor+1,"runs to win")
                            break
                        else:
                            cor+=ba
                            csc(cor=cor,ball=ball,i=i)
                    print("SCORE:\n computer:",cor,",",str(ball//6)+"."+str(ball%6))
                    x=str(str(ball//6)+"."+str(ball%6))
                    plr,ball,i,w=0,0,1,0
                    print(uname,"about to bat")
                    while True:
                        ba,bo=bat()
                        ball+=1
                        if wicket(ba,bo):
                            w+=1
                            out()
                            csc(plr=plr,i=i,ball=ball,w=w)
                            if plr<cor:
                                print(uname+" lost the game")
                                print("the computer beat",uname," by",cor-plr,"runs")
                            break
                        else:
                            plr+=ba
                            csc(plr=plr,i=i,ball=ball,w=w)
                            if plr>cor:
                                print(uname+" beat the computer")
                                break
                            print(uname+" needs",cor-plr+1,"runs to win")
                    y=str(ball//6)+"."+str(ball%6)
                    print("SCORE:\n computer:",cor,",",x,"\n "+uname+":",plr,",",y)
                    if plr==cor:
                        print("game is a tie, it will head into super over")
                        while sbat(result):
                            pass
            result="SCORE: "+uname+":"+str(plr)+","+x+" computer:"+str(cor)+","+y
            stat=status(plr=plr,cor=cor)
            plsc,cosc=plr,cor
        elif ch2==2:
            result=""
            game="football"
            print(uname+" chose football")
            print("3 consequtive passes(1-3) result in goal chance")
            print("there will be nine goal chances in total")
            print("entering invalid nos result in goal chance for teh computer")
            print("the nos for goal chance will be (4-6)")
            if toss(tc=tc,sel=sel):
                print(uname+" won the toss")
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
                    print(uname+" chose touch")
                    i=0
                    plgo,cogo=football(i=i,uname=uname)
                    print("SCORE: \n computer:",cogo,"\n "+uname+":",plgo)
                    if plgo>cogo:
                        print(uname+" won teh game")
                    elif plgo<cogo:
                        print("teh computer won teh game")
                    else:
                        print("game is a draw")
                        print("game will head into extra time(3 more goal chances)")
                        i=1
                        if plge>coge:
                            print(uname+" won the game after extra time")
                        elif plge<coge:
                            print("computer won the game after extra time")
                        else:
                            print("the game is a draw after extra time, the game will be decided on penalties")
                            sc=ppen(uname)
                            
                else:
                    print(uname+" chose post")
                    nog=0
                    i=1
                    nop=0
                    plgo,cogo=football(i=i,uname=uname)
                    print("SCORE: \n computer:",cogo,"\n "+uname+":",plgo)
                    if plgo>cogo:
                        print(uname+" won teh game")
                    elif plgo<cogo:
                        print("teh computer won teh game")
                    else:
                        print("game is a draw")
                        print("game will head into extra time(3 more goal chances)")
                        i=0
                        plge,coge=football(i=i,nogc=3,plgo=plgo,cogo=cogo,uname=uname)
                        if plge>coge:
                            print(uname+" won the game after extra time")
                        elif plge<coge:
                            print("computer won the game after extra time")
                        else:
                            print("the game is a draw after extra time, the game will be decided on penalties")
                            sc=cpen(uname=uname)   

            

            else:
                print("teh computer won the toss")
                coch=random.choice(["TO","PO"])
                if coch=="PO":
                    print("teh computer chose post")
                    nog=0
                    i=0
                    nop=0
                    plgo,cogo=football(i=i,uname=uname)
                    print("SCORE: \n computer:",cogo,"\n "+uname+":",plgo)
                    if plgo>cogo:
                        print(uname+" won teh game")
                    elif plgo<cogo:
                        print("teh computer won teh game")
                    else:
                        print("game is a draw")
                        print("game will head into extra time(3 more goal chances)")
                        i=1
                        plge,coge=football(i=i,nogc=3,plgo=plgo,cogo=cogo,uname=uname)
                        if plge>coge:
                            print(uname+" won the game after extra time")
                        elif plge<coge:
                            print("computer won the game after extra time")
                        else:
                            print("the game is a draw after extra time, the game will be decided on penalties")
                            sc=ppen(uname=uname)
                else:
                    print("teh computer chose touch")
                    nog=0
                    i=1
                    nop=0
                    plgo,cogo=football(i=i,uname=uname)
                    print("SCORE: \n computer:",cogo,"\n "+uname+":",plgo)
                    if plgo>cogo:
                        print(uname+" won teh game")
                    elif plgo<cogo:
                        print("teh computer won teh game")
                    else:
                        print("game is a draw")
                        print("game will head into extra time(3 more goal chances)")
                        i=0
                        plgo,cogo=football(i=i,nogc=3,plgo=plgo,cogo=cogo,uname=uname)
                        if plgo>cogo:
                            print(uname+" won the game after extra time")
                        elif plgo<cogo:
                            print("computer won the game after extra time")
                        else:
                            print("the game is a draw after extra time, the game will be decided on penalties")
                            sc=cpen(uname=uname)
            result+="SCORE: computer:"+str(cogo)+" "+uname+":"+str(plgo)
            if cogo==plgo:
                result+="AET: computer:"+str(cogo)+" "+uname+":"+str(plgo)
                if plge==coge:
                    result+="PEN:"+sc
            plsc,cosc=plgo,cogo
            stat=status(plr=plgo,cor=cogo)
        elif ch2==3:
            game="baseball"
            print(uname+"chose baseball")
            print("there will be 7 balls")
            print("adjacent nos will result in a strike(will not count to the 7 balls)")
            print("same nos result in a homerun(7 runs!)")
            print("other nos will result in runs added to the runs scored")
            if toss(tc=tc,sel=sel):#uname won the toss
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
                            print(uname+" has taken",plr,"runs")
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for"+uname)
                            break
                    print(uname+" took",plr,"runs, teh computer requires",plr+1,"runs to win")
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
                                print("teh computer beat teh "+uname+" with",7-bn,"balls remaining")
                                break
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for teh computer")
                            break
                    print("SCORE:\n "+uname+":",plr,"\n computer:",cor)
                    if plr>cor:
                        print(uname+" beat teh computer by",plr-cor,"runs")
                    elif plr<cor:
                        print("teh computer beat "+uname)
                    else:
                        print("the game is tie")
                        print("the side with more homeruns will win the game")
                        if hr1>hr2:
                            print(uname+" beat teh computer on homerun count")
                        elif hr1<hr2:
                            print("teh computer beat "+uname+" on homerun count")
                        else:
                            print("both sides have same no of homeruns")
                            print("therefore the game is a tie")
                        print("SCORE(*after homerun count rule*):\n "+uname+":",plr,"homeruns:",hr1,"\n computer:",cor,"homeruns:",hr2)

                else:
                    print(uname+" decided to pitch first")
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
                    print("teh computer took",cor,"runs, "+uname+" requires",cor+1,"runs to win")
                    print(uname+" is about to bat")
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
                                print(uname+" beat teh computer with",7-bn,"balls remaining")
                                break
                            print(uname+" has taken",plr,"runs, they need",cor-plr+1,"runs to win")
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for "+uname)
                            break
                    print("SCORE:\n computer:",cor,"\n "+uname+":",plr)
                    if plr>cor:
                        print(uname+" beat teh computer ")
                    elif plr<cor:
                        print("teh computer beat "+uname+" by",cor-plr,"runs")
                    else:
                        print("the game is tie")
                        print("the side with more homeruns will win the game")
                        if hr1>hr2:
                            print("teh computer beat "+uname+" on homerun count")
                        elif hr1<hr2:
                            print(uname+" beat teh computer on homerun count")
                        else:
                            print("both sides have same no of homeruns")
                            print("therefore the game is a tie")
                        print("SCORE(*after homerun count rule*):\n computer:",cor,"homeruns:",hr1,"\n "+uname+":",plr,"homeruns:",hr2)
                
                
                        
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
                            print(uname+" has taken",plr,"runs")
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for"+uname)
                            break
                    print(uname+" took",plr,"runs, teh computer requires",plr+1,"runs to win")
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
                                print("teh computer beat teh "+uname+" with",7-bn,"balls remaining")
                                break
                            print("teh computer has taken",cor,"runs, they need",plr-cor+1,"runs to win")
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for teh computer")
                            break
                    print("SCORE:\n "+uname+":",plr,"\n computer:",cor)
                    if plr>cor:
                        print(uname+" beat teh computer by",plr-cor,"runs")
                    elif plr<cor:
                        print("teh computer beat "+uname)
                    else:
                        print("the game is tie")
                        print("the side with more homeruns will win the game")
                        if hr1>hr2:
                            print(uname+" beat teh computer on homerun count")
                        elif hr1<hr2:
                            print("teh computer beat "+uname+" on homerun count")
                        else:
                            print("both sides have same no of homeruns")
                            print("therefore the game is a tie")
                        print("SCORE(*after homerun count rule*):\n "+uname+":",plr,"homeruns:",hr1,"\n computer:",cor,"homeruns:",hr2)
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
                    print("teh computer took",cor,"runs, "+uname+" requires",cor+1,"runs to win")
                    print(uname+" is about to bat")
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
                                print(uname+" beat teh computer with",7-bn,"balls remaining")
                                break
                            print(uname+" has taken",plr,"runs, they need",cor-plr+1,"runs to win")
                        print("balls remaining:",7-bn)
                        if 7-bn==0:
                            print("innings over for "+uname)
                            break
                    print("SCORE:\n computer:",cor,"\n "+uname+":",plr)
                    if plr>cor:
                        print(uname+" beat teh computer ")
                    elif plr<cor:
                        print("teh computer beat "+uname+" by",cor-plr,"runs")
                    else:
                        print("teh game is tie")
                        print("teh side with more homeruns will win teh game")
                        if hr1>hr2:
                            print("teh computer beat "+uname+" on homerun count")
                        elif hr1<hr2:
                            print(uname+" beat teh computer on homerun count")
                        else:
                            print("both sides have same no of homeruns")
                            print("therefore teh game is a tie")
                        print("SCORE(*after homerun count rule*):\n computer:",cor,"homeruns:",hr1,"\n "+uname+":",plr,"homeruns:",hr2)
            result+="SCORE: computer:"+str(cor)+" "+uname+":"+str(plr)
            if plr==cor:
                result+="HR:computer:"+str(hr1)+" "+uname+":"+str(hr2)
            stat=status(plr=plr,cor=cor)
            plsc,cosc=plr,cor
        gd,tg=d_t()
        enter_data(uid=uid,game=game,stat=stat,tg="NORMAL",res=result,gd=gd,gt=tg,plsc=plsc,cosc=cosc)

    elif chm ==2:
        uid,uname,p=acc_man(uid=uid,uname=uname)
    elif chm ==3:
        print("thank you "+uname+" for playing the game")
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
it's still here. 

Started because of a bet at age 13.
Finished because I refused to lose to that bet.

============================================""")
        print("PROJECT 001")
        break

while True:
    _=input()
        
