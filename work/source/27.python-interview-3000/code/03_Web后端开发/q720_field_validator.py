try:
    from pydantic import BaseModel, ValidationError, field_validator
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Order(BaseModel):
    items: list[str] = []

    @field_validator("items", mode="before")
    @classmethod
    def split_str(cls, v, info):
        if isinstance(v, str):
            return [x for x in v.split(",") if x]
        return v

    @field_validator("items")
    @classmethod
    def not_empty(cls, v, info):
        if not v:
            raise ValueError("至少购买一件商品")
        return v

print(Order(items="a,b,c").items)
try:
    Order(items="")
except ValidationError as e:
    print("校验失败:", e.errors()[0]["msg"])
