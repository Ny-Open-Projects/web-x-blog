"""日志标签规范: 低基数白名单 + 别名归一 + 高基数字段移回消息体"""

ALLOWED_KEYS = {"service", "env", "region", "level", "job"}
ENV_VALUES = {"production", "staging", "dev"}
ENV_ALIAS = {"prod": "production", "online": "production", "test": "staging"}
FORBIDDEN_KEYS = {"user_id", "order_id", "trace_id", "session_id"}


def normalize(raw_labels, message):
    labels, moved, violations = {}, [], []
    for key, value in raw_labels.items():
        key = key.lower()
        if key in FORBIDDEN_KEYS:
            moved.append(key)
            message = f"{message} {key}={value}"
            continue
        if key not in ALLOWED_KEYS:
            violations.append(f"标签 {key} 不在白名单 {sorted(ALLOWED_KEYS)}")
            continue
        if key == "env":
            value = str(value).lower()
            value = ENV_ALIAS.get(value, value)
            if value not in ENV_VALUES:
                violations.append(f"env 取值 {value!r} 不在规范集合中")
        labels[key] = value
    return {"labels": labels, "message": message, "moved": moved,
            "violations": violations}


if __name__ == "__main__":
    raw1 = {"service": "pay", "env": "prod", "region": "cn-north-1",
            "level": "error", "user_id": "u_123"}
    raw2 = {"service": "pay", "ENV": "PROD", "region": "cn-north-1",
            "level": "warn", "trace_id": "abc-9"}
    raw3 = {"service": "pay", "env": "prod", "region": "cn-north-1",
            "level": "error", "request_id": "req-99"}
    for i, (raw, msg) in enumerate([(raw1, "支付超时"), (raw2, "降级触发"),
                                    (raw3, "风控拦截")], 1):
        out = normalize(raw, msg)
        print(f"记录{i}: labels={out['labels']}")
        if out["moved"]:
            print(f"       移入消息体 {out['moved']}, message={out['message']!r}")
        if out["violations"]:
            print(f"       违规 {out['violations']}")
    out1 = normalize(raw1, "支付超时")
    out2 = normalize(raw2, "降级触发")
    out3 = normalize(raw3, "风控拦截")
    assert out1["labels"]["env"] == "production" and out1["moved"] == ["user_id"]
    assert out2["labels"]["env"] == "production", "ENV 大写经归一应变成 production"
    assert out2["moved"] == ["trace_id"]
    assert out3["violations"] and "request_id" in out3["violations"][0]
    assert len(out1["labels"]) <= len(ALLOWED_KEYS)
    print("要点: 标签是聚合维度, 值的基数必须可控; user_id 这类唯一值进消息体, env 走别名归一, 白名单外一律打回")
