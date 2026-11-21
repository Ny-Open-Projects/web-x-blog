---
title: [Q501] LoggerAdapter 与日志上下文注入
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q501 · LoggerAdapter 与日志上下文注入

> 难度:★★★☆ | 标签:logging, 上下文

**问**:每条日志都手动拼 request_id 太啰嗦,logging 有什么内建机制自动附加上下文?

**答**:LoggerAdapter 包装 logger,持有 extra 字典;process() 钩子在每条记录发出前把 extra 合并进 record,格式串里用 %(req_id)s 输出——业务代码只管 log.info("done"),上下文自动带上。子类化 Adapter 可定制合并策略(允许单条覆盖)。更现代的方案是 logging.Filter 在 record 上补字段(跨模块生效、不改变 logger 实例),或 contextvars 存请求级数据由 Filter 读取——三者的选择标准:作用域是「一个组件」用 Adapter,「一个请求」用 contextvars + Filter。

```python
# file: code/01_语言核心与底层/q501_logger_adapter.py
import logging

class RequestContextAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = {"req_id": self.extra.get("req_id", "-")}
        extra.update(kwargs.get("extra") or {})
        kwargs["extra"] = extra
        return f"[req {extra['req_id']}] {msg}", kwargs

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=logging.INFO,
    )
    log = RequestContextAdapter(logging.getLogger("app"), {"req_id": "r-42"})
    log.info("start processing")
    log.info("done", extra={"req_id": "r-override"})   # 单条覆盖
    logging.getLogger("app").info("plain logger, no context")
```

**追问**:1) LoggerAdapter 与直接 getLogger("app.r42") 命名子 logger 的取舍?——命名子 logger 会改变层级传播与配置匹配,适合组件级;Adapter 只加数据不动层级,适合请求级。2) Adapter 为什么「只加数据不动层级」?——它包装 logger,调用时把 extra 字段附加到 record;层级与 propagate 完全不变;子 logger 则改变配置匹配——子 logger 未配级别时沿用父级 effective level。3) extra 的底层落点?——调用处理时 extra 的键值写进 record.__dict__,formatter 用 %(request_id)s 取用;键与 LogRecord 保留属性冲突会抛 KeyError。4) 生产陷阱?——extra 键撞内置名(name/msg/args)KeyError;各模块手写 Adapter 字段不一致,聚合检索困难;JSON formatter 忘了把 extra 字段并入输出。
