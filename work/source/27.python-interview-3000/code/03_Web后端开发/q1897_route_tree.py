"""路由优先级: 静态段优先于参数, 参数优先于通配的解析树(纯标准库)。"""


class Node:
    """ trie 节点: static 是精确段表, param 是参数子树, wildcard 是通配叶。"""

    def __init__(self):
        self.static = {}
        self.param = None       # (param_name, Node)
        self.wildcard = None    # (param_name, handler)
        self.handler = None


class Router:
    def __init__(self):
        self.root = Node()

    def add(self, pattern, handler):
        node = self.root
        segs = pattern.strip("/").split("/")
        for i, seg in enumerate(segs):
            if seg.startswith("{") and seg.endswith(":path}"):
                node.wildcard = (seg[1:-6], handler)
                return
            if seg.startswith("{") and seg.endswith("}"):
                if node.param is None:
                    node.param = (seg[1:-1], Node())
                node = node.param[1]
            else:
                node = node.static.setdefault(seg, Node())
            if i == len(segs) - 1:
                node.handler = handler

    def match(self, path):
        """匹配时静态段优先, 其次参数, 最后通配; 保证 /users/me 不会被 /users/{id} 抢走。"""
        segs = [s for s in path.strip("/").split("/") if s]
        params = {}
        node = self.root
        for idx, seg in enumerate(segs):
            if seg in node.static:
                node = node.static[seg]
                continue
            if node.param is not None:
                params[node.param[0]] = seg
                node = node.param[1]
                continue
            if node.wildcard is not None:
                params[node.wildcard[0]] = "/".join(segs[idx:])
                return node.wildcard[1], params
            return None, params
        if node.handler is not None:
            return node.handler, params
        if node.wildcard is not None:
            params[node.wildcard[0]] = ""
            return node.wildcard[1], params
        return None, params


router = Router()
router.add("/users/me", "list_my_profile")
router.add("/users/{id}", "get_user")
router.add("/users/{id}/orders", "get_orders")
router.add("/files/{rest:path}", "serve_file")

cases = [
    ("/users/me", "list_my_profile", {}),
    ("/users/42", "get_user", {"id": "42"}),
    ("/users/42/orders", "get_orders", {"id": "42"}),
    ("/files/a/b/c.txt", "serve_file", {"rest": "a/b/c.txt"}),
]
for path, want_handler, want_params in cases:
    handler, params = router.match(path)
    print("{:22s} -> {} {}".format(path, handler, params))
    assert handler == want_handler and params == want_params, path

handler, _ = router.match("/unknown/x/y")
print("无路由命中:", handler, "(交 404)")
assert handler is None
print("要点: 优先级是结构性的, 静态 > 参数 > 通配, 不依赖注册先后, /users/me 永远赢过 /users/{id}")
