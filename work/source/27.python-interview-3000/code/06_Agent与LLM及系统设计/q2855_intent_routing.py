"""Q2855 查询意图的分级路由:事实题 荟题与探索题各走各的管线。

「发票丢了怎么补」和「总结全部售后政策」不该走同一条检索管线:
事实题浅挖快答,总结题要多路召回加分段汇总,探索题要重排保多样。
规则路由按意图分派管线,匹配顺序即优先级。
"""

import re

PIPELINES = {
    "fact": {"top_k": 3, "rerank": False, "mode": "direct"},
    "summary": {"top_k": 12, "rerank": False, "mode": "map_reduce"},
    "exploratory": {"top_k": 8, "rerank": True, "mode": "two_stage"},
}


def classify(q):
    if re.match(r"^(总结|概述|帮我归纳)", q):
        return "summary"
    if re.search(r"多少钱|几号|多久|\d+\s*(天|元|个)", q):
        return "fact"
    if re.search(r"为什么|如何|怎么|对比", q):
        return "exploratory"
    return "fact"


def route(q):
    return PIPELINES[classify(q)]


def main():
    cases = [
        ("退款多久到账", "fact"),
        ("总结全部售后政策", "summary"),
        ("为什么退款会被驳回", "exploratory"),
        ("发票丢了怎么补", "exploratory"),
        ("退货要 7 天还是 15 天", "fact"),
    ]
    for q, want in cases:
        assert classify(q) == want, (q, classify(q), want)
    p = route("退款多久到账")
    assert p == {"top_k": 3, "rerank": False, "mode": "direct"}, p
    assert route("总结全部售后政策")["mode"] == "map_reduce"
    assert route("为什么退款会被驳回")["rerank"] is True
    print("退款多久到账 ->", route("退款多久到账"))
    print("总结全部售后政策 ->", route("总结全部售后政策"))
    print("为什么退款会被驳回 ->", route("为什么退款会被驳回"))


if __name__ == "__main__":
    main()
