---
title: [Q2641] logger.exception 与 exc_info:把 traceback 记进日志的正确姿势
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2641 · logger.exception 与 exc_info:把 traceback 记进日志的正确姿势

> 难度:★★☆☆☆ | 标签:logging, 异常记录, 排障

**问**:`logger.error(str(e))` 为什么是反模式?记录 traceback 的标准写法是什么?

**答**:在 except 块里,`logger.exception("msg")` 与 `logger.error("msg", exc_info=True)` 等价,都会把**当前正在处理的异常**连同完整 traceback 记成 ERROR——这是排障时的第一手信息:类型、消息、完整调用栈,缺一不可。`logger.error(str(e))` 只留一行消息,丢掉栈,基本等于销毁现场。两个变体:不在 except 块内又想记某个异常对象,用 `exc_info=err` 显式传入(会把该异常的 traceback 展开);想记 WARNING 但附栈,同样 `exc_info=True`。延迟格式化纪律依然适用:消息用 `%s` 占位,让字符串拼接只在真正输出时发生。

```python
# file: code/01_语言核心与底层/q2641_logger_exception.py
"""logger.exception 与 exc_info 的三种用法。"""
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("demo")


def load(path):
    raise FileNotFoundError(path)


if __name__ == "__main__":
    task_id = "job-7"

    try:
        load("/etc/missing.conf")
    except FileNotFoundError:
        log.exception("任务 %s 加载配置失败", task_id)     # 等价 exc_info=True

    try:
        load("/etc/missing.conf")
    except FileNotFoundError as err:
        log.warning("任务 %s 可跳过: %s", task_id, err, exc_info=True)

    saved = None
    try:
        load("/etc/missing.conf")
    except FileNotFoundError as err:
        saved = err
    if saved is not None:
        log.error("延迟记录: %s", saved, exc_info=saved)
```

**追问**:1) logger.exception 能在 except 块外用吗?——能调用但没有「当前异常」可挂,栈信息会缺失或不准;块外想带栈必须 exc_info=异常对象。2) 正确姿势全家桶?——except 块内 logger.exception("...") 等价 error(exc_info=True);块外 error("...", exc_info=e) 或 error(..., exc_info=(t,v,tb));debug 也支持 exc_info 供细粒度排查。3) 与日志重复的治理?——每层都 exception 会重复输出;约定只在边界记录一次(Q2642);exc_info 与 traceback 文本分离交给 formatter。4) 生产陷阱?——块外裸 exception 没栈;exc_info=True 在无异常上下文;同一异常多层记录三次。
