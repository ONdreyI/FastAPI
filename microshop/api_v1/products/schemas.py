from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):  # basis model

    name: str
    description: str
    price: int
    tax: int


class ProductCreate(ProductBase):  # create model
    pass


class ProductUpdate(ProductCreate):  # update model
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None
    tax: int | None = None


class Product(ProductBase):  # to call back data
    model_config = ConfigDict(from_attributes=True)  # свойства берутся из атрибутов
    id: int
