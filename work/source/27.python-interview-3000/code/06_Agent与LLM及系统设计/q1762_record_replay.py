"""工具录制回放:真实执行时写卡带,回放时同参数直接命中,不产生副作用。"""
import json


def canon(args):
    return json.dumps(args, sort_keys=True, ensure_ascii=False)


class ToolRecorder:
    def __init__(self, real_tools):
        self.real = real_tools
        self.cassette = {}
        self.mode = "record"
        self.executed = 0

    def call(self, tool, args):
        key = tool + "::" + canon(args)
        if self.mode == "replay":
            if key not in self.cassette:
                raise KeyError("卡带无此调用: " + key)
            return self.cassette[key]["result"]
        self.executed += 1
        result = self.real[tool](args)
        self.cassette[key] = {"tool": tool, "args": canon(args), "result": result}
        return result

    def to_replay(self):
        self.mode = "replay"


def real_tools():
    return {"query_db": lambda a: {"rows": [a["sql"]], "cost": 42}}


if __name__ == "__main__":
    live = ToolRecorder(real_tools())
    r1 = live.call("query_db", {"sql": "select 1"})
    r2 = live.call("query_db", {"sql": "select 2"})
    assert live.executed == 2 and live.mode == "record"
    assert r1 == {"rows": ["select 1"], "cost": 42}

    live.to_replay()                             # 切换为离线回放
    p1 = live.call("query_db", {"sql": "select 1"})
    p2 = live.call("query_db", {"sql": "select 2"})
    assert live.executed == 2, "回放绝不触发真实执行"
    assert p1 == r1 and p2 == r2, "回放结果与录制逐字段一致"
    assert len(live.cassette) == 2

    miss = False
    try:
        live.call("query_db", {"sql": "select 3"})
    except KeyError as e:
        miss = "卡带无此调用" in str(e)
    assert miss, "未录制过的调用必须显式失败而不是伪造"
    print("录制回放通过:2 次录制后切回放 0 次执行,未命中显式报错")
