---
title: [Q2920] 路由表的注册与反转: match 与 url_for 双向
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2920 · 路由表的注册与反转: match 与 url_for 双向

> 难度:★★★☆ | 标签:路由, 反向解析

**问**:手写一个路由表要支持带参数的路径注册、请求匹配, 还要能按路由名反查 URL, 你的 match 和 reverse 各怎么实现?

**答**:注册时把 `<int:id>`、`<str:slug>` 这样的参数段编译成正则命名组, int 段是 `\d+` 且匹配时顺带完成类型转换, 字面量段用 re.escape 防元字符注入。match 对整段正则做全串匹配, 长度严格一致, 不会出现 `/users/42/extra` 误命中; 没匹配到返回 None 让上层给 404, 而不是抛异常。反转 url_for 按注册的声明清单校验参数: 未注册路由名 KeyError、多余参数与缺参 ValueError、int 参数类型不符也报错, 错误在开发期暴露而不是上线后生成一个坏链接。路由名重复直接拒绝注册, 名字是反转的唯一索引。

```python
# file: code/03_Web后端开发/q2920_route_reverse.py
"""路由表的注册与反转: 参数化匹配 match + url_for 反查(纯标准库)。"""
import re
from urllib.parse import urlencode

SEG = re.compile(r"^<(int|str):([a-zA-Z_]\w*)>$")


class Router:
    def __init__(self):
        self.routes = {}    # name -> pattern
        self.matchers = []  # (compiled, name, converters) 保注册序

    def add(self, name, pattern):
        if name in self.routes:
            raise ValueError("路由名重复: %s" % name)
        converters = {}
        seg_patterns = []
        for seg in pattern.strip("/").split("/"):
            m = SEG.match(seg)
            if m:
                typ, pname = m.groups()
                converters[pname] = typ
                seg_patterns.append(r"(?P<%s>%s)" % (pname, r"\d+" if typ == "int" else "[^/]+"))
            else:
                seg_patterns.append(re.escape(seg))
        regex = "^" + "/".join(seg_patterns) + "$"
        self.routes[name] = pattern
        self.matchers.append((re.compile(regex), name, converters))

    def match(self, path):
        """返回 (路由名, 参数字典) 或 None; int 段顺带完成类型转换。"""
        target = path.strip("/")
        for compiled, name, converters in self.matchers:
            m = compiled.match(target)
            if not m:
                continue
            params = {}
            for key, raw in m.groupdict().items():
                params[key] = int(raw) if converters[key] == "int" else raw
            return name, params
        return None

    def url_for(self, name, query=None, **params):
        """反转查找: 按声明填充参数, 多参/缺参/类型不符都显式报错。"""
        if name not in self.routes:
            raise KeyError("未注册的路由名: %s" % name)
        pattern = self.routes[name]
        declared = {}
        for seg in pattern.strip("/").split("/"):
            m = SEG.match(seg)
            if m:
                declared[m.group(2)] = m.group(1)
        extra = set(params) - set(declared)
        missing = set(declared) - set(params)
        if extra:
            raise ValueError("多余参数: %s" % ",".join(sorted(extra)))
        if missing:
            raise ValueError("缺少参数: %s" % ",".join(sorted(missing)))
        out = []
        for seg in pattern.strip("/").split("/"):
            m = SEG.match(seg)
            if m:
                typ, pname = m.groups()
                value = str(params[pname])
                if typ == "int" and not value.isdigit():
                    raise ValueError("参数 %s 需要 int, 拿到 %r" % (pname, params[pname]))
                out.append(value)
            else:
                out.append(seg)
        url = "/" + "/".join(out) if out else "/"
        if query:
            url += "?" + urlencode(query)
        return url


router = Router()
router.add("user_detail", "/users/<int:id>")
router.add("comment", "/blog/<str:slug>/comments/<int:cid>")
router.add("home", "/")

hit = router.match("/users/42")
print("匹配:", hit)
assert hit == ("user_detail", {"id": 42})
assert router.match("/users/abc") is None, "int 段不吞非数字"
assert router.match("/blog/x/comments/7/extra") is None, "长度必须严格一致"

url = router.url_for("comment", query={"page": 2}, slug="hello-world", cid=7)
print("反转:", url)
assert url == "/blog/hello-world/comments/7?page=2"
assert router.url_for("user_detail", id=1) == "/users/1"
assert router.url_for("home") == "/"

for bad_call, expect in [
    (lambda: router.url_for("ghost", id=1), "未注册路由名"),
    (lambda: router.url_for("user_detail", id=1, extra=2), "多余参数"),
    (lambda: router.url_for("user_detail"), "缺少参数"),
    (lambda: router.url_for("user_detail", id="x"), "类型不符"),
]:
    try:
        bad_call()
        raise AssertionError("应当报错: %s" % expect)
    except (KeyError, ValueError) as e:
        print("反转报错被拒 [%s]:" % expect, e)

try:
    router.add("user_detail", "/users/<int:id>")
except ValueError as e:
    print("重名注册被拒:", e)
print("路由注册与反转演示通过")
```

**追问**:
- 反转查找为什么不做通配?——URL 里的通配会产生无法预测的链接, 只接受显式参数才能保证生成的 URL 可测试。
- 字面量段与参数段同形时怎么办?——注册顺序即优先级, 字面量段要排在参数段前, 否则 /users/new 会被 /users/\<int:id\> 吞掉。
