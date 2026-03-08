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



class User:

    def __init__(self, user_id:str, name:str, age:int, sessions):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sessions: list[ListeningSession] = []


    def add_session(self,session):
        self.sessions.append(session)


    def total_listening_seconds(self) -> int:
        total = 0
        for session in self.sessions:
            total += session.duration_listened_seconds
        return total


    def total_listening_minutes(self) -> float:
        return sum(session.duration_listened_minutes() for session in self.sessions)

    def unique_tracks_listened(self) -> set[str]:
        return set(session.track.track_id for session in self.sessions)












class FamilyAccountUser(User):

    def __init__(self, sub_users:list[FamilyMember]):
        super().__init__(user_id="", name="", age=0, sessions=[])
        self.sub_users = sub_users

        def add_sub_user(self,sub_user):
            self.sub_users.append(sub_user)



        def all_members(slef) -> list[User]:
            return [self] + self.sub_users






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

