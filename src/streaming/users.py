from __future__ import annotations

import datetime

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
from src.streaming.sessions import ListeningSession


class User:

    def __init__(self, user_id:str, name:str, age:int, sessions:list[ListeningSession]):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions = sessions

    def add_session(session):
        pass


    def total_listening_seconds(self) -> int:
        pass


    def total_listening_minutes(self) -> float:
        pass

    def unique_tracks_listened(self) -> set[str]:
        pass












class FamilyAccountUser(User):

    def __init__(self, sub_users:list[FamilyMember]):
        super().__init__(user_id="", name="", age=0, sessions=[])
        self.sub_users = sub_users


class FamilyMember(User):

    def __init__(self, parent: FamilyAccountUser):
        super().__init__(user_id="", name="", age=0, sessions=[])
        self.parent = parent



class FreeUser(User):
    def __init__(self, MAX_SKIPS_PER_HOUR:int = 6):
        super().__init__(user_id="", name="", age=0, sessions=[])
        self.MAX_SKIPS_PER_HOUR = MAX_SKIPS_PER_HOUR




class PremiumUser(User):
    def __init__(self, subscription_start):
        super().__init__(user_id="", name="", age=0, sessions=[])
        self.subscription_start_date = datetime.date

