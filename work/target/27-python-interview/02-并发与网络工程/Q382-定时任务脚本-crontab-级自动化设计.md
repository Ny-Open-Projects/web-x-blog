---
title: [Q382] 定时任务脚本:crontab 级自动化设计
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q382 · 定时任务脚本:crontab 级自动化设计

> 难度:★★☆ | 标签:自动化, cron, 运维

**问**:写一个适合放进 crontab 的自动化脚本,要考虑哪些工程细节?

**答**:要点:①日志重定向与轮转(`>> log 2>&1`,程序内配 RotatingFileHandler);②文件锁防重叠(上一题);③失败要能被感知——退出码非 0、发通知(邮件/webhook);④路径用绝对路径,cron 的 PATH 和 shell 环境与登录 shell 不同;⑤任务幂等,可安全重跑;⑥用 `python script.py` 显式指定解释器或加 shebang + chmod +x。Python 内也常直接用 `sched`/`APScheduler` 做进程内调度。

```python
# file: code/02_并发与网络工程/q382_cron_script.py
"""适合 crontab 的自动化任务骨架:锁 + 日志 + 退出码 + 通知钩子。
crontab 示例: * * * * * /usr/local/bin/python3 /opt/jobs/backup_job.py >> /var/log/backup.log 2>&1
"""
import logging
import os
import sys
import tempfile
from logging.handlers import RotatingFileHandler

try:
    import fcntl
except ImportError:  # Windows 环境降级
    fcntl = None


def setup_logger() -> logging.Logger:
    log_path = os.path.join(tempfile.gettempdir(), "backup_job.log")
    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=3)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    log = logging.getLogger("backup_job")
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log


def acquire_lock(name="backup_job") -> bool:
    if fcntl is None:
        return True
    fd = open(os.path.join(tempfile.gettempdir(), name + ".lock"), "w")
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        return False
    return True


def notify(level, msg):
    """生产里替换成发邮件或企业微信 webhook。"""
    print(f"[NOTIFY-{level}] {msg}")


def do_work(log):
    log.info("开始备份")
    # ... 真实备份逻辑 ...
    log.info("备份完成")


def main():
    log = setup_logger()
    if not acquire_lock():
        log.warning("上一次任务尚未结束, 跳过本轮")
        return 0
    try:
        do_work(log)
        return 0
    except Exception as e:
        log.exception("任务失败")
        notify("ERROR", f"backup_job 失败: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())  # cron 依据退出码判断成败
```

**追问**:
- 如何让任务错峰而不是整点齐跑?crontab 随机 sleep 几分钟,或程序内 `random.uniform` 抖动,避免同时打爆下游。
- cron 5 个字段忘了怎么写?分 时 日 月 周,`*/5 * * * *` 每 5 分钟,`0 3 * * 1` 每周一 3 点。
