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
