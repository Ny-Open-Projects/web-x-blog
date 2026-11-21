---
title: [Q1507] 评估集版本化:快照指纹与跨版本 diff
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1507 · 评估集版本化:快照指纹与跨版本 diff

> 难度:★★☆ | 标签:RAG, 评估, 版本管理

**问**:评估集被同事改了,分数涨了,怎么知道是模型变好还是考题变简单?

**答**:把评估集当代码管理:每次提交生成不可变快照,内容寻址指纹防篡改,版本链记录父子关系,任何分数都必须绑定版本号。跨版本 diff 按用例 id 算三类变更:新增、删除、修改,分数对比必须在同一版本内进行,跨版本的分数差异要拆解为变更贡献与真实性能变化。回滚以历史版本为基础提交新版本,历史快照永远不动。指纹校验能在任何时候发现用例被篡改,这在多人协作与审计场景是底线能力。演进方向是评估集与模型版本一起登记,回归报告自动带上两个坐标。

```python
# file: code/06_Agent与LLM及系统设计/q1507_evalset_version.py
"""评估集版本化:快照指纹、版本链、跨版本 diff 新增删除修改,可回滚引用。"""
import hashlib
import json


class EvalSetStore:
    """评估集仓库:每次提交生成不可变快照,版本号递增,内容寻址防篡改。"""

    def __init__(self):
        self.versions = {}                 # v -> {"cases": [...], "parent": v-1, "hash": ...}
        self.head = None

    @staticmethod
    def _hash(cases):
        return hashlib.sha256(json.dumps(cases, sort_keys=True, ensure_ascii=False)
                              .encode()).hexdigest()[:12]

    def commit(self, cases, note=""):
        v = 1 if self.head is None else self.head + 1
        self.versions[v] = {"cases": [dict(c) for c in cases],
                            "parent": self.head, "note": note,
                            "hash": self._hash(cases)}
        self.head = v
        return v

    def get(self, v=None):
        return self.versions[v or self.head]["cases"]

    def checkout(self, v):
        """回滚:以历史版本内容为基础提交新版本,历史保持不可变。"""
        assert v in self.versions, "版本不存在"
        return [dict(c) for c in self.versions[v]["cases"]]

    def diff(self, v_from, v_to):
        """以 case id 为主键:新增 删除 修改 三类变更。"""
        a = {c["id"]: c for c in self.versions[v_from]["cases"]}
        b = {c["id"]: c for c in self.versions[v_to]["cases"]}
        added = sorted(set(b) - set(a))
        removed = sorted(set(a) - set(b))
        changed = sorted(k for k in set(a) & set(b) if a[k] != b[k])
        return {"added": added, "removed": removed, "changed": changed}

    def verify(self, v):
        return self.versions[v]["hash"] == self._hash(self.versions[v]["cases"])


if __name__ == "__main__":
    store = EvalSetStore()
    v1 = store.commit([{"id": "q1", "q": "退款多久", "rel": ["d1"]},
                       {"id": "q2", "q": "发票怎么开", "rel": ["d2"]}], note="初版")
    v2 = store.commit([{"id": "q1", "q": "退款多久", "rel": ["d1"]},
                       {"id": "q3", "q": "积分过期吗", "rel": ["d3"]},
                       {"id": "q2", "q": "电子发票在哪开", "rel": ["d2"]}], note="补查询 改写q2")

    d = store.diff(v1, v2)
    assert d == {"added": ["q3"], "removed": [], "changed": ["q2"]}
    assert store.get(v1) != store.get(v2), "快照互不影响"
    assert store.checkout(v1)[0]["q"] == "退款多久"
    v3 = store.commit(store.checkout(v1), note="回滚到初版再修")   # 基于历史版本演化
    assert store.diff(v1, v3) == {"added": [], "removed": [], "changed": []}

    tamper = store.versions[v1]["cases"][0]["q"] = "被篡改"
    assert store.verify(v1) is False, "内容寻址能发现篡改"
    assert store.verify(v2) is True
    assert store.versions[v2]["parent"] == v1 and store.versions[v3]["parent"] == v2
    print("评估集版本化通过:v1→v2 增 1 改 1 回滚演化零 diff 篡改被指纹识破")
```

**追问**:
- 用例 id 怎么保证稳定? 答:id 一旦分配不可复用,修改内容不改 id,删除要标记而非物理移除;
- 快照存哪里? 答:内容寻址对象存储加版本指针,大评估集按版本增量存差异。
