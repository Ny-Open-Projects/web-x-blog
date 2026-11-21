"""防重 token: 发放 -> 原子校验并消费 -> 业务执行"""
import secrets

class TokenService:
    def __init__(self):
        self.tokens = set()

    def issue(self) -> str:
        token = secrets.token_hex(8)
        self.tokens.add(token)                  # SETNX token EX 300
        return token

    def consume(self, token) -> bool:
        """Lua: EXISTS 且 DEL 原子返回"""
        if token in self.tokens:
            self.tokens.remove(token)
            return True
        return False

def submit(svc, token, payload):
    if not svc.consume(token):
        return "重复提交, 拒绝"
    return f"业务已处理: {payload}"

if __name__ == "__main__":
    svc = TokenService()
    token = svc.issue()
    print("首次提交:", submit(svc, token, {"sku": "x", "qty": 1}))
    print("重放同一 token:", submit(svc, token, {"sku": "x", "qty": 1}))
    print("伪造 token:", submit(svc, "deadbeef", {"sku": "x"}))
