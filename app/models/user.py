from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.order import Order


class UserRole(str, Enum):
    """User roles enum"""

    client = "client"
    courier = "courier"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    role: Mapped[UserRole] = mapped_column(default=UserRole.client)

    client_orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="client", foreign_keys="[Order.client_id]"
    )
    courier_orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="courier", foreign_keys="[Order.courier_id]"
    )

    created_at: Mapped[datetime] = mapped_column(default=func.now())
