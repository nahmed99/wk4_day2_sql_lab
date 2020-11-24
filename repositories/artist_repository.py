from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values) 
    id = results[0]['id'] 
    artist.id = id
    return artist


def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)


    for row in results:
     
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists 