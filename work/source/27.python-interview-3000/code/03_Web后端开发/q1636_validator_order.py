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
