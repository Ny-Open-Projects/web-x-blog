"""流量染色:入口打标 + 全链路透传路由 + 灰度监控独立 + 秒级回滚。"""
import hashlib


def stable_hash(s):
    return int(hashlib.md5(s.encode()).hexdigest(), 16) % 100


class DyeRules:
    def __init__(self):
        self.rules = []                       # (condition, color)

    def add_whitelist(self, users, color="gray"):
        self.rules.append((lambda ctx: ctx.get("user") in users, color))

    def add_percent(self, pct, color="gray"):
        self.rules.append((lambda ctx: stable_hash(ctx.get("user", "")) < pct, color))

    def color_of(self, ctx):
        for cond, color in self.rules:
            if cond(ctx):
                return color
        return "stable"

    def clear(self):
        self.rules = []                       # 回滚 = 清规则


class Gateway:
    def __init__(self, rules, services):
        self.rules, self.services = rules, services

    def handle(self, ctx, path):
        color = self.rules.color_of(ctx)
        target = self.services.get(color, self.services["stable"])
        resp = target(ctx, color=color)       # 染色头随请求透传到下游
        return resp, color


if __name__ == "__main__":
    def order_service_v2(ctx, color):
        return f"v2 处理 {ctx['user']}"
    def order_service_v1(ctx, color):
        return f"v1 处理 {ctx['user']}"

    rules = DyeRules()
    rules.add_whitelist({"emp-1", "emp-2"})
    gw = Gateway(rules, {"stable": order_service_v1, "gray": order_service_v2})

    resp, color = gw.handle({"user": "emp-1"}, "/order")
    print("员工白名单:", resp, "染色:", color)
    assert color == "gray" and "v2" in resp

    rules.add_percent(10)
    gray_users = sum(1 for i in range(1000) if gw.handle({"user": f"u{i}"}, "/order")[1] == "gray")
    print(f"放量 10%: 1000 用户中 {gray_users} 人进入灰度")
    assert 50 <= gray_users <= 150, "按用户稳定哈希放量"

    rules.clear()                             # 一键回滚
    resp2, color2 = gw.handle({"user": "emp-1"}, "/order")
    assert color2 == "stable" and "v1" in resp2
    print("回滚后全部流量回 v1;稳定哈希保证同一用户始终同色")
