---
title: [Q036] Protocol 与结构化子类型
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q036 · Protocol 与结构化子类型

> 难度:★★☆ | 标签:typing

**问**:鸭子类型很好,但静态检查器怎么表达「只要有 run 方法就行」?

**答**:`typing.Protocol` 定义结构化接口:任何具备兼容方法/属性的对象都视为实现了该 Protocol,无需显式继承,这就是静态检查器中的鸭子类型。配合 `@runtime_checkable` 还可用 `isinstance` 做运行时检查(仅检查方法存在,不检查签名)。相比 ABC,Protocol 不要求目标类知情,适合适配第三方类型。

```python
# file: code/01_语言核心与底层/q036_protocol.py
from typing import Protocol, runtime_checkable

@runtime_checkable
class Runner(Protocol):
    def run(self) -> str:
        """结构声明,不含实现"""

class Job:
    def run(self) -> str:
        return "job running"

class StubRunner:
    def run(self) -> str:
        raise NotImplementedError

class NotARunner:
    pass

def execute(r: Runner) -> str:
    return r.run()

if __name__ == "__main__":
    print(execute(Job()))                # 无需继承 Runner
    print(isinstance(Job(), Runner))     # True,运行时检查
    print(isinstance(NotARunner(), Runner))  # False

    class Legacy:
        def run(self):
            return "legacy"
    print(execute(Legacy()))             # 兼容旧类,结构满足即可
```

**追问**:1) Protocol 与 ABC 怎么选?——需要给实现类提供共享代码或强制注册时用 ABC;只需约束形状、类不可修改时用 Protocol。2) @runtime_checkable 的 isinstance 检查什么?——只检查方法/属性名字存在,不检查签名与返回类型;运行时严谨校验靠静态检查器,这点要主动说出来防止误用。3) Protocol 和鸭子类型的关系?——Protocol 把鸭子类型搬进静态检查:mypy 只看形状不看继承;对无法修改的第三方类型适配是首选,而 ABC 适合自家继承体系并共享实现。
