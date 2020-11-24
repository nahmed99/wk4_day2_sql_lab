from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album


def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)

    return albums


def select(id):
    album = None
    sql = "SELECT * FROM album WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist_id = result['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(result['title'], artist, result['genre'], result['id'])

    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)