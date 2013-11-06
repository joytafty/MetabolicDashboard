import os
import redis

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:10935')
redis = redis.from_url(redis_url)