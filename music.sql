CREATE TABLE [IF NOT EXISTS] Artist (artist_id integer PRIMARY KEY, artist_name TEXT NOT NULL)
CREATE TABLE Album (album_id integer PRIMARY KEY, album_name TEXT NOT NULL, artist_id integer)
CREATE TABLE Song (song_id integer PRIMARY KEY, song_name TEXT NOT NULL, track_number integer, duration integer, artist_id integer, album_id integer)