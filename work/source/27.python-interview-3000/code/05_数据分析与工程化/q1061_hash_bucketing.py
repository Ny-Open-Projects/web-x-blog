import hashlib

def bucket(key, salt, n=100):
    digest = hashlib.md5(f"{salt}:{key}".encode("utf-8")).hexdigest()
    return int(digest, 16) % n

for u in ("u1", "u2", "u3"):
    print(u, "实验 exp-42 桶号:", bucket(u, "exp-42"), "分层实验 exp-43 桶号:", bucket(u, "exp-43"))
print("同盐同用户必同桶,换盐重新洗牌;md5 仅用于分桶,不涉及安全语义")
print("放量 20% 即桶号 < 20 的用户进入实验组")
