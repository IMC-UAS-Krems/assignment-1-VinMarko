"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
from collections import defaultdict
from datetime import datetime, timezone, timedelta

from streaming.tracks import Track, Song
from streaming.users import User, PremiumUser, FamilyMember
from streaming.artists import Artist
from streaming.albums import Album
from streaming.playlists import Playlist, CollaborativePlaylist
from streaming.sessions import ListeningSession


class StreamingPlatform:

    def __init__(self, name: str):
        self.name = name
        self._catalogue: dict[str, Track] = {}
        self._users: dict[str, User] = {}
        self._artists: dict[str, Artist] = {}
        self._albums: dict[str, Album] = {}
        self._playlists: dict[str, Playlist] = {}
        self._sessions: list[ListeningSession] = []

    def add_track(self, track: Track) -> None:
        self._catalogue[track.track_id] = track

    def add_user(self, user: User) -> None:
        self._users[user.user_id] = user

    def add_artist(self, artist: Artist) -> None:
        self._artists[artist.artist_id] = artist

    def add_album(self, album: Album) -> None:
        self._albums[album.album_id] = album

    def add_playlist(self, playlist: Playlist) -> None:
        self._playlists[playlist.playlist_id] = playlist

    def record_session(self, session: ListeningSession) -> None:
        self._sessions.append(session)
        session.user.add_session(session)

    def get_track(self, track_id: str) -> Track | None:
        return self._catalogue.get(track_id)

    def get_user(self, user_id: str) -> User | None:
        return self._users.get(user_id)

    def get_artist(self, artist_id: str) -> Artist | None:
        return self._artists.get(artist_id)

    def get_album(self, album_id: str) -> Album | None:
        return self._albums.get(album_id)

    def all_users(self) -> list[User]:
        return list(self._users.values())

    def all_tracks(self) -> list[Track]:
        return list(self._catalogue.values())



    #Query Methods

    # Q1: Total Cumulative Listening Time
    #returns total listening time from all sessions in start- end
    def total_listening_time_minutes(self, start: datetime, end: datetime) -> float:
        total_seconds = sum(
            s.duration_listened_seconds
            for s in self._sessions
            if start <= s.timestamp <= end
        )
        return total_seconds / 60.0

    # Q2: Average Unique Tracks per Premium User
    #avg number of distinct tracks listened by PremiumUser
    def avg_unique_tracks_per_premium_user(self, days: int = 30) -> float:

        if self._sessions and self._sessions[0].timestamp.tzinfo is not None:
            cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        else:
            cutoff = datetime.now() - timedelta(days=days)



        premium_users = [u for u in self._users.values() if isinstance(u, PremiumUser)]
        if not premium_users:
            return 0.0

        total_unique = 0
        for user in premium_users:
            unique_tracks = {
                s.track.track_id
                for s in user.sessions
                if s.timestamp >= cutoff
            }
            total_unique += len(unique_tracks)

        return total_unique / len(premium_users)





    # Q3: Track with Most Distinct Listeners
    #Returns the track with the highest number of distinct listeners
    def track_with_most_distinct_listeners(self) -> Track | None:
        if not self._sessions:
            return None

        listeners_per_track: dict[str, set[str]] = defaultdict(set)
        for s in self._sessions:
            listeners_per_track[s.track.track_id].add(s.user.user_id)

        best_track_id = max(listeners_per_track, key=lambda tid: len(listeners_per_track[tid]))
        return self._catalogue.get(best_track_id)




    # Q4: Average Session Duration by User Type
    #Avg session duration(secs) per user subtype from longest to shortest

    def avg_session_duration_by_user_type(self) -> list[tuple[str, float]]:
        durations_by_type: dict[str, list[int]] = defaultdict(list)
        for s in self._sessions:
            type_name = type(s.user).__name__
            durations_by_type[type_name].append(s.duration_listened_seconds)

        result = [
            (type_name, sum(durs) / len(durs))
            for type_name, durs in durations_by_type.items()
        ]
        result.sort(key=lambda x: x[1], reverse=True)
        return result



    # Q5: Total Listening Time for Underage Sub-Users
    # Total listening time min - for FamilyMember, sub accounts under 18
    def total_listening_time_underage_sub_users_minutes(self, age_threshold: int = 18) -> float:
        total_seconds = sum(
            s.duration_listened_seconds
            for s in self._sessions
            if isinstance(s.user, FamilyMember) and s.user.age < age_threshold
        )
        return total_seconds / 60.0




    # Q6: Top Artists by Listening Time

    def top_artists_by_listening_time(self, n: int = 5) -> list[tuple[Artist, float]]:
        minutes_by_artist: dict[str, float] = defaultdict(float)
        for s in self._sessions:
            if isinstance(s.track, Song):
                artist_id = s.track.artist.artist_id
                minutes_by_artist[artist_id] += s.duration_listened_seconds / 60.0

        artist_totals = [
            (self._artists[aid], mins)
            for aid, mins in minutes_by_artist.items()
            if aid in self._artists
        ]
        artist_totals.sort(key=lambda x: x[1], reverse=True)
        return artist_totals[:n]



    # Q7: User's Top Genre
    def user_top_genre(self, user_id: str) -> tuple[str, float] | None:
        user = self._users.get(user_id)
        if user is None or not user.sessions:
            return None

        seconds_by_genre: dict[str, int] = defaultdict(int)
        for s in user.sessions:
            seconds_by_genre[s.track.genre] += s.duration_listened_seconds

        total = sum(seconds_by_genre.values())
        if total == 0:
            return None

        top_genre = max(seconds_by_genre, key=lambda g: seconds_by_genre[g])
        percentage = (seconds_by_genre[top_genre] / total) * 100.0
        return top_genre, percentage



    # Q8: Collaborative Playlists with Many Artists
    def collaborative_playlists_with_many_artists(self, threshold: int = 3) -> list[CollaborativePlaylist]:
        result = []
        for playlist in self._playlists.values():
            if not isinstance(playlist, CollaborativePlaylist):
                continue
            distinct_artists = {
                track.artist.artist_id
                for track in playlist.tracks
                if isinstance(track, Song)
            }
            if len(distinct_artists) > threshold:
                result.append(playlist)
        return result



    # Q9: Average Tracks per Playlist Type

    #Avg number of tracks per PlayList and CollaborativePlaylist

    def avg_tracks_per_playlist_type(self) -> dict[str, float]:
        standard_counts = []
        collab_counts = []

        for playlist in self._playlists.values():
            if isinstance(playlist, CollaborativePlaylist):
                collab_counts.append(len(playlist.tracks))
            else:
                standard_counts.append(len(playlist.tracks))

        return {
            "Playlist": sum(standard_counts) / len(standard_counts) if standard_counts else 0.0,
            "CollaborativePlaylist": sum(collab_counts) / len(collab_counts) if collab_counts else 0.0,
        }


    # Q10: Users Who Completed Albums
    #Return user, album_titles for users who listened to every track on at least one album.
    def users_who_completed_albums(self) -> list[tuple[User, list[str]]]:
        listened: dict[str, set[str]] = defaultdict(set)
        for s in self._sessions:
            listened[s.user.user_id].add(s.track.track_id)

        result = []
        for user in self._users.values():
            user_tracks = listened.get(user.user_id, set())
            completed_titles = [
                album.title
                for album in self._albums.values()
                if album.track_ids() and album.track_ids().issubset(user_tracks)
            ]
            if completed_titles:
                result.append((user, completed_titles))

        return result

