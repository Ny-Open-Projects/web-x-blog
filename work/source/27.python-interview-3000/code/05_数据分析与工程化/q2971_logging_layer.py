"""日志完整规范层: 统一格式 + 请求上下文注入 + 分级 + 按大小轮转"""
import logging
import logging.handlers
import os
import tempfile

FILE_FMT = "%(asctime)s|%(levelname)s|%(request_id)s|%(name)s|%(message)s"
STREAM_FMT = "%(levelname)-7s [%(request_id)s] %(message)s"


class ContextFilter(logging.Filter):
    """兜底注入 request_id: 任何 handler 的任何记录都有该字段, 不会因缺字段而炸"""
    def filter(self, record):
        if not hasattr(record, "request_id"):
            record.request_id = "-"
        return True


class RequestContextAdapter(logging.LoggerAdapter):
    """上下文适配器: 让业务代码写 logger.info(msg) 时自动带上 request_id"""
    def process(self, msg, kwargs):
        extra = dict(kwargs.get("extra") or {})
        extra.setdefault("request_id", self.extra["request_id"])
        kwargs["extra"] = extra
        return msg, kwargs


def setup_logging(log_dir, level=logging.INFO, max_bytes=1024, backups=2):
    """幂等装配: 重复调用不叠加 handler; 文件 handler 按大小轮转"""
    logger = logging.getLogger("app")
    logger.setLevel(level)
    logger.propagate = False
    if logger.handlers:
        return logger
    ctx = ContextFilter()
    fh = logging.handlers.RotatingFileHandler(
        os.path.join(log_dir, "app.log"), maxBytes=max_bytes,
        backupCount=backups, encoding="utf-8")
    fh.setFormatter(logging.Formatter(FILE_FMT))
    fh.addFilter(ctx)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(STREAM_FMT))
    sh.addFilter(ctx)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger


def write_burst(logger, n):
    """写足量日志触发轮转"""
    for i in range(n):
        logger.info("处理分片 %d 完成", i)


if __name__ == "__main__":
    d = tempfile.mkdtemp(prefix="logs_")
    logger = setup_logging(d)

    req_a = RequestContextAdapter(logging.getLogger("app"), {"request_id": "req-0001"})
    req_b = RequestContextAdapter(logging.getLogger("app"), {"request_id": "req-0002"})

    logger.debug("这条 DEBUG 低于 INFO 级别, 不应出现")
    req_a.info("开始处理上传")
    req_b.warning("配额即将用尽")
    try:
        raise RuntimeError("下游存储 503")
    except RuntimeError:
        req_a.exception("处理失败")          # exception 自动附堆栈
    write_burst(logger, 60)                  # 每条约 70 字节, 60 条必触发轮转

    files = sorted(f for f in os.listdir(d) if f.startswith("app.log"))
    print("日志目录:", files, "-> maxBytes=1024 backupCount=2 触发了轮转")
    with open(os.path.join(d, "app.log"), "r", encoding="utf-8") as f:
        last = f.readlines()[-1].rstrip()
    print("最新一行:", last)
    if "DEBUG" in open(os.path.join(d, "app.log.1"), encoding="utf-8").read():
        print("轮转文件中不应有 DEBUG")
    print("要点: 格式统一含 request_id 才能把一次请求的日志串起来; 分级靠 logger.setLevel; 轮转靠 handler 不靠脚本自己切")
