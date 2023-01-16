import src.schemas.delivery as schemas
import src.models.delivery as models
from src.core import tracing_tools


@tracing_tools.trace_it('Service', 'Get delivery info')
async def get_deliveries_info_by_user_id(user_id: int) -> list[models.Delivery]:
    return models.Delivery.objects(user_id=user_id)


@tracing_tools.trace_it('Service', 'Get delivery info')
async def get_deliveries_info_by_user_id(user_id: int) -> list[models.Delivery]:
    return models.Delivery.objects(user_id=user_id)
