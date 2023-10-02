"""Query the database"""

import sqlite3

import sqlite3

def query_bottom_5():
    """Query the database for the bottom 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    # Use ORDER BY to sort the rows in reverse order by the primary key (assuming there's a primary key column)
    # and LIMIT to get the bottom 5 rows.
    cursor.execute("SELECT * FROM GroceryDB ORDER BY primary_key_column DESC LIMIT 5")
    print("Bottom 5 rows of the GroceryDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"



