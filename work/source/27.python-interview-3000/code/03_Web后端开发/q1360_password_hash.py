"""密码哈希:生产选 argon2 或 bcrypt,这里用标准库 PBKDF2 演示同等流程。"""
import hashlib
import hmac
import os

try:
    import argon2
    print("[环境] 已安装 argon2-cffi,生产应使用 argon2.PasswordHasher")
except ImportError:
    print("[降级] 未安装 argon2-cffi,以下用标准库 PBKDF2-HMAC-SHA256 演示")


def hash_password(password, iterations=100_000):
    salt = os.urandom(16)                                # 每密码独立随机盐
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations)
    return f"pbkdf2_sha256${iterations}${salt.hex()}${dk.hex()}"


def verify_password(stored, password):
    algo, iters, salt_hex, dk_hex = stored.split("$")
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(),
                             bytes.fromhex(salt_hex), int(iters))
    return hmac.compare_digest(dk.hex(), dk_hex)          # 恒定时间比较


stored = hash_password("S3cure-pass!")
print("存储串:", stored[:40], "...")
print("正确密码:", verify_password(stored, "S3cure-pass!"))
print("错误密码:", verify_password(stored, "wrong-password"))
