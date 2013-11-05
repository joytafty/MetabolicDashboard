import os
import redis
	
redis_url = os.getenv('REDISTOGO_URL', 'redis://redistogo:15d661206506247835d3ccd45c1d0f90@beardfish.redistogo.com:10935')
redis = redis.from_url(redis_url)