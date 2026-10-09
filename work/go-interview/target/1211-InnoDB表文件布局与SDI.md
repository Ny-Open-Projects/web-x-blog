# 1211 InnoDB 表文件布局与 SDI

> 分类：MySQL 存储 | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**.ibd 文件**/**.frm 废弃**/**SDI**/**ibd2sdi**/**数据路径**
> 原文锚点：第 39~53 段「InnoDB 表文件与 ibd2sdi 导出」

## 一句话总述
MySQL 8.0 下一个 InnoDB 表通常只有一个 `.ibd` 文件；8.0 之前还有 `.frm`（表结构）和 `.opt`（库字符集），8.0 起这两者取消，表结构信息统一写入 `.ibd` 内的 **SDI（Serialized Dictionary Information）**；可用 `ibd2sdi` 命令从 `.ibd` 导出 json 表结构。

## 面试官视角
- 考察意图：是否跟进了 MySQL 8.0 的表文件布局变化（.frm 取消、SDI 入 .ibd），这是常考的版本差异点。
- 分档：P5 知 InnoDB 表有 .ibd；P6 知 8.0 取消 .frm/.opt；P7 知 SDI 概念与 ibd2sdi 导出。
- 红旗答案：以为 8.0 仍有 .frm；或不知道表结构存在哪。
- 惊艳点：点出「ibd2sdi 把表结构导成 json（columns/索引/存储引擎/物理路径），可用于无 frm 恢复表结构」。

## 主问答
**Q（面试官原话）：** MySQL 8.0 一个 InnoDB 表在磁盘上是什么文件？
**A：**
1. **单文件**：MySQL 8.0 下，自建 InnoDB 表只有一个 `.ibd` 表文件（数据+索引+结构都在内）。
2. **8.0 之前**：还有 `.frm` 存表结构、`.opt` 存库字符集与校验规则；MyISAM 表则有 `.MYD/.MYI`。
3. **8.0 变化**：取消 `.frm` 与 `.opt`，表结构信息全部写入 `.ibd` 内的 **SDI**（Serialized Dictionary Information）。
4. **数据路径**：MySQL 8.0 数据目录默认在 `/var/lib/mysql`，每库独立目录，每表独立 `.ibd`。
5. **ibd2sdi**：`ibd2sdi --dump-file=user.sdi user.ibd` 从 .ibd 提取表结构 json，内含 columns（字段类型/nullable/自增/有符号等）、索引、存储引擎、物理路径。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 8.0 InnoDB 表几个文件？ | 基础 | 单 .ibd | P5 |
| L2 | .frm 还在吗？ | 版本 | 8.0 取消 | P6 |
| L3 | 表结构存哪？ | 细节 | .ibd 内 SDI | P6 |
| L4 | 怎么导出表结构？ | 工具 | ibd2sdi | P7 |
| L5 | SDI 是什么？ | 进阶 | 序列化字典信息 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 8.0 | 取消 .frm/.opt，SDI 入 .ibd；5.7 及之前仍有 .frm | 面试按 8.0 现状答，并提 5.7 差异显专业 |

## 关键代码
```bash
# 从 .ibd 提取表结构（SDI → json）
ibd2sdi --dump-file=user.sdi /var/lib/mysql/test/user.ibd
cat user.sdi   # 内含 columns / indexes / engine / 物理路径
```

## 总结与追问预判
表文件布局是「8.0 单 .ibd + SDI」的范式。更深一层是表空间与数据字典——下一张讲。

## ⚠️ 原文纠错
1. 事实核校： [经验] 8.0 单 .ibd、取消 .frm/.opt、SDI 入 .ibd、ibd2sdi 导出 json(含 columns/索引/引擎/路径)、数据路径 /var/lib/mysql——均正确。
2. 崩坏词归一：源码将 MySQL 音译为崩坏词（本卡统一为 MySQL）、InnoDB 音译为 inlDB/inoDB/innODB、MyISAM 音译为 mmysam/mysam、.ibd 音译为 点IBD、ibd2sdi 音译为 IBDQSDI、.sdi 音译为 点PST/点TTST、.frm 音译为 点FRM、.opt 音译为 点OPT/点OPCE、var/lib/mysql 音译为 wordlab；据官方事实补正「8.0 起 .frm/.opt 取消、SDI 入 .ibd」。
