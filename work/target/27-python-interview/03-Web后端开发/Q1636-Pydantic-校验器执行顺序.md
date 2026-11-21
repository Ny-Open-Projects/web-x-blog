---
title: [Q1636] Pydantic 校验器执行顺序
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1636 · Pydantic 校验器执行顺序

> 难度:★★★★ | 标签:Pydantic, 校验

**问**:Pydantic 里 field_validator 和 model_validator 的执行顺序到底是什么?

**答**:顺序规则:先按字段定义顺序逐字段执行,每个字段内部先 mode=before 再 mode=after;所有字段通过后,才执行 model_validator(mode=after) 的跨字段校验;任何一步失败立即短路,后面的校验器不再运行。两个推论:before 校验器拿到的是原始输入,所以能做清洗;after 拿到的是类型化后的值,所以能做强类型断言;model 级校验看到完整字段集,适合起止时间先后这类跨字段约束。执行顺序不要靠背,写一个记录执行序号的用例锁住它,升级 Pydantic 大版本时它就是回归哨兵。

```python
# file: code/03_Web后端开发/q1636_validator_order.py
"""Pydantic 校验器执行顺序: 字段级按定义顺序, 模型级收尾, 失败短路(纯标准库模拟)。"""
try:
    import pydantic
    HAS_PYDANTIC = True
except ImportError:
    HAS_PYDANTIC = False
    print("[降级] 未安装 pydantic, 以下用管线模拟同一执行顺序")


class Pipeline:
    """模拟: 每个字段先跑 before 校验器, 再跑 after, 最后模型级。"""

    def __init__(self):
        self.order = []

    def field_before(self, name, fn):
        def step(data):
            self.order.append(f"{name}.before")
            data[name] = fn(data.get(name))
        return step

    def field_after(self, name, fn):
        def step(data):
            self.order.append(f"{name}.after")
            if not fn(data.get(name)):
                raise ValueError(f"{name} 未通过格式校验")
        return step

    def model_after(self, fn):
        def step(data):
            self.order.append("model.after")
            fn(data)
        return step


def run(steps, data):
    for step in steps:
        step(data)          # 任一步失败即短路, 后面的校验器不再执行
    return data


p = Pipeline()
steps = [
    p.field_before("email", lambda v: str(v).strip().lower()),
    p.field_after("email", lambda v: "@" in v),
    p.field_before("age", lambda v: int(v)),
    p.field_after("age", lambda v: 0 <= v < 150),
    p.model_after(lambda d: d.update(summary=f'{d["email"]}-{d["age"]}')),
]
print("合法输入:", run(steps, {"email": " A@B.COM ", "age": "18"}))
print("执行顺序:", p.order)

bad = Pipeline()
steps_bad = [
    bad.field_before("email", lambda v: str(v).strip().lower()),
    bad.field_after("email", lambda v: "@" in v),
    bad.field_before("age", lambda v: int(v)),
    bad.field_after("age", lambda v: 0 <= v < 150),
]
try:
    run(steps_bad, {"email": "not-an-email", "age": "18"})
except ValueError as e:
    print("短路于:", e, "| 后续校验器不再执行, 已执行:", bad.order)
```

**追问**:
- before 与 after 里抛错的报错有何不同?——before 多是类型错误如解析失败,after 是业务断言错误,客户端文案要区分。
- 同一字段多个 before 校验器按什么顺序跑?——按装饰器注册顺序执行,定义顺序即执行顺序。
