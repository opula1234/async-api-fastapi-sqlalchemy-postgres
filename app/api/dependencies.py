from typing import Annotated
from fastapi import Depends
from app.database.session import get_session
from app.services.shipment import ShipmentService
from sqlalchemy.ext.asyncio import AsyncSession

# Session Dependency Annotation
SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_shipment_service(session: SessionDep):
    return ShipmentService(session)


ServiceDep = Annotated[ShipmentService, Depends(get_shipment_service)]
