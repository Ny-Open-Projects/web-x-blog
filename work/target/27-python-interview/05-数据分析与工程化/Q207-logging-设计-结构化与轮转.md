---
title: [Q207] logging 设计:结构化与轮转
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q207 · logging 设计:结构化与轮转

> 难度:★★★ | 标签:logging, 结构化日志, RotatingFileHandler

**问**:为什么不要用 print 打日志?生产环境日志怎么设计?

**答**:logging 相比 print 有**级别**(DEBUG/INFO/WARNING/ERROR)、**模块归属**(logger name 层级)、**多目标输出**(console、file、远程)、**运行时可控**(改配置不用改代码)。生产实践:一,用 logger 层级 `logging.getLogger(__name__)`,按模块过滤;二,格式里带时间、级别、模块、进程/线程 id,容器环境输出 JSON 结构化日志便于采集系统解析;三,文件日志用 `RotatingFileHandler`(按大小)或 `TimedRotatingFileHandler`(按时间,如午夜切割、保留 7 份)防磁盘撑爆;四,库代码只添加 handler 之外的 logger 调用,`logging.basicConfig` 交给应用入口,避免劫持宿主日志。

```python
# file: code/05_数据分析与工程化/q207_logging_demo.py
import logging
import json
from logging.handlers import TimedRotatingFileHandler


class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


def build_logger(path: str = "app.log") -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    fh = TimedRotatingFileHandler(path, when="midnight", backupCount=7)
    fh.setFormatter(JsonFormatter())
    logger.addHandler(fh)
    return logger


def test_structured_log(tmp_path):
    log_file = tmp_path / "t.log"
    lg = build_logger(str(log_file))
    lg.info("user login", extra={})
    line = log_file.read_text().strip().splitlines()[0]
    parsed = json.loads(line)
    assert parsed["level"] == "INFO"
    assert parsed["logger"] == "app"
```

**追问**:
- 多进程写同一个日志文件会怎样?——RotatingFileHandler 在多进程下会竞争导致丢日志,应按进程分文件或交给 logrotate/采集器,或用 QueueHandler 汇聚。
- logger 层级怎么组织?——`getLogger(__name__)` 形成 app.module 层级,根 logger 配置兜底;子 logger 未设级别时向上传播。
- propagate 是什么?——日志向父 logger 传播的开关;重复输出(控制台+文件双份)通常是 handler 加了两遍,关 propagate 或检查配置。
- 异常栈怎么记?——`logger.exception("msg")` 在 except 块内自动附 traceback;用 exc_info=False 控制是否带栈。
