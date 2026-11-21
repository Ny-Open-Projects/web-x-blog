try:
    from pydantic import BaseModel, model_validator
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Range(BaseModel):
    start: int
    end: int
    label: str = "range"

    @model_validator(mode="before")
    @classmethod
    def coerce_pair(cls, data):
        if isinstance(data, str) and "-" in data:
            a, b = data.split("-", 1)
            data = {"start": a, "end": b}
        return data

    @model_validator(mode="after")
    def check_order(self):
        if self.start >= self.end:
            raise ValueError("start 必须小于 end")
        self.label = f"{self.label}:{self.start}-{self.end}"
        return self

print(Range("10-20").model_dump())
try:
    Range(start=5, end=2)
except Exception as e:
    print("失败类型:", type(e).__name__)
