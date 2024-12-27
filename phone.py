import pyodbc

# Function to connect to the SQL Server database
def connect_to_database():
    try:
        # Connection string for SQL Server
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"  # Update with your server name if different
            "DATABASE=PhoneDirectoryDB;"
            "Trusted_Connection=yes;"
        )
        print("Connected to the SQL Server database successfully!")
        return connection
    except Exception as e:
        print("Failed to connect to the database:", e)
        exit()

# Example function to create a table
def create_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Contacts' AND xtype='U')
        CREATE TABLE Contacts (
            ContactID INT IDENTITY(1,1) PRIMARY KEY,
            Name NVARCHAR(100),
            PhoneNumber NVARCHAR(15),
            Email NVARCHAR(100)
        );
    """)
    connection.commit()
    print("Table created successfully!")
    connection.close()

# Function to insert data into the table
def insert_contact(name, phone, email):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Contacts (Name, PhoneNumber, Email) VALUES (?, ?, ?)
    """, (name, phone, email))
    connection.commit()
    print(f"Contact '{name}' added successfully!")
    connection.close()

# Function to fetch and display all contacts
def fetch_contacts():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Contacts;")
    rows = cursor.fetchall()
    print("\nContactID\tName\t\tPhoneNumber\t\tEmail")
    for row in rows:
        print(f"{row.ContactID}\t\t{row.Name}\t\t{row.PhoneNumber}\t\t{row.Email}")
    connection.close()

# Function to edit an existing contact
def edit_contact(contact_id, name, phone, email):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Contacts
        SET Name = ?, PhoneNumber = ?, Email = ?
        WHERE ContactID = ?
    """, (name, phone, email, contact_id))
    connection.commit()
    print(f"Contact ID {contact_id} updated successfully!")
    connection.close()

# Function to delete a contact
def delete_contact(contact_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM Contacts WHERE ContactID = ?
    """, (contact_id,))
    connection.commit()
    print(f"Contact ID {contact_id} deleted successfully!")
    connection.close()

# Main program
def main():
    create_table()
    while True:
        print("\nPhone Directory Menu:")
        print("1. Add a Contact")
        print("2. View All Contacts")
        print("3. Edit a Contact")
        print("4. Delete a Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            insert_contact(name, phone, email)
        elif choice == "2":
            fetch_contacts()
        elif choice == "3":
            contact_id = int(input("Enter ContactID to edit: "))
            name = input("Enter new Name: ")
            phone = input("Enter new Phone Number: ")
            email = input("Enter new Email: ")
            edit_contact(contact_id, name, phone, email)
        elif choice == "4":
            contact_id = int(input("Enter ContactID to delete: "))
            delete_contact(contact_id)
        elif choice == "5":
            print("Exiting Phone Directory. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
