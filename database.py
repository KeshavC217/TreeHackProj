import sqlite3
from plant import Plant

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE gardens
             (ID int PRIMARY KEY, plant_count int, carb_footprint int)""")
c.execute("""CREATE TABLE users
    (ID int, username string, user_plants text, user_plant_count int, user_carb_footprint int)""")


def insert_garden(hasher):
    with conn:
        c.execute("INSERT INTO gardens VALUES (:ID, :plant_count, :carb_footprint)",
                  {'ID': hasher, 'plant_count': 0, 'carb_footprint': 0})


def insert_user(hasher, name):
    with conn:
        c.execute("INSERT INTO users VALUES (:ID, :username, :user_plants, :user_plant_count, :user_carb_footprint)",
                  {'ID': hasher, 'username': name, 'user_plants': "", 'user_plant_count': 0, 'user_carb_footprint': 0})


def add_existing_plant(hasher, name, add_plants, carb):
    with conn:
        c.row_factory = lambda cursor, row: row[0]
        c.execute("SELECT user_plant_count FROM users WHERE username=?", (name,))
        a = c.fetchall()[0] + add_plants
        c.execute("SELECT plant_count FROM gardens WHERE ID=?", (hasher,))
        d = c.fetchall()[0] + add_plants
        c.execute("SELECT carb_footprint FROM gardens WHERE ID=?", (hasher,))
        e = c.fetchall()[0] + add_plants * carb
        c.execute("SELECT user_carb_footprint FROM users WHERE username=?", (name,))
        f = c.fetchall()[0] + add_plants * carb
        c.row_factory = None
        c.execute("UPDATE users SET user_plant_count=? WHERE username=?", (a, name))
        c.execute("UPDATE gardens SET plant_count=? WHERE ID =  ?", (d, hasher))
        c.execute("UPDATE gardens SET carb_footprint=? WHERE ID = ?", (e, hasher))
        c.execute("UPDATE users SET user_carb_footprint=? WHERE username=?", (f, name))


def insert_new_plant(hasher, name, plant, add_plants, carb):
    add_existing_plant(hasher, name, add_plants, carb)
    with conn:
        c.row_factory = lambda cursor, row: row[0]
        c.execute("SELECT user_plants FROM users WHERE username=?", (name,))
        b = c.fetchall()[0] + " " + plant
        c.row_factory = None
        c.execute("UPDATE users SET user_plants=? WHERE username=?",(b, name))


def get_users(hasher):
    with conn:
        c.execute("SELECT * FROM users WHERE ID = ?", (hasher,))


user1 = "TOM"
user2 = "FRED"
user3 = "Jeff"
tomatoes = "tomatoes"
broc = "broccoli"
bana = "banana"
insert_garden(1)
insert_garden(2)
insert_user(1, user1)
insert_user(2, user2)
insert_user(1, user3)
insert_new_plant(1, user1, bana, 2, 20)
insert_new_plant(1, user3, broc, 1, 15)
add_existing_plant(1, user3, 2, 15)
get_users(1)
print(c.fetchall())
get_users(2)
print(c.fetchall())

conn.close()