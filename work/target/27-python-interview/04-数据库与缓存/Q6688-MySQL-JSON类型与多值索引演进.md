---
title: [Q6688] MySQL JSON 类型与多值索引的演进迁移
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6688 · 从 TEXT 存 JSON 到 JSON 类型 + 多值索引：一个标签查询的演进

难度：P6 ｜ 标签：版本演进、MySQL JSON、多值索引
基线：MySQL 5.7（JSON 类型引入）→ 8.0.17（多值索引 Multi-Valued Index）→ 8.0+。

**问**：商品表用 TEXT 字段存了标签数组 JSON，"查包含某标签的商品"全表扫描。演进到 MySQL 8.0 的 JSON 类型与多值索引，怎么改？每一步解决了什么、付出什么代价？

**答**：**结论**：三步演进：① **TEXT→JSON 类型**：JSON 类型写入时做格式校验与**二进制列式存储**，`JSON_EXTRACT` 不用每次解析文本，但列不能直接建普通索引；② **生成列 + 普通索引**：对固定路径（如 `$.brand`）加生成列并索引——单值路径索引问题解决；③ **多值索引（8.0.17+）**：`CREATE INDEX ... ((CAST(tags->'$' AS UNSIGNED ARRAY)))`，让"数组包含某元素"这类 `MEMBER OF` / `JSON_CONTAINS` 查询走索引——数组语义的索引终于原生支持。代价：多值索引只支持等值/包含类谓词，`optimizer` 对 `JSON_TABLE` 参与的复杂查询仍可能不选；写入路径每次更新整个 JSON 文档都要**重写全列**（MySQL JSON 无局部更新），大文档高频更新是反模式。

**取舍**：JSON 索引 vs 关系化拆表：查询模式固定且只有 1-2 个路径，生成列索引最简单；查询模式长尾、标签还会做聚合统计，回归"标签表 + 关联表"的经典关系化更稳。JSON 多值索引的隐含约束是**数组元素类型必须一致**（CAST 声明什么就是什么），混入字符串元素静默不走索引——这是最常见的"索引建了却不生效"事故。

**实战**：用 Python 演示 CAST 语义与查询命中判断（SQL 逻辑用标准库模拟验证）：

```python
# MySQL JSON 多值索引的语义模拟：什么查询能走索引
import json
from typing import Any

DDL = """
CREATE TABLE product (
  id BIGINT PRIMARY KEY,
  tags JSON,
  INDEX mv ((CAST(tags->'$' AS UNSIGNED ARRAY)))   -- 8.0.17+ 多值索引
);
"""

def explain_hit(query_pred: str, index_elem_type: str = "UNSIGNED") -> bool:
    """多值索引只对 MEMBER OF / JSON_CONTAINS 等值类谓词生效。"""
    ok_preds = {
        "MEMBER OF", "JSON_CONTAINS", "JSON_OVERLAPS",
    }
    return any(p in query_pred.upper() for p in ok_preds)

docs = [
    {"tags": [1, 5, 9]},          # 全数字：可 CAST 为 UNSIGNED ARRAY
    {"tags": ["sale", 5]},        # 混入字符串：CAST 失败的元素被跳过/报错
]

for d in docs:
    try:
        vals = [int(x) for x in d["tags"]]
        castable = True
    except ValueError:
        vals, castable = [], False
    q = f"SELECT id FROM product WHERE 3 MEMBER OF(tags->'$')"
    print(f"doc={d['tags']} castable={castable} "
          f"谓词命中索引={explain_hit(q)}")

# TEXT->JSON 的读取收益：TEXT 每次读要 parse，JSON 类型读取直接取二进制
import timeit
text_doc = json.dumps({"tags": list(range(50)), "attrs": {"a": 1}})
parse_cost = timeit.timeit(lambda: json.loads(text_doc), number=10_000) / 10_000
print(f"TEXT 路径每次读取需解析: {parse_cost*1e6:.1f} us/次（JSON 类型省掉）")

# 写放大：更新一个属性也要重写全列
doc_size_kb = len(text_doc.encode()) / 1024
updates = 1000
print(f"高频小更新场景：{updates} 次更新重写 {updates*doc_size_kb:.0f} KB —— "
      f"这类负载应拆属性表而非塞 JSON")
```

**追问 1**：多值索引为什么只支持等值/包含类谓词？范围查询怎么办？
提示：索引按"元素→行"的倒排组织，支持成员判断；范围谓词需在生成列上做单值标量索引或引入 `JSON_TABLE` 物化。

**追问 2**：`JSON_OVERLAPS` 与 `MEMBER OF` 在优化器上的差别？
提示：`MEMBER OF` 对单个常量是标准点查；`JSON_OVERLAPS` 两侧都是数组时索引利用受限，常退化为全扫——大表上要用 EXPLAIN 验证。

**追问 3**：从 TEXT 迁到 JSON 类型的在线变更怎么做？
提示：JSON 校验使直改可能失败（历史脏数据），先清洗 + gh-ost/instANT DDL 双轨回填 + 双写对账，灰度读新列后切流。

## 背诵要点
1. 三步演进：TEXT→JSON（校验+二进制存储）→ 生成列索引（单值路径）→ 多值索引 8.0.17+（数组成员谓词）。
2. 多值索引只吃等值/包含谓词（MEMBER OF / JSON_CONTAINS），元素类型与 CAST 声明不一致则静默不走索引。
3. MySQL JSON 无局部更新：每次更新重写全列，高频小更新负载应拆表而不是塞 JSON。

## 复盘追问
1. 你们线上有没有"建了 JSON 索引却全表扫"的查询？EXPLAIN 验证是例行动作还是出问题才看？
2. 当时选 JSON 而不是拆表的理由是什么？如果查询模式后来变多了，回拆的迁移成本算过吗？
