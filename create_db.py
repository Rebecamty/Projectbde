import sqlite3
import os
print("Current working directory:", os.getcwd())

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the tables
cursor.execute('''
    CREATE TABLE Persoana (
        Cod_Cititor INTEGER PRIMARY KEY,
        Nume TEXT,
        Prenume TEXT,
        Adresa TEXT,
        Data_nasterii TEXT,
        Student INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE fisa (
        Cod_cititor INTEGER,
        Cod_carte TEXT,
        Data_imprumut TEXT,
        Data_retur TEXT,
        Penalizari INTEGER,
        FOREIGN KEY (Cod_cititor) REFERENCES Persoana(Cod_Cititor),
        FOREIGN KEY (Cod_carte) REFERENCES carte(Cod_carte)
    )
''')

cursor.execute('''
    CREATE TABLE carte (
        Cod_carte TEXT PRIMARY KEY,
        Titlu TEXT,
        Categorie TEXT,
        Autor TEXT
    )
''')

# Insert sample data into the tables
cursor.execute('''
    INSERT INTO Persoana (Cod_Cititor, Nume, Prenume, Adresa, Data_nasterii, Student)
    VALUES (1, 'Doe', 'John', '123 Main St', '1990-01-01', 0)
''')

cursor.execute('''
    INSERT INTO carte (Cod_carte, Titlu, Categorie, Autor)
    VALUES ('ABC123', 'Book Title', 'Fiction', 'John Author')
''')

cursor.execute('''
    INSERT INTO fisa (Cod_cititor, Cod_carte, Data_imprumut, Data_retur, Penalizari)
    VALUES (1, 'ABC123', '2023-05-20', '2023-06-03', 0)
''')

# Insert more sample data into the tables
cursor.execute('''
    INSERT INTO Persoana (Cod_Cititor, Nume, Prenume, Adresa, Data_nasterii, Student)
    VALUES (2, 'Smith', 'Jane', '456 Elm St', '1995-03-15', 1)
''')

cursor.execute('''
    INSERT INTO carte (Cod_carte, Titlu, Categorie, Autor)
    VALUES ('DEF456', 'Another Book', 'Non-Fiction', 'Jane Author')
''')

cursor.execute('''
    INSERT INTO fisa (Cod_cititor, Cod_carte, Data_imprumut, Data_retur, Penalizari)
    VALUES (2, 'DEF456', '2023-05-25', '2023-06-08', 1)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
