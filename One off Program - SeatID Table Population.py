from SQLServerAccess import *

max_rows = 10
max_columns = 20

if __name__ == "__main__":
    import sys

    db_connection = SQLServerAccess()
    db_connection.open()
    for row in range(0, 10):
        for column in range(0, 20):
            ID = (row * max_columns) + column
            SQLStatement = "INSERT INTO tSeats VALUES("+str(ID)+")"
            db_connection.execute(SQLStatement)
            db_connection.commit() # write the data...
    db_connection.close()


