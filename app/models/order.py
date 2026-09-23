from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.user import User


class OrderStatus(str, Enum):
    """Order status enum"""

    created = "created"
    in_delivery = "in_delivery"
    completed = "completed"
    cancelled = "cancelled"


class Order(Base):
    """Orders table"""

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    description: Mapped[str]
    status: Mapped[OrderStatus] = mapped_column(default=OrderStatus.created)

    from_lat: Mapped[float]
    from_lon: Mapped[float]

    to_lat: Mapped[float]
    to_lon: Mapped[float]

    client_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    client: Mapped["User"] = relationship(
        "ClientOrders", back_populates="client_orders"
    )

    courier_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    courier: Mapped["User"] = relationship(
        "CourierOrders", back_populates="courier_orders"
    )

    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
