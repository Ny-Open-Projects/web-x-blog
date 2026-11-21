"""中间件的路径作用域: 只对 /admin 前缀生效的调度(纯标准库)。"""


class ScopedPipeline:
    """按路径前缀挂载中间件: 命中最长前缀链, 其余路径直接进 handler。"""

    def __init__(self):
        self.scopes = []          # [(prefix, [(name, fn)])]

    def scope(self, prefix, middlewares):
        self.scopes.append((prefix, list(middlewares)))

    def applicable(self, path):
        """返回匹配到的中间件链, 按前缀长度降序保证最长优先。"""
        hits = [(p, mws) for p, mws in self.scopes if path.startswith(p)]
        hits.sort(key=lambda pm: -len(pm[0]))
        chain = []
        for _, mws in hits:
            chain.extend(mws)
        return chain

    def handle(self, path, request, handler):
        response = {"status": 200, "body": handler(path, request)}
        for name, fn in self.applicable(path):
            short = fn(request, response)
            if short is not None:          # 中间件可短路改写响应
                return short
        return response


def admin_handler(path, req):
    return {"data": "admin metrics"}


def public_handler(path, req):
    return {"data": "public page"}


pipe = ScopedPipeline()
pipe.scope("/admin", [("ip-allowlist",
                       lambda req, resp: {"status": 403} if req.get("ip") == "10.0.0.99" else None),
                      ("audit",
                       lambda req, resp: resp if resp["status"] != 200 else dict(resp, audited=True))])

r1 = pipe.handle("/admin/dashboard", {"ip": "10.0.0.5"}, admin_handler)
r2 = pipe.handle("/admin/dashboard", {"ip": "10.0.0.99"}, admin_handler)
r3 = pipe.handle("/home", {}, public_handler)
print("admin 正常访问 ->", r1)
print("admin 黑名单 ->", r2)
print("公共路径不走 admin 中间件 ->", r3)
assert r1.get("audited") and r2["status"] == 403 and "audited" not in r3
print("要点: 作用域中间件让重逻辑只挂在敏感前缀上, 公共路径零开销, 命中最长前缀者优先")
