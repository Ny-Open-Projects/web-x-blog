---
title: [Q2839] 工具失败的降级路径表:声明式 fallback 链
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2839 · 工具失败的降级路径表:声明式 fallback 链

> 难度:★★★☆ | 标签:Agent, 降级, 工具治理

**问**:核心工具挂了,你的 Agent 是直接报错还是能继续干活?降级链怎么声明、怎么留痕?

**答**:每个核心工具都该有一张降级路径表:实时接口挂了走缓存,缓存没有走滞留副本,再没有给静态默认值,逐级尝试直到有东西可交付。声明式的价值在于路径是评审过的:每一级给什么质量的数据、打什么折扣,业务方签字后才上线,而不是故障发生时值班同学现场发挥。降级必须留痕,调用方拿到结果的同时知道它走了第几级、打了折,下游才能决定信多少;全链失败要显式抛错,不能假装成功。路径表还是演练脚本:平时按表注入故障验证每一级真的接得住,而不是等到事故才发现滞留副本早就过期了。

```python
# file: code/06_Agent与LLM及系统设计/q2839_fallback_path_table.py
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
```

**追问**:
- 追问一:降级结果会不会被误当实时数据存下来? 答:会,所以降级结果要带 degraded 标记且不回写缓存,只允许用于本次应答。
- 追问二:降级链的顺序能动态调吗? 答:可以按工具健康度把更可靠的级提前,但变更要走评审,顺序本身就是业务决策。
