---
title: [Q2168] sparse fieldsets 的演进:嵌套字段选择
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2168 · sparse fieldsets 的演进:嵌套字段选择

> 难度:★★★★ | 标签:REST, 字段裁剪

**问**:带 include 的复合响应里,sparse fieldsets 从 v1 平铺参数演进到 v2 嵌套语法,要考虑什么?

**答**:平铺的 fields=title,views 只能裁剪主资源,复合响应里 included 的每个资源类型需要独立的掩码,于是演进出 JSON:API 风格的 fields[author]=name&fields[comment]=text。演进要处理四件事:两套参数并存时的优先级与兼容(老参数继续生效一个版本窗口);掩码的保留字段规则——type 与 id 是资源标识,永远保留,否则客户端无法关联;解析器从单个查询参数变成多参数正则提取;最重要的代价是序列化缓存的键必须包含全部掩码组合,否则不同字段集的响应会互相污染,缓存基数爆炸时要对掩码做规范化(排序、去空)并设组合上限。

```python
# file: code/03_Web后端开发/q2168_sparse_fieldsets_v2.py
"""sparse fieldsets 演进: 平铺 fields 到按资源的嵌套掩码(纯标准库)。"""
import re

RESPONSE = {
    "data": {"type": "article", "id": 1, "title": "T", "body": "B", "views": 9},
    "included": [
        {"type": "author", "id": 7, "name": "Ann", "email": "a@x.io", "bio": "b"},
        {"type": "comment", "id": 31, "text": "好文", "ip": "10.0.0.1"},
    ],
}
NESTED_RE = re.compile(r"fields\[([a-z_]+)\]")      # fields[author] 形态的键


def parse_fieldsets(query_pairs):
    """返回 (平铺掩码, 按类型的嵌套掩码); 两套参数并存。"""
    flat, nested = None, {}
    for key, value in query_pairs:
        m = NESTED_RE.fullmatch(key)
        if m:
            nested[m.group(1)] = {f.strip() for f in value.split(",") if f.strip()}
        elif key == "fields":
            flat = {f.strip() for f in value.split(",") if f.strip()}
    return flat, nested


def apply_fieldsets(doc, flat, nested):
    """主资源用平铺掩码, included 按类型用嵌套掩码; type 与 id 恒保留。"""
    data = dict(doc["data"])
    if flat:
        data = {k: v for k, v in data.items() if k in flat or k in ("type", "id")}
    included = []
    for inc in doc["included"]:
        mask = nested.get(inc["type"])
        if mask:
            inc = {k: v for k, v in inc.items() if k in mask or k in ("type", "id")}
        included.append(inc)
    return {"data": data, "included": included}


flat, nested = parse_fieldsets(
    [("fields", "id,title"), ("fields[author]", "name"), ("fields[comment]", "text")])
out = apply_fieldsets(RESPONSE, flat, nested)
print("主资源:", out["data"])
print("included:", [(i["type"], sorted(i)) for i in out["included"]])
assert "email" not in out["included"][0] and "ip" not in out["included"][1]
assert out["included"][0]["type"] == "author" and out["data"]["id"] == 1
print("要点: 嵌套掩码按类型下推, type 与 id 恒保留; 代价是序列化缓存键必须含全部掩码组合并做规范化")
```

**追问**:
- 掩码组合爆炸怎么办?——掩码规范化后设组合上限,超出按最近通用掩码降级并打点,或者干脆放弃缓存改实时序列化。
- 客户端传 fields[author]=email 这种敏感字段怎么办?——掩码先与该类型的公开白名单求交,敏感字段从源头就不可选。
