# DRF Messages application

### Installation

* pip install -r requirements.txt
* install redis as a message broker according to the docs: 
   * https://docs.celeryproject.org/en/stable/getting-started/brokers/redis.html
   * https://redis.io/topics/quickstart
* run 
> celery -A messages worker
