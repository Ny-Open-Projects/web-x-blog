"""graphlib:拓扑排序、并发就绪层与环检测。"""
from graphlib import CycleError, TopologicalSorter

deps = {
    "install": set(),
    "migrate": {"install"},
    "test": {"migrate"},
    "deploy": {"test"},
    "docs": {"install"},
}

if __name__ == "__main__":
    sorter = TopologicalSorter(deps)
    print("线性顺序:", list(sorter.static_order()))

    # 增量 API:按就绪层输出,适合并行调度
    sorter = TopologicalSorter(deps)
    sorter.prepare()
    layer = 0
    while sorter.is_active():
        ready = sorter.get_ready()
        print(f"第 {layer} 层可并发:", sorted(ready))
        for node in ready:
            sorter.done(node)
        layer += 1

    try:
        TopologicalSorter({"a": {"b"}, "b": {"a"}}).prepare()
    except CycleError as exc:
        print("环检测:", exc)
