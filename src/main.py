from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mongoengine import connect, disconnect

from prometheus_fastapi_instrumentator import Instrumentator
import aio_pika
import json

from src.core import tracing_tools
from src.core.settings import settings
from src.endpoints.router import delivery_router

app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def on_message(message: aio_pika.IncomingMessage):
    txt = message.body.decode("utf-8")
    print(json.loads(txt))


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)
    tracing_tools.init_tracer()
    connect(
        host=f'mongodb://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}?authSource={settings.DATABASE_USERNAME}')
    connection = await aio_pika.connect("amqp://guest:guest@192.168.0.111:5672/")
    channel = await connection.channel()

    queue = await channel.declare_queue("fastapi_task")

    await queue.consume(on_message, no_ack=True)


@app.on_event("shutdown")
def shutdown_event():
    disconnect()


app.include_router(delivery_router)
