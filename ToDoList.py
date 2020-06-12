from mysql.connector import Error

def add_activity(conn , activity , start_date , due_date):
    query = "INSERT INTO Activity(activity , start_date , due_date) " \
            "VALUES(%s,%s,%s)"
    args = (activity , start_date , due_date)
 
    try:
        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        
        
        
        
def delete_activity(conn , id ):
    query = "DELETE FROM Activity WHERE id = %s"
    args = (id,)
    
    try:
        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        
        
        
        
def pending_activities(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Activity")
        rows = cursor.fetchall()

        return rows

    except Error as e:
        print(e)

    finally:
        cursor.close()
        



