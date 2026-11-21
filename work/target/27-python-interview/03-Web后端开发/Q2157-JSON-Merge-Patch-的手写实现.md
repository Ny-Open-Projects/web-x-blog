---
title: [Q2157] JSON Merge Patch 的手写实现
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2157 · JSON Merge Patch 的手写实现

> 难度:★★★☆ | 标签:REST, PATCH

**问**:RFC 7386 的 JSON Merge Patch 到底定义了什么?手写一遍核心算法要几行?

**答**:Merge Patch 把 PATCH 请求体本身当作"目标文档想要的样子",三条规则构成全部语义:补丁是对象时逐键合并,值仍是对象则递归;值为 null 表示删除该键;值为数组或标量时整体替换,不做元素级合并。补丁不是对象时,直接用它替换整个目标文档。手写核心算法只有十几行递归,但面试官真正想听的是边界:数组永远整体替换(所以列表类字段的大文档不适合 Merge Patch)、null 的唯一语义是删除(所以无法把字段"置 null 保留"),以及服务端必须拒绝 Content-Type 不是 merge-patch+json 的 PATCH 体。这三条决定了它适合字段稀疏更新,不适合结构复杂的文档。

```python
# file: code/03_Web后端开发/q2157_merge_patch.py
"""RFC 7386 JSON Merge Patch: 递归合并与 null 删除语义(纯标准库)。"""


def merge_patch(target, patch):
    """Merge Patch 核心算法。
    patch 是 dict: 逐键合并, 值为 None 表示删除该键, 值为 dict 递归, 其他值整体替换。
    patch 不是 dict: 直接替换整个目标文档。
    """
    if not isinstance(patch, dict):
        return patch
    result = dict(target) if isinstance(target, dict) else {}
    for key, value in patch.items():
        if value is None:
            result.pop(key, None)                       # null 的唯一语义: 删除成员
        elif isinstance(value, dict):
            result[key] = merge_patch(result.get(key), value)
        else:
            result[key] = value
    return result


doc = {"title": "旧标题", "tags": ["a"], "meta": {"color": "red", "size": "L"},
       "obsolete": True}
patch = {"title": "新标题", "meta": {"color": "blue"}, "obsolete": None, "extra": 1}
merged = merge_patch(doc, patch)
print("原文档:", doc)
print("补丁  :", patch)
print("结果  :", merged)
assert merged == {"title": "新标题", "tags": ["a"],
                  "meta": {"color": "blue", "size": "L"}, "extra": 1}
assert merge_patch({"tags": [1, 2]}, {"tags": [3]}) == {"tags": [3]}   # 数组整体替换
assert merge_patch({"a": 1}, "flat") == "flat"                          # 非对象补丁整体替换
assert "obsolete" not in merged                                         # null 即删除
print("要点: 对象递归合并、null 即删除、数组与标量整体替换, 三条规则就是 RFC 7386 的全部")
```

**追问**:
- Merge Patch 怎么表达"把 tags 数组追加一个元素"?——表达不了,只能整体提交新数组,高并发下会丢并发写,这时要换 JSON Patch 或子资源端点。
- 为什么 null 不能表示"置空"?——RFC 7386 规定 null 只用于删除成员,想保留键并置 null 只能换哨兵值或改用 JSON Patch。
