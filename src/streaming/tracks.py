"""
tracks.py
---------
Implement the class hierarchy for all playable content on the platform.

Classes to implement:
  - Track (abstract base class)
    - Song
      - SingleRelease
      - AlbumTrack
    - Podcast
      - InterviewEpisode
      - NarrativeEpisode
    - AudiobookTrack
"""
import datetime
from typing import Optional

from src.streaming.albums import Album
from src.streaming.artists import Artist


class Track:

    def __init__(self, track_id:str, title:str, duration_seconds:int, genre:str):
        self.track_id = track_id
        self.title = title
        self.duration_seconds = duration_seconds
        self.genre = genre

    def duration_minutes(self) -> float:
        return self.duration_seconds / 60




class Song(Track):
    def __init__(self,artist):
        super().__init__(track_id="", title="", duration_seconds=0, genre="")
        self.artist = artist


class Podcast(Track):
    def __init__(self, host:str, descrtiption:str):
        super().__init__(track_id="", title="", duration_seconds=0, genre="")
        self.host = host
        self.description = descrtiption



class AudiobookTrack(Track):
    def __init__(self, author:str, narrator:str):
        super().__init__(track_id="", title="", duration_seconds=0, genre="")
        self.author = author
        self.narrator = narrator



class AlbumTrack(Song):
    def __init__(self, track_number:int, album):
        super().__init__(artist=album.artist)
        self.track_number = track_number
        self.album = Optional[Album]



class SingleRelease(Song):
    def __init__(self, release_date):
        super().__init__(artist=None)
        self.release_date = release_date


class NarrativeEpisode(Podcast):
    def __init__(self, season:int, episode_number:int):
        super().__init__(host="", descrtiption="")
        self.season = season
        self.episode_number = episode_number



class InterviewEpisode(Podcast):
    def __init__(self, guest:str):
        super().__init__(host="", descrtiption="")
        self.guest = guest








