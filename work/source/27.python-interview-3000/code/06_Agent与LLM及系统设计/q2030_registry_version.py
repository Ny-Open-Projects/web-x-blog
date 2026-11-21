"""工具注册表的版本管理:多版本并存 默认路由最新稳定版 弃用版本调用留痕告警。"""
import warnings


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name, version, func, stable=True):
        self.tools.setdefault(name, {})[version] = {"func": func, "stable": stable}

    def deprecate(self, name, version):
        self.tools[name][version]["deprecated"] = True

    def resolve(self, name, version=None):
        versions = self.tools.get(name)
        if not versions:
            raise KeyError("工具 %s 未注册" % name)
        if version is None:
            stable = [v for v, e in versions.items()
                      if e.get("stable") and not e.get("deprecated")]
            version = max(stable or list(versions))
        if version not in versions:
            raise KeyError("工具 %s 无版本 %s" % (name, version))
        entry = versions[version]
        meta = {"name": name, "version": version,
                "deprecated": entry.get("deprecated", False)}
        return entry["func"], meta


def call_with_meta(func, args, meta):
    """调用并处理弃用告警:降级为日志事件而不是让调用失败。"""
    events = []
    if meta["deprecated"]:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            warnings.warn("工具 %s@%s 已弃用,请迁移" % (meta["name"], meta["version"]))
            events = [str(x.message) for x in w]
    return func(**args), events


if __name__ == "__main__":
    reg = ToolRegistry()

    def query_v1(sql):
        return {"rows": sql}

    def query_v2(sql, limit=10):
        return {"rows": sql, "limit": limit}

    reg.register("db_query", "1.0", query_v1)
    reg.register("db_query", "2.0", query_v2)
    reg.deprecate("db_query", "1.0")

    fn, meta = reg.resolve("db_query")            # 不带版本 -> 最新稳定版
    assert meta["version"] == "2.0" and meta["deprecated"] is False

    fn1, meta1 = reg.resolve("db_query", "1.0")   # 显式钉住旧版仍可用
    res, events = call_with_meta(fn1, {"sql": "select 9"}, meta1)
    assert res == {"rows": "select 9"} and events, "钉住弃用版要能跑但必须留痕"

    try:
        reg.resolve("db_query", "9.9")
        raise AssertionError("未知版本必须报错")
    except KeyError:
        pass

    reg2 = ToolRegistry()
    reg2.register("beta_tool", "0.1", lambda: {}, stable=False)
    fn3, meta3 = reg2.resolve("beta_tool")
    assert meta3["version"] == "0.1", "无稳定版时退回任意版本而不是拒绝服务"
    print("版本管理通过:默认路由 2.0,钉旧版可用且留痕,未知版本显式报错")
