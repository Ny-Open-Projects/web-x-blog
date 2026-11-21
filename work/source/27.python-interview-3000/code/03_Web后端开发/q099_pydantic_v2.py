try:
    from pydantic import BaseModel, Field, field_validator, model_validator
except ImportError:
    print("该题演示需要第三方库 pydantic:pip install pydantic,原理见正文")
    raise SystemExit(0)

class OrderIn(BaseModel):
    item: str = Field(..., min_length=1, max_length=50)
    quantity: int = Field(1, gt=0, le=100)
    price: float = Field(..., gt=0)
    discount: float = Field(0, ge=0, le=1)

    @field_validator('item')
    @classmethod
    def strip_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError('item 不能为空')
        return v

    @model_validator(mode='after')
    def check_total(self):
        if self.price * self.quantity < 1:
            raise ValueError('订单金额至少为 1 元')
        return self

order = OrderIn(item=' book ', quantity=2, price=9.9)
print(order.model_dump())   # {'item': 'book', 'quantity': 2, ...}
