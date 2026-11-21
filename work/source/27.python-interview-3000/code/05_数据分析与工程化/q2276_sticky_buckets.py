"""灰度开关的桶分配持久化: 放量不换人"""

import hashlib


def base_bucket(exp, user, buckets=100):
    digest = hashlib.md5(f"{exp}:{user}".encode()).hexdigest()
    return int(digest[:8], 16) % buckets


def assign(exp, user, ratio, persisted):
    """已持久化的分配优先, 哈希只作兜底"""
    if user in persisted:
        return persisted[user], "沿用"
    in_test = base_bucket(exp, user) < ratio
    persisted[user] = in_test      # 首次判定即持久化
    return in_test, "新判定"


if __name__ == "__main__":
    users = [f"u{i}" for i in range(12)]
    persisted = {}
    in10 = {u: assign("pay_v2", u, 10, persisted)[0] for u in users}
    in20 = {u: assign("pay_v2", u, 20, persisted)[0] for u in users}
    exited = [u for u in users if in10[u] and not in20[u]]
    entered = [u for u in users if not in10[u] and in20[u]]
    print(f"放量 10%->20%: 原实验组 {sum(in10.values())} 人, 退出 {len(exited)} 人 {exited}")
    print(f"新进实验组 {len(entered)} 人: {entered}")
    print("要点: 首次判定即持久化, 后续只读; 哈希兜底可复现; 缩量保留记录不弹回")
