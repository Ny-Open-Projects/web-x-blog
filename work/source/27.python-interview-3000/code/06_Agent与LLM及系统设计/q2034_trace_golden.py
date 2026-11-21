"""端到端回归的轨迹金样本:把工具调用序列与终态做成指纹快照,差异需审批才更新。"""
import hashlib
import json


def trace_core(trace):
    return {"tool_seq": [t["tool"] + ":" + t["args"] for t in trace["tool_calls"]],
            "answer": trace["answer"]}


def fingerprint(trace):
    """轨迹指纹:只取工具序列与终答,时间戳等噪声不参与。"""
    return hashlib.sha256(
        json.dumps(trace_core(trace), ensure_ascii=False, sort_keys=True)
        .encode("utf-8")).hexdigest()[:12]


def diff_trace(golden, actual):
    diffs = []
    if trace_core(golden)["tool_seq"] != trace_core(actual)["tool_seq"]:
        diffs.append("工具序列变化")
    if golden["answer"] != actual["answer"]:
        diffs.append("终答变化")
    return diffs


class GoldenStore:
    def __init__(self):
        self.golden = {}

    def approve(self, case, trace):
        """人工审批后的差异才允许写入金样本。"""
        self.golden[case] = {"fingerprint": fingerprint(trace), "trace": trace}

    def check(self, case, trace):
        if case not in self.golden:
            return {"status": "new", "diffs": []}
        g = self.golden[case]
        if g["fingerprint"] != fingerprint(trace):
            return {"status": "diff", "diffs": diff_trace(g["trace"], trace)}
        return {"status": "match", "diffs": []}


if __name__ == "__main__":
    store = GoldenStore()
    v1 = {"tool_calls": [{"tool": "search", "args": "退货政策"}],
          "answer": "7 天无理由退货"}
    store.approve("退货问答", v1)

    same = store.check("退货问答", v1)
    assert same["status"] == "match"

    # 换了工具参数但终答一致:仍算差异,序列敏感性是轨迹金样本的意义
    v2 = {"tool_calls": [{"tool": "search", "args": "退货流程"}],
          "answer": "7 天无理由退货"}
    r2 = store.check("退货问答", v2)
    assert r2["status"] == "diff" and r2["diffs"] == ["工具序列变化"]

    v3 = {"tool_calls": [{"tool": "search", "args": "退货政策"}],
          "answer": "15 天可退"}
    r3 = store.check("退货问答", v3)
    assert r3["diffs"] == ["终答变化"]

    v4 = {"tool_calls": [{"tool": "kb_search", "args": "退货"}],
          "answer": "15 天可退"}
    r4 = store.check("退货问答", v4)
    assert sorted(r4["diffs"]) == ["工具序列变化", "终答变化"]

    store.approve("退货问答", v4)             # 审批通过,金样本升级
    assert store.check("退货问答", v4)["status"] == "match"
    assert store.check("新用例", v1)["status"] == "new", "无金样本标记为 new 而非 fail"
    print("轨迹金样本通过:指纹稳定 序列与终答分级报差,审批后才更新金样本")
