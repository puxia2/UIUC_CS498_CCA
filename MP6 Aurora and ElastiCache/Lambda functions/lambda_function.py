import json
import sys
import logging
import redis
import pymysql


DB_HOST = "mp6-db-instance-1.cmwvk2h4xwso.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "rEBd3C0TUoSfGWI5YaJ4"
DB_NAME = "mp6"
DB_TABLE = "heros"
REDIS_URL = "redis://redis-new-mp6.8rmbia.ng.0001.use1.cache.amazonaws.com:6379"

TTL = 10

class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)

        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_idx(self, table_name):
        with self.mysql.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")
            idx = str(cursor.fetchone()['id'] + 1)
            return idx

    def insert(self, idx, data):
        with self.mysql.cursor() as cursor:
            hero = data["hero"]
            power = data["power"]
            name = data["name"]
            xp = data["xp"]
            color = data["color"]
            
            sql = f"INSERT INTO heros (`id`, `hero`, `power`, `name`, `xp`, `color`) VALUES ('{idx}', '{hero}', '{power}', '{name}', '{xp}', '{color}')"

            cursor.execute(sql)
            self.mysql.commit()

def read(use_cache, indices, Database, Cache):
    
    result = []
    for i in indices:
        sql = f"SELECT * FROM heros WHERE id = '{i}'"
        if use_cache:
            if Cache.exists(i): # cache already contains the data
                result.append(json.loads(Cache.get(i)))
            else: # cache doesn't contain the data, read the data from RDS
                data = Database.query(sql)
                if data: 
                    result.append(data[0])
                    Cache.set(i, json.dumps(data[0]))
                
        else:
            data = Database.query(sql)
            if data:
                result.append(data[0])

    return result

    
    
def write(use_cache, sqls, Database, Cache):
    
    for data in sqls:
        idx = Database.get_idx(DB_TABLE)
        data['id'] = idx
        Database.insert(idx=idx, data=data)
    
        if use_cache:
            # write through strategy
            Cache.set(idx, json.dumps(data))


def lambda_handler(event, context):
    
    USE_CACHE = (event['USE_CACHE'] == "True")
    REQUEST = event['REQUEST']
    
    # initialize database and cache
    try:
        Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()
        
    Cache = redis.Redis.from_url(REDIS_URL)
    print("Connected to REDIS? {0} ".format(Cache.ping()))
    
    result = []
    if REQUEST == "read":
        # event["SQLS"] should be a list of integers
        result = read(USE_CACHE, event["SQLS"], Database, Cache)
    elif REQUEST == "write":
        # event["SQLS"] should be a list of jsons
        write(USE_CACHE, event["SQLS"], Database, Cache)
        result = "write success"
    
    
    return {
        'statusCode': 200,
        'body': result
    }
