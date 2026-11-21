"""405 与 404 的正确语义: 路由双查与 Allow 头(纯标准库)。"""


class MethodRouter:
    """路径与方法两级表: 先查路径, 再查方法, 才能区分 404 与 405。"""

    def __init__(self):
        self.paths = {}

    def add(self, path, method, handler):
        self.paths.setdefault(path, {})[method.upper()] = handler

    def dispatch(self, path, method):
        """返回 (status, headers, payload); path 有而 method 无 -> 405 加 Allow。"""
        methods = self.paths.get(path)
        if methods is None:
            return 404, {}, "路由不存在"
        method = method.upper()
        if method not in methods:
            allow = ", ".join(sorted(methods))
            return 405, {"Allow": allow}, "该资源不支持此方法"
        return 200, {}, methods[method]()


router = MethodRouter()
router.add("/items/42", "GET", lambda: "item body")
router.add("/items/42", "DELETE", lambda: "deleted")

print(router.dispatch("/items/42", "GET"))
print(router.dispatch("/items/42", "POST"))     # 405 + Allow: DELETE, GET
print(router.dispatch("/items/43", "GET"))      # 404

status, headers, _ = router.dispatch("/items/42", "POST")
assert status == 405 and headers["Allow"] == "DELETE, GET"
status, _, _ = router.dispatch("/items/43", "GET")
assert status == 404

# 监控语义差异: 405 是客户端用错方法, 404 才可能是路径回退或资源下线
print("要点: 先查路径再查方法, 405 必须带 Allow 头列出全部支持方法, 两者在监控里是不同的告警")
