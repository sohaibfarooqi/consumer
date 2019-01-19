import pytest
from marshmallow.exceptions import ValidationError

from consumer.schema import UserSchema

def test_schema_valid_data(valid_data):
    """
    Test schema with valid data should not
    raise any error.
    """
    schema = UserSchema()
    assert schema.validate(valid_data) == {}


def test_schema_invalid_data(invalid_data):
    """
    Test with invalid data schema should raise
    marshmallow ValidationError.
    """
    schema = UserSchema()
    with pytest.raises(ValidationError):
        assert schema.load(invalid_data)
