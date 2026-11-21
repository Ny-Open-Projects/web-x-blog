---
title: [Q1079] pytest 插件机制与 hookimpl
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1079 · pytest 插件机制与 hookimpl

> 难度:★★★★★ | 标签:pytest, 插件

**问**:pytest 的插件体系底层是什么?写一个最小插件要做什么?

**答**:底层是 pluggy:pytest 定义一组钩子规范(hook spec),插件实现同名钩子函数(装饰 `@pytest.hookimpl`),pluggy 在框架执行的固定时点调用所有实现,结果可按 firstresult/historic 语义合并。分发方式三种:入口点(setuptools entry-points,安装即生效)、`conftest.py`(目录级)、`-p` 参数(显式加载)。写插件的最小集:实现 1-2 个钩子如 `pytest_addoption`、`pytest_collection_modifyitems`,再加 setup.cfg 声明 entry point。理解 pluggy 后,pytest 的一切"魔法"都是钩子调用的结果。

```python
# file: code/05_数据分析与工程化/q1079_plugin_mechanism.py

class Registry:
    """pluggy 思想的最小实现:钩子名 -> 依次调用所有插件的实现"""

    def __init__(self):
        self.plugins = []

    def register(self, plugin):
        self.plugins.append(plugin)

    def call(self, hook, payload):
        results = []
        for p in self.plugins:
            method = getattr(p, hook, None)
            if method is not None:
                results.append(method(payload))
        return results

class TimingPlugin:
    def before_run(self, payload):
        print(f"[timing] start {payload['name']}")
        return "started"

    def after_run(self, payload):
        print(f"[timing] finished {payload['name']}")
        return "finished"

class RetryPlugin:
    def on_result(self, payload):
        if not payload["ok"]:
            print(f"[retry] will retry {payload['name']}")
            return "retry"

if __name__ == "__main__":
    reg = Registry()
    reg.register(TimingPlugin())
    reg.register(RetryPlugin())
    reg.call("before_run", {"name": "test_a"})
    reg.call("on_result", {"name": "test_a", "ok": False})
    reg.call("after_run", {"name": "test_a"})
    # 真实 pytest:插件经 entry-points 装载,钩子函数用 @pytest.hookimpl 标注
```

**追问**:
- 追问 1:两个插件都实现同一钩子,顺序谁定?—— 注册顺序加 hookimpl 的 tryfirst/trylast 调整,`hookwrapper` 还能包裹原实现。
- 追问 2:conftest.py 本质上是什么?—— 一个按目录自动注册的本地插件,pytest 收集时沿目录向上查找并依次装载。
