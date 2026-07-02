import redis

redis_connection = redis.Redis(host="localhost", port=6379, db=0);
print(redis_connection)

# Chave Valor (variavel)
redis_connection.set('chave_1', 'valor_1')
redis_connection.set('chave_2', 'valor_2')

valor = redis_connection.get('chave_1')
redis_connection.delete('chave_1', 'cidade')

valor_1_exist = redis_connection.exists('chave_1')
valor_2_exist = redis_connection.exists('chave_2')


print(valor_1_exist)
print(valor)
print(valor_2_exist)
print(valor.decode("utf-8"))

# Hash (Dicionario)

redis_connection.hset('meu_hash', 'nome', 'joao')
redis_connection.hset('meu_hash', 'idade', 30)
redis_connection.hset('meu_hash', 'cidade', 'Niteroi')


nome = redis_connection.hget('meu_hash', 'nome').decode("utf-8")
cidade = redis_connection.hget('meu_hash', 'cidade').decode("utf-8")

meu_hash_exist = redis_connection.exists('meu_hash')

meu_hash_nome_exists = redis_connection.hexists('meu_hash', 'nome')



print(nome)
print(cidade)
print(meu_hash_exist)
print(meu_hash_nome_exists)


redis_connection.hdel('meu_hash', 'cidade')
