# Consumer
[![Build Status](https://travis-ci.org/sohaibfarooqi/consumer.svg?branch=master)](https://travis-ci.org/sohaibfarooqi/consumer)[![Coverage Status](https://coveralls.io/repos/github/sohaibfarooqi/consumer/badge.svg?branch=master)](https://coveralls.io/github/sohaibfarooqi/consumer?branch=master)

This app implements a consumer component of classic [Producer-Consumer Architecture](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem). It uses celery as a task management framework and SQL database to store
incoming data stream. Celery can be bound to a queue at initilization. Whenever there is a new message in queue
consumer will automatically pick this message and after performing some validation on the data, store it
in the database.
