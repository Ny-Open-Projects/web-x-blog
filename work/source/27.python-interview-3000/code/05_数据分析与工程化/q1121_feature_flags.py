import hashlib

class Flags:
    def __init__(self):
        self.flags = {}

    def add(self, name, enabled=True, rollout=100):
        self.flags[name] = {"enabled": enabled, "rollout": rollout}

    def is_on(self, name, user_id):
        cfg = self.flags.get(name, {"enabled": False, "rollout": 0})
        if not cfg["enabled"]:
            return False
        digest = hashlib.md5(f"{name}:{user_id}".encode()).hexdigest()
        return int(digest, 16) % 100 < cfg["rollout"]

    def kill(self, name):
        self.flags[name]["enabled"] = False

if __name__ == "__main__":
    f = Flags()
    f.add("new-checkout", enabled=True, rollout=20)
    hits = sum(f.is_on("new-checkout", f"u{i}") for i in range(1000))
    print(f"灰度 20%,命中 {hits} 人")
    f.kill("new-checkout")
    print("kill switch 后:", f.is_on("new-checkout", "u1"))
