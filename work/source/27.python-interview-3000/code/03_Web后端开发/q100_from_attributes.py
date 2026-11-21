try:
    from pydantic import BaseModel, ConfigDict
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class UserORM:
    """模拟一个 ORM 对象"""
    def __init__(self):
        self.id = 1
        self.name = 'alice'
        self.password_hash = 'secret'
        self.created_at = '2026-01-01'

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='forbid')
    id: int
    name: str
    created_at: str

user = UserORM()
print(UserOut.model_validate(user))   # password_hash 被过滤
