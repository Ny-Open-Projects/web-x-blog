---
title: [Q6611] MySQL 排序规则差异导致判重失效事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6611 · MySQL 排序规则差异导致判重失效事故复盘

难度：P6 ｜ 标签：事故复盘 / 排序规则 / 唯一索引

**问**：业务侧用 Python 做了邮箱大小写归一后再判重，但线上仍然出现了同一邮箱两条记录，且唯一索引没拦住。事后发现新旧表（以及库与库之间）排序规则（collation）不一致。这类事故的完整机理是什么？怎么系统性排查与收口？

**答**：
- **结论**：机理分三层：① MySQL 的 `utf8mb4_general_ci` / `utf8mb4_0900_ai_ci` 等排序规则决定**字符串相等语义**——唯一索引的比较、`WHERE email = ?` 的命中、`GROUP BY` 的合并全部按 collation 走，而不是按字节；② 应用层的判重（Python 里 `email.lower()` 后查库）与数据库唯一索引的判重语义可能不一致：`ci`（不区分大小写）collation 下 `'ABC@x.com'` 与 `'abc@x.com'` 在索引层就是同一个键，Python 侧以为"归一过了"，实际撞在另一对字符上（如全角/半角、`ß` vs `ss` 在 0900_ai_ci 下相等）；③ 老库 `utf8mb4_general_ci`、新库默认 `utf8mb4_0900_ai_ci`，同一查询在两环境结果集不同，双写/迁移期间出现"这边判重通过、那边唯一键冲突"或反过来"该拦没拦"。本次事故的直接链路：迁移工具按字节复制数据（绕过 collation 比较）→ 新表 collation 变了 → 历史里两条在旧 collation 下不相等的邮箱，在新 collation 下相等 → 迁移后建唯一索引或后续写入触发冲突/漏判。
- **取舍**：排查顺序：① `SHOW CREATE TABLE` 对齐库/表/列三级 collation 与 `character_set`，`SELECT @@collation_connection` 检查连接默认值（驱动 `charset` 参数影响它）；② 找出"语义敏感列"（唯一键、判重字段、join 键），确认业务需要 ci 还是 cs/二进制语义——账号类字段通常要 `utf8mb4_0900_ai_ci` 或应用层强归一，token/哈希类字段必须 `utf8mb4_bin`；③ 收口手段优先级：改列 collation（`ALTER ... CONVERT TO CHARACTER SET`，注意重建索引锁与时长）> 应用层统一归一（NFKC + lower + 白名单）> 唯一键改表达式索引/前加归一列。双写过渡期用"字节比对 + collation 比对"双闸门，差异行人工裁决。
- **实战**：预防措施：① CI 里加 schema 快照 diff，collation/charset 纳入门禁，禁止新表 collation 与基线漂移；② Python 驱动显式 `charset='utf8mb4'`，别依赖服务器默认；③ 判重逻辑只在**一处**实现（数据库唯一索引为主），应用层归一函数与数据库 collation 做一致性测试（用 `ß`、全角、emoji 变体等构造用例）；④ 迁移后先跑 collation 敏感列的重复检测脚本再建唯一索引。

```python
# 排序规则语义差异模拟：不同 collation 下"相等"集合不同
# 基线：Python 3.9+ 标准库；真实场景用 MySQL SHOW COLLATION + 重复检测 SQL 验证
import unicodedata


def collate_general_ci(s: str) -> str:
    """模拟 utf8mb4_general_ci：小写折叠，近似不区分大小写/重音。"""
    return unicodedata.normalize("NFKD", s).casefold()


def collate_bin(s: str) -> str:
    """模拟 utf8mb4_bin：按码点（字节）比较。"""
    return s


def find_dupes(rows: list[str], collate) -> set[frozenset]:
    seen: dict[str, str] = {}
    dupes = set()
    for r in rows:
        key = collate(r)
        if key in seen and seen[key] != r:
            dupes.add(frozenset((seen[key], r)))
        seen[key] = seen.get(key, r)
    return dupes


def main() -> None:
    rows = ["ABC@x.com", "abc@x.com", "Straße@x.de", "STRASSE@x.de", "token_8f3a"]

    dupes_ci = find_dupes(rows, collate_general_ci)
    dupes_bin = find_dupes(rows, collate_bin)
    # ci 下大小写对冲突；0900_ai_ci 甚至 ß==ss（casefold 模拟这一行为）
    assert frozenset(("ABC@x.com", "abc@x.com")) in dupes_ci
    assert frozenset(("Straße@x.de", "STRASSE@x.de")) in dupes_ci
    assert dupes_bin == set()          # bin 下都不相等 -> 唯一索引"该拦的没拦"
    # token 类字段在 ci 下若恰巧只差大小写也会误判重
    assert find_dupes(["Token_8F3a", "token_8f3a"], collate_general_ci) != set()

    # 迁移检查：旧表 general_ci 允许的两行，新表语义下变重复 -> 建唯一索引会失败
    legacy_rows = ["Ann@x.com", "ANN@x.com"]
    assert find_dupes(legacy_rows, collate_general_ci) != set()

    print("OK: collation 决定唯一索引的相等语义，迁移前后必须对齐敏感列")
    print("  general_ci 撞对:", {"".join(sorted(p)) for p in dupes_ci})
    print("  bin 下撞对数:", len(dupes_bin))


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"迁移工具按字节复制数据"会放大这个问题？
→ 一句话提示：字节复制绕过了 collation 的相等语义，数据原样进来；等新表 collation 变化后再在业务写入路径上做比较，才会暴露冲突，问题被推迟到切换之后最危险的时刻。

**追问 2**：表达式唯一索引或"归一化影子列"方案各有什么代价？
→ 一句话提示：MySQL 8 函数索引让唯一键按归一表达式生效，查询也要匹配同样表达式才能走索引；影子列则要维护写路径一致性（触发器或应用双写），但普通索引可用、排查直观。

## 背诵要点
- collation 决定唯一索引、WHERE、GROUP BY 的相等语义：`utf8mb4_0900_ai_ci` 下 `ß==ss`、大小写不敏感；token/哈希类字段必须 `utf8mb4_bin`。
- 排查三级对齐：`@@collation_connection`（连接）→ 表默认 → 列；驱动 `charset` 参数决定连接默认，迁移工具按字节复制会把冲突推迟到切换后。
- 收口优先级：改列 collation > 应用层统一归一（NFKC+casefold）> 归一影子列/函数索引；schema collation 纳入 CI 门禁。

## 复盘追问
- 为什么这次唯一索引"该拦的没拦"而不是"不该拦的拦了"？提示：旧数据在旧 collation 下不相等（bin 语义或旧表无唯一索引），迁移后新 collation 认为相等——冲突暴露的时机取决于唯一索引何时建立。
- 应用层归一函数要与数据库 collation 做一致性测试，怎么构造用例？提示：NFKC 折叠对（全角/半角）、casefold 对（ß/ss、土耳其 İ）、emoji 变体选择符（U+FE0F），每类各造一对"看起来不同、语义相同"的字符串。
