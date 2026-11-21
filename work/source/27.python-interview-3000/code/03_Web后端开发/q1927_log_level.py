"""日志级别动态调整: 运行时生效与变更审计(纯标准库)。"""
import json
import logging


def build_logger():
    logger = logging.getLogger("order-api")
    logger.setLevel(logging.WARNING)
    logger.propagate = False
    handler = logging.StreamHandler(open("/dev/null", "w"))
    handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def apply_level(logger, new_level, operator, audit):
    """应用新级别并记录审计; 生效方式只是 logger.setLevel 一行。"""
    old = logging.getLevelName(logger.level)
    logger.setLevel(new_level)
    audit.append({"op": operator, "from": old,
                  "to": logging.getLevelName(new_level)})
    return old


def probe(logger, emit_debug):
    """观测级别是否生效: 尝试发 DEBUG, handler 层会被级别过滤器拦下。"""
    record = logger.makeRecord(logger.name, logging.DEBUG, "f", 1,
                               "expensive-debug-payload", None, None)
    if record.levelno >= logger.level:
        emit_debug.append(record.getMessage())
        return "emitted"
    return "suppressed"


logger = build_logger()
debug_out = []
audit = []

print("默认 WARNING 时:", probe(logger, debug_out))
assert probe(logger, debug_out) == "suppressed"

apply_level(logger, logging.DEBUG, "oncall@ops", audit)
print("调成 DEBUG 后:", probe(logger, debug_out))
assert probe(logger, debug_out) == "emitted"

apply_level(logger, logging.WARNING, "oncall@ops", audit)
print("调回 WARNING 后:", probe(logger, debug_out))
assert probe(logger, debug_out) == "suppressed"

print("变更审计:", json.dumps(audit, ensure_ascii=False))
assert len(audit) == 2 and audit[0]["to"] == "DEBUG"

print("要点: 动态级别是排障第一杠杆, 热生效一行 setLevel, 但每次变更必须留审计且会自动回滚")
