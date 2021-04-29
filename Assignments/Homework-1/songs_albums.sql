/*
 * TODO: Create a table called 'songs' that has the following fields:
 * - id - integer, primary key
 * - name - string
 * - album_id - foreign key
 * 
 * Note that album - song is a one-to-many relationship, so no bridge table is needed.
 */

CREATE TABLE Songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_name VARCHAR(70) NOT NULL,
    album_id VARCHAR(70) NOT NULL,
    FOREIGN KEY (album_id) REFERENCES Albums(id)
);


CREATE TABLE Albums (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    album_name name VARCHAR(70) NOT NULL,
    artist VARCHAR(70) NOT NULL,
    year_published INTEGER NOT NULL
);


/* 
 * TODO: Insert at least 4 rows of data into the songs table. You can change up the albums as well. :)
 */
 
INSERT INTO Songs
    (song_name, album_id)
VALUES
    ('Speak to Me / Breathe', 1)
    ('Come Together', 2),
    ('New Kid In Town', 3),
    ('Cover Me', 4)
;

INSERT INTO Albums
    (album_name, artist, year_published)
VALUES
    ('The Dark Side of the Moon', 'Pink Floyd', 1973),
    ('Abbey Road', 'The Beatles', 1969),
    ('Hotel California', 'Eagles', 1976),
    ('Born in the U.S.A.', 'Bruce Springsteen', 1984),
    ('California', 'Blink-182', 2016)
;



/* Required to get result in column format */
.headers on
.mode column


/* Queries */

-- SELECT * FROM Songs;
SELECT * FROM Songs;
SELECT * FROM Albums;

/* 
 * TODO: Write a table join query to construct a table of Song Name : Album Name
 */

SELECT Songs.song_name, Albums.album_name FROM Albums
JOIN Songs ON Albums.id = Songs.album_id
;
/*
 * TODO: Find all albums published between 1970 and 1980.
 */
 SELECT * FROM Albums
 WHERE year_published <= 1980 and year_published >= 1970
 ;

/*
 * TODO: Find all songs on albums published between 1970 and 1980. 
 *(Hint: Use a table join.)
 */
  SELECT Songs.song_name, Albums.album_name, Albums.year_published FROM Albums
 JOIN Songs ON Albums.id = Songs.album_id
 WHERE year_published <= 1980 and year_published >= 1970
 ;

/*
 * TODO: Find all songs on albums with names containing 'California'.
 */
 SELECT * FROM Songs
 JOIN Albums ON Songs.album_id = Albums.id
 WHERE Albums.album_name  LIKE '%California'