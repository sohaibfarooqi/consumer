import celery

from consumer import Consumer
from consumer.model import User

def test_consumer_valid_data(db_session, valid_data):
    """
    Test consumer class with valid data. Verify the results
    by querying the database.
    """
    c = Consumer()
    task_id = c.s(**valid_data).apply_async()
    all_users = db_session.query(User).all()

    assert len(all_users) == 1
    assert all_users[0].email == valid_data['email']


def test_consumer_duplicate_email(db_session, duplicate_email):
    """
    Test to detemine unique contraint violation is handled
    properly in code.
    """
    c = Consumer()
    for data in duplicate_email:
        task_id = c.s(**data).apply_async()

    all_users = db_session.query(User).all()
    assert len(all_users) == len(duplicate_email) - 1


def test_consumer_invalid_data(db_session, invalid_data):
    """
    Test with invalid data schema should not load anything
    to database.
    """
    c = Consumer()
    task_id = c.s(**invalid_data).apply_async()
    all_users = db_session.query(User).all()

    assert isinstance(task_id, celery.result.EagerResult)
    assert len(all_users) == 0
