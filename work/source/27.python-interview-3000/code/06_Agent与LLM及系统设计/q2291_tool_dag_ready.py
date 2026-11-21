"""就绪驱动的工具 DAG 执行:上游完成即解锁下游,输出绑定进下游参数,统计并行波次数。"""
from collections import defaultdict


def check_cycle(deps):
    state = {}

    def visit(n):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            raise ValueError("依赖环经过 %s" % n)
        state[n] = 1
        for d in deps[n]:
            visit(d)
        state[n] = 2
    for n in deps:
        visit(n)


def run_dag(tools, deps, inputs):
    check_cycle(deps)
    indeg = {n: len(d) for n, d in deps.items()}
    dependents = defaultdict(list)
    for n, ups in deps.items():
        for u in ups:
            dependents[u].append(n)
    results, order, waves = {}, [], []
    ready = sorted(n for n, k in indeg.items() if k == 0)
    while ready:
        waves.append(list(ready))
        nxt = []
        for name in ready:
            kwargs = dict(inputs.get(name, {}))
            for u in deps[name]:
                kwargs["from_" + u] = results[u]
            results[name] = tools[name](**kwargs)
            order.append(name)
            for down in dependents[name]:
                indeg[down] -= 1
                if indeg[down] == 0:
                    nxt.append(down)
        ready = sorted(nxt)
    return order, results, waves


if __name__ == "__main__":
    log = []
    tools = {
        "search": lambda q: log.append("search") or {"docs": 3},
        "rank": lambda from_search=None: log.append("rank") or {"top": from_search["docs"]},
        "fetch": lambda from_search=None: log.append("fetch") or {"full": from_search["docs"]},
        "answer": lambda from_rank=None, from_fetch=None: log.append("answer") or {"n": from_rank["top"] + from_fetch["full"]},
    }
    deps = {"search": [], "rank": ["search"], "fetch": ["search"], "answer": ["rank", "fetch"]}
    order, results, waves = run_dag(tools, deps, {"search": {"q": "退货"}})
    assert order.index("search") < order.index("rank") < order.index("answer")
    assert order.index("search") < order.index("fetch") < order.index("answer")
    assert len(waves) == 3 and sorted(waves[1]) == ["fetch", "rank"], "第二波应并行两个工具"
    assert results["answer"] == {"n": 6}, "上游输出正确绑定进下游"
    assert log[0] == "search" and log[-1] == "answer"

    try:
        run_dag(tools, {"a": ["b"], "b": ["a"]}, {})
        raise SystemExit("环检测失效")
    except ValueError:
        pass
    print("就绪驱动 DAG 通过:环拒绝 波次并行 上游输出绑定下游")
