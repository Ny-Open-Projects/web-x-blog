import logging

class RequestContextAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = {"req_id": self.extra.get("req_id", "-")}
        extra.update(kwargs.get("extra") or {})
        kwargs["extra"] = extra
        return f"[req {extra['req_id']}] {msg}", kwargs

if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        level=logging.INFO,
    )
    log = RequestContextAdapter(logging.getLogger("app"), {"req_id": "r-42"})
    log.info("start processing")
    log.info("done", extra={"req_id": "r-override"})   # 单条覆盖
    logging.getLogger("app").info("plain logger, no context")
