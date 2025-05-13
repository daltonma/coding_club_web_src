from kpop import Group, Artist
from peewee import SqliteDatabase

db = SqliteDatabase('kpop.db')
# Example data
# Create a group
db.begin()
group1 = Group.create(name="ENHYPEN", debut_date="2020-11-30", company="BELIFT LAB", generation=4)
group2 = Group.create(name="TXT", debut_date="2019-03-04", company="Big Hit Entertainment", generation=4)
group3 = Group.create(name="SEVENTEEN", debut_date="2015-05-26", company="Pledis Entertainment", generation=3)
group4 = Group.create(name="Stray Kids", debut_date="2018-03-25", company="JYP Entertainment", generation=4)
group5 = Group.create(name="ZEROBASEONE", debut_date="2023-07-10", company="Wake One Entertainment", generation=5)
group6 = Group.create(name="NewJeans", debut_date="2022-08-01", company="ADOR", generation=4)


jungwon = Artist.create(name="Yang Jungwon", stage_name="Jungwon", group=group1)
sunghoon = Artist.create(name="Park Sung-hoon", stage_name="Sunghoon", group=group1)
sunoo = Artist.create(name="Kim Sun-oo", stage_name="Sunoo", group=group1)
heeseung = Artist.create(name="Heeseung", stage_name="Heeseung", group=group1)
taehyun = Artist.create(name="Choi Tae-hyun", stage_name="Taehyun", group=group2)
soobin = Artist.create(name="Choi Soo-bin", stage_name="Soobin", group=group2)
yeonjun = Artist.create(name="Choi Yeon-jun", stage_name="Yeonjun", group=group2)
beomgyu = Artist.create(name="Choi Beom-gyu", stage_name="Beomgyu", group=group2)
hoshi = Artist.create(name="Kwon Soonyoung", stage_name="Hoshi", group=group3)
woozi = Artist.create(name="Lee Jihoon", stage_name="Woozi", group=group3)
felix = Artist.create(name="Lee Yong-bok", stage_name="Felix", group=group4)
bangchan = Artist.create(name="Bang Chan", stage_name="Bang Chan", group=group4)
leeknow = Artist.create(name="Lee Min-ho", stage_name="Lee Know", group=group4)
zhanghao = Artist.create(name="Zhang Hao", stage_name="Zhang Hao", group=group5)
yujin = Artist.create(name="Han Yujin", stage_name="Yujin", group=group5)
hanbin = Artist.create(name="Sung Han-bin", stage_name="Hanbin", group=group5)
danielle = Artist.create(name="Danielle Marsh", stage_name="Danielle", group=group6)
haerin = Artist.create(name="Kim Haerin", stage_name="Haerin", group=group6)
# Commit the changes
db.commit()

# Querying the database
# Get all groups
groups = Group.select()
for group in groups:
    print(f"Group: {group.name}, Debut Date: {group.debut_date}, Company: {group.company}, Generation: {group.generation}")