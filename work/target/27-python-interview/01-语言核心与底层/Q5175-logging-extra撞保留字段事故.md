---
title: "[Q5175] logging extra 撞 LogRecord 保留字段事故"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5175 · logging extra 撞 LogRecord 保留字段事故

难度：P6 ｜ 标签：logging、LogRecord、extra、结构化日志、事故复盘

**问**：接入统一日志封装后，支付接口突然开始 500：日志调用本身抛 `KeyError: "Attempt to overwrite 'message' in LogRecord"`。`logging` 的 `extra` 到底往哪里写？哪些键是保留字段、为什么不能覆盖？为什么有些冲突在 `logger.info()` 当场炸、有些要等到 Formatter 格式化才变成 `KeyError` 文本？与 Q501（LoggerAdapter）、Q502（propagate）、Q503（延迟格式化）的边界在哪？

**答**：
结论：`Logger.makeRecord()` 先构造一条 `LogRecord`（自带 `name/msg/args/levelname/levelno/pathname/filename/module/lineno/funcName/created/msecs/relativeCreated/thread/threadName/processName/process/exc_info/exc_text/stack_info`，3.12 还有 `taskName`），然后把 `extra` 的每个键**直接写进 `record.__dict__`**；如果键已存在，或键是 `message`/`asctime`（这两个由 Formatter 在格式化时生成），就抛 `KeyError`。所以 `extra={"message": ...}`、`extra={"name": ...}` 这类"看起来只是加了个字段"的调用会在日志语句处直接打断业务。另一类冲突是 Formatter 模板引用了不存在的字段（`%(order_id)s` 但这条日志没传），格式化时才抛 `ValueError: Formatting field not found`，被 `logging` 吞成 `--- Logging error ---` 或把异常写进输出。Q501 讲用 LoggerAdapter 统一注入上下文，Q502 讲层级/重复输出，Q503 讲为什么用 `%s` 延迟格式化；本题专攻"extra 的命名空间与保留字段"。

取舍：不要把用户输入/动态键名直接塞进 `extra`——键名必须是代码里固定的标识符。需要一组结构化上下文时，用**单一命名空间**：`extra={"ctx": {"request_id": ..., "user_id": ...}}`，Formatter 用 `%(ctx)s` 或自定义 `format()` 取；或者用 `LoggerAdapter`/`structlog` 在入口统一注入。上线前用一条"最全字段"的日志跑一遍 Formatter，能在启动期暴露缺字段问题。

实战：事故形态是"日志中间件把 HTTP 头解析成 dict 直接 `extra=headers`"，某个请求带了名为 `message` 或 `name` 的头（或上游把 header 名规范化成小写后撞上 `levelno`），日志调用抛异常，异常又进错误处理，最后 500。下面复现三种情况：正常自定义键、撞 `message`、撞 `name`，并展示 Formatter 只在字段存在时才能工作。

```python
import io
import logging

stream = io.StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)s %(message)s order=%(order_id)s"))
log = logging.getLogger("pay")
log.handlers[:] = [handler]
log.setLevel(logging.INFO)
log.propagate = False


def emit(**extra):
    try:
        log.info("charge ok", extra=extra)
        return "OK: " + stream.getvalue().splitlines()[-1]
    except KeyError as e:
        return f"KeyError: {e}"


print(emit(order_id="o-1"))
print(emit(message="client-controlled"))
print(emit(name="x", levelno=99))
```

**追问一**：为什么 `message` 和 `asctime` 被特殊对待，而 `name` 只是"已存在"？——`message` 是 `Formatter.format()` 调 `record.getMessage()` 后写入的最终文本，`asctime` 是格式化时按 `datefmt` 生成的；它们是"派生字段"，不允许外部预先占用，否则格式化结果不可预期。`name`、`levelno` 等是 `LogRecord.__init__` 已经设置的原始字段，`extra` 写入时发现键已存在就报错。两者都归 `makeRecord` 的同一段检查，只是 `message/asctime` 即使当前不存在也被列入禁用名单。

**追问二**：如果业务确实需要一个叫 `name` 的字段，怎么安全落地？——换命名空间（`ctx.name`）是首选；其次是在 Formatter 里用 `record.__dict__.get("biz_name")` 自定义输出，避免占用保留键；再不然用 `LoggerAdapter` 的 `process()` 把上下文合并进 `msg` 的参数而不是 record 属性。不要用 `setattr(record, "name", ...)` 硬改，那会破坏依赖 `record.name` 做过滤/路由的 Handler 和过滤器。

## 背诵要点
- `extra` 的键直接进 `LogRecord.__dict__`；撞已有字段或 `message`/`asctime` 立即 `KeyError`。
- Formatter 引用缺失字段是另一类错误，发生在格式化阶段；启动时用最全字段自检。
- 结构化上下文放单一命名空间（`ctx`）或用 LoggerAdapter，键名必须是代码常量，不能来自用户输入。

## 复盘追问
- 接入结构化日志后支付接口 500，栈停在 `logger.info`，如何定位是 `extra` 撞键并修复？（保留字段清单、命名空间、入口统一注入）
- 为什么"日志里出现 `--- Logging error ---` 但业务没抛异常"？与 `extra` 撞键的区别是什么？（Formatter 阶段缺字段/格式化异常被 handler 捕获）
