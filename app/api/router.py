from fastapi import APIRouter, HTTPException, status
from rich import panel, print
from .dependencies import ServiceDep
from app.api.schemas.shipment import ShipmentCreate, ShipmentRead, ShipmentUpdate


router = APIRouter(prefix="/shipment", tags=["Shipment"])


@router.get("/", response_model=ShipmentRead)
async def get_shipment(id: int, service: ServiceDep):
    print(panel.Panel(f"Read a shipment by #{id}", border_style='green'))
    shipment = await service.get(id)

    if shipment is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't Exist!"
        )

    return shipment

# Create a new shipment with content and weight


@router.post("/", response_model=ShipmentRead)
async def submit_shipment(shipment: ShipmentCreate,
                          service: ServiceDep):
    return await service.add(shipment)


# Update fields of a shipment

@router.patch("/", response_model=ShipmentRead)
async def update_shipment(id: int, shipment_update: ShipmentUpdate, service: ServiceDep):
    update = shipment_update.model_dump(exclude_none=True)

    if not update:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="No data provided to update")

    return await service.update(id, update)


# Delete a shipment by id

@router.delete("/")
async def delete_shipment(id: int, service: ServiceDep) -> dict[str, str]:
    await service.delete(id)
    return {"detail": f"Shipment with id #{id} is deleted!"}
