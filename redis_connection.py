import redis
from redis.backoff import ConstantBackoff
from redis.exceptions import NoPermissionError
from redis.retry import Retry
from environs import Env


def get_redis_connection():
    env = Env()
    env.read_env()
    redis_pool = redis.ConnectionPool(
        host=env.str('REDIS_HOST', 'localhost'),
        port=env.int('REDIS_PORT', 6379),
        retry=Retry(ConstantBackoff(10), 30),
        retry_on_error=[
            ConnectionError, TimeoutError, NoPermissionError, ConnectionRefusedError, PermissionError
        ],
        socket_timeout=300,
        socket_connect_timeout=300,
        health_check_interval=300,
    )
    return redis.StrictRedis(connection_pool=redis_pool, db=0)
