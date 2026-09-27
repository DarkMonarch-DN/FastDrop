from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db import get_db_session
from app.services.user import UserService


async def get_user_service(session: Annotated[AsyncSession, Depends(get_db_session)]):
    return UserService(session)


# Aliases
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
