

class FieldError:
    def __init__(self, field, message, value):
        self.field = field
        self.message = message
        self.value = value

    def __repr__(self):
        return "%s: %s (got %r)" % (self.field, self.message, self.value)


def validate_config(cfg):
    """聚合所有错误,而不是第一个就抛。"""
    errors = []

    def check(field, predicate, message):
        value = cfg.get(field)
        if not predicate(value):
            errors.append(FieldError(field, message, value))

    def is_int(value):
        try:
            return value == int(value)
        except (TypeError, ValueError):
            return False

    def is_nonempty(value):
        return isinstance(value, str) and value.strip() != ""

    check("port", lambda v: is_int(v) and 1 <= int(v) <= 65535,
          "必须是 1-65535 的整数")
    check("host", is_nonempty, "host 不能为空")
    check("retries", lambda v: is_int(v) and int(v) >= 0, "必须是非负整数")
    check("mode", lambda v: v in ("dev", "prod"), "mode 只能是 dev 或 prod")
    return errors


if __name__ == "__main__":
    bad_cfg = {"port": "99999", "host": "  ", "retries": -1, "mode": "qa"}
    errors = validate_config(bad_cfg)
    print("%d 个错误, 一次报全:" % len(errors))
    for e in errors:
        print("  -", e)

    good_cfg = {"port": 5432, "host": "db.internal", "retries": 3, "mode": "prod"}
    print("good cfg errors:", validate_config(good_cfg))

    # fail-fast 对比:结构类致命错误立即抛
    try:
        raise FileNotFoundError("config.yaml 不存在")
    except FileNotFoundError as err:
        print("fatal, fail-fast:", err)
