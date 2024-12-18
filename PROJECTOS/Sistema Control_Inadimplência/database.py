# =========================
# database.py (Banco de Dados)
# =========================

import sqlite3

def connect_to_db(db_name="credit_data.db"):
    return sqlite3.connect(db_name)

def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS credit_data (
        name TEXT,
        ldday TEXT,
        lamount REAL,
        balprinc REAL,
        arrears REAL,
        days INTEGER,
        lastrepdate TEXT,
        PRIMARY KEY (name, ldday)
    )
    """

def update_database(data, connection):
     cursor = connection.cursor()
    for _, row in data.iterrows():
         cursor.execute(
             """
            INSERT INTO credit_data (name, ldday, lamount, balprinc, arrears, days, lastrepdate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(name, ldday) DO UPDATE SET
                lamount=excluded.lamount,
                balprinc=excluded.balprinc,
                arrears=excluded.arrears,
                days=excluded.days,
                lastrepdate=excluded.lastrepdate
            """,
            (
                row["name"],
                row["ldday"],
                row["lamount"],
                row["balprinc"],
                row["arrears"],
                row["days"],
                row["lastrepdate"],
            ),
        )

    connection.commit()
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()