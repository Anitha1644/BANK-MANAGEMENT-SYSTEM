import mysql.connector
con=mysql.connector.connect(
    user='root',
    password='Anitha@1644',
    database='bankdb',
    host='localhost'
)

crsr=con.cursor()
query="""
          CREATE TABLE IF NOT EXISTS ACCOUNTS(ACC_NO INT PRIMARY KEY AUTO_INCREMENT,
                         NAME VARCHAR(20),BALANCE DECIMAL(10,2))
      """
crsr.execute(query)
con.commit()

def create_account():
    name=input("enter your name: ")
    balance=float(input("enter your initial balance: "))

    query= """
          INSERT INTO 
          ACCOUNTS(name,balance)
          values(%s,%s)
        """
    crsr.execute(query,(name,balance))
    con.commit()
    print("Account created successfully")

def deposit():
    acc_no = int(input('Enter your account number: '))
    amount = float(input('Enter your amount: '))

    if amount > 0:
        query = """
                    UPDATE ACCOUNTS
                    SET BALANCE = BALANCE + %s
                    WHERE ACC_NO = %s
                """

        crsr.execute(query,(amount,acc_no))
        con.commit()
        print('Amount Credited Seccussfully..!')
    else:
        print('Enter valid amount!')

def withdraw():
    acc_no = int(input('Enter your account number: '))
    amount = float(input('Enter your amount: '))

    query = """
                SELECT BALANCE
                FROM ACCOUNTS
                WHERE ACC_NO = %s
            """
    crsr.execute(query,(acc_no,))
    result = crsr.fetchone() # (5000,) // None
    if result != None:
        balance = result[0]
        if balance >= amount:
            query1 = """
                        UPDATE ACCOUNTS
                        SET BALANCE = BALANCE - %s
                        WHERE ACC_NO = %s
                     """
            crsr.execute(query1,(amount,acc_no))
            con.commit()
            print('Amount Debited Successfully..!')
        else:
            print('Insufficient Balanace')
    else:
        print('Account not Found')

def check_balance():
    acc_no = int(input('Enter your account number: '))

    query = """
                SELECT * FROM ACCOUNTS WHERE ACC_NO = %s
            """
    
    crsr.execute(query,(acc_no,))
    result = crsr.fetchone() # (1,Nayab,55000)
    con.commit()

    if result != None:
        print('------- Acount Details -------')
        print('Account Number:',result[0])
        print('Customer Name:',result[1])
        print('Balance:',result[2])
        print('------------------------------')
    else:
        print('Account not Found')

def money_transfer():
    sender = int(input("Enter sender's account number: "))
    receiver = int(input("Enter receiver's account number: "))
    amount = float(input('Enter your amount: '))

    query = """
                SELECT BALANCE
                FROM ACCOUNTS
                WHERE ACC_NO = %s
            """
    crsr.execute(query,(sender,))

    result = crsr.fetchone()

    try:
        if result != None:
            balance = result[0]
            if balance >= amount:
                query1 = """
                            UPDATE ACCOUNTS
                            SET BALANCE = BALANCE - %s
                            WHERE ACC_NO = %s
                        """
                crsr.execute(query1,(amount,sender))

                query2 = """
                            UPDATE ACCOUNTS
                            SET BALANCE = BALANCE + %s
                            WHERE ACC_NO = %s
                        """
                crsr.execute(query2,(amount,receiver))
                con.commit()
                print('Money Transfered Succussfully..!')
            else:
                print('Insufficient Balance')
        else:
            print('Account Not Found!')
    except Exception as e:
        con.rollback()
        print('Transaction Failed..!')
        print(e)

def delete_account():
    acc_no = int(input('Enter your account number: '))

    query = """
                DELETE FROM
                ACCOUNTS
                WHERE ACC_NO = %s
            """
    crsr.execute(query,(acc_no,))

if crsr.rowcount > 0:
        con.commit()
        print('Account Deleted Successfully..!')
else:
        print('Account Not Found!')

def view_all_accounts():
    query = """SELECT * FROM ACCOUNTS"""

    crsr.execute(query)
    rows = crsr.fetchall()

    print('<----- All Account Details ----->')
    for row in rows:
        print('\nAccount Number:',row[0])
        print('Customer Name:',row[1])
        print('Balance:',row[2])
        print('--------------------------')
    con.commit()

print('<========== BANK MANAGEMENT SYSTEM ==========>')

while True:
    print('\n1. CREATE ACCOUNT')
    print('2. DEPOSIT AMOUNT')
    print('3. WITHDRAW AMOUNT')
    print('4. CHECK BALANCE')
    print('5. MONEY TRANSFER')
    print('6. DELETE ACCOUNT')
    print('7. VIEW ALL ACCOUNTS')
    print('8. EXIT FROM APP')

    choice = int(input('Enter your choice: '))

    match (choice):
        case 1: create_account()
        case 2: deposit()
        case 3: withdraw()
        case 4: check_balance()
        case 5: money_transfer()
        case 6: delete_account()
        case 7: view_all_accounts()
        case 8:
            print('THANK YOU, VISIT AGAIN..!')
            break
        case _: print('Invaid Choice..!')