# Consumer
[![Build Status](https://travis-ci.org/sohaibfarooqi/consumer.svg?branch=master)](https://travis-ci.org/sohaibfarooqi/consumer)   [![Coverage Status](https://coveralls.io/repos/github/sohaibfarooqi/consumer/badge.svg?branch=master)](https://coveralls.io/github/sohaibfarooqi/consumer?branch=master)

This app implements a consumer component of classic [Producer-Consumer Architecture](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem). It uses celery as a task management framework and SQL database to store
incoming data stream. Celery can be bound to a queue at initilization. Whenever there is a new message in queue
consumer will automatically pick this message and after performing some validation on the data, store it
in the database.

This model is scalable and will sustain high rate of incoming messages. We can deploy same application to
multiple servers(depending upon the load) and whichever instance is idle will process the new incoming message.

### Installation and Running
The following steps will get you a copy of app(single instance) on you local system:

  - `git clone https://github.com/sohaibfarooqi/consumer.git`
  - `virtualenv -p python3 .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements/dev.txt`
  - `set environemnt variable CELERY_BROKER_URL`
  - `celery -A consumer worker -l info -Q <queue_name>`

At this point the app is ready to process incoming message.

### Running tests
Follow these commands to run tests and generate coverage reports

 - `pip install -r requirements/test.txt`
 - `pytest`
 - `pytest --cov=consumer tests/`

