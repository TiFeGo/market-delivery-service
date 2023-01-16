import src.schemas.delivery as schemas
import src.models.delivery as models
from src.core import tracing_tools

from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context


@tracing_tools.trace_it_sync(tag='mapper', value='model to schema')
def mapping_model_schema(model: models.Delivery):
    schema = schemas.Delivery(
        delivery_uuid=model.delivery_uuid,
        user_id=model.user_id,
        cart_uuid=model.cart_uuid,
        date=model.date,
        address=model.address,
        description=model.description,
        status=model.status,
    )
    return schema


@tracing_tools.trace_it_sync(tag='mapper', value='schema to model')
def mapping_schema_model(schema: schemas.Delivery):
    model = models.Delivery(
        delivery_uuid=schema.delivery_uuid,
        user_id=schema.user_id,
        cart_uuid=schema.cart_uuid,
        date=schema.date,
        address=schema.address,
        description=schema.description,
        status=schema.status,
    )
    return model

