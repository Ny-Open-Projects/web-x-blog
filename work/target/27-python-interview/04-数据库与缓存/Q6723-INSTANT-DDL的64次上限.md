---
title: "[Q6723] INSTANT DDL 的 64 次上限：第 65 次为什么突然锁表"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6723 · INSTANT DDL 的 64 次上限：第 65 次为什么突然锁表

难度：P7 ｜ 标签：MySQL 8.0、INSTANT DDL、row_version、元数据

基线：Python 3.12；MySQL 8.0.29+ `ALGORITHM=INSTANT`（8.0.12 起支持末尾加列）；纯 Python 模拟行版本位图。

**问**：团队把加列都改成了 `ALTER TABLE ... ADD COLUMN ..., ALGORITHM=INSTANT`，前几十次都是毫秒级。某天同一个表的加列突然变成 `ALGORITHM=COPY`、锁表十几分钟。为什么 INSTANT 会"用着用着就失效"？64 这个数字从哪来？

**答**：
- **结论**：INSTANT 加列不重写数据，而是在**数据字典里记录"这个列从哪个 row_version 开始存在"**，旧行读出来时按版本补默认值。InnoDB 给每行留的 `row_version` 只有 **1 字节、有效值 1-64**，因此一张表最多累计 **64 次** INSTANT 变更；第 65 次无法再分配版本号，只能退化成 COPY（8.0.29 之前是 INPLACE）重建表，期间大量占用 IO 并可能阻塞写入。
- **取舍**：INSTANT 的收益是秒级、几乎不占空间；代价是**版本预算有限**且行格式变复杂（每次读旧行要做版本回溯）。8.0.29 之前只支持在**最后一列之后**加列，且不支持删除列；DROP COLUMN 的 INSTANT 也消耗版本号。把 INSTANT 当"无限免费"用，迟早撞上限；而一旦退化，重建成本比一开始就规划好 schema 更高。
- **实战**：① 用 `information_schema.innodb_tables.total_row_versions` 监控每张表的已用版本数，接近 48 就预警；② 加列前先 `EXPLAIN ALTER` 或看 `ALGORITHM` 是否被接受，CI 里断言关键大表 DDL 必须是 INSTANT；③ 需要频繁加列的场景（如稀疏属性）改用 JSON 列或纵表，别消耗版本预算；④ 重建安排在低峰，用 gh-ost/pt-osc 或主从切换，不要直接在主库跑 COPY。

```python
"""模拟 InnoDB row_version：1 字节、有效 1..64，用尽后退化重建。"""
MAX_ROW_VERSION = 64


class InstantTable:
    def __init__(self, name: str) -> None:
        self.name = name
        self.row_version = 1          # 建表时占用 1
        self.columns: list[tuple[str, int]] = [("id", 1)]
        self.rebuilds = 0

    def add_column(self, col: str) -> str:
        if self.row_version >= MAX_ROW_VERSION:
            # 没有可用版本号：必须重建，重建后版本号复位
            self.rebuilds += 1
            self.row_version = 1
            self.columns.append((col, self.row_version))
            return "COPY(rebuild)"
        self.row_version += 1
        self.columns.append((col, self.row_version))
        return "INSTANT"

    def read_row(self, row_version: int) -> dict[str, object]:
        """旧行只物化 '出生版本 <= 该行版本' 的列，其余补默认值。"""
        return {c: ("<default>" if born > row_version else f"{c}_v")
                for c, born in self.columns}


if __name__ == "__main__":
    t = InstantTable("orders")
    for i in range(1, 67):
        algo = t.add_column(f"c{i}")
        if algo != "INSTANT" or i in (63, 64, 65, 66):
            print(f"第 {i:>2} 次加列 -> {algo:<14} row_version={t.row_version}")
    print("累计重建次数:", t.rebuilds)
    print("旧行读到的新列为默认值:", t.read_row(2)["c60"])
```

**追问一**：INSTANT 加列后，`SELECT *` 读旧行为什么不会变慢很多？
→ 解析：旧行的列值不存在，InnoDB 按数据字典里的 `born_version` 判断该列是否可见，不可见就返回默认值，不需要回表找额外数据。代价是每行要做版本比较、列数多时元数据回溯变长；如果默认值不是常量（8.0 只允许常量默认），就无法 INSTANT。

**追问二**：既然 64 次是硬上限，为什么 MySQL 不直接把版本号做成 2 字节？
→ 解析：`row_version` 存在每行记录头里，改宽度会改变行格式、影响所有页的解析与兼容性，代价极高。1 字节 + 64 个有效值是历史兼容与成本的折中。社区的做法是把"频繁变更的属性"外置到 JSON 或子表，而不是扩版本号。
