# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays(
    songplay_id int, 
    start_time timestamp, 
    user_id int, 
    level int, 
    song_id int, 
    artist_id int, 
    session_id int, 
    location varchar, 
    user_agent varchar
)
""")

user_table_create = ("""
create table if not exists users(
    user_id int, 
    first_name varchar,
    last_name varchar,
    gender varchar,
    level int
)
""")

song_table_create = ("""
create table if not exists songs(
    song_id int, 
    title varchar,
    artist_id int,
    year int,
    duration int
)
""")

artist_table_create = ("""
create table if not exists artists(
    artist_id int, 
    name varchar,
    location varchar,
    latitude int,
    longtitude int
)
""")

time_table_create = ("""
create table if not exists time(
    hour int, 
    day int,
    month int,
    year int,
    weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]