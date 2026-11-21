"""增量评估集:基线冻结 逐期追加用例 每期只跑增量加抽样基线,通过率分账。"""


class EvalSet:
    def __init__(self):
        self.cases = []
        self.frozen = {}

    def add_batch(self, batch, batch_no):
        added = []
        for c in batch:
            if any(x["id"] == c["id"] for x in self.cases):
                continue
            self.cases.append({"id": c["id"], "q": c["q"], "expect": c["expect"],
                               "batch": batch_no})
            self.frozen[c["id"]] = c["expect"]
            added.append(c["id"])
        return added

    def run(self, system, new_ids, sample_baseline):
        results = []
        for c in self.cases:
            if c["id"] in new_ids or c["id"] in sample_baseline:
                got = system(c["q"])
                results.append((c["id"], got == self.frozen[c["id"]]))
        return results


if __name__ == "__main__":
    es = EvalSet()
    b1 = es.add_batch([{"id": "q1", "q": "退货政策", "expect": "30天"},
                       {"id": "q2", "q": "退款进度", "expect": "3个工作日"},
                       {"id": "q3", "q": "发票开具", "expect": "支持"}], batch_no=1)
    assert b1 == ["q1", "q2", "q3"]
    dup = es.add_batch([{"id": "q1", "q": "退货政策", "expect": "被改坏的期望"}], batch_no=2)
    assert dup == [] and es.frozen["q1"] == "30天", "同 id 重入库被拒 旧期望不漂移"
    b2 = es.add_batch([{"id": "q4", "q": "换货流程", "expect": "7天"}], batch_no=2)
    assert b2 == ["q4"]

    def system(q):
        return {"退货政策": "30天", "退款进度": "3个工作日",
                "发票开具": "支持", "换货流程": "7天"}[q]

    results = es.run(system, new_ids=set(b2), sample_baseline={"q1", "q3"})
    assert len(results) == 3, "增量全跑 基线抽样 q2 本期不跑省成本"
    assert all(p for _, p in results)
    assert dict(results) == {"q1": True, "q3": True, "q4": True}
    print("增量评估集通过:批次追加 期望冻结 增量加抽样分账")
