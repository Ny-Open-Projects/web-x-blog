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
