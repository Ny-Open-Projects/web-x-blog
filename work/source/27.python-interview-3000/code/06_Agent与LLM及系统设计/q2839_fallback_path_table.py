"""Q2839 工具失败的降级路径表:声明式 fallback 链与降级留痕。

每个核心工具都该有一张降级路径表:实时接口挂了走缓存,缓存没有走
滞留副本,再没有给静态默认值。逐级尝试、走了哪级全程留痕,调用方
拿到结果的同时知道它打了折,而不是把降级数据冒充实时的用。
"""

CACHE = {}
STALE = {"gpu": {"price": 4999}}


def cache_lookup(args):
    v = CACHE.get(args["sku"])
    if v is None:
        raise KeyError("cache miss")
    return dict(v, degraded=False)


def stale_copy(args):
    v = STALE.get(args["sku"])
    if v is None:
        raise KeyError("stale miss")
    return dict(v, degraded=True, note="2小时前快照")


def static_default(args):
    return {"price": None, "degraded": True, "note": "默认占位"}


FALLBACK_TABLE = {
    "get_price": [
        ("cache", cache_lookup),
        ("stale", stale_copy),
        ("default", static_default),
    ],
}


def call_tool(tool, args):
    """沿降级链逐级尝试,返回结果与走过的路径。"""
    chain = FALLBACK_TABLE.get(tool)
    if not chain:
        raise RuntimeError("工具无降级路径:" + tool)
    path = []
    for level, fn in chain:
        try:
            value = fn(args)
            path.append(level)
            return value, path
        except KeyError:
            path.append(level + "_miss")
    raise RuntimeError("全部降级路径失败:" + ",".join(path))


def main():
    v1, p1 = call_tool("get_price", {"sku": "gpu"})
    assert p1 == ["cache_miss", "stale"], p1
    assert v1["price"] == 4999 and v1["degraded"] is True, v1
    # 完全没数据的 sku:一路降到默认值
    v2, p2 = call_tool("get_price", {"sku": "npu"})
    assert p2 == ["cache_miss", "stale_miss", "default"], p2
    assert v2["price"] is None, v2
    # 没有降级表的工具:失败必须显式抛出,不能假装成功
    err_msg = ""
    try:
        call_tool("send_mail", {"to": "x"})
        raise AssertionError("应当抛出")
    except RuntimeError as exc:
        err_msg = str(exc)
        assert "无降级路径" in err_msg, err_msg
    print("走滞留副本:", p1, v1)
    print("一路降到底:", p2, v2)
    print("无降级表工具显式失败:", err_msg)


if __name__ == "__main__":
    main()
