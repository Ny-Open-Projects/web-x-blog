try:
    from pydantic import BaseModel, field_validator, model_validator
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class BatchDeleteIn(BaseModel):
    ids: list[int]

    @field_validator('ids')
    @classmethod
    def no_empty(cls, v: list[int]) -> list[int]:
        if not v:
            raise ValueError('ids 不能为空')
        if len(v) != len(set(v)):
            raise ValueError('ids 存在重复')
        return v

class NotifyIn(BaseModel):
    email: str | None = None
    phone: str | None = None

    @model_validator(mode='after')
    def exclusive_channel(self):
        if bool(self.email) == bool(self.phone):
            raise ValueError('email 与 phone 必须二选一')
        return self

print(BatchDeleteIn(ids=[1, 2]).model_dump())
print(NotifyIn(phone='13800000000').model_dump())
