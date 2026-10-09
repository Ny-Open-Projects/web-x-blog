# 1214 file-per-table 独立表空间

> 分类：MySQL 存储 | 难度：L3 | 题型：机制题 | 频率：中 | 关键词：**file-per-table**/**独立表空间**/**.ibd**/**空间回收**/**innodb_file_per_table**
> 原文锚点：第 1~38 段「独立表空间（file-per-table）优缺点」

## 一句话总述
file-per-table（独立表空间）是 InnoDB 默认开启的表空间类型（`innodb_file_per_table=ON`），每张表数据存进自己的 `.ibd` 文件；**删表/删数据后磁盘空间可回收给 OS**，单表大小上限 64TB，但 fsync 按文件分散、文件描述符占用更高。

## 面试官视角
- 考察意图：是否理解独立表空间与共享表空间的利弊权衡，以及默认行为与版本差异。
- 分档：P5 知每表 .ibd；P6 知默认 ON、删数据可回收；P7 知 fsync 分散、文件描述符、64TB 单表上限等细节。
- 红旗答案：以为删表都立刻回收空间（共享表空间不会）；或不知道默认开启。
- 惊艳点：点出「共享表空间 64TB 是万表共享上限、分摊到单表很小；file-per-table 每表各 64TB」。

## 主问答
**Q（面试官原话）：** 什么是 file-per-table 表空间？它有什么优缺点？
**A：**
1. **定义与默认**：file-per-table 即独立表空间，`innodb_file_per_table` 默认 ON，每张 InnoDB 表的数据+索引存进自己的 `.ibd` 文件，支持所有行格式。
2. **优点-空间回收**：表数据删除后磁盘空间归还 OS（共享表空间删除只复用不回收）；可通过文件大小直接监控单表占用；支持把表放到独立存储设备做 IO 优化；支持跨实例导入、企业版在线备份。
3. **优点-性能**：当 `innodb_flush_method=O_DIRECT` 时，文件系统不允许对共享表空间单文件并发写，file-per-table 单文件并发写性能更高。
4. **缺点**：删除页只能同表内复用，跨表空间复用率低易浪费；fsync 按每个 .ibd 执行、无法合并多表写入，总 fsync 次数更高；大量表会打开大量文件描述符；删大表需扫描缓冲池可能阻塞几秒；`innodb_autoextend_increment` 对其无效（自动扩展但不可自定义增量，初始小、后续 4MB 递增）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | file-per-table 是什么？ | 基础 | 每表 .ibd | P5 |
| L2 | 默认开吗？ | 配置 | innodb_file_per_table=ON | P6 |
| L3 | 最大优点？ | 区别 | 删数据回收空间 | P6 |
| L4 | 主要缺点？ | 深度 | fsync 分散/打开 fd 多 | P7 |
| L5 | 单表大小上限？ | 进阶 | 每表 64TB | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| MySQL 5.6+ | innodb_file_per_table 默认 ON | 默认独立 .ibd；共享表空间仍存数据字典/undo 等 |

## 关键代码
```sql
SHOW VARIABLES LIKE 'innodb_file_per_table';  -- ON = 每表独立 .ibd
-- 删除大表后空间归还 OS（独立表空间）
DROP TABLE big_table;
-- 查看单表文件大小（独立表空间可直接反映占用）
ls -lh /var/lib/mysql/test/user.ibd
```

## 总结与追问预判
file-per-table 是默认且最常用，但 fsync 分散与 fd 占用是代价。共享/通用表空间在另一些场景更优——下一张对比。

## ⚠️ 原文纠错
1. 事实核校： [经验] file-per-table 默认 ON、删数据回收空间、单表 64TB 上限、fsync 按文件执行、autoextend 无效、O_DIRECT 下性能更优——均正确。
2. 崩坏词归一：源码将若干 InnoDB 专有名词（file-per-table/IBdata/InnoDB 等）音译为崩坏词，本卡统一为规范术语。
