---
title: [Q6692] utf8 与 utf8mb4：emoji 写入被截断事故复盘
date: 2026-11-21
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6692 · utf8 与 utf8mb4：emoji 写入被截断事故复盘

难度：P6 ｜ 标签：事故复盘、字符集、utf8mb4、数据截断

基线：MySQL 5.7/8.0（5.7 默认 latin1/utf8，8.0 默认 utf8mb4）；PyMySQL / SQLAlchemy 2.0。

**问**：用户昵称里带 emoji，写入后变成 `?` 或被截断，甚至触发 `Incorrect string value` 报错。为什么 MySQL 的 "utf8" 存不了 emoji？上线前的校验为什么没拦住？这类问题怎么一次性根治？

**答**：
- **结论**：MySQL 的 `utf8` 是历史遗留的**残缺实现**，最长只支持 3 字节，而 emoji 是 4 字节 UTF-8 序列。要存 emoji/生僻字/部分 CJK 扩展必须用 `utf8mb4`。截断 vs 报错误决于 `sql_mode`：严格模式（8.0 默认）报错，宽松模式静默截断成 `?`——后者更危险，因为坏数据已经入库。
- **取舍**：改列字符集（`CONVERT TO CHARACTER SET utf8mb4`）会锁表重建大表，线上要用 pt-online-schema-change / gh-ost 或 8.0 的 INSTANT 能力；只改表默认字符集不改已有列是常见踩坑点——已有的 VARCHAR 列仍然带着旧字符集。
- **实战**：根治要四层同改——(1) 库/表/列字符集统一 utf8mb4 + `utf8mb4_0900_ai_ci`（8.0）或 `utf8mb4_unicode_ci`（5.7，注意 8.0 的 0900 collation 与 5.7 排序结果有差异，主从混跑会不一致）；(2) 连接层 `charset='utf8mb4'`，SQLAlchemy 体现在 connect_args；(3) 应用入口做长度校验用"字符数"而非"字节数"要和列宽语义对齐（MySQL VARCHAR(N) 是字符数，但 utf8mb4 下索引长度限制 767/3072 字节要重新算）；(4) 测试集加入 emoji/四字节样例。

```python
# 用 Python 演示 utf8(3字节上限) 与 utf8mb4(4字节) 的差异与检测逻辑。
def mysql_utf8_len(s: str) -> int:
    """模拟 MySQL 'utf8'(3字节) 列对字符串的存储视角。
    4 字节字符在宽松模式被替换为 ? (1字节)，严格模式直接报错。"""
    total = 0
    bad = []
    for ch in s:
        b = len(ch.encode("utf-8"))
        if b > 3:
            bad.append(ch)
            total += 1          # 宽松模式：替换为 '?'，1 字节
        else:
            total += b
    return total, bad

def check_column(s: str, col_chars: int, strict: bool, mb4: bool = False):
    """模拟写入前校验：col_chars 为 VARCHAR(N) 的 N（字符数）。
    utf8mb4 下所有合法 UTF-8 都能存；utf8(3字节) 下 4 字节字符是风险。"""
    if mb4:
        if len(s) > col_chars:
            return "REJECT", "超列宽（字符数）"
        return "OK", None
    _, bad = mysql_utf8_len(s)
    if bad:
        if strict:
            return "REJECT", f"Incorrect string value: {bad!r}"
        return "SILENT_TRUNCATE", f"{len(bad)} 个字符将变成 '?'"
    if len(s) > col_chars:
        return "REJECT", "超列宽"
    return "OK", None

if __name__ == "__main__":
    nick = "张三😀A"
    print("utf8 视角字节数:", mysql_utf8_len(nick))       # (7, ['😀'])
    print("严格模式 utf8 列:", check_column(nick, 10, strict=True))
    # -> ('REJECT', "Incorrect string value: ['😀']")
    print("宽松模式 utf8 列:", check_column(nick, 10, strict=False))
    # -> ('SILENT_TRUNCATE', '1 个字符将变成 ?')
    print("utf8mb4 列:", check_column(nick, 10, strict=True, mb4=True))
    # -> ('OK', None)
```

**追问**：
- 一层：为什么连接字符集对了还会出问题？→ 提示：链路每一跳都可能转码（客户端/连接/库/表/列），`SHOW VARIABLES LIKE 'character%'` 逐层对齐。
- 二层：utf8mb4 换 collation 对索引和唯一约束有什么影响？→ 提示：0900_ai_ci 不区分重音声调，唯一约束判定变宽；改 collation 等价于重建索引，注意唯一键冲突提前预检。

**背诵要点**：
1. MySQL 的 utf8 是 3 字节残缺实现，emoji 必须用 utf8mb4；宽松 sql_mode 下会静默截断成 `?` 入库。
2. 根治四层：库表列字符集、连接 charset、列宽与索引字节限制重算、测试样例加四字节字符。
3. 大表改字符集用 gh-ost/pt-osc；5.7 与 8.0 默认 collation 不同（unicode_ci vs 0900_ai_ci），混跑影响排序与唯一约束。

**复盘追问**：
1. 为什么测试环境没暴露？提示：检查测试数据是否全是 ASCII/常用汉字，缺四字节样例。
2. 如果已经有一批 `?` 坏数据入库，还能恢复吗？提示：信息已丢失，只能从源头（埋点日志/上游消息）对账回补。
