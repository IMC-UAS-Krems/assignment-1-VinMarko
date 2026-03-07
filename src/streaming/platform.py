"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from __future__ import annotations

from src.streaming.albums import Album
from src.streaming.artists import Artist
from src.streaming.playlists import Playlist
from src.streaming.sessions import ListeningSession
from src.streaming.tracks import Track
from src.streaming.users import User


class StreamingPlatform:

    def __init__(self, name:str, _catalogue, _users, _artists, _albums, _playlists, _sessions):
        self.name = name
        self._catalogue = dict[str,Track]
        self._users = dict[str,User]
        self._artists = dict[str,Artist]
        self._albums = dict[str,Album]
        self._playlists = dict[str,Playlist]
        self._sessions = list[ListeningSession]


    def add_track(track):
        pass

    def add_user(user):
        pass

    def add_artist(artist):
        pass

    def add_album(album):
        pass

    def add_playlist(playlist):
        pass

    def record_session(session):
        pass

    def get_track(track_id) -> Track | None:
        pass

    def get_user(user_id) -> User | None:
        pass

    def get_artist(artist_id) -> Artist | None:
        pass

    def get_album(album_id) -> Album | None:
        pass

    def all_users(self) -> list[User]:
        pass

    def all_tracks(self) -> list[Track]:
        pass



