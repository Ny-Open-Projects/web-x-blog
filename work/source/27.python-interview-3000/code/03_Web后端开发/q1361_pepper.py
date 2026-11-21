"""pepper:对慢哈希结果再叠一层应用级 HMAC(纯标准库)。"""
import hashlib
import hmac
import os


def load_pepper():
    pepper = os.environ.get("APP_PEPPER")
    if not pepper:
        pepper = "demo-pepper-change-me"
        print("[降级] 未设置 APP_PEPPER,使用演示值;生产必须来自 KMS 或环境变量")
    return pepper.encode()


PEPPER = load_pepper()


def with_pepper(base_hash_hex):
    return hmac.new(PEPPER, base_hash_hex.encode(), hashlib.sha256).hexdigest()


def verify(base_hash_hex, stored):
    return hmac.compare_digest(with_pepper(base_hash_hex), stored)


base = hashlib.pbkdf2_hmac("sha256", b"pw", b"salt", 100_000).hex()
stored = with_pepper(base)
print("校验通过:", verify(base, stored))

wrong = hmac.new(b"other-pepper", base.encode(), hashlib.sha256).hexdigest()
print("pepper 不符即失败(拖库者无 pepper 时正是这种局面):", verify(base, wrong))
