import hashlib


class FeatureFlags:
    def __init__(self):
        self.flags: dict[str, dict] = {
            "new_checkout": {"enabled": True, "percent": 30, "whitelist": ["admin"]},
            "beta_search": {"enabled": False, "percent": 0, "whitelist": []},
        }

    def is_enabled(self, flag: str, user_id: str) -> bool:
        cfg = self.flags.get(flag)
        if not cfg or not cfg["enabled"]:
            return False
        if user_id in cfg["whitelist"]:
            return True
        # 哈希分桶:同一用户结果稳定,与请求顺序无关
        bucket = int(hashlib.md5(f"{flag}:{user_id}".encode()).hexdigest(), 16) % 100
        return bucket < cfg["percent"]


if __name__ == "__main__":
    flags = FeatureFlags()
    samples = [flags.is_enabled("new_checkout", f"user{i}") for i in range(10)]
    print(samples)
    print("stable for same user:",
          flags.is_enabled("new_checkout", "u1") == flags.is_enabled("new_checkout", "u1"))
