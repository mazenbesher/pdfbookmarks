import redis

from app.utils.envvars import envvars

_REDIS_CONN = None


def init():
    global _REDIS_CONN
    _REDIS_CONN = redis.Redis(
        host=envvars["REDIS_HOST"],
        port=envvars["REDIS_PORT"],
        decode_responses=True,
    )

    # flush all keys in redis
    _REDIS_CONN.flushall()


def get_conn():
    return _REDIS_CONN
