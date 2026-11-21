---
title: [Q1102] json logger 与 contextvars 上下文注入
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1102 · json logger 与 contextvars 上下文注入

> 难度:★★★★ | 标签:logging, contextvars

**问**:每条日志都要带 trace_id 和 user_id,又不想每处调用都手动传参,怎么落地?

**答**:用 `contextvars` 存请求级上下文,Formatter 统一注入:请求入口 set 一次 trace_id/user_id,之后任意层 logger.info 都自动携带,业务代码零侵入。输出用 JSONFormatter 把 record 序列化成一行 JSON,字段固定(ts/level/msg/logger/上下文字段),采集端直接索引。注意:线程模型下 contextvars 每线程独立;asyncio 下自动随 task 传播,这正是它优于 threading.local 的地方;exc_info 要在 formatter 里格式化进 JSON,别丢栈。

```python
# file: code/05_数据分析与工程化/q1102_json_logging.py
import contextvars
import json
import logging

trace_id = contextvars.ContextVar("trace_id", default="-")
user_id = contextvars.ContextVar("user_id", default="-")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
            "trace_id": trace_id.get(),
            "user_id": user_id.get(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)

def setup():
    h = logging.StreamHandler()
    h.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.handlers = [h]
    root.setLevel(logging.INFO)

def handle_request(rid, uid):
    trace_id.set(rid)
    user_id.set(uid)
    logging.getLogger("app").info("处理请求")

if __name__ == "__main__":
    setup()
    handle_request("t-1001", 42)
    handle_request("t-1002", 43)
```

**追问**:
- 追问 1:contextvar 忘了 set 会怎样?—— 拿 default 值,日志可查但缺 trace,建议入口中间件强制 set,配合默认值兜底。
- 追问 2:第三方库的日志没上下文怎么办?—— contextvars 是进程内全局生效的,第三方库走同一 root logger 就会带上下文。
