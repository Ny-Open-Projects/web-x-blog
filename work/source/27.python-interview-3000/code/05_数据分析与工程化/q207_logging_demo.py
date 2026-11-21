import logging
import json
from logging.handlers import TimedRotatingFileHandler


class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "ts": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


def build_logger(path: str = "app.log") -> logging.Logger:
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    fh = TimedRotatingFileHandler(path, when="midnight", backupCount=7)
    fh.setFormatter(JsonFormatter())
    logger.addHandler(fh)
    return logger


def test_structured_log(tmp_path):
    log_file = tmp_path / "t.log"
    lg = build_logger(str(log_file))
    lg.info("user login", extra={})
    line = log_file.read_text().strip().splitlines()[0]
    parsed = json.loads(line)
    assert parsed["level"] == "INFO"
    assert parsed["logger"] == "app"
