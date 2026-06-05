from fastapi import HTTPException, Depends, APIRouter
from sqlmodel import Session, select

from app.db import get_session
from app.schemas import Car, CarInput, Car_DBModel

router = APIRouter(prefix="/api/cars")


@router.get("/")
def get_cars(
    size: str | None = None,
    doors: int | None = None,
    session: Session = Depends(get_session),
) -> list[Car]:
    query = select(Car_DBModel)
    if size is not None:
        query = query.where(Car_DBModel.size == size)
    if doors is not None:
        query = query.where(Car_DBModel.doors >= doors)
    result = session.exec(query).all()
    if result:
        return result
    raise HTTPException(status_code=404, detail="No cars match filters.")


@router.get("/{id}", response_model=Car)
def car_by_id(id: int, session: Session = Depends(get_session)) -> Car:
    car = session.get(Car_DBModel, id)
    if car:
        return car
    raise HTTPException(status_code=404, detail=f"No car with id = {id}.")


@router.post("/", response_model=Car_DBModel)
def add_car(car: CarInput, session: Session = Depends(get_session)) -> Car_DBModel:
    new_car = Car_DBModel.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@router.delete("/{id}", status_code=204)
def remove_car(id: int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


@router.put("/{id}", response_model=Car_DBModel)
def change_car(
    id: int, new_data: CarInput, session: Session = Depends(get_session)
) -> Car_DBModel:
    car = session.get(Car_DBModel, id)
    if car:
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission
        session.commit()
        return car
    raise HTTPException(status_code=404, detail=f"No car with id={id}.")