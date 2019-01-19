import pytest
from sqlalchemy import exc
from consumer.model import User

def test_model_valid_data(db_session, valid_data):
  """
  Test model directly with valid data schema. Verify that
  correct data is loaded to database.
  """
  user = User(**valid_data)
  db_session.add(user)
  db_session.commit()

  all_users = db_session.query(User).all()
  assert len(all_users) == 1
  assert all_users[0].email == valid_data['email']

def test_model_duplicate_data(db_session, duplicate_email):
  """
  Check SQLAlchemy raises IntegrityError on failure of
  unique contraint violation. This test would be helpful
  if later versions of SQLAlchemy decides to rename the
  exception or move to different package.
  """
  with pytest.raises(exc.IntegrityError):
    for data in duplicate_email:
      user = User(**data)
      db_session.add(user)
      db_session.commit()

def test_model_invalid_dtype(db_session, invalid_data):
  """
  Test to verify that invalid data values would not be
  inserted in the database.
  """
  invalid_data.update({"timestamp": "abc"})
  with pytest.raises(exc.DataError):
    user = User(**invalid_data)
    db_session.add(user)
    db_session.commit()



