import pydantic
import uuid
import time
from src.models.delivery import Status


class BaseDelivery(pydantic.BaseModel):
    user_id: int
    cart_uuid: uuid.UUID
    date = time.time()
    address: str
    description: str
    status: Status


class Delivery(BaseDelivery):
    delivery_uuid: uuid.UUID

