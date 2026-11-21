try:
    from pydantic import BaseModel, computed_field
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Rect(BaseModel):
    w: float
    h: float

    @property
    def area(self) -> float:        # 普通 property 不进序列化
        return self.w * self.h

    @computed_field(alias="area2x")
    @property
    def area2x(self) -> float:      # 计算字段进序列化
        return self.area * 2

r = Rect(w=3, h=4)
print(r.area)
print(r.model_dump())
