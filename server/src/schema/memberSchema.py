from .baseSchema import MemberBase

class MemberCreate(MemberBase):
    first_name: str
    last_name: str
    email: str
    id_member: str


class Member(MemberBase):
    id: int
    first_name: str
    last_name: str
    email: str
    id_member: str

    class Config:
        orm_mode = True