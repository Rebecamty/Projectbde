import sqlite3

def display_client_information():
    reader_code = input("Enter the reader code: ")

    try:
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()

        cursor.execute("SELECT Cod_Cititor, Nume, Prenume FROM Persoana WHERE Cod_Cititor=?", (reader_code,))
        client_data = cursor.fetchone()

        if client_data is not None:
            print("Client Information:")
            print("Code:", client_data[0])
            print("Name:", client_data[1])
            print("Surname:", client_data[2])
            print()
        else:
            print("Client not found in the database.")

        connection.close()
    except sqlite3.Error as e:
        print("Error executing display_client_information():", e)

def calculate_penalties():
    try:
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Persoana.Cod_Cititor,
                   CASE
                       WHEN Persoana.Student = 1 AND julianday('now') - julianday(fisa.Data_Retur) > 28 THEN 1
                       WHEN Persoana.Student = 0 AND julianday('now') - julianday(fisa.Data_Retur) > 14 THEN
                           julianday('now') - julianday(fisa.Data_Retur) - 14
                       ELSE 0
                   END AS Penalizari
            FROM Persoana
            INNER JOIN fisa ON Persoana.Cod_Cititor = fisa.Cod_Cititor
            WHERE julianday('now') - julianday(fisa.Data_Retur) > 14 OR Persoana.Student = 1;
        """)
        penalties = cursor.fetchall()

        connection.close()

        print("Penalties:")
        for row in penalties:
            print("Reader Code:", row[0])
            print("Penalties:", row[1])
            print()
    except sqlite3.Error as e:
        print("Error executing calculate_penalties():", e)

def display_top_book_lovers():
    try:
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Persoana.Cod_Cititor,
                   Persoana.Nume,
                   Persoana.Prenume,
                   COUNT(fisa.Cod_Carte) AS Numar_Carti_Citite
            FROM Persoana
            INNER JOIN fisa ON Persoana.Cod_Cititor = fisa.Cod_Cititor
            WHERE DATE(fisa.Data_Retur) = DATE('now')
            GROUP BY Persoana.Cod_Cititor
            ORDER BY Numar_Carti_Citite DESC;
        """)
        top_book_lovers = cursor.fetchall()

        connection.close()

        print("Top Book Lovers:")
        for row in top_book_lovers:
            print("Reader Code:", row[0])
            print("Name:", row[1])
            print("Surname:", row[2])
            print("Number of Books Read:", row[3])
            print()
    except sqlite3.Error as e:
        print("Error executing display_top_book_lovers():", e)

def display_most_read_books():
    try:
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT carte.Titlu,
                   carte.Autor,
                   COUNT(fisa.Cod_Carte) AS Aparitii
            FROM carte
            INNER JOIN fisa ON carte.Cod_Carte = fisa.Cod_Carte
            WHERE DATE(fisa.Data_Retur) = DATE('now')
            GROUP BY carte.Cod_Carte
            ORDER BY Aparitii DESC;
        """)
        most_read_books = cursor.fetchall()

        connection.close()

        print("Most Read Books:")
        for row in most_read_books:
            print("Title:", row[0])
            print("Author:", row[1])
            print("Occurrences:", row[2])
            print()
    except sqlite3.Error as e:
        print("Error executing display_most_read_books():", e)

def display_category_statistics():
    try:
        connection = sqlite3.connect("library.db")
        cursor = connection.cursor()

        cursor.execute("""
            SELECT carte.Categorie,
                   AVG(strftime('%Y', 'now') - strftime('%Y', Persoana.Data_nasterii)) AS Medie_Varsta,
                   COUNT(DISTINCT fisa.Cod_Carte) AS Numar_Carti_Imprumutate,
                   AVG(julianday(fisa.Data_Retur) - julianday(fisa.Data_Imprumut)) AS Medie_Zile_Citire
            FROM carte
            INNER JOIN fisa ON carte.Cod_Carte = fisa.Cod_Carte
            INNER JOIN Persoana ON fisa.Cod_Cititor = Persoana.Cod_Cititor
            GROUP BY carte.Categorie
            ORDER BY Medie_Varsta DESC;
        """)
        category_statistics = cursor.fetchall()

        connection.close()

        print("Category Statistics:")
        for row in category_statistics:
            print("Category:", row[0])
            print("Average Age:", row[1])
            print("Number of Books Borrowed:", row[2])
            print("Average Reading Days:", row[3])
            print()
    except sqlite3.Error as e:
        print("Error executing display_category_statistics():", e)

while True:
    print("Library Management System")
    print("1. Display Client Information")
    print("2. Calculate Penalties")
    print("3. Display Top Book Lovers")
    print("4. Display Most Read Books")
    print("5. Display Category Statistics")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_client_information()
    elif choice == "2":
        calculate_penalties()
    elif choice == "3":
        display_top_book_lovers()
    elif choice == "4":
        display_most_read_books()
    elif choice == "5":
        display_category_statistics()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
