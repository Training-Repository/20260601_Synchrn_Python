from sqlmodel import SQLModel, Field


class CarInput(SQLModel):
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"


class Car(CarInput):
    id: int


class Car_DBModel(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)