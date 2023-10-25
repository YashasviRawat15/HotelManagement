import mysql.connector
def hotel():
    conn=mysql.connector.connect(host='localhost', user='root',passwd='')
    cursor=conn.cursor()
    cursor.execute('create database hotel')
    
def createtables():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    query="create table empl(empid varchar(5) PRIMARY KEY,name varchar(30),sal int,jobtype varchar(20),phone_no int(11))";
    cursor.execute(query)
    query="create table price(sno int,type varchar(20),cost int)";
    cursor.execute(query)
    query="create table item(sno int,itmname varchar(30),cost int)";
    cursor.execute(query)
    query="create table guest(guestid varchar(30),name varchar(50),id_proof varchar(50),phone_no int(12),checkin date,checkout date,roomtype varchar(30),room_no int,total_people int,extra_bedding varchar(5))";
    cursor.execute(query)
    




def new_empl():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    EMPID=input("ENTER EMPLOYEE ID:")
    NAME=input("ENTER EMPLOYEE NAME:")
    SALARY=int(input("ENTER SALARY:"))
    JOB_TYPE=input("ENTER JOB TYPE:")
    PHONE_NO=int(input("ENTER PHONE NO.:"))
    query="insert into empl values('{}','{}',{},'{}',{})".format(EMPID,NAME,SALARY,JOB_TYPE,PHONE_NO)
    cursor.execute(query)
    conn.commit()
    print("EMPLOYEE DETAIL ADDED SUCCESSFULLY")



    
def show_emp():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    print('==========EMPLOYEE==========')
    query="select * from empl"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)




def del_emp():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    EMPID=input("ENTER EMPLOOYEE ID:")
    query="delete from empl where EMPID='{}'".format(EMPID)
    cursor.execute(query)
    conn.commit()
    print("EMPLOYEE RECORD DELETED SUCCESSFULLY")



def price():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    SNO=1
    TYPE='DIAMOND'
    COST=30000
    query="insert into price values({},'{}',{})".format(SNO,TYPE,COST)
    cursor.execute(query)
    conn.commit()
    SNO=2
    TYPE='EMERALD'
    COST=25000
    query="insert into price values({},'{}',{})".format(SNO,TYPE,COST)
    cursor.execute(query)
    conn.commit()
    SNO=3
    TYPE='SAPPHIRE'
    COST=20000
    query="insert into price values({},'{}',{})".format(SNO,TYPE,COST)
    cursor.execute(query)
    conn.commit()
    SNO=4
    TYPE='RUBY'
    COST=15000
    query="insert into price values({},'{}',{})".format(SNO,TYPE,COST)
    cursor.execute(query)
    conn.commit()
    SNO=5
    TYPE='TANZANITE'
    COST=10000
    query="insert into price values({},'{}',{})".format(SNO,TYPE,COST)
    cursor.execute(query)
    conn.commit()
    print('\n==========PRICE==========\n')
    query="select* from price"
    cursor.execute(query)
    data=cursor.fetchall()
    print(*data, sep = "\n\n")
    



def item():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    SNO=1
    ITEMNAME='SOFT DRINKS'
    COST=100
    query="insert into item values({},'{}',{})".format(SNO,ITEMNAME,COST)
    cursor.execute(query)
    conn.commit()
    SNO=2
    ITEMNAME='WATER BOTTLE'
    COST=70
    query="insert into item values({},'{}',{})".format(SNO,ITEMNAME,COST)
    cursor.execute(query)
    conn.commit()
    SNO=3
    ITEMNAME='COCKTAIL'
    COST=2500
    query="insert into item values({},'{}',{})".format(SNO,ITEMNAME,COST)
    cursor.execute(query)
    conn.commit()
    SNO=4
    ITEMNAME='CHOCOLATE'
    COST=100
    query="insert into item values({},'{}',{})".format(SNO,ITEMNAME,COST)
    cursor.execute(query)
    conn.commit()
    SNO=5
    ITEMNAME='BISCUIT'
    COST=50
    query="insert into item values({},'{}',{})".format(SNO,ITEMNAME,COST)
    cursor.execute(query)
    conn.commit()
    print('==========ITEMS==========')
    query="select* from item"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    
    
    
def guest():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    GUESTID=input("ENTER GUEST ID:")
    NAME=input("ENTER NAME:")
    ID_PROOF=input("ENTER ID PROOF:")
    PHONE_NO=input("ENTER PHONE NUMBER:")
    CHECKIN=input("ENTER CHECKIN DATE:")
    CHECKOUT=input("ENTER CHECKOUT DATE :")
    ROOMTYPE=input("ENTER ROOM TYPE:")
    ROOM_NO=int(input("ENTER ROOM NUMBER:"))
    TOTAL_PEOPLE=int(input("ENTER TOTAL NUMBER PEOPLE:"))
    EXTRA_BEDDING=input("EXTRA BEDDING (YES/NO):")
    query="insert into guest values('{}','{}','{}',{},'{}','{}','{}',{},{},'{}')".format(GUESTID,NAME,ID_PROOF,PHONE_NO,CHECKIN,CHECKOUT,ROOMTYPE,ROOM_NO,TOTAL_PEOPLE,EXTRA_BEDDING)
    cursor.execute(query)
    conn.commit()
    print("GUEST DETAILS ADDED SUCCESSFULLY")


    
    
def show_guest():
    conn=mysql.connector.connect(host='localhost', user='root',passwd="",database="hotel")
    cursor=conn.cursor()
    print("==========GUEST DETAILS==========")
    query="select* from guest"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    

    
    
    
#main
hotel()
createtables()



while True: 
    print('\n\n==========WELCOME TO KOHINOOR PALACE==========\n')
    print('=====MENU=====\n')
    print('1. FOR EMPLOYEE')
    print('2. FOR PRICE LISTS')
    print('3. FOR GUEST DETAILS')
    print('4. EXIT')
    choice=int(input('ENTER CHOICE(1-4):'))


    
    if choice==1:
        print('\n================================================\n')
        print('1. ADD EMPLOYEE')
        print('2. VIEW EMPLOYEE')
        print('3. DELETE EMPLOPYEE')

        
        choice2=int(input('ENTER YOUR CHOICE(1-3)'))
        print('\n================================================\n')
        if choice2==1:
            new_empl()
        if choice2==2:
            show_emp()
        if choice2==3:
            del_emp()


    if choice==2:
        print('\n================================================\n')
        print('1. ROOM PRICE')
        print('2. ITEM PRICE')

        
        choice3=int(input('ENTER YOUR CHOICE(1-2)'))
        print('\n================================================\n')
        if choice3==1:
            price()
        if choice3==2:
            item()



    if choice==3:
        print('\n================================================\n')
        print('1. ADD GUEST DETAIL')
        print('2. SHOW DETAILS')

        
        choice4=int(input('ENTER YOUR CHOICE(1-2)'))
        print('\n================================================\n')
        if choice4==1:
            guest()
        if choice4==2:
            show_guest()
        


    if choice==4:
        break



        
print('THANK YOU!!!!!!')
            
            
