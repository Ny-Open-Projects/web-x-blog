import contextvars
import json
import logging

trace_id = contextvars.ContextVar("trace_id", default="-")
user_id = contextvars.ContextVar("user_id", default="-")

class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
            "trace_id": trace_id.get(),
            "user_id": user_id.get(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)

def setup():
    h = logging.StreamHandler()
    h.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.handlers = [h]
    root.setLevel(logging.INFO)

def handle_request(rid, uid):
    trace_id.set(rid)
    user_id.set(uid)
    logging.getLogger("app").info("处理请求")

if __name__ == "__main__":
    setup()
    handle_request("t-1001", 42)
    handle_request("t-1002", 43)
