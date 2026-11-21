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
