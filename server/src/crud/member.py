from sqlalchemy.orm import Session

from ..models.Club import Member, Contribution

# read
def get_member_by_id(db:Session, user_id:int):
    return db.query(Member).filter(Member.id == user_id).first()

def get_members(db:Session,skip: int = 0, limit: int = 100):
    return db.query(Member).offset(skip).limit(limit).all()