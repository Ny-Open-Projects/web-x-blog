import json
import logging
import time

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(record.created)),
            "level": record.levelname,
            "msg": record.getMessage(),
            "request_id": getattr(record, "request_id", None),
        }, ensure_ascii=False)

log = logging.getLogger("app")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
log.addHandler(handler)
log.setLevel(logging.INFO)

log.info("订单创建成功", extra={"request_id": "req-42"})
log.warning("下游超时", extra={"request_id": "req-42"})
