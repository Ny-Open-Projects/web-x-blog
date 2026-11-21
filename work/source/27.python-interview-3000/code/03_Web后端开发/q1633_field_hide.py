"""敏感字段隐藏: exclude 只护出口, 分层读模型与日志脱敏才是纵深(纯标准库)。"""
import json

USER_ROW = {"id": "u1", "nickname": "王工", "email": "u1@example.com",
            "password_hash": "pbkdf2$..."}


def naive_exclude(obj, exclude):
    """坏味道: 只在序列化出口裁, 嵌套结构与日志路径仍然可能带出。"""
    return {k: v for k, v in obj.items() if k not in exclude}


def redact_for_log(obj):
    """纵深: 日志层统一递归脱敏, 防止上游忘了裁。"""
    sensitive = ("password_hash", "token", "secret")
    if isinstance(obj, dict):
        return {k: ("***" if any(s in k.lower() for s in sensitive) else redact_for_log(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact_for_log(v) for v in obj]
    return obj


print("出口裁剪:", naive_exclude(USER_ROW, {"password_hash"}))
leak = {"event": "user.update", "data": {"nickname": "王工", "password_hash": "pbkdf2$..."}}
print("日志若不脱敏会带出:", "password_hash" in json.dumps(leak))
print("脱敏后:", redact_for_log(leak))
print("结论: 敏感字段干脆不进读模型, 而不是靠出口 exclude 一层层堵")
