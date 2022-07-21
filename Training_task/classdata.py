from dataclasses import dataclass, asdict


class User:
    name: str
    age: int

a = User()


class UserHadle:
    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, velue):
        self.user.__dict__[key] = velue

