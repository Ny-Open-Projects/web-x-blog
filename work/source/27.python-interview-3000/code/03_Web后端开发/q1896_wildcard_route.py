"""通配路由: 贪婪匹配、非贪婪参数与路径穿越防护(纯标准库)。"""
import posixpath


def match(pattern, path):
    """实现两类通配: {name} 匹配单段, {name:path} 跨段贪婪匹配到最后。

    返回 (params, None) 或 (None, 说明文本)。
    """
    p_segs = pattern.strip("/").split("/")
    u_segs = path.strip("/").split("/")
    params = {}
    for idx, pseg in enumerate(p_segs):
        if pseg.startswith("{") and pseg.endswith(":path}"):
            name = pseg[1:-6]
            if idx == len(p_segs) - 1:
                rest = "/".join(u_segs[idx:])
                if not rest:
                    return None, "通配段不允许匹配到空串"
                params[name] = rest
                return params, None
            return None, ":path 通配只能作为最后一段"
        if pseg.startswith("{") and pseg.endswith("}"):
            if idx >= len(u_segs) or not u_segs[idx]:
                return None, "段数不足"
            params[pseg[1:-1]] = u_segs[idx]
            continue
        if idx >= len(u_segs) or pseg != u_segs[idx]:
            return None, "静态段不匹配"
    if len(u_segs) != len(p_segs):
        return None, "段数不一致"
    return params, None


def safe_join(root, sub):
    """通配命中静态文件路由后必须防穿越: 归一化后仍需在根内。"""
    joined = posixpath.normpath(posixpath.join(root, sub))
    if not (joined == root or joined.startswith(root.rstrip("/") + "/")):
        return None
    return joined


print(match("/static/{rest:path}", "/static/img/logo.png"))
print(match("/static/{rest:path}", "/static/a/b/c/d.txt"))
print(match("/users/{id}/avatar", "/users/42/avatar"))
print(match("/users/{id}/avatar", "/users/42/posts"))      # 应不匹配
params, why = match("/static/{rest:path}", "/static/")
print("空通配:", params, why)
print("穿越尝试归一化:", safe_join("/srv/files", "docs/../../etc/passwd"))
assert safe_join("/srv/files", "docs/../../etc/passwd") is None
assert safe_join("/srv/files", "docs/readme.md") == "/srv/files/docs/readme.md"
print("要点: 通配要贪婪但不可越界, :path 只允许在最后一段, 命中后还要做归一化穿越防护")
