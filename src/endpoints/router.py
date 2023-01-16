from fastapi import APIRouter, Depends, status, HTTPException

from src.core import tracing_tools
import src.schemas.delivery as del_schemas
import src.models.delivery as del_model
import src.utils.mappers as mapper
from src.endpoints import services

delivery_router = APIRouter(
    tags=['Delivery'],
    prefix='/delivery'
)


@delivery_router.get('/{user_id}', response_model=list[del_schemas.Delivery], status_code=status.HTTP_200_OK)
@tracing_tools.trace_it('Endpoint', 'Get delivery info')
async def get_deliveries_info_by_user_id(user_id: int) -> list[del_schemas.Delivery]:
    return [
        mapper.mapping_model_schema(model)
        for model in await services.get_deliveries_info_by_user_id(user_id)
    ]
