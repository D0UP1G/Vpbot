import sqlite3
import api

APi = api.API('https://147.45.149.141:6269/N0Nxavb2MW7PUwwf5cRJHA')
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

#надо создать функцию которая только по айди выдаёт сервер


def add_user(id:int,name:str):
    try:
        cursor.execute("INSERT INTO user (id, name) VALUES  (?,?)", (id,name))
    except:
        print('err to create user')
        return 'err'
    return conn.commit()

def add_server(name:str, key:str):
    cursor.execute("INSERT INTO servers (name, key) VALUES  (?,?)", (name,key))
    return conn.commit()

def set_free_server(user_id:int):
    server_uses = 100
    cursor.execute("SELECT id, users FROM servers")
    servers = cursor.fetchall()
    print(servers)
    for server_id, user in servers:
        if user < server_uses:

            server_id = server_id
            cursor.execute("UPDATE servers SET users = ? WHERE id = ?", (user+1, server_id))
            cursor.execute("UPDATE user SET server = ? WHERE id = ?", (server_id, user_id))
            conn.commit()

def give_server(user_id:int):
    cursor.execute('SELECT server FROM user')
    user_server = cursor.fetchall()
    if type(user_server[0][0]) ==  None:
        return APi.get_key(user_server[0][0])
    else:
        import json
        ids = int(json.loads(APi.create_key().text)['id'])
        cursor.execute("UPDATE user SET server = ? WHERE id = ?", (ids, user_id))
        conn.commit()
        return APi.get_key(ids)
    return True