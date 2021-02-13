import sqlite3
from plant import Plant

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE gardens
             (ID int PRIMARY KEY, plant_count int, carb_footprint int)""")
c.execute("""CREATE TABLE users
    (ID int, username string, user_plants text, user_plant_count int)""")


def insert_garden(hasher):
    with conn:
        c.execute("INSERT INTO gardens VALUES (:ID, :plant_count, :carb_footprint)",
                  {'ID': hasher, 'plant_count': 0, 'carb_footprint': 0})


def insert_user(hasher, name):
    with conn:
        c.execute("INSERT INTO users VALUES (:ID, :username, :user_plants, :plant_count)",
                  {'ID': hasher, 'username': name, 'user_plants': "", 'plant_count': 0})


def insert_plant(hasher, name, plant, add_plants, carb):
    with conn:
        c.row_factory = lambda cursor, row: row[0]
        c.execute("SELECT user_plant_count FROM users WHERE username=?", (name,))
        a = c.fetchall()[0] + add_plants
        c.execute("SELECT plant_count FROM gardens WHERE ID=?", (hasher,))
        d = c.fetchall()[0] + add_plants
        c.execute("SELECT user_plants FROM users WHERE username=?", (name,))
        b = c.fetchall()[0] + " " + plant
        c.execute("SELECT carb_footprint FROM gardens WHERE ID=?", (hasher,))
        e = c.fetchall()[0] + carb
        print(b)
        c.row_factory = None
        c.execute("UPDATE users SET user_plant_count=?, user_plants=? WHERE username=?",(a, b, name))
        c.execute("UPDATE gardens SET plant_count=? WHERE ID =  ?", (d, hasher))
        c.execute("UPDATE gardens SET carb_footprint=? FROM gardens WHERe ID=?", (e, hasher))

def get_users(hasher):
    with conn:
        c.execute("SELECT * FROM users WHERE ID = ?", (hasher,))




conn.close()