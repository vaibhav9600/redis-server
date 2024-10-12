import redis

def connect_to_redis(host='qa-redis.cykuib.ng.0001.aps1.cache.amazonaws.com', port=6379, db=0):
    return redis.Redis(host=host, port=port, db=db)

def hset(redis_client, key, field, value):
    redis_client.hset(key, field, value)

def hget(redis_client, key, field):
    return redis_client.hget(key, field)

# Example usage
if __name__ == "__main__":
    redis_client = connect_to_redis()
    key = 'my_hash'
    field = 'my_field'
    value = 'my_value'

    # hset(redis_client, key, field, value)
    result = hget(redis_client, key, field)
    print(result.decode('utf-8'))
