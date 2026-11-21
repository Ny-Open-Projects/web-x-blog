"""Trie 路由器: 静态段优先于参数段的树匹配(纯标准库)。"""


class Node:
    __slots__ = ("children", "param", "param_name", "handler")

    def __init__(self):
        self.children = {}            # 静态段 -> 子节点
        self.param = None             # 参数段子节点
        self.param_name = None
        self.handler = None


class Router:
    def __init__(self):
        self.root = Node()

    def add(self, path, handler):
        node = self.root
        for seg in path.strip("/").split("/"):
            if seg.startswith("{") and seg.endswith("}"):
                if node.param is None:
                    node.param = Node()
                    node.param_name = seg[1:-1]
                node = node.param
            else:
                node = node.children.setdefault(seg, Node())
        node.handler = handler

    def match(self, path):
        """返回 (handler, 参数字典); 匹配失败返回 (None, None) 对应 404。"""
        params = {}
        node = self.root
        for seg in path.strip("/").split("/"):
            if seg in node.children:               # 静态段永远优先
                node = node.children[seg]
            elif node.param is not None:
                params[node.param_name] = seg
                node = node.param
            else:
                return None, None
        return node.handler, params


router = Router()
router.add("/users/{uid}/posts", lambda params: "posts of {}".format(params["uid"]))
router.add("/users/new", lambda params: "create form")
router.add("/users/{uid}", lambda params: "user {}".format(params["uid"]))
router.add("/health", lambda params: "ok")

cases = [("/users/42/posts", "posts of 42"),
         ("/users/new", "create form"),          # 静态段优先于参数段
         ("/users/42", "user 42"),
         ("/health", "ok")]
for path, expect in cases:
    handler, params = router.match(path)
    got = handler(params) if handler else None
    print("{:20s} -> {} params={}".format(path, got, params))
    assert got == expect, (path, got, expect)

handler, params = router.match("/orders/9")
assert handler is None and params is None
print("/orders/9        -> 404  未注册的顶层段无处可去")
handler, params = router.match("/users/42/posts/99")
assert handler is None
print("/users/42/posts/99 -> 404  树比正则更容易发现多出的段")
print("要点: Trie 路由把 段 变成树的边, 静态优先参数兜底, "
      "参数名只在参数节点上记一次, 匹配过程天然拒绝悬空子路径")
