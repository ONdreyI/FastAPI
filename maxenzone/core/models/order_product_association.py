from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint

from .base import Base


order_product_association_table = Table(
    "order_product_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
    UniqueConstraint("order_id", "product_id"),
)
