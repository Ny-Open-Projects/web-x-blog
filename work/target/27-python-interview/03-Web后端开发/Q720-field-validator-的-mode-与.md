---
title: [Q720] field_validator 的 mode 与校验信息
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q720 · field_validator 的 mode 与校验信息

> 难度:★★★☆ | 标签:Pydantic v2, 校验

**问**:Pydantic v2 里 field_validator 的 mode=before 和 mode=after 有什么区别?什么时候必须用 before?

**答**:`mode="before"` 在**类型解析之前**执行,拿到的是原始输入(str/dict/任意对象),适合做输入规整,比如把逗号分隔字符串拆成列表;`mode="after"` 在类型解析之后执行,拿到的是已转换的目标类型,适合做值域校验。同一个字段可以叠多个 validator,按声明顺序执行。`info.data` 能拿到**之前字段**的校验结果,所以字段声明顺序会影响它。

```python
# file: code/03_Web后端开发/q720_field_validator.py
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
```

**追问**:
- validator 抛出的异常怎么变成 422?——Pydantic 把 ValueError 收集进 ValidationError,FastAPI 的 RequestValidationError 处理器统一转成 422 响应。
- 需要用"后面字段"的值怎么办?——field_validator 只能看到前面的字段,跨字段校验应改用 model_validator。
