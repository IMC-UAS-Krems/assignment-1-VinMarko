"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""
from streaming.tracks import Track
from streaming.users import User


class Playlist :

    def __init__(self, playlist_id:str, name:str, owner: User, tracks: list[Track] | None = None):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = list(tracks) if tracks is not None else []


    def add_track(self, track: Track) -> None:
        self.tracks.append(track)

    def remove_track(self,track_id: str) -> None:
        for track in self.tracks:
            if track.track_id == track_id:
                self.tracks.remove(track)
                return


    def total_duration_seconds(self) -> int:
        return sum(track.duration_seconds for track in self.tracks)



class CollaborativePlaylist(Playlist):

    def __init__( self, playlist_id: str, name: str, owner: User, contributors: list[User],tracks: list[Track] | None = None):
        super().__init__(playlist_id, name, owner, tracks)
        self.contributors = list(contributors)


    def add_contributor(self,user: User) -> None:
            self.contributors.append(user)

    def remove_contributor(self,user: User) -> None:
        if user in self.contributors:
            self.contributors.remove(user)










