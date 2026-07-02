from models.connection.redis_connection import RedisConnectionHandle
from models.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().connect();
redis_repository = RedisRepository(redis_conn=redis_conn);
print(redis_conn)

redis_repository.set("Chave_1_Repo", "Valor_1_Repo");
value = redis_repository.get("Chave_1_Repo");

print(value);


redis_repository.hset("Hash_Repo", "Hash_Chave_1_Repo", "Hash_Valor_1_Repo");
hash_value = redis_repository.hget("Hash_Repo", "Hash_Chave_1_Repo");
print(hash_value)