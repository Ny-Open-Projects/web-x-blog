import hashlib


def bucket(user_id: str, salt: str = "exp-new-ui") -> int:
    digest = hashlib.md5(f"{salt}:{user_id}".encode()).hexdigest()
    return int(digest[:8], 16) % 100


def in_rollout(user_id: str, percent: int, salt: str = "exp-new-ui") -> bool:
    return bucket(user_id, salt) < percent


def main() -> None:
    users = [f"user-{i}" for i in range(10000)]

    assert all(in_rollout(u, 20) == in_rollout(u, 20) for u in users[:100])

    c5 = {u for u in users if in_rollout(u, 5)}
    c20 = {u for u in users if in_rollout(u, 20)}
    c50 = {u for u in users if in_rollout(u, 50)}
    print(f"放量 5% -> {len(c5)} 人, 20% -> {len(c20)} 人, 50% -> {len(c50)} 人")
    assert 400 <= len(c5) <= 600
    assert c5 < c20 < c50, "嵌套性: 提量不洗牌, 老用户永远在"

    other = {u for u in users if in_rollout(u, 20, salt="exp-dark-mode")}
    overlap = len(c20 & other) / len(c20)
    print(f"另一实验 20% 与本实验 20% 的重合率 {overlap:.0%} (应接近 20%)")
    assert 0.15 < overlap < 0.25

    reshuffled = {u for u in users if in_rollout(u, 20, salt="exp-new-ui-v2")}
    kept = len(c20 & reshuffled) / len(c20)
    print(f"中途改 salt 后原 20% 用户的留存率 {kept:.0%} -> 等于重新抽样, 实验作废")
    assert kept < 0.35


if __name__ == "__main__":
    main()
