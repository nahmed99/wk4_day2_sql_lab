import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()


symbol = Artist("AFKAP")
artist_repository.save(symbol)

mj = Artist("Michael Jackson")
artist_repository.save(mj)

big_wall = Album("On the wall", mj, "how should I know!")
album_repository.save(big_wall)

polyfilla = Album("Gorilla", mj, "Scary song")
album_repository.save(polyfilla)


purple = Album("Raining outside", symbol, "Purple bridge")
album_repository.save(purple)


pdb.set_trace()