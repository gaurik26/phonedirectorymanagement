CREATE DATABASE PhoneDirectoryDB;
GO
USE PhoneDirectoryDB;
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Contacts' AND xtype='U')
CREATE TABLE Contacts (
    ContactID INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100),
    PhoneNumber NVARCHAR(15),
    Email NVARCHAR(100)
);
INSERT INTO Contacts (Name, PhoneNumber, Email)
VALUES ('Gauri Kadlag', '9527534263', 'gaurikadlag@gmail.com');
UPDATE Contacts
SET Name = 'New Name', PhoneNumber = '1234567890', Email = 'newemail@example.com'
WHERE ContactID = 1;
DELETE FROM Contacts WHERE ContactID = 1;

SELECT * FROM Contacts;