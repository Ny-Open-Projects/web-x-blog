"""secrets:令牌与安全随机的正确来源。"""
import secrets
import string


def url_token(nbytes=16):
    return secrets.token_urlsafe(nbytes)    # URL 安全,长度约 1.3 倍 nbytes


def hex_token(nbytes=16):
    return secrets.token_hex(nbytes)


def otp_code(digits=6):
    return "".join(secrets.choice(string.digits) for _ in range(digits))


def constant_time_compare():
    a = secrets.token_bytes(16)
    b = secrets.token_bytes(16)
    return secrets.compare_digest(a, b)     # 常数时间比较,防时序侧信道


def password(pool=None, length=12):
    pool = pool or (string.ascii_letters + string.digits)
    return "".join(secrets.choice(pool) for _ in range(length))


if __name__ == "__main__":
    print("token_urlsafe:", url_token())
    print("token_hex    :", hex_token())
    print("6 位验证码    :", otp_code())
    print("常数时间比较(不同值):", constant_time_compare())
    print("随机密码:", password())
