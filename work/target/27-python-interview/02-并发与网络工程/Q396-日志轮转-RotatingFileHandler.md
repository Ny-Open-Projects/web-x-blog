---
title: [Q396] 日志轮转:RotatingFileHandler 与 TimedRotating
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q396 · 日志轮转:RotatingFileHandler 与 TimedRotating

> 难度:★★☆ | 标签:logging, 日志轮转, 运维

**问**:单文件日志无限增长会出什么问题?标准库怎么轮转?

**答**:磁盘打满、单文件过大无法 grep/传输。标准库两种:`RotatingFileHandler` 按大小轮转(maxBytes + backupCount),`TimedRotatingFileHandler` 按时间(when="midnight", backupCount=保留天数)。多进程写同一文件时轮转会互相覆盖,要么每进程写独立文件再采集,要么交给 logrotate/copytruncate;容器环境更推荐输出 stdout 由采集器统一处理。

```python
# file: code/02_并发与网络工程/q396_log_rotation.py
"""按大小与按时间两种日志轮转。"""
import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

if __name__ == "__main__":
    # 按大小:单文件最大 1MB, 保留 3 个历史
    size_log = logging.getLogger("size")
    size_log.setLevel(logging.INFO)
    size_log.addHandler(RotatingFileHandler(
        "/tmp/size.log", maxBytes=1024 * 1024, backupCount=3,
        encoding="utf-8"))

    # 按时间:每天午夜切割, 保留 7 天
    time_log = logging.getLogger("time")
    time_log.setLevel(logging.INFO)
    time_log.addHandler(TimedRotatingFileHandler(
        "/tmp/time.log", when="midnight", backupCount=7,
        encoding="utf-8"))

    for i in range(3):
        size_log.info("record %d", i)
        time_log.info("record %d", i)
    print("写入完成, 轮转将在超限或跨天时自动发生")
```

**追问**:
- 多进程同时写一个轮转日志为什么危险?各进程独立持有文件偏移,轮转改名后老进程仍写旧 inode,日志错乱;方案:进程各自写文件、用 SocketHandler 集中、或 QueueHandler+QueueListener。
- 轮转时备份命名怎么管理?——RotatingFileHandler 默认 log.1/log.2 追加模式会与 logrotate 冲突,二选一;TimedRotating 的 suffix 可自定义便于采集器按日期切。
- 容器里日志怎么轮转?——容器内写 stdout/stderr 交给 docker/k8s 日志驱动轮转,容器内自轮转会与采集冲突;这是云原生下的标准答案。
- backupCount 怎么定?——磁盘配额 ÷ 单文件大小,再按排障保留窗口(如 7 天)校验;只设 maxBytes 不设 backupCount 等于没管磁盘。
