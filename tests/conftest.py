import os

import pytest
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

uri = os.environ.get('DATABASE_URI')


@pytest.fixture
def db():
    """
    Fixture to create test database, apply migrations
    and finally delete it once the test cases are executed.
    """
    if not database_exists(uri):
        create_database(uri)
    alembic_config = AlembicConfig('alembic.ini')
    alembic_config.set_main_option('sqlalchemy.url', uri)
    alembic_upgrade(alembic_config, 'head')
    yield "success"
    drop_database(uri)


@pytest.fixture
def db_session(db):
    """
    Fixture to provide SQLAlchemy session for querying.
    """
    engine = create_engine(uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session


@pytest.fixture
def valid_data():
    """
    Fixture to load valid data according to specified schema.
    """
    d1 = {
        'name': 'Milla Nova',
        'timestamp': 1547865754.330828,
        'email': 'catos.sadf.df@google.com.hk',
        'parent_task_id': '92487b0e-211f-4b1a-bf11-55429760ba68'
    }
    yield d1


@pytest.fixture
def duplicate_email():
    """
    This Fixture contains duplicate emails. It is
    used to test unique constraint violations.
    """
    d2 = [
        {
            'name': 'Milla Nova',
            'timestamp': 1547865754.330828,
            'email': 'catos.sadf.df@google.com.hk',
            'parent_task_id': '92487b0e-211f-4b1a-bf11-55429760ba68'
        },
        {
            'name': 'Milla Nova',
            'timestamp': 1547865754.330828,
            'email': 'catos.sadf.df@google.com.hk',
            'parent_task_id': '92487b0e-211f-4b1a-bf11-55429760ba68'
        }
    ]
    yield d2


@pytest.fixture
def invalid_data():
    """
    Fixture with invalid email address format
    """
    d3 = {
        'name': 'Milla Nova',
        'timestamp': 1547865754.330828,
        'email': 'catos.sadf',
        'parent_task_id': '92487b0e-211f-4b1a-bf11-55429760ba68'
    }
    yield d3
