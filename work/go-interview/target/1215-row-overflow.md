# 1215 行溢出与 DYNAMIC / COMPRESSED

> 分类：MySQL 存储 | 难度：中高 | 题型：原理 | 频率：中 | 关键词：**行溢出、溢出页、DYNAMIC、COMPRESSED、768 前缀、20 字节指针**

> 原文锚点：第 85~97 段「页 16KB、VARCHAR 上限、行溢出、768 前缀 vs 全溢出、zlib 压缩」

## 一句话总述
InnoDB 页默认 16KB（16384 字节），而 VARCHAR 最多 65532 字节、TEXT/BLOB 更大，单行可能放不下一页即「行溢出」。InnoDB 规定**一页至少存两条记录**，放不下就把数据移到「溢出页」。REDUNDANT/COMPACT 溢出时在页内保留**前 768 字节前缀 + 20 字节溢出页地址**；DYNAMIC/COMPRESSED 则把**全部内容放溢出页**，页内只留 20 字节地址；COMPRESSED 额外用 zlib 压缩行数据。

## 面试官视角
行溢出是 DYNAMIC 相对 COMPACT 的核心改进点，面试常考。考官看你能说出「768 前缀 vs 全溢出」这个具体差异，以及 COMPRESSED 多一层 zlib 压缩。能补「一页至少两条记录」的约束与「多个溢出页组成链表」更佳。

## 主问答
**Q（面试官原话）：** 什么是行溢出？DYNAMIC 和 COMPACT 处理有什么不同？

1. **触发条件**：页 16KB，而 VARCHAR/TEXT/BLOB 可能远超；InnoDB 要求一页至少容纳 2 条记录，放不下即行溢出，多余数据存溢出页。
2. **COMPACT / REDUNDANT 做法**：数据页保留**前 768 字节**的前缀数据，后接 **20 字节**指向溢出页的偏移量。
3. **DYNAMIC / COMPRESSED 做法**：变长字段**全部内容**放溢出页，当前数据页只保存 **20 字节的溢出页地址**；一个溢出页放不下则由多个溢出页组成页面链表。
4. **COMPRESSED 额外**：在 DYNAMIC 基础上用 zlib 算法压缩行数据，对 BLOB/TEXT 等大字段尤其省空间；5.7 起默认 DYNAMIC。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 何谓行溢出？ | 说不清页放不下 |
| L2 | COMPACT 留多少？ | 说不清 768 前缀 |
| L3 | DYNAMIC 呢？ | 说不清全溢出 |
| L4 | 地址多长？ | 说不清 20 字节 |
| L5 | COMPRESSED 特点？ | 说不清 zlib |

## 版本与兼容性
| 行格式 | 溢出处理 |
|--------|----------|
| REDUNDANT/COMPACT | 保留 768B 前缀 + 20B 指针 |
| DYNAMIC | 全放溢出页，仅留 20B 地址 |
| COMPRESSED | 同 DYNAMIC + zlib 压缩 |

## 关键代码
```text
页 16KB(16384B) < VARCHAR 65532B → 行溢出
DYNAMIC：本页只存 20B 溢出页地址，数据全在溢出页
```

## 总结与追问预判
核心：**行溢出 = 页(16KB)放不下大字段；COMPACT 留 768B 前缀，DYNAMIC 全溢出只留 20B 地址，COMPRESSED 再加 zlib 压缩**。追问可回「行格式总览」（见 1215-row-format-overview）。

## ⚠️ 原文纠错
1. 事实核校： [经验] 页默认 16KB、VARCHAR 上限 65532B、一页至少两条记录、行溢出触发、COMPACT 留 768B 前缀+20B 指针、DYNAMIC 全溢出仅留 20B 地址、多溢出页成链、COMPRESSED 加 zlib——均正确，本卡为准。
2. 崩坏词归一：源码将 InnoDB/MySQL/行格式/溢出页 等音译为多组崩坏词；本卡统一为规范术语。
