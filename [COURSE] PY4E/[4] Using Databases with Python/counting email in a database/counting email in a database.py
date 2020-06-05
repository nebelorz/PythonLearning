# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Delete table if exists
cur.execute('DROP TABLE IF EXISTS Counts')
# Create table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Defining and opening the file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
file = open(fname)

# Searching for the emails
for line in file:
    if not line.startswith('From: '):
        continue
    split = line.split()
    # Searching the organization
    split_org = split[1].split('@')
    org = split_org[1]

    # Working with the DB
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    # Check if it doesn't exist, then create it
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    # If it exists, update it
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
# Save
conn.commit()

# Reading top 10 organizations by count
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
