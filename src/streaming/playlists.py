"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""


class Playlist :

    def __init__(self, playlist_id:str, name:str, owner, tracks):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = tracks


    def add_track(track):
        pass

    def remove_track(track_id):
        pass


    def total_duration_seconds(self) -> int:
        return 0



class CollaborativePlaylist(Playlist):

    def __init__(self, contributors):

        super().__init__(playlist_id="", name="", owner="", tracks=[])
        self.contributors = contributors

    def add_contributor(user):
        pass

    def remove_contributor(user):
        pass










