---
title: "[Q7229] 库在 import 时调 basicConfig：应用的日志配置被悄悄改掉"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7229 · 库在 import 时调 basicConfig：应用的日志配置被悄悄改掉

难度：P7 ｜ 标签：logging、basicConfig、root logger、库设计

基线：Python 3.12；`logging.basicConfig(force=True)`、`NullHandler`、`propagate`；纯 Python 模拟 handler 语义。

**问**：一个内部工具库在模块顶层写了 `logging.basicConfig(level=logging.DEBUG)`。应用自己配了 JSON formatter 和 INFO 级别，但只要 import 了这个库，日志就变成 DEBUG 的纯文本，而且重复输出两遍。basicConfig 不是"没配置时才生效"吗？

**答**：
- **结论**：`basicConfig()` 只在 **root logger 没有任何 handler** 时才添加 handler。但"没配置"是按**调用时刻**判断的：库 import 发生在应用配置之前，它就抢先装了一个 `StreamHandler` + 默认格式；之后应用再调 `basicConfig(...)` 因为已有 handler 而**静默不生效**（除非 `force=True`）。重复输出通常是 root 有 handler + 子 logger 也加了 handler 且 `propagate=True`（默认），一条记录被打印两次。
- **取舍**：库**不应该**配置 root logger——它不知道宿主的输出目标（文件/stdout/JSON/采集器/容器日志）。库只该 `logging.getLogger(__name__)` 并挂一个 `NullHandler`，把配置权留给应用入口。应用侧统一 `dictConfig`，或 `basicConfig(force=True)` 夺回控制权（但会清掉别人加的 handler，库不能用）。
- **实战**：① 库顶层只写 `logging.getLogger(__name__).addHandler(logging.NullHandler())`；② 应用入口显式 `dictConfig`，禁止业务代码散落 `basicConfig`；③ CI 加 lint 规则禁止库目录出现 `basicConfig`；④ 排查重复日志先看 `logger.handlers`、`logger.propagate`、`logger.level` 三件套。

```python
"""basicConfig 只生效一次、子 logger 冒泡导致重复输出的最小模型。"""
from typing import Callable

Handler = Callable[[str], None]


class Logger:
    def __init__(self, name: str, parent: "Logger | None" = None) -> None:
        self.name = name
        self.parent = parent
        self.handlers: list[Handler] = []
        self.propagate = True

    def emit(self, record: str) -> None:
        for h in self.handlers:
            h(record)
        if self.propagate and self.parent is not None:
            self.parent.emit(record)        # 默认冒泡：同一条记录继续往上走


class Registry:
    def __init__(self) -> None:
        self.root = Logger("root")
        self.loggers: dict[str, Logger] = {"root": self.root}

    def get(self, name: str) -> Logger:
        if name in self.loggers:
            return self.loggers[name]
        parent = self.get(name.rsplit(".", 1)[0]) if "." in name else self.root
        lg = Logger(name, parent)
        self.loggers[name] = lg
        return lg

    def basic_config(self, handler: Handler, force: bool = False) -> bool:
        """只在 root 没有 handler 时生效；force=True 才强制重配。"""
        if self.root.handlers and not force:
            return False
        if force:
            self.root.handlers.clear()
        self.root.handlers.append(handler)
        return True


if __name__ == "__main__":
    reg = Registry()

    # 1) 库在 import 时抢先配置 root
    lib = reg.get("mylib")
    print("库 basicConfig 生效:", reg.basic_config(lambda r: print("[lib]", r)))

    # 2) 应用随后配置：静默失败
    print("应用 basicConfig 生效:", reg.basic_config(lambda r: print("[app-json]", r)),
          "-> False，JSON 配置被忽略")

    app = reg.get("myapp")
    app.emit("hello")
    print("  这一行是 lib 的 handler 打的，不是应用的 JSON handler")

    # 3) 子 logger 自己加 handler 且 propagate=True => 打两遍
    child = reg.get("myapp.sub")
    child.handlers.append(lambda r: print("[child]", r))
    print("--- 子 logger 也加了 handler ---")
    child.emit("dup")

    # 4) 正确姿势：库只挂 NullHandler，root 保持干净
    reg2 = Registry()
    quiet = reg2.get("mylib")
    quiet.handlers.append(lambda r: None)          # NullHandler
    print("库挂 NullHandler 后 root handlers:", reg2.root.handlers)
    print("结论：库不许配置 root；应用入口 dictConfig；重复日志查 propagate 与 handlers")
```

**追问一**：`basicConfig` 在 3.8 之后多了哪些参数？
→ 解析：`force=True`（先移除 root 上已有 handler 再重配）、`encoding`、`errors`（3.9+）。`force` 是**应用侧**夺回控制权的正确姿势，但会清掉其他库/框架装的 handler，所以库代码绝不能用。

**追问二**：为什么同一条日志会打两遍？
→ 解析：子 logger 自己有 handler 且 `propagate=True`（默认）时，记录先由子 handler 输出，再冒泡到 root 的 handler 输出一次。修法二选一：子 logger 不挂 handler（只依赖 root），或设 `propagate=False`（但这样 root 上的统一格式就管不到它了，按场景选）。
