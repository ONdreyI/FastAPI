from sqlalchemy import Table, Column, ForeignKey

from .base import Base


order_product_association_table = Table(
    "order_product_association",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)
