"""任务分解器:规则模板拆解 + LLM 拆解校验(无环/引用合法/叶子可执行)。"""
import json


TOOLBOX = {"search", "calculator", "writer", "chart"}


class Decomposer:
    def rule_based(self, goal):
        if "报告" in goal:
            tasks = [
                {"id": "t1", "type": "search", "deps": [], "desc": "收集数据"},
                {"id": "t2", "type": "calculator", "deps": ["t1"], "desc": "计算指标"},
                {"id": "t3", "type": "writer", "deps": ["t1", "t2"], "desc": "撰写报告"},
                {"id": "t4", "type": "chart", "deps": ["t2"], "desc": "生成图表"},
            ]
            return tasks, "ok"
        return [{"id": "t1", "type": "search", "deps": [], "desc": goal}], "ok"

    def llm_based(self, goal):
        # FakeLLM 桩:返回一个含错误依赖的拆解,演示校验拦截
        raw = json.dumps([
            {"id": "a", "type": "search", "deps": [], "desc": "查"},
            {"id": "b", "type": "writer", "deps": ["a", "c"], "desc": "写"},
            {"id": "c", "type": "chart", "deps": ["b"], "desc": "图"},
        ])
        return self._validate(raw)

    def _validate(self, raw):
        try:
            tasks = json.loads(raw)
        except json.JSONDecodeError:
            return None, "JSON 不合法"
        ids = {t["id"] for t in tasks}
        for t in tasks:
            if t["type"] not in TOOLBOX:
                return None, f"任务 {t['id']} 类型不可执行 {t['type']}"
            for d in t["deps"]:
                if d not in ids:
                    return None, f"任务 {t['id']} 依赖不存在的 {d}"
        # 环检测:Kahn
        indeg = {t["id"]: 0 for t in tasks}
        for t in tasks:
            for d in t["deps"]:
                indeg[t["id"]] += 1
        queue, seen = [i for i, v in indeg.items() if v == 0], 0
        adj = {t["id"]: [x["id"] for x in tasks if t["id"] in x["deps"]] for t in tasks}
        while queue:
            n = queue.pop()
            seen += 1
            for m in adj[n]:
                indeg[m] -= 1
                if indeg[m] == 0:
                    queue.append(m)
        if seen != len(tasks):
            return None, "依赖存在环"
        return tasks, "ok"


if __name__ == "__main__":
    d = Decomposer()
    ok_tasks, status = d.rule_based("生成季度报告")
    print("模板拆解:", [(t["id"], t["type"]) for t in ok_tasks], status)
    assert status == "ok" and ok_tasks[2]["deps"] == ["t1", "t2"]

    bad, why = d.llm_based("自由目标")
    print("LLM 拆解校验:", why, "(b 与 c 互相依赖)")
    assert bad is None and "环" in why, "循环依赖必须被拦截"
    print("校验器把不合格拆解挡在执行前")
