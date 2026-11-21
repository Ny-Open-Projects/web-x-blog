---
title: [Q464] Literal、Final 与 Annotated
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q464 · Literal、Final 与 Annotated

> 难度:★★★☆ | 标签:typing, 注解

**问**:Literal、Final、Annotated 各解决什么问题?运行时读注解时能看到它们吗?

**答**:Literal["a","b"] 把类型收窄到具体取值集合,适合模式、开关、状态名,拼错在静态期就报错;Final 声明「不可重新赋值/覆盖」的常量,替代魔法数字的命名;Annotated[int, ...] 在类型上挂任意元数据,静态检查器忽略自定义部分,而框架(pydantic/FastAPI)在运行时通过 `get_type_hints(include_extras=True)` 读取并驱动校验。三者都是「零运行时成本、高静态收益」的注解,生产代码里 Literal + Final 能显著减少字符串参数的隐性错误。

```python
# file: code/01_语言核心与底层/q464_literal_final_annotated.py
from typing import Literal, Final, Annotated, get_type_hints

Mode = Literal["read", "write", "append"]

MAX_RETRIES: Final = 3

Timeout = Annotated[int, "seconds", "gt=0"]

def open_file(path: str, mode: Mode = "read") -> str:
    return f"opened {path} with {mode}"

def connect(host: str, timeout: Timeout = 5) -> str:
    return f"connected {host} timeout={timeout}"

if __name__ == "__main__":
    print(open_file("a.txt"))
    print(open_file("a.txt", "write"))
    print(open_file("a.txt", "rw"))       # 运行时不拦:mypy 才报错
    print(connect("db.local"))
    print(get_type_hints(connect, include_extras=True))
    print("MAX_RETRIES:", MAX_RETRIES)
```

**追问**:1) Final 变量被重新赋值运行时会报错吗?——不会,Final 只是静态声明;mypy/pyright 在检查阶段拦截,运行时它就是个普通变量。2) Annotated 的元数据谁能读?——静态检查器只消费第一个类型参数、其余透传;运行时 get_type_hints(include_extras=True) 返回 Annotated 包装,pydantic/FastAPI 从 __metadata__ 取约束驱动校验与文档生成。3) Literal 的类型代数?——Literal["a"] | Literal["b"] 等价 Literal["a","b"],检查器做字面量集合运算实现收窄;isinstance 配 Literal 无意义,收窄只发生在静态控制流分析里。4) 生产陷阱?——Literal 取值集与数据库枚举/远端 API 漂移,新增值运行时静默通过;字面量集合要从单一 schema 生成,边界处再配运行时校验兜底。
