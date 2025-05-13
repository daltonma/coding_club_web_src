from peewee import *

db = SqliteDatabase('kpop.db')



class BaseModel(Model):
    class Meta:
        database = db


class Group(BaseModel):
    name = CharField()
    debut_date = DateField()
    company = CharField()
    generation = IntegerField()

class Artist(BaseModel):
    name = CharField()
    stage_name = CharField()
    group = ForeignKeyField(Group)

if __name__ == "__main__":

    db.connect()
    db.create_tables([Group, Artist])

