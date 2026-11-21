"""Agent 日志的轨迹导出:扁平事件流组装为 span 树 JSON,父子关系与时长可校验。"""
import json


class TraceExporter:
    def __init__(self):
        self.events = []

    def log(self, span_id, parent, name, start, end, attrs=None):
        self.events.append({"id": span_id, "parent": parent, "name": name,
                            "start": start, "end": end, "attrs": attrs or {}})

    def export(self):
        nodes = {e["id"]: dict(e, children=[]) for e in self.events}
        roots = []
        for e in self.events:
            p = e["parent"]
            if p is None:
                roots.append(nodes[e["id"]])
            elif p in nodes:
                nodes[p]["children"].append(nodes[e["id"]])
            else:
                raise ValueError("事件 %s 的父 span %s 不存在" % (e["id"], p))
        if len(roots) != 1:
            raise ValueError("一次轨迹应有且只有一个根 span")

        def sort_tree(n):
            n["children"].sort(key=lambda c: c["start"])
            for c in n["children"]:
                sort_tree(c)

        sort_tree(roots[0])
        return roots[0]

    def spans_json(self):
        return json.dumps(self.export(), ensure_ascii=False)


if __name__ == "__main__":
    t = TraceExporter()
    t.log("root", None, "agent.run", 0, 100)
    t.log("s2", "root", "tool.db_query", 30, 60, {"sql": "select 1"})
    t.log("s1", "root", "llm.chat", 5, 25)
    t.log("s3", "s2", "tool.auth_check", 32, 36)

    tree = t.export()
    assert tree["name"] == "agent.run"
    assert [c["name"] for c in tree["children"]] == ["llm.chat", "tool.db_query"]
    db = tree["children"][1]
    assert db["children"][0]["name"] == "tool.auth_check"
    # 父 span 必须包住子 span
    for c in tree["children"]:
        assert tree["start"] <= c["start"] and c["end"] <= tree["end"]
    parsed = json.loads(t.spans_json())
    assert parsed["id"] == "root"

    bad = TraceExporter()
    bad.log("x", "ghost", "orphan", 0, 1)
    try:
        bad.export()
        raise AssertionError("孤儿事件必须报错")
    except ValueError as e:
        assert "不存在" in str(e)
    print("轨迹导出通过:扁平日志组出两层的 span 树,兄弟有序 父包子 孤儿拦截")
