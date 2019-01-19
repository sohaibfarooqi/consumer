from marshmallow import EXCLUDE, Schema, fields

class UserSchema(Schema):
    """
    Class definition for User model.

    Fields Definition:
    ------------------
        - name: Name of User.
        - email: Email address of User. This field should be unique.
        - timestamp: EPOCH timestamp when this datapoint was loaded in queue.
        - created_at: Datetime when this object was loaded in database
        - parent_task_id: task_id of producer celery task
    """
    class Meta:
        unknown = EXCLUDE

    name = fields.Str(required=True)
    email = fields.Email(required=True)
    timestamp = fields.Float()
    created_at = fields.DateTime()
    parent_task_id = fields.UUID()
