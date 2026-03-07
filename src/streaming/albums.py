"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
from src.streaming.tracks import AlbumTrack


class Album :

    def __init__(self, album_id:str, title:str, artist, release_year:int, tracks):

        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.tracks = list[AlbumTrack]

    def add_track(track) -> None:
        pass



    def track_ids(self) -> set[str]:
        return self.track_ids()
    def duration_seconds(self) ->int:
        return sum(track.duration_seconds for track in self.tracks)





