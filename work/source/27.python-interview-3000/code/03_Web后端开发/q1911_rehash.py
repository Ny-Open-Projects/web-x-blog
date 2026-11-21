"""密码哈希参数升级: 登录时透明重哈希(纯标准库)。"""
import hashlib
import hmac
import os

CURRENT = {"algo": "pbkdf2_sha256", "iters": 120000}


def hash_password(password, iters, salt=None):
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iters)
    return {"algo": "pbkdf2_sha256", "iters": iters, "salt": salt.hex(),
            "hash": digest.hex()}


def verify_and_upgrade(password, record):
    """常数时间比较; 命中后若参数过时, 立即用当前参数重哈希并返回新记录。"""
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(),
                                 bytes.fromhex(record["salt"]), record["iters"])
    if not hmac.compare_digest(digest.hex(), record["hash"]):
        return False, None, "密码错误"
    if record["iters"] < CURRENT["iters"]:
        new_rec = hash_password(password, CURRENT["iters"])
        return True, new_rec, "验证成功且参数已升级"
    return True, record, "验证成功"


# 库里躺着三年前的旧参数记录(1 万次迭代)
legacy = hash_password("hunter2", 10000)
print("旧记录参数:", legacy["algo"], legacy["iters"])
ok, upgraded, msg = verify_and_upgrade("wrong", legacy)
print("错误密码 ->", ok, msg)
assert not ok

ok, upgraded, msg = verify_and_upgrade("hunter2", legacy)
print("正确密码 ->", ok, msg, "新迭代数:", upgraded["iters"] if upgraded else None)
assert ok and upgraded["iters"] == CURRENT["iters"]

# 升级后的记录再次验证: 不再触发重哈希
ok2, again, msg2 = verify_and_upgrade("hunter2", upgraded)
print("升级后复验 ->", ok2, msg2)
assert ok2 and again is upgraded

print("要点: 哈希参数必然随算力增长过时, 登录是唯一同时拿到明文的时机, 顺手重哈希实现零打扰升级")
