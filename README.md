# DRF Messages application

### Installation

* pip install -r requirements.txt
* install redis as a message broker according to the docs: https://docs.celeryproject.org/en/stable/getting-started/brokers/redis.html
* run 
> celery -A messages worker
