
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
