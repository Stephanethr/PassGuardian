import os
import sqlite3

class ConnexionDB:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect_db()

    def get_cursor(self):
        return self.cursor

    def get_conn(self):
        return self.conn

    def connect_db(self):
        # Construire le chemin vers la base de données
        database_folder = os.path.join(os.path.dirname(__file__), "../database")
        database_path_file = os.path.join(database_folder, "passGuardian.db")

        # Vérifier si le dossier database existe, sinon le créer
        if not os.path.exists(database_folder):
            os.makedirs(database_folder)

        # Vérifier si la base de données existe sinon la créer
        if not os.path.exists(database_path_file):
            # Si la base de données n'existe pas, créer la base de données et la structure de table
            self.conn = sqlite3.connect(database_path_file)
            self.cursor = self.conn.cursor()
            self.create_db()

            self.conn.commit()

        # Connexion à la base de données
        self.conn = sqlite3.connect(database_path_file)
        self.cursor = self.conn.cursor()

    def create_db(self):
        self.cursor.executescript("""
        CREATE TABLE IF NOT EXISTS password (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT, categoryName TEXT, siteName TEXT, userID INTEGER, iv TEXT, tag TEXT, FOREIGN KEY(userID) REFERENCES user(id));
        CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, master_password TEXT);
        """)
        self.conn.commit()
