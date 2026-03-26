import sqlite3

# Conecta ao arquivo (ele vai criar se não existir)
conn = sqlite3.connect("musicas.sqlite")
cur = conn.cursor()

# 1. Limpa tudo para não dar erro de "já existe"
cur.executescript(
    """
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
);

CREATE TABLE Album (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title       TEXT
);

CREATE TABLE Track (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT,
    album_id    INTEGER,
    genre_id    INTEGER,
    len         INTEGER, rating INTEGER, count INTEGER
);
"""
)

# 2. Insere os Dados (Seguindo a ordem hierárquica)
cur.execute("INSERT INTO Artist (name) VALUES (?)", ("Led Zeppelin",))
artist_id = cur.lastrowid  # Pega o ID 1 automaticamente

cur.execute("INSERT INTO Genre (name) VALUES (?)", ("Rock",))
genre_id = cur.lastrowid

cur.execute("INSERT INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, "IV"))
album_id = cur.lastrowid

cur.execute(
    """INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES (?, ?, ?, ?, ?, ?)""",
    ("Black Dog", 5, 297, 0, album_id, genre_id),
)

conn.commit()
print("✅ Banco de Dados Criado e Dados Inseridos com Sucesso!")

# 3. Fazendo o JOIN (A mágica que junta as tabelas)
print("\n--- Resultado do JOIN ---")
sqlstr = """
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track 
JOIN Artist JOIN Album JOIN Genre 
    ON Track.album_id = Album.id 
    AND Album.artist_id = Artist.id 
    AND Track.genre_id = Genre.id
"""

for row in cur.execute(sqlstr):
    print(f"Música: {row[0]} | Artista: {row[1]} | Álbum: {row[2]} | Gênero: {row[3]}")

cur.close()
