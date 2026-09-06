import sqlite3 as mc
import random
import time

con=mc.connect("Odd_or_Even.db")
cur=con.cursor()
def create_acc():#fn to create acc
    while True:
        un=input("enter teh username(no of char<=20):")
        if len(list(un))<=20 and check_uname(un):#checking length of uname
            print("valid username")
            break
        else:
            if len(list(un)) >20:
                print("invalid username: exceeded the limit of no of char")
            else:
                print("invalid username: username already exists")
    while True:
        pa1=input("enter password(no of char<=16):")
        if len(list(pa1))<=16:
            print("valid password")
            pa2=input("reenter the password to confirm:")
            if pa1==pa2:
                break
            print("enter again:")
        else:
            print("invalid username: exceeded the limit of no of char")
    pa=pa1
    while True:
        uid=random.randint(1000000,10000000)
        if check_uid(uid):
            break
    doj,toj=d_t()
    cr="INSERT INTO UID_DATA VALUES(?,?,?,?,?)"
    vr=(uid,un,pa,doj,toj)
    cur.execute(cr,vr)
    con.commit()
    print("account created!")
    return un

def check_uname(un):#checking whether the username already exists in the database
    cur.execute("select username from uid_data where lower(username) = ?",(un.lower(),))
    return cur.fetchone() is None
def check_uid(uid):#checking whether the uid already exists
    cur.execute("select user_id from uid_data where USER_ID=? ",(uid,))
    return cur.fetchone() is None
    
def d_t():#fn to find the current date and time
    do=(time.ctime(time.time())).split()
    d1={'01':"Jan",'02':"Feb",'03':"Mar",'04':"Apr",'05':"May",'06':"Jun",'07':"Jul",'08':"Aug",'09':"Sep",'10':"Oct","11":"Nov","12":"Dec"}    
    mm=""
    for i,j in d1.items():
        if j.lower()==do[1].lower():
            mm+=i
    dd=do[2]
    yy=do[-1]
    doj=yy+"-"+mm+"-"+dd
    toj=do[-2]
    return doj,toj
def login():#fn to login to acc
    p=False#login check var
    un=input("enter your acc username:")
    un,uid=un.lower(),None
    cur.execute("select user_id,password from uid_data where username=lower(?)",(un,))
    i=cur.fetchone()
    if i is None:
        print("account does not exist in the database")
    else:
        while True:
            pa=input("enter the password:")
            if i[1]==pa:
                print("login completed successfully")
                p=True
                uid=i[0]
                break
            else:
                print("entered password is wrong")
    return uid,un,p
                
def enter_data(uid,game,stat,tg,res,gd,gt,plsc,cosc):#fn to enter game data into table game history
    cr= """INSERT INTO GAME_HISTORY
        (USER_ID, GAME, STATUS, TYPE_OF_GAME, RESULT, DATE_OF_GAME, TIME_OF_GAME,PLAYER_SCORE,COMPUTER_SCORE)
        VALUES (?, ?, ?, ?, ?, ?, ?,?,?)"""
    val=(uid,game,stat,tg,res,gd,gt,plsc,cosc)
    cur.execute(cr,val)
    con.commit()

def disp_data(uid):
    cur.execute("SELECT * FROM GAME_HISTORY WHERE USER_ID=?",(uid,))
    lines= cur.fetchall()
    d=["USER_ID", "GAME", 'STATUS', 'TYPE_OF_GAME', 'RESULT', 'DATE_OF_GAME', 'TIME_OF_GAME','PLAYER_SCORE','COMPUTER_SCORE']
    c=1#counter var
    if lines ==[]:
        print("no games played yet")
    else:
        for line in lines:
            print("game:",c)
            c+=1
            for i in range(len(line)):
                print(d[i],":",line[i])
            print()

def create_db():
    
    cur.execute("""
CREATE TABLE IF NOT EXISTS UID_DATA (
    USER_ID INTEGER PRIMARY KEY,
    USERNAME TEXT NOT NULL UNIQUE,
    PASSWORD TEXT,
    DOJ TEXT,
    TOJ TEXT
)
    """)
    cur.execute("""
CREATE TABLE IF NOT EXISTS GAME_HISTORY (
    USER_ID INTEGER,
    GAME TEXT,
    STATUS TEXT,
    TYPE_OF_GAME TEXT,
    RESULT TEXT,
    DATE_OF_GAME TEXT,
    TIME_OF_GAME TEXT,
    PLAYER_SCORE TEXT,
    COMPUTER_SCORE TEXT
)
    """)
    con.commit()
        
def logout(uid):
    uid=None
    username="player"
    p=False
    print("logged out")
    return uid,username,p
def disp_acc_data(uid):
    cur.execute("select * from uid_data where user_id= ?",(uid,))
    lines=cur.fetchall()
    d=["USER_ID","USERNAME","","DATE OF JOINING","TIME OF JOINING"]
    for line in lines:
        if line[0]==uid:
            for i in range(len(line)):
                if i!=2:
                    print(d[i],":",line[i])
        print()
def disp_all():
    cur.execute("select username,user_id from uid_data")
    rows=cur.fetchall()
    print("usernames: user id")
    for row in rows:
        print(row[0],":",row[1])


