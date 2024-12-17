# models
from sqlalchemy import String, BIGINT, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
from typing import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]
str_256 = Annotated[str, mapped_column(String(256))]
bigint = Annotated[int, mapped_column(BIGINT)]


