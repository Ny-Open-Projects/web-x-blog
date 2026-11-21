---
title: [Q1625] 快照更新的 diff 审查门禁
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1625 · 快照更新的 diff 审查门禁

> 难度:★★★☆ | 标签:测试, 研发流程

**问**:快照 diff 出现删除或类型变化时,合并门禁应该怎么分级处理?

**答**:把 diff 分三级:新增字段是兼容变更,快照随 PR 更新自动通过;删除字段与类型变化是破坏性变更,默认阻断合并;确需破坏时走评审豁免——提交说明标注 BREAKING、记录影响调用方、按弃用流程先加后删。门禁的判断要机器化:diff 分类器输出 breaking 列表,CI 看列表为空才放行,不靠人眼扫 diff。豁免记录进变更台账,回溯时能说清谁在哪个版本同意了删这个字段。这套流程把快照挂了从烦人的红灯变成契约治理的抓手。

```python
# file: code/03_Web后端开发/q1625_snapshot_review.py
"""快照更新治理: diff 分级与合并门禁(纯标准库)。"""


def classify_diff(old, new):
    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(k for k in set(old) & set(new) if old[k] != new[k])
    # 分级: 新增可选输出是兼容变更; 删除或类型变化是破坏性变更
    breaking = removed + changed
    return {"added": added, "removed": removed, "changed": changed, "breaking": breaking}


def merge_gate(diff, approved_breaking=False):
    if not diff["breaking"]:
        return "自动通过", "纯新增, 快照随 PR 更新"
    if approved_breaking:
        return "人工放行", "破坏性变更已评审: " + ", ".join(diff["breaking"])
    return "阻断合并", "请评审破坏性变更并在提交说明中标注 BREAKING"


old_snap = {"buyer": "dict", "id": "str", "status": "str", "stable.id": "ord_1"}

new_snap = dict(old_snap, coupon="NoneType")                # 兼容新增
diff_ok = classify_diff(old_snap, new_snap)
print("新增场景:", diff_ok)
print("门禁:", merge_gate(diff_ok))

removed_snap = {k: v for k, v in old_snap.items() if k != "buyer"}   # 删字段
diff_bad = classify_diff(old_snap, removed_snap)
print("删除场景门禁:", merge_gate(diff_bad))
print("评审后放行:", merge_gate(diff_bad, approved_breaking=True))
```

**追问**:
- 豁免被滥用怎么办?——豁免必须在 PR 描述写影响面与迁移指引,台账定期审计豁免率。
- 内部服务也要这么严吗?——调用方可控的服务可降级为通知加观察,对外 API 必须硬门禁。
