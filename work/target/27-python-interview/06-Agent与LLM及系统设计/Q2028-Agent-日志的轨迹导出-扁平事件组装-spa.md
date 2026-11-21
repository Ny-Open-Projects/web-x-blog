---
title: [Q2028] Agent 日志的轨迹导出:扁平事件组装 span 树
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2028 · Agent 日志的轨迹导出:扁平事件组装 span 树

> 难度:★★☆☆ | 标签:Agent, 可观测性, 轨迹

**问**:线上 Agent 出了怪行为,日志是几百条扁平记录,怎么快速还原它当时到底怎么走的?

**答**:把日志从行升级为 span:每个事件带 span id、父 span、起止时间,导出时组装成树,根是本次会话,子节点是工具调用和 LLM 调用。导出器做三个校验:每个事件的父亲必须存在,孤儿事件报错;根 span 有且只有一个;兄弟按开始时间排序,父 span 的时间区间必须包住子 span。有了这棵树,慢在哪一步、哪次工具调用嵌套了鉴权检查,一眼可见;树序列化成 JSON 后可直接进轨迹系统。扁平日志回答发生了什么,span 树回答为什么和怎么发生的。

```python
# file: code/06_Agent与LLM及系统设计/q2028_trace_export.py
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
```

**追问**:
- 父子关系从哪来? 答:Agent 循环里每个动作入栈时创建 span,异常出栈时关闭,上下文变量自动传递父子关系
- 跨进程的调用怎么串起来? 答:把 trace id 和父 span id 写进消息头,下游服务继续展开子树,链路自然拼接
