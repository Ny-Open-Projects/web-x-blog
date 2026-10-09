# 1215 InnoDB 行格式（深挖）

> 分类：MySQL 存储 | 难度：中高 | 题型：原理深挖 | 频率：中 | 关键词：**行格式、COMPACT、记录头、行溢出、隐藏列、软删除**

> 原文锚点：第 1~101 段「页面层级、四种行格式、COMPACT 结构、记录头、REDUNDANT、行溢出」

## 思路与架构
行格式理解分四层：
- 存储层级：表空间 → 段(segment) → 区(extent) → 页(page, 16KB) → 行(row)。
- 行内布局（COMPACT）：变长字段长度列表（逆序）→ NULL 值列表（逆序）→ 记录头(5B/40bit) → 真实数据 + 隐藏列(DB_TRX_ID 6B / DB_ROLL_PTR 7B / 无主键时 DB_ROW_ID 6B)。
- 记录间组织：next_record 把页内记录串成**按主键升序**的单链表；删除走 delete_mask 软删除，进垃圾链表、空间可重用。
- 大字段处理：行溢出时 COMPACT 留 768B 前缀、DYNAMIC 全溢出仅留 20B 地址、COMPRESSED 再加 zlib 压缩。

## 方案取舍
- 选 COMPACT 而非 REDUNDANT：前者只存变长非 NULL 列长度 + 独立 NULL 位图，比「所有列偏移量 + NULL 比特位」省空间，页内可放更多行。
- 选 DYNAMIC 而非 COMPACT：大字段场景避免页内残留 768B 前缀，把整页空间留给更多行记录，5.7 起成为默认。
- 选 COMPRESSED 的代价：zlib 压缩省磁盘但增加 CPU 开销，适合归档/冷数据，不适合高频写入热表。
- 逆序存储的巧思：变长长度列表与 NULL 列表逆序，配合 next_record 位于「记录头与真实数据之间」，使向左读元数据、向右读真实数据都能高效定位。

## 答题技巧
1. 开口给层级：段/区/页/行，页默认 16KB，行是最终单位。
2. 报四种格式与版本默认：<5.1 REDUNDANT、5.1+ COMPACT、**5.7/8.0 DYNAMIC**。
3. 拆解 COMPACT 四段 + 逆序 + 记录头 5 字节 40 位（重点 delete_mask 软删除、next_record 按主键升序）。
4. 对比 REDUNDANT：偏移列表 + NULL 比特位，冗余被淘汰。
5. 收尾行溢出：768B 前缀 vs 全溢出 20B 地址，COMPRESSED 加 zlib；实战话术「大字段多用 DYNAMIC，冷数据才考虑 COMPRESSED」。
