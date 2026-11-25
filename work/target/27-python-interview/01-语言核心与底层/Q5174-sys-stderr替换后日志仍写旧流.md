---
title: "[Q5174] sys.stderr 被替换后日志仍写旧流"
date: 2026-11-23
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5174 · sys.stderr 被替换后日志仍写旧流

难度：P6 ｜ 标签：logging、StreamHandler、sys.stderr、重定向、可观测性

**问**：一个服务在启动时 `logging.basicConfig()` 建了 `StreamHandler`，运行期为了实现"日志双写"把 `sys.stderr` 换成自己的 `Tee` 对象；结果文件里有日志，但 `Tee` 里一条都没有。`StreamHandler` 到底在什么时候取 `sys.stderr`？为什么换 `sys.stderr` 不影响已经建好的 handler？`logging.basicConfig(force=True)`、`handler.setStream()`、`os.dup2()` 三种做法分别改的是哪一层？和 Q502（propagate）、Q503（延迟格式化）的边界在哪？

**答**：
结论：`logging.StreamHandler()` 在**构造时**就把 `sys.stderr` 赋给 `self.stream`（`stream=None` 时才用 `sys.stderr`，但也是在 `__init__` 里取），之后 `emit()` 一直往这个对象写。运行期把 `sys.stderr` 指向新对象，只是改了模块属性，handler 手里仍是旧引用；旧流如果已被关闭，`emit()` 会捕获异常并走 `handleError()`（默认打印 `--- Logging error ---` 到 `sys.stderr`，而此时 stderr 也可能已换）。所以"换 `sys.stderr` 实现日志重定向"对已存在的 handler 无效。三种修法层次不同：`handler.setStream(new_stream)`（3.7+）改 handler 的引用；`basicConfig(force=True)` 移除并重建 root handlers（会丢自定义配置）；`os.dup2(fd, 2)` 改的是**文件描述符 2** 的指向，对任何持有 fd 2 的对象（包括 C 扩展、子进程继承）都生效，但不会改变 Python 层 `sys.stderr` 对象本身。

取舍：应用层想动态改日志目的地，优先显式持有 handler 并 `setStream()`，或在配置里用 `QueueHandler`/自定义 handler；`dup2` 适合"进程级重定向"（守护化、容器日志），但要注意 `sys.stderr` 仍指向旧 fd 号，只是 fd 号的内容变了；`basicConfig(force=True)` 适合测试/启动期，运行期重建会丢 handler 状态、可能重复/丢日志。不要依赖"替换 `sys.stderr`"这种隐式约定，库代码更不该假设它。

实战：事故形态是"接入日志采集 Sidecar 后，业务日志在容器 stdout 有、采集文件没有；代码里明明换过 `sys.stderr`"。下面复现：handler 创建后替换 `sys.stderr`，日志仍写旧流，新 `StringIO` 为空；`setStream(sys.stderr)` 后新流才收到。注意第一行会打到真实 stderr，这是预期的。

```python
import io
import logging
import sys

handler = logging.StreamHandler()                 # 创建时捕获 sys.stderr
log = logging.getLogger("svc")
log.handlers[:] = [handler]
log.setLevel(logging.INFO)
log.propagate = False

old_stderr = sys.stderr
captured = io.StringIO()
sys.stderr = captured                             # 运行期替换 sys.stderr
log.warning("redirect 之后的日志")

print("handler.stream is 旧 stderr:", handler.stream is old_stderr)
print("新 stderr 捕获到:", repr(captured.getvalue()))

handler.setStream(sys.stderr)                     # 3.7+：显式重绑
log.warning("重绑之后的日志")
print("重绑后捕获到:", repr(captured.getvalue()))

sys.stderr = old_stderr
```

**追问一**：`os.dup2` 重定向为什么"看起来生效"？——`dup2(newfd, 2)` 让 fd 2 指向新的打开文件描述；`sys.stderr` 对象内部仍保存 fd 2，所以它写出去的内容会到新目标。区别在于：`dup2` 影响所有使用 fd 2 的代码（C 扩展、`print(file=sys.stderr)`、子进程继承），但不改变 Python 对象的身份；`setStream` 只影响这个 handler，其它写 `sys.stderr` 的代码不受影响。排查时要分清"对象替换"与"fd 重定向"两层。

**追问二**：`logging.basicConfig()` 为什么有时候完全不生效？——它只在 root **没有任何 handler** 时才配置；如果之前已经有人（库/框架/上一次调用）加过 handler，再调 `basicConfig()` 是空操作。`force=True`（3.8+）会先移除 root 现有 handler 再配置，所以能"重来"，但会丢掉之前的自定义 handler/过滤器。生产上更稳的是显式 `dictConfig`（注意 `disable_existing_loggers`，Q5177）或自己构造 handler，别依赖 `basicConfig` 的隐式条件。

## 背诵要点
- `StreamHandler` 在构造时捕获 `sys.stderr`；之后替换 `sys.stderr` 不影响已建 handler，日志仍写旧流。
- 修法分层：`handler.setStream()` 改引用；`basicConfig(force=True)` 重建 root；`os.dup2` 改 fd 2 的指向（影响所有用 fd 2 的代码）。
- `basicConfig()` 仅在 root 无 handler 时生效；生产用显式配置，注意 `disable_existing_loggers`。

## 复盘追问
- 替换 `sys.stderr` 后采集文件没有日志、容器 stdout 有，如何解释并修复？（构造时捕获、setStream、dup2 的层次差异）
- `basicConfig(force=True)` 和 `dictConfig` 各会带来什么副作用？（丢自定义 handler、disable_existing_loggers 静默）
