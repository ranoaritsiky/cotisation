from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from ..database.db_connection import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    date_created = Column(Date, default=datetime.now())
    id_member = Column(String)

    contribution_id = relationship("contribution", back_populates="member_id")


class Contribution(Base):
    __tablename__ = "contribution"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, default=0)

    member_id = relationship("members", back_populates="contribution_id")

    