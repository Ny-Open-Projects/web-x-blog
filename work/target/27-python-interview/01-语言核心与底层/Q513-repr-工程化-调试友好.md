---
title: [Q513] __repr__ 工程化:调试友好
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q513 · __repr__ 工程化:调试友好

> 难度:★★☆☆ | 标签:repr, 调试

**问**:为什么说默认的 <Object at 0x...> 是调试阻力?好的 __repr__ 有什么标准?

**答**:repr 出现在 traceback、日志、容器打印、调试器里,信息量直接决定排障速度。标准:1) eval 友好——`Money(1999)` 这种「粘回去就能重建」的形式;2) 包含身份判别字段(金额、id、状态),不含全量 dump;3) 永不抛异常(字段可能是 None 时要兜底);4) 大集合截断显示前几项。__str__ 面向最终用户(如 ¥19.99),__repr__ 面向开发者;只定义一个时定义 __repr__,因为容器与未定义 __str__ 的场景都回落到它。dataclass 自动生成的 __repr__ 已达标,自定义类值得花两分钟写。

```python
# file: code/01_语言核心与底层/q513_repr_engineering.py
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __repr__(self):
        return f"Money({self.cents!r})"       # eval 友好

    def __str__(self):
        return f"¥{self.cents / 100:.2f}"     # 面向用户

class Task:
    def __init__(self, name, status, deps=None):
        self.name = name
        self.status = status
        self.deps = deps or []

    def __repr__(self):
        deps = ",".join(self.deps[:3]) + ("..." if len(self.deps) > 3 else "")
        return f"Task(name={self.name!r}, status={self.status!r}, deps=[{deps}])"

if __name__ == "__main__":
    m = Money(1999)
    print(repr(m), "|", str(m))
    t = Task("build", "running", ["a", "b", "c", "d", "e"])
    print(repr(t))
    print([m, m])                             # 容器自动用 __repr__
    print(f"debug: {t!r}")
```

**追问**:1) 为什么 __repr__ 不该有副作用或抛异常?——它会被调试器、日志框架在任意时刻调用,副作用会扭曲程序行为,异常会把原本的报错掩盖成更难查的二次错误。2) repr 与 str 的工程分工?——repr 是无歧义形式(理想情况 eval 可还原),str 是人读形式;dataclass 自动生成的 repr 含全部字段,敏感字段要 field(repr=False)。3) 调用协议的底层?——repr() 调 type(obj).__repr__,内置容器自动用元素的 repr;f-string 的 !r 转换、调试器、traceback 都走它——所以它必须便宜且安全。4) 生产陷阱?——嵌套大结构 repr 把调试器卡死(要截断或省略);lazy 属性在 repr 里触发加载(DB 查询),日志一行打一次库;密钥进 repr 泄漏到日志。
