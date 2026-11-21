"""TOTP 多因素原理: RFC 6238 与标准库 hmac 的实现(纯标准库)。"""
import base64
import hashlib
import hmac
import struct
import time


def totp(secret_b32, now=None, step=30, digits=6):
    """RFC 6238: 密钥 + 时间计数器经 HMAC-SHA1 得到 6 位动态码。"""
    secret = base64.b32decode(secret_b32, casefold=True)
    counter = int((now if now is not None else time.time()) // step)
    msg = struct.pack(">Q", counter)                      # 8 字节大端计数器
    digest = hmac.new(secret, msg, hashlib.sha1).digest()
    offset = digest[-1] & 0x0F                            # 动态截断偏移
    code = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(code % 10 ** digits).zfill(digits)


def verify(secret_b32, code, now=None, window=1):
    """验证时容忍前后各 1 个时间窗, 吸收手机与服务器的小幅时钟漂移。"""
    now = now if now is not None else time.time()
    return any(totp(secret_b32, now + w * 30) == code
               for w in range(-window, window + 1))


SECRET = base64.b32encode(b"my-app-secret-key-2026!").decode("utf-8")
t0 = 1762050000.0
code = totp(SECRET, t0)
print("步长 30s, 计数器", int(t0 // 30), "动态码:", code)
assert verify(SECRET, code, t0)
print("同窗口内验证:", verify(SECRET, code, t0 + 5))
print("下一窗口验证:", verify(SECRET, code, t0 + 31), "(窗口容忍内仍通过)")
print("漂移 2 窗后:", verify(SECRET, code, t0 + 61), "(超出容忍应拒绝)")
assert not verify(SECRET, code, t0 + 61, window=1)
assert totp(SECRET, t0) == totp(SECRET, t0 + 29.9)
print("要点: TOTP 是离线可验证的共享密钥方案, 服务端只需存密钥与最后成功计数, 验证必须限速防爆破")
