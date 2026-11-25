---
title: [Q6678] utf8mb3到utf8mb4迁移破坏点
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6678 · utf8mb3 到 utf8mb4 迁移：那些会炸的破坏点

难度：P6 ｜ 标签：版本演进、MySQL、字符集
基线：MySQL 5.7（utf8mb4 可用但默认仍 utf8mb3）→ 8.0（默认 utf8mb4）。

**问**：MySQL 8.0 默认字符集从 utf8mb3 换成 utf8mb4。这次"顺手的升级"有哪些破坏点？迁移一张线上表前要做哪些检查？

**答**：**结论**：utf8mb4 最大的破坏点不是"能存 emoji"这个收益，而是**代价侧的三件事**：① **索引长度上限**——utf8mb4 每字符最多 4 字节，`varchar(255)` 的索引键从 255×3=765 字节变 1020 字节，超过 InnoDB 767/3072 字节限制时建索引直接报错或被截断（取决于 `innodb_large_prefix`）；② **空间与内存翻倍风险**——CHAR 类型按最大宽度分配（CHAR(10) 从 30B 变 40B），行变宽加剧溢出页；③ **连接字符集不一致**——客户端连接仍声明 utf8mb3 时，写入 emoji 会被截断成 `?` 或报错，这是迁移后最高频的线上事故。

**取舍**：两条迁移路线：改表 `ALTER TABLE ... CONVERT TO CHARACTER SET utf8mb4`（锁表/复制延迟，需 online DDL 与大表策略）vs 新列双写灰度（安全但周期长）。排序规则要同步定：utf8mb4_general_ci 与 utf8mb4_unicode_ci 的比较规则不同，**只改 charset 不改 collation 会造成判重行为漂移**（唯一索引判重口径变化）。

**实战**：迁移前跑"破坏点扫描"：列出所有 `varchar/char` 索引并算字节数、统计含 4 字节字符的历史数据、核对应用连接串的 `characterEncoding`；迁移后在双写期做"字符集 diff 对账"（读新旧库比较，专看四字节字符行）。

```python
# 迁移前的破坏点扫描：字符数 -> 字节数换算与 4 字节字符检测
def bytes_len(s: str, charset: str) -> int:
    return len(s.encode(charset))

def scan_column(varchar_len: int, is_indexed: bool,
                mysql_row_limit: int = 767) -> dict:
    """模拟 utf8mb3 -> utf8mb4 后索引键宽变化。"""
    b3 = varchar_len * 3
    b4 = varchar_len * 4
    ok = (not is_indexed) or b4 <= mysql_row_limit
    return {
        "varchar": varchar_len,
        "key_bytes_mb3": b3,
        "key_bytes_mb4": b4,
        "indexed": is_indexed,
        "verdict": "OK" if ok else f"超限！{b4}>{mysql_row_limit}B，"
                   "需缩短前缀或开 innodb_large_prefix/DYNAMIC 行格式",
    }

print(scan_column(255, is_indexed=True))     # 765B -> 1020B：默认设置下超限
print(scan_column(191, is_indexed=True))     # 191*4=764B：mb4 时代的经典上限

# 历史数据扫描：找出存量里已含 4 字节字符（mb3 会存坏）的数据
sample_rows = ["张三", "naïve café", "ok✅", "中文emoji😀"]
def needs_mb4(s: str) -> bool:
    return any(ord(ch) > 0xFFFF for ch in s)   # 超出 BMP 才是 4 字节
bad = [s for s in sample_rows if needs_mb4(s)]
print("需要 utf8mb4 才能存的行:", bad)

# 连接字符集检查：客户端声明 mb3 时 emoji 的真实下场
raw = "评论😀"
client_bytes = raw.encode("utf-8")             # 客户端实际发出的字节
declared = "utf-8"                             # 声明为 utf8mb3 的连接
stored = client_bytes.decode("utf-8", errors="replace")
print("mb3 连接存入后读出:", stored)           # 😀 变成替换符/?
print("修复：连接串显式 characterEncoding=utf8mb4")
```

**追问 1**：为什么老项目常见 `varchar(191)` 这种奇怪长度？
提示：就是 utf8mb4 迁移的遗迹——255×4 超过 767B 限制时把索引列缩到 191×4=764B 以下；看到 191 应立刻联想到字符集变更历史。

**追问 2**：CHAR(10) 与 VARCHAR(10) 在字符集切换后哪个空间代价更大？
提示：CHAR 按最大宽度（10×4=40B）预留，VARCHAR 只存实际字节 + 长度前缀；全 CHAR 宽行表迁移后行宽直接涨 33%。

**追问 3**：迁移期"只改 charset 不改 collation"会出什么事故？
提示：新表按表默认 collation（utf8mb4_0900_ai_ci）建、老列还是 general_ci，同库两种比较规则：JOIN 时排序规则不一致会导致索引失效与判重漂移（Q1397/Q6611 同类问题在字符集维度的再现）。

## 背诵要点
1. utf8mb4 迁移三破坏点：索引键宽 ×4/3 超 767B 限制（varchar(255)→191）、CHAR 行宽放大、连接字符集不一致截断 emoji。
2. 排序规则与字符集必须一起定，混用 collation 会引起索引失效与判重漂移。
3. 迁移前扫描：索引字节数清单 + 4 字节字符存量检测 + 连接串核对。

## 复盘追问
1. 你的库里有 varchar(191) 这类"遗迹"列吗？当时是缩列、换行格式还是开 large_prefix 解决的？
2. 如果存量数据里已经有被 mb3 存坏的 `?`/替换符，修复策略是什么？如何防止继续写入坏数据？
