"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""



class Playlist :

    def __init__(self, playlist_id:str, name:str, owner, tracks: list[Track]):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
        self.tracks = tracks


    def add_track(self,track):
        return self.tracks.append(track)

    def remove_track(self,track_id):
        for track in self.tracks:
            if track.track_id == track_id:
                self.tracks.remove(track)
                return


    def total_duration_seconds(self) -> int:
        return sum(track.duration_seconds for track in self.tracks)



class CollaborativePlaylist(Playlist):

    def __init__(self, contributors: list[str]):

        super().__init__(playlist_id="", name="", owner="", tracks=[])
        self.contributors = contributors

    def add_contributor(self,user):
        return self.contributors.append(user)

    def remove_contributor(self,user):
        if user in self.contributors:
            self.contributors.remove(user)










