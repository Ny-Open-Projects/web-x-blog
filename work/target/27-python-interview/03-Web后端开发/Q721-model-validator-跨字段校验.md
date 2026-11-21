---
title: [Q721] model_validator 跨字段校验
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q721 · model_validator 跨字段校验

> 难度:★★★☆ | 标签:Pydantic v2, 校验

**问**:比如 start 必须小于 end、密码和确认密码一致,这类跨字段校验在 v2 里怎么写?

**答**:用 `model_validator`。`mode="before"` 接收**原始输入整体**(dict 甚至非 dict),适合做输入形态归一,比如把 `"10-20"` 字符串拆成两个字段;`mode="after"` 拿到**已构造好的模型实例**,适合做字段间关系断言,校验失败抛 ValueError,Pydantic 会包装成 ValidationError。after 阶段模型默认可变,可以顺手做规整后再返回 self。

```python
# file: code/03_Web后端开发/q721_model_validator.py
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
```

**追问**:
- before 阶段输入不是 dict 会怎样?——需要自己处理任意形态,比如字符串先解析,否则内部字段访问报错,错误信息对用户不友好。
- 校验之间有依赖导致顺序敏感怎么办?——把强依赖逻辑都收敛到一个 after 校验器,before 只做形态归一。
