import mysql.connector
import streamlit as st

host = "localhost"
user = "root"
password = ""
database = "pharmacy"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

c = connection.cursor()

def cust_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Customers(
                    C_Name VARCHAR(50) NOT NULL,
                    C_Password VARCHAR(50) NOT NULL,
                    C_Email VARCHAR(50) PRIMARY KEY NOT NULL, 
                    C_State VARCHAR(50) NOT NULL,
                    C_Number VARCHAR(50) NOT NULL 
                    )''')
    print('Customer Table create Successfully')

def customer_add_data(Cname,Cpass, Cemail, Cstate,Cnumber):
    print('''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Number) VALUES(%s, %s, %s, %s, %s)''', (Cname, Cpass, Cemail, Cstate, Cnumber))
    c.execute('''INSERT INTO Customers (C_Name,C_Password,C_Email, C_State, C_Number) VALUES(%s, %s, %s, %s, %s)''', (Cname, Cpass, Cemail, Cstate, Cnumber))

def customer_view_all_data():
    st.subheader("Customer Details")
    c.execute('SELECT * FROM Customers')
    customer_data = c.fetchall()
    return customer_data
def customer_update(Cemail,Cnumber):
    c.execute(''' UPDATE Customers SET C_Number = %s WHERE C_Email = %s''', (Cnumber,Cemail,))
    connection.commit()
    print("Updating")
def customer_delete(Cemail):
    c.execute(''' DELETE FROM Customers WHERE C_Email = %s''', (Cemail,))
    connection.commit()

def drug_update(Duse, Did):
    c.execute(''' UPDATE Drugs SET D_Use = %s WHERE D_id = %s''', (Duse,Did))
    connection.commit()
def drug_delete(Did):
    c.execute(''' DELETE FROM Drugs WHERE D_id = %s''', (Did,))
    connection.commit()

def drug_create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS Drugs(
                D_Name VARCHAR(50) NOT NULL,
                D_ExpDate DATE NOT NULL, 
                D_Use VARCHAR(50) NOT NULL,
                D_Qty INT NOT NULL, 
                D_id INT PRIMARY KEY NOT NULL)
                ''')
    print('DRUG Table create Successfully')

def drug_add_data(Dname, Dexpdate, Duse, Dqty, Did):
    c.execute('''INSERT INTO Drugs (D_Name, D_Expdate, D_Use, D_Qty, D_id) VALUES(%s,%s,%s,%s,%s)''', (Dname, Dexpdate, Duse, Dqty, Did))
    connection.commit()

def drug_view_all_data():
    c.execute('SELECT * FROM Drugs')
    drug_data = c.fetchall()
    return drug_data

def order_create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
                O_Name VARCHAR(100) NOT NULL,
                O_Items VARCHAR(100) NOT NULL,
                O_Qty VARCHAR(100) NOT NULL,
                O_id VARCHAR(100) PRIMARY KEY NOT NULL)
    ''')

def order_delete(Oid):
    c.execute(''' DELETE FROM Orders WHERE O_id = %s''', (Oid,))

def order_add_data(O_Name,O_Items,O_Qty,O_id):
    c.execute('''INSERT INTO Orders (O_Name, O_Items,O_Qty, O_id) VALUES(%s,%s,%s,%s)''',
              (O_Name,O_Items,O_Qty,O_id))
    connection.commit()


def order_view_data(customername):

    c.execute('''SELECT * FROM ORDERS WHERE O_Name = %s''', (customername,))

    order_data = c.fetchall()
    return order_data

def order_view_all_data():
    c.execute('SELECT * FROM ORDERS')
    order_all_data = c.fetchall()
    return order_all_data


# @st.cache
def getauthenticate(username, password):
    c.execute('''SELECT C_Password FROM Customers WHERE C_Name = %s''', (username,))
    print('''SELECT C_Password FROM Customers WHERE C_Name = %s''', (username,))
    cust_password = c.fetchall()
    print(cust_password, "Outside password")
    print(password, "Parameter password")
    
    if cust_password[0][0] == password:
        return True
    else:
        return False
