import sqlite3
import json


if __name__ == "__main__":
    try:
        with open("test.db", "w") as f:
            f.write("")
    except Exception:
        open("test.db", "x")

    database_connection = sqlite3.connect("test.db")
    database_cursor = database_connection.cursor()
    
    with open("config/config.json") as config_file:
        json.load

