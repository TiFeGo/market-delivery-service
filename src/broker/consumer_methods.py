import pydantic
import uuid
import enum
import json
import aio_pika


class Method(str, enum.Enum):
    CREATE = 'create'


class AddDelivery(pydantic.BaseModel):
    method: Method
    user_id: int
    cart_uuid: str


async def on_message(message: aio_pika.IncomingMessage):
    txt = message.body.decode("utf-8")
    delivery_info = AddDelivery(**json.loads(txt))
    if delivery_info.method == Method.CREATE:
        await create_delivery()


async def update_status():
    pass


async def create_delivery():
    pass
