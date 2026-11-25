---
title: "[Q5265] logging.lastResort 兜底：没有 handler 时日志到底去哪了"
date: 2026-11-25
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5265 · logging.lastResort 兜底：没有 handler 时日志到底去哪了

难度：P6 ｜ 标签：logging、lastResort、NullHandler、日志丢失、容器

基线：CPython 3.12.2，纯标准库；替换 `logging.lastResort` 捕获兜底输出，验证 handler 计数与级别过滤。

**问**：一个支付回调 worker 在启动早期打了一条 `logger.warning("duplicate callback")`，此时日志配置还没加载。容器日志里能看到这条消息，但格式和后面的 JSON 日志完全不一样，采集器解析失败直接丢弃；更奇怪的是，另一条 `logger.info("warmup")` 在同一次启动里彻底消失了。后来有同事给库加了 `logging.NullHandler()`，结果连 warning 也没了。没有 handler 时 logging 到底把日志写去哪？为什么 info 消失而 warning 出现？`NullHandler` 为什么会把兜底也关掉？

**答**：

- **结论**：`Logger.callHandlers()` 会沿 `propagate` 链收集 handler；如果**一个都没找到**，并且 `logging.lastResort` 不为 `None`，就把这条记录交给 `lastResort`。默认的 `lastResort` 是一个 `_StderrHandler`，level 是 `WARNING`，没有 formatter，所以输出形如 `duplicate callback`（只有 message），直接写 `sys.stderr`。`info` 消失有两层原因：logger 的有效级别（默认继承 root 的 `WARNING`）先把它过滤了；即使把 logger 调到 `DEBUG`，`lastResort` 自身的 `WARNING` 级别仍会挡住 info。`NullHandler` 是一个**真实 handler**，它让"找到的 handler 数"变成 1，于是 `lastResort` 不再启用，而它本身又什么都不做——所以 warning 也消失了。
- **取舍**：`lastResort` 的价值是"配置缺失时不要静默"，代价是输出不可控（无格式、无轮转、写 stderr）。库作者加 `NullHandler` 是为了避免"库未配置日志时向 stderr 乱喷"，但这会把兜底一起关掉；正确做法是**应用**在入口尽早 `dictConfig`/`basicConfig`，**库**只加 `NullHandler` 并且不假设自己拥有 root。另一个取舍是 `lastResort=None`：完全静默，适合 CLI 自己管理输出，但在服务端会把"配置漏了"变成"日志全丢"，必须配合启动自检（启动后检查 root 是否有 handler）。
- **实战**：worker 的启动顺序是"先起消费线程，再初始化日志"，回调在配置完成前就来了。修复：① 把日志初始化提到进程入口第一行，配置完成前用 `logging.basicConfig(level=WARNING, stream=sys.stderr)` 兜底；② 启动完成后断言 `logging.getLogger().handlers` 非空，否则拒绝启动（fail fast）；③ 采集器同时兼容"纯文本 stderr"与 JSON 两种格式，避免兜底日志被丢。上线后启动窗口的日志丢失从每周 3～5 条降到 0。

下面用 `StringIO` 接管 `lastResort`，验证默认级别、格式、`NullHandler` 的抑制效果，以及 `lastResort=None` 的完全静默。

```python
# lastResort 只在"整条 propagate 链一个 handler 都没有"时启用
import io
import logging

buffer = io.StringIO()
original_last_resort = logging.lastResort

logging.lastResort = logging.StreamHandler(buffer)
logging.lastResort.setLevel(logging.WARNING)
logging.lastResort.setFormatter(
    logging.Formatter("%(levelname)s:%(name)s:%(message)s")
)

logger = logging.getLogger("checkout.callback")
logger.handlers.clear()
logger.propagate = False          # 不向 root 传播, 模拟"没配置"的独立 logger
logger.setLevel(logging.DEBUG)    # logger 自身放行 DEBUG, 用于观察 handler 级别

logger.warning("paid %s", 42)
logger.info("warmup")             # 被 lastResort 的 WARNING 级别挡住
output = buffer.getvalue()
print("[1] 兜底输出:", repr(output))
assert output == "WARNING:checkout.callback:paid 42\n"
assert "warmup" not in output

# NullHandler 是真实 handler: 计数变为 1, lastResort 不再启用
logger.addHandler(logging.NullHandler())
logger.warning("swallowed by NullHandler")
print("[2] 加 NullHandler 后:", repr(buffer.getvalue()))
assert "swallowed" not in buffer.getvalue()

# 去掉 NullHandler, 再把 lastResort 设为 None: 完全静默
logger.handlers.clear()
logging.lastResort = None
logger.warning("silent")
print("[3] lastResort=None 后:", repr(buffer.getvalue()))
assert "silent" not in buffer.getvalue()

logging.lastResort = original_last_resort
print("[4] 已恢复 lastResort; 默认是 WARNING 级 _StderrHandler")
```

**追问一**：`logger.propagate=False` 且没有 handler 时，还会用 `lastResort` 吗？—— 会。`callHandlers` 先沿链找 handler，`propagate=False` 只是不继续往上找；如果当前 logger 自己没有 handler，最终 `found == 0`，仍然走 `lastResort`。真正的区别是：`propagate=True` 时如果 root 配了 handler，就用 root 的，`lastResort` 不参与；`propagate=False` 则把"有没有 handler"完全交给当前 logger，没配就兜底。

**追问二**：为什么 `logging.basicConfig()` 之后再调用不生效？—— `basicConfig` 只在 root 没有任何 handler 时才添加 handler；如果上一次已经加过，第二次调用是 no-op（除非 `force=True`，3.8+）。这和 `lastResort` 的交互是：一旦 root 有了 handler，`found > 0`，兜底永远不再触发。排查"日志格式不对"时，先看 `logging.getLogger().handlers` 和每个 logger 的 `propagate`，而不是怀疑 `lastResort`。

## 背诵要点

- `lastResort` 只在整条 propagate 链**一个 handler 都没有**时启用，默认是 WARNING 级的 stderr handler、无格式。
- `NullHandler` 是真实 handler，会抑制 `lastResort`；库加它是为了不污染 stderr，应用必须自己配置日志。
- `lastResort=None` 完全静默；服务端应在启动后断言 root 有 handler，避免"配置漏了 = 日志全丢"。

## 复盘追问

- 为什么把 logger 调到 DEBUG 后 info 仍然不出现？（`lastResort` 自身 level=WARNING，handler 级过滤在 logger 级之后）
- 库代码加 `NullHandler` 和应用配置日志的职责边界在哪？（库只负责不报错、不污染；应用负责输出目的地与格式）
