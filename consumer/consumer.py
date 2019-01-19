from celery import Celery
from celery.utils.log import get_task_logger
from .config import CeleryConfig

celery_app = Celery("consumer")
celery_app.config_from_object(CeleryConfig)

logger = get_task_logger(__name__)

class Consumer(celery_app.Task):

  name = 'consumer'

  def run(self, *args, **kwargs):
    pass

celery_app.tasks.register(Consumer())
