"""忘记密码的枚举防护: 响应一致性与时间均衡(纯标准库)。"""
import hashlib
import hmac
import secrets

GENERIC = {"message": "如果该邮箱存在, 重置邮件已发送", "code": 0}
DUMMY = hashlib.sha256(b"constant-dummy-work").hexdigest()
outbox = []


def deliver(email, token):
    outbox.append((email, token))


def forgot(email, users):
    token = secrets.token_urlsafe(32)
    if email in users:
        deliver(email, token)
        digest = hashlib.sha256(token.encode()).hexdigest()
    else:
        digest = hashlib.sha256(secrets.token_urlsafe(32).encode()).hexdigest()
    hmac.compare_digest(digest, DUMMY)     # 枚举路径也走等量哈希比较, 抹平时间差
    return dict(GENERIC)


users = {"alice@example.com": "u1"}
r1 = forgot("alice@example.com", users)
r2 = forgot("mallory@example.com", users)
print("真实用户响应:", r1)
print("枚举者响应:  ", r2)
print("两次响应一致:", r1 == r2)
print("邮件只投给真实用户:", outbox)
print("要点: 存在与否的差异只体现在收件箱里, 绝不体现在 HTTP 响应的状态码话术和时延中")
