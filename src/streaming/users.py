"""

users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""
from datetime import date
from streaming.sessions import ListeningSession


class User:

    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        sessions: list[ListeningSession] | None = None
    ):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = list(sessions) if sessions is not None else []

    def add_session(self, session: ListeningSession) -> None:
        self.sessions.append(session)

    def total_listening_seconds(self) -> int:
        return sum(session.duration_listened_seconds for session in self.sessions)

    def total_listening_minutes(self) -> float:
        return self.total_listening_seconds() / 60

    def unique_tracks_listened(self) -> set[str]:
        return {session.track.track_id for session in self.sessions}


class FreeUser(User):

    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        sessions: list[ListeningSession] | None = None,
        max_skips_per_hour: int = 6
    ):
        super().__init__(user_id, name, age, sessions)
        self.max_skips_per_hour = max_skips_per_hour


class PremiumUser(User):

    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        subscription_start: date,
        sessions: list[ListeningSession] | None = None
    ):
        super().__init__(user_id, name, age, sessions)
        self.subscription_start = subscription_start


class FamilyAccountUser(PremiumUser):

    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        subscription_start: date,
        sub_users: list["FamilyMember"] | None = None,
        sessions: list[ListeningSession] | None = None
    ):
        super().__init__(user_id, name, age, subscription_start, sessions)
        self.sub_users = list(sub_users) if sub_users is not None else []

    def add_sub_user(self, sub_user: "FamilyMember") -> None:
        self.sub_users.append(sub_user)

    def all_members(self) -> list[User]:
        return [self] + self.sub_users


class FamilyMember(User):

    def __init__(
        self,
        user_id: str,
        name: str,
        age: int,
        parent: FamilyAccountUser,
        sessions: list[ListeningSession] | None = None
    ):
        super().__init__(user_id, name, age, sessions)
        self.parent = parent

