def create_db(cursor):
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT, categoryName TEXT, siteName TEXT, userID INTEGER, FOREIGN KEY(userID) REFERENCES user(id));
    CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, master_password TEXT);
    """)


def save_password(cursor, value, categoryName, siteName, userID):
    cursor.execute("""
    INSERT INTO password (value, categoryName, siteName, userID) VALUES (? , ? , ? , ?);
    """, (value, categoryName, siteName, userID))


def create_user_bdd(cursor, username, password):
    cursor.execute("""
    INSERT INTO user (username, master_password) VALUES (?, ?);
    """, (username, password))


def get_user_bdd(cursor, username, password):
    cursor.execute("""
    SELECT username, master_password FROM user WHERE username = ? AND master_password = ?;
    """, (username, password))
    return cursor.fetchone()
