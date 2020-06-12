import mysql.connector
from mysql.connector import Error
import gui

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='ToDo',
                                       user='root',
                                       password='Bhavya123!@#')
        if conn.is_connected():
            print('Connected to MySQL database')
            gui.GUI(conn)
            #ToDoList.delete_activity(conn , id )
            #ToDoList.add_activity(conn , "book", "2020-06-12", "2020-06-15")
            
    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
