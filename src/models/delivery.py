import mongoengine
import enum
import time


class Status(enum.Enum):
    CREATED = 'created'
    ONGOING = 'ongoing'
    DONE = 'done'


class Delivery(mongoengine.Document):
    meta = {
        # 'db_alias': 'mydb',
        'collection': 'delivery'
    }

    delivery_uuid = mongoengine.UUIDField(primary_key=True)
    user_id = mongoengine.IntField()
    cart_uuid = mongoengine.UUIDField()
    date = mongoengine.DateField(default=time.time())
    address = mongoengine.StringField(default='')
    description = mongoengine.StringField(default='')
    status = mongoengine.EnumField(Status, default=Status.CREATED)
