"""secrets 的三种典型用法。"""
import secrets
import string

if __name__ == "__main__":
    # 1. 随机字节与 hex token(会话 ID、API key)
    print("token  :", secrets.token_hex(32))     # 64 个 hex 字符
    print("urlsafe:", secrets.token_urlsafe(32))  # 可进 URL 的 token

    # 2. 生成强随机密码
    alphabet = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(secrets.choice(alphabet) for _ in range(16))
    print("password:", password)

    # 3. 安全比较:防止时序攻击(内部即 hmac.compare_digest)
    print("compare:", secrets.compare_digest("abc", "abc"))
