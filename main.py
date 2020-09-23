from pymongo import MongoClient
from typeschemalib import typeschemalib


class Database:
    def __init__(self, location: str = "localhost", port: int = 27017):
        self.location = location
        self.port = port
        self.connect()

    def connect(self):
        self.client = MongoClient(self.location, self.port)
        self.db = self.client.my_database
        self.profiles = self.db.profiles
        self.messages = self.db.messages

    def write_profile(self, document):
        schema = "schema/profile.stml"
        valid = typeschemalib.schema_check(schema, document)
        if valid is not True:
            print(valid)
        else:
            print(document)
            self.profiles.insert_one(document)


if __name__ == "__main__":
    data = {
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "lang": input("Lang: "),
        "percent": float(input("Percent: "))
    }
    db = Database()
    db.write_profile(data)
