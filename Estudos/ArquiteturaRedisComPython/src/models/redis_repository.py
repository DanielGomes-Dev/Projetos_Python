from redis import Redis
from typing import Optional, Any

class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    # --- Operações de String ---
    def set(self, key: str, value: str, ex: Optional[int] = None) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def get(self, key: str) -> Optional[str]:
        value = self.__redis_conn.get(key)
        return value.decode("utf-8") if value else None

    def delete(self, *keys: str) -> None:
        self.__redis_conn.delete(*keys)

    def exists(self, key: str) -> bool:
        return self.__redis_conn.exists(key) > 0

    # --- Operações de Hash ---
    def hset(self, hash_name: str, key: str, value: Any) -> None:
        self.__redis_conn.hset(hash_name, key, value)

    def hget(self, hash_name: str, key: str) -> Optional[str]:
        value = self.__redis_conn.hget(hash_name, key)
        return value.decode("utf-8") if value else None

    def hdel(self, hash_name: str, key: str) -> None:
        self.__redis_conn.hdel(hash_name, key)

    def hexists(self, hash_name: str, key: str) -> bool:
        return self.__redis_conn.hexists(hash_name, key)
