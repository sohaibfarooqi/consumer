from celery import Celery
from celery.utils.log import get_task_logger
from marshmallow import ValidationError
from sqlalchemy import exc

from .config import CeleryConfig
from .schema import UserSchema
from .model import User, session

celery_app = Celery("consumer")
celery_app.config_from_object(CeleryConfig)

logger = get_task_logger(__name__)

class Consumer(celery_app.Task):
  """
  Class definition for consumer class. This class
  instance will be registered as a celery task which
  which will consume data stream from a specific queue.

  To invoke this task use following command:
    - celery -A consumer worker -l info -Q <queue_name>
  """
  name = 'consumer'

  def run(self, *args, **kwargs):
    """
    Main task body. This task will first load the incoming
    stream of data into UserSchema and validate whether the
    datatypes are correct. The validated data will then be loaded
    into database table.

    Raises:
    -------
      - marshmallow.ValidationError: In case of wrong datatypes.
      - sqlalchemy.exc.IntegrityError: In case of duplicate email

    """
    try:

      user = UserSchema()
      user_obj = user.load(kwargs)
      user_model = User(**user_obj)
      session.add(user_model)
      session.commit()

    except ValidationError as err:
      logger.error('Schema validation error for email: {}, Err: {}'.format(kwargs.get('email'), err))

    except exc.IntegrityError as ierr:
      logger.error('Unique constraint violation for email: {}'.format(kwargs.get('email')))
      session.rollback()

celery_app.tasks.register(Consumer())
