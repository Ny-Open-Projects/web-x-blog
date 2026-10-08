# 1216 InnoDB 数据页的物理结构（七部分）

> 分类：MySQL 存储内核 | 难度：L3 | 题型：深挖题 | 频率：中 | 关键词：**数据页 16KB**/**七部分结构**/**file header 38B**/**page header 56B**/**file trailer 8B**/**行单链表**
> 原文锚点：第 1~16 段「数据以行存、以页(16KB)读；页分空闲/干净/脏；数据页七部分结构；行 next_record 串单链表」

## 一句话总述
InnoDB 中数据**按行存、按页读**（默认页 16KB）；磁盘上的**数据页**由**七部分**物理拼接：file header(38B) / page header(56B) / 最大最小记录(26B) / user records(真实数据) / free space(未用空间) / page directory(页目录) / file trailer(8B 校验+LSN)。页内行记录通过 `next_record` 偏移按主键从小到大串成**单链表**；插入时从 free space 划空间给 user records，free space 用完就申请新页 `[经验]`。

## 面试官视角
- 考察意图：是否理解"InnoDB 最小的 IO 单位是页、页内是链表"，而非只背 B+树。
- 分档：P5 知页 16KB、行存页读；P6 能背出七部分及各自大小；P7 能讲清 file header 双指针(上一页/下一页) + 行单链表 + 空闲/干净/脏页状态。
- 红旗：把"页"说成"行的数组"；或不知 file header/page header 的固定字节数。
- 惊艳点：点出"file header 有指向上一页/下一页的指针 → 页之间也是双向链表"，以及"脏页=已在内存改但未刷盘"，把页结构连到 Buffer Pool。

## 主问答
**Q（面试官原话）：** InnoDB 一个数据页里到底存了什么？
**A：**
1. **七部分结构**（固定+可变）：
   - file header **38B**：页通用信息，含**指向上一页/下一页的两个指针**（页间双向链表）。
   - page header **56B**：本页通用信息。
   - 最大记录 + 最小记录 **26B**：当前页内边界记录。
   - user records：真实插入的行，大小不定（含 varchar/text 可变类型）。
   - free space：尚未使用的空间，插入时从这里划给 user records。
   - page directory：页目录（槽），见 1216-page-directory。
   - file trailer **8B**：校验和(前4B) + LSN(后4B)，见 1216-page-crash-recovery `[经验]`。
2. **行组织**：用户记录通过 `next_record` 偏移、按主键由小到大串成**单链表**；插一条就从 free space 划一块到 user records，free space 用完需新页。
3. **页状态**：数据页在 Buffer Pool 中分**空闲页 / 干净页 / 脏页**（脏页=内存改过未刷盘）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 页多大？ | 基础 | 16KB，行存页读 | P5 |
| L2 | 七部分？ | 结构 | 七段+各自字节 | P6 |
| L3 | 行间怎么连？ | 机制 | next_record 单链表 | P6+ |
| L4 | file header 指针？ | 深度 | 上下页双向链 | P7 |
| L5 | 脏页是什么？ | 进阶 | 内存改未刷盘 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| InnoDB（MySQL 5.7/8.0） | 页大小可配(4K~64K)，默认 16KB 长期不变 | 答"默认 16KB、七部分固定+可变、行单链表、file header 双指针、脏页概念" |

## 关键代码
```sql
-- 查看当前实例页大小（默认 16384 = 16KB）
SHOW VARIABLES LIKE 'innodb_page_size';
-- 查看 Buffer Pool 中各类页状态计数（空闲/脏等）
SHOW STATUS LIKE 'Innodb_buffer_pool_pages_%';
```

## 总结与追问预判
数据页是 InnoDB 磁盘 IO 的最小单位，七部分 + 行单链表是其物理骨架。页内快速查找靠页目录（1216-page-directory），页级崩溃恢复靠 file trailer（1216-page-crash-recovery）。上层串联见 1211-index-storage（表空间/段/区/B+树）、1215-row-format（行格式）。

## ⚠️ 原文纠错
1. 事实核校：页默认 16KB、七部分结构及字节数(file header 38B/page header 56B/最大最小记录 26B/file trailer 8B)、行 next_record 单链表、空闲/干净/脏页、file header 双指针——均与 InnoDB 实现一致 `[经验]`。
2. 崩坏词归一：源码将 MySQL 音译为买sql/我买、InnoDB 音译为英格DB/因格DB、page 音译为液/张页、file header 音译为 fileheader/非黑、file trailer 音译为 fileteller、record 音译为记录/液、next_record 音译为 nextreport/lessrecord；源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
