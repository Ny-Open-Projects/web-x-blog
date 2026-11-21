"""ACL 规则建模: 用户/命令类别/键前缀 校验器"""
class ACL:
    DANGEROUS = {"keys", "flushall", "flushdb", "config", "debug", "shutdown"}

    def __init__(self):
        self.users = {}

    def create_user(self, name, password, patterns, allow_categories,
                    deny_commands=()):
        self.users[name] = {"password": password, "patterns": patterns,
                            "allow": allow_categories,
                            "deny": set(deny_commands) | self.DANGEROUS}

    def check(self, name, password, cmd, key):
        u = self.users.get(name)
        if not u or u["password"] != password:
            return False, "认证失败"
        if cmd in u["deny"]:
            return False, f"命令 {cmd} 被禁用"
        if not any(key.startswith(p.rstrip("*")) for p in u["patterns"]):
            return False, f"键 {key} 越权"
        return True, "ok"

if __name__ == "__main__":
    acl = ACL()
    acl.create_user("app", "s3cret", ["app:*"], ["read", "write"])
    for user, pwd, cmd, key in [
            ("app", "s3cret", "get", "app:stock:1"),
            ("app", "s3cret", "keys", "*"),
            ("app", "wrong", "get", "app:stock:1"),
            ("app", "s3cret", "get", "other:secret")]:
        ok, msg = acl.check(user, pwd, cmd, key)
        print(f"{cmd:>5} {key:<18} -> {'允许' if ok else '拒绝: ' + msg}")
