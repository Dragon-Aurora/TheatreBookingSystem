from SQLServerAccess import *

max_rows = 10
max_columns = 20

if __name__ == "__main__":
    import sys

    db_connection = SQLServerAccess()
    # db_connection.open()
    for row in range(0, 10):
        for column in range(0, 20):
            ID = (row * max_columns) + column
            print(ID)
            # db_connection.execute("INSERT INTO tSeats values("+str(ID)+")")
