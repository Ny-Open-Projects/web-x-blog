"""任务调度最小 DAG 执行器: 依赖校验 + Kahn 分层 + 失败传染跳过 + 环检测"""
import json


class DagError(Exception):
    pass


def make_task(name, fail=False):
    """构造一个可执行任务: 打印进入/退出, fail=True 模拟运行失败"""
    def fn():
        print("  执行 %s" % name)
        if fail:
            raise RuntimeError(name + " 写库超时")
        return True
    return fn


class DagExecutor:
    def __init__(self, name=""):
        self.name = name
        self.nodes = {}  # task -> {"deps": set, "fn": callable}

    def add(self, task, deps=(), fn=None):
        self.nodes[task] = {"deps": set(deps), "fn": fn}

    def layers(self):
        """Kahn 算法分层: 同层任务可并行, 层间串行; 有环则抛 DagError"""
        for task in self.nodes:
            for d in self.nodes[task]["deps"]:
                if d not in self.nodes:
                    raise DagError("未知依赖: %s -> %s" % (task, d))
        indeg = {t: len(self.nodes[t]["deps"]) for t in self.nodes}
        dependents = {t: set() for t in self.nodes}
        for t, spec in self.nodes.items():
            for d in spec["deps"]:
                dependents[d].add(t)
        placed, layers = [], []
        cur = sorted(t for t, k in indeg.items() if k == 0)
        while cur:
            layers.append(cur)
            placed.extend(cur)
            nxt = []
            for t in cur:
                for m in sorted(dependents[t]):
                    indeg[m] -= 1
                    if indeg[m] == 0:
                        nxt.append(m)
            cur = sorted(nxt)
        if len(placed) != len(self.nodes):
            stuck = sorted(set(self.nodes) - set(placed))
            raise DagError("存在环, 无法调度: " + ", ".join(stuck))
        return layers

    def run(self):
        """按层执行: 失败与跳过都会传染, 下游一律 SKIPPED"""
        results = {}
        blocked = set()
        for layer in self.layers():
            for t in layer:
                deps = self.nodes[t]["deps"]
                if deps & blocked:
                    results[t] = "SKIPPED"
                    blocked.add(t)
                    continue
                try:
                    self.nodes[t]["fn"]()
                    results[t] = "OK"
                except Exception as e:
                    results[t] = "FAILED: %s" % e
                    blocked.add(t)
        return results


if __name__ == "__main__":
    dag = DagExecutor("订单日报")
    dag.add("extract", fn=make_task("extract"))
    dag.add("load", ["extract"], make_task("load", fail=True))
    dag.add("agg", ["load"], make_task("agg"))
    dag.add("mail", ["agg"], make_task("mail"))
    dag.add("archive_raw", ["extract"], make_task("archive_raw"))
    print("分层结果:", dag.layers())
    print("执行台账:", json.dumps(dag.run(), ensure_ascii=False, indent=None))

    cyclic = DagExecutor("坏图")
    cyclic.add("a", ["c"], make_task("a"))
    cyclic.add("b", ["a"], make_task("b"))
    cyclic.add("c", ["b"], make_task("c"))
    try:
        cyclic.layers()
    except DagError as e:
        print("故意造环被拦截:", e)

    missing = DagExecutor("缺依赖")
    missing.add("x", ["ghost"], make_task("x"))
    try:
        missing.layers()
    except DagError as e:
        print("故意缺依赖被拦截:", e)
    print("要点: 调度器三件事——拓扑分层给并行度, 未知依赖与环在执行前拦截, 失败传染保证下游不吃脏输入")
