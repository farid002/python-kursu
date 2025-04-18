# https://sqliteonline.com/
"""
CREATE TABLE
INSERT INTO
SELECT
UPDATE
DELETE

WHERE
IN
ORDER BY
ASC
DESC
GROUP BY
LIMIT

INTEGER
TEXT
PRIMARY KEY
"""

"""
CREATE TABLE IF NOT EXISTS posts (
  id TEXT PRIMARY KEY,
  header TEXT,
  body TEXT NOT NULL
);

INSERT INTO posts (id, header, body) VALUES (15, 'aa', 'bodyy');
INSERT INTO posts (id, header, body) VALUES (16, 'as', 'd');
INSERT INTO posts (id, header, body) VALUES (17, 'SAD', 'boddyy');
INSERT INTO posts (id, header, body) VALUES (18, 'AS', 'bosddyy');
INSERT INTO posts (id, header, body) VALUES (19, 'ASD', 'as');
INSERT INTO posts (header, body) VALUES ('D', 'boddyy');

SELECT * FROM posts;

UPDATE posts SET body = 'asdsd' WHERE header = 'AS';

DELETE FROM posts WHERE header = 'AS';

SELECT DISTINCT header FROM posts;

SELECT * FROM posts ORDER BY header DESC;

SELECT header, COUNT(*) AS post_count FROM posts GROUP BY header;
"""

"""
import sqlite3

# Qoşul
conn = sqlite3.connect('telebeler.db')
cursor = conn.cursor()

# Cədvəl yarat
cursor.execute('''
CREATE TABLE IF NOT EXISTS telebeler (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    yas INTEGER
)
''')

# Məlumat əlavə et
cursor.execute('INSERT INTO telebeler (ad, yas) VALUES (?, ?)', ('Anar', 22))

# Məlumat oxu
cursor.execute('SELECT * FROM telebeler')
for satir in cursor.fetchall():
    print(satir)

# Bağla
conn.commit()
conn.close()
"""

import sqlite3

# Qoşul
conn = sqlite3.connect('telebeler.db')
cursor = conn.cursor()

# Cədvəl yarat
cursor.execute('''
CREATE TABLE IF NOT EXISTS telebeler (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    yas INTEGER
)
''')

# Məlumat əlavə et
cursor.execute('INSERT INTO telebeler (ad, yas) VALUES (?, ?)', ('Anar', 22))

# Məlumat oxu
cursor.execute('SELECT * FROM telebeler')
for satir in cursor.fetchall():
    print(satir)

# Bağla
conn.commit()
conn.close()
