from redis import Redis
from etc.config import config


class RedisApi:
    def __init__(self, host, port, password, db):
        self.redis_conn = Redis(host=host, port=port, password=password, db=db)

    def set(self, key, value):
        self.redis_conn.set(key, value)

    def get(self, key):
        return self.redis_conn.get(key)

    def delete(self, key):
        self.redis_conn.delete(key)

    def update(self, key, value):
        self.redis_conn.set(key, value)

    def get_all(self):
        keys = self.redis_conn.keys()
        data = []
        for key in keys:
            value = self.redis_conn.get(key)
            data.append(
                {
                    "mpid": key,
                    "ip": value.decode(),
                }
            )
        return data

    def get_by_ip(self, ip):
        keys = self.redis_conn.keys()
        for key in keys:
            value = self.redis_conn.get(key)
            if value.decode() == ip:
                return key.decode()
        return None


redis_api = RedisApi(
    host=config.redis_host,
    port=config.redis_port,
    password=config.redis_password,
    db=config.redis_db,
)
