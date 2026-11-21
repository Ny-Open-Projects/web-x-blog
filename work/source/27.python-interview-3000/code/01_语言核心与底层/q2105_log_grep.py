"""日志消息的可检索性规范:稳定事件词、键值对与级别语义。"""
import io
import logging


def make_logger(name):
    buf = io.StringIO()
    handler = logging.StreamHandler(buf)
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
    log = logging.getLogger(name)
    log.handlers = [handler]
    log.propagate = False
    log.setLevel(logging.INFO)
    return log, buf


if __name__ == "__main__":
    log, buf = make_logger("pay")

    log.warning("PAY_RETRY attempt=2 order=1001 delay=0.5s")   # 事件词 + 键值对
    log.info("PAY_OK order=1001 amount=99.0")
    log.error(f"PAY_FAIL order={1002} reason=timeout")          # 反例:f-string 提前求值

    for line in buf.getvalue().splitlines():
        print(line)
    print("grep PAY_ 全命中,grep attempt= 精确定位;f-string 版本无法按字段过滤")
