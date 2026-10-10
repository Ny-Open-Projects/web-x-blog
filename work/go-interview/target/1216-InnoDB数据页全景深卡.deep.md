# 1216 InnoDB 数据页全景（深卡）

> 分类：MySQL 存储内核 | 难度：L3 | 题型：综合题 | 频率：中 | 关键词：**数据页**/**七部分**/**页目录**/**半写检测**/**LSN/MTR**
> 原文锚点：第 1~62 段「数据页七部分结构、行单链表、页目录分组与二分、file trailer 校验和/LSN/MTR 崩溃恢复」

## 思路与架构
把 InnoDB 磁盘 IO 最小单位"数据页"从物理到恢复串成一条线：

1. **物理骨架**（1216-page-structure）：默认 16KB，七部分——file header(38B, 含上下页指针) / page header(56B) / 最大最小记录(26B) / user records / free space / page directory / file trailer(8B)。行靠 `next_record` 串单链表；页分空闲/干净/脏。
2. **页内加速**（1216-page-directory）：页目录=槽稀疏索引；分组 min1/max1-8/其他4-8、n_owned 计数、槽满8拆4+5；查找先二分定位槽再遍历组链表。
3. **崩溃恢复**（1216-page-crash-recovery）：file trailer 前4B 校验和 vs file header 校验和检半写；后4B LSN 记 redo 量；MTR=一组 redo 原子重放单元。

## 方案取舍
| 关注点 | 设计 | 取舍 |
| --- | --- | --- |
| 最小 IO 单位 | 页 16KB（非行） | 减磁盘 IO，但行小则页内浪费 |
| 页内查找 | 链表 + 页目录二分 | 省空间(稀疏索引)换可接受查找 |
| 刷盘原子性 | file trailer 校验和 + doublewrite | 多一次写换半写安全 |

**取舍总纲**：InnoDB 在"IO 效率(页)/ 空间(稀疏页目录)/ 安全(doublewrite+校验和)"间取平衡；页是连接上层 B+树与下层磁盘的枢纽。

## 答题技巧
- 被问"InnoDB 数据怎么落盘"：从页切入——先讲页是最小 IO 单位、七部分结构，再讲页内靠页目录加速点查，最后讲刷盘靠 file trailer 校验和+LSN+MTR 保原子。
- 被问"页内怎么快速查"：归到 1216-page-directory 的二分+槽。
- 被问"宕机怎么恢复页"：归到 1216-page-crash-recovery 的校验和半写检测 + MTR 原子重放。
- 边界声明：本卡是**数据页层**的整合总纲。上层"表空间→段→区→B+树"归 `1211-index-storage`、行格式(COMPACT/DYNAMIC)归 `1215-row-format-overview`、可插拔引擎层归 `1210-storage-engine-layer`、Buffer Pool(脏页/空闲页管理)归 `125-bufferpool-internals`。本卡只覆盖"页"这一层（七部分/页目录/页级恢复），不重述已被专项卡覆盖的论证。

## 细节与核心 API

**数据页 16KB 七部分结构**：

```text
file header  38B  (含上下页指针 FIL_PAGE_PREV/NEXT)
page header  56B
最大/最小记录 26B
user records       (行单链表，next_record 串联)
free space
page directory     (槽稀疏索引)
file trailer  8B   (前4B 校验和 / 后4B LSN)
```

**页内查找**：页目录 = 槽稀疏索引；分组规则 min1 / max1-8 / 其他 4-8；`n_owned` 计数；查找先二分定位槽、再遍历组内链表。

**崩溃恢复**：`file trailer` 前 4B 校验和 vs `file header` 校验和 → 检测半写（页断裂）；后 4B LSN 记录已写 redo 量；MTR（Mini-Transaction）= 一组 redo 的原子重放单元。

```ini
# 校验和算法（配合 doublewrite 防半写）
innodb_checksum_algorithm = crc32   # 默认
```

> 边界：Buffer Pool 脏页/空闲页管理见 125/1300；doublewrite 见 1212；本卡只覆盖"页"这一层。
