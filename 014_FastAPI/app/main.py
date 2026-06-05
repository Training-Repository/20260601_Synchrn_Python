from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import Session, SQLModel, select

from app.db import engine
from app.routers import cars
from app.schemas import Car_DBModel

# Same list as Step 3 (no id); DB will generate ids
INITIAL_CARS = [
    {"size": "s", "fuel": "petrol", "doors": 3, "transmission": "auto"},
    {"size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"size": "m", "fuel": "electric", "doors": 3, "transmission": "auto"},
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if session.exec(select(Car_DBModel)).first() is None:
            for obj in INITIAL_CARS:
                session.add(Car_DBModel.model_validate(obj))  # id=None → DB generates
            session.commit()
    yield

app = FastAPI(title="Car API", lifespan=lifespan)

app.include_router(cars.router)
