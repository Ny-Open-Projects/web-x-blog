# MySQL 面试指南 · 输入分诊与剔除台账

> 项目：`mysql-interview`（机翻 MySQL 面试课 → 面试卡）
> 生成时间：2026-10-15
> 技能：`mt-to-interview-cards`（从零出卡流程，SPEC v3 + validate.py 门禁）

---

## 一、源素材清单（13 个原始 txt）

| 文件 | 字节 | 判定 | 动作 |
|---|---|---|---|
| 01-course-intro | 10.4K | **R4 元内容**（导学/卖课） | 剔除 |
| 02-version | 54.4K | 技术 | 保留（本次校准章） |
| 03-user-management | 32.9K | 技术 | 保留（待产） |
| 04-server-config | 55.4K | 技术 | 保留（待产） |
| 05-logs | 74.5K | 技术 | 保留（待产） |
| 06-storage-engine | 70.2K | 技术 | 保留（待产） |
| 07-architecture | 152.5K | 技术（最大章） | 保留（待产） |
| 08-backup-recovery | 66.9K | 技术 | 保留（待产） |
| 09-monitoring | 39.2K | 技术 | 保留（待产） |
| 10-exception-handling | 26.7K | 技术 | 保留（待产） |
| 11-course-summary | 13.2K | **R4 元内容**（课程总结） | 剔除 |
| 资料/ITJC8-*.txt ×2 | 108B | R4（广告碎片） | 剔除（未复制） |

**保留 9 章 / 剔除 2 章 + 2 碎片**。无 R1（纯软技能）/ R2（技术<20%）/ R3（刻板印象）命中——本课程是纯技术面试题课。

## 二、机翻解码对照表（MySQL 专属，跨批复用）

| 机翻（音译） | 还原 | 类型 |
|---|---|---|
| 买CQ / myc九 / 满星星5.5 | MySQL / MySQL 5.9 / MySQL 5.5 | 近音 |
| 马瑞亚DB / 马热DB / 瑞masDB | MariaDB | 近音 |
| 引诺DB / 影楼DB / 影诺DB | InnoDB | 近音 |
| 跑克note / 可curomysql / pkerono | Percona | 近音 |
| cpermodel / cmodell / cmodel | sql_mode | 近音 |
| 安度log / 暗度log | undo log | 近音 |
| 锐度log / 闪回 | redo log / flashback | 近音 |
| 马千头 / 马瑞尔 | MariaDB（分支名） | 近音 |
| 冈利亚 / 钢利亚集群 | Galera 集群 | 近音 |
| 收序索引 | 升序索引（ascending） | 反义错译 |
| 组成切换 / 组千线 | 主从切换 / 主库 | 近音 |
| 重来 / 存重 / 重库 | 从库（slave） | 近音 |
| 爱慕克 / 伪造顾group | 演示用资源组名 example / CREATE RESOURCE GROUP | 演示词 |
| 三w点IPGC八点com / IT教程吧 | 广告残留（必须剥离，不入卡） | 品牌残留 |

> 规则：机翻音译在出卡时**直接还原为标准术语**，不写进卡片；只在「原文纠错」节说明还原动作，不计为技术错误。广告尾句一律不进卡。

## 三、出卡节奏（体量分层，先量后跑）

| 章 | 字节 | 档 | 估计出卡 |
|---|---|---|---|
| 02 version | 54K | L | 15~18 |
| 03 user | 33K | M~L | 8~12 |
| 04 server-config | 55K | L | 15~18 |
| 05 logs | 74K | XL | 18~24 |
| 06 storage-engine | 70K | XL | 18~22 |
| 07 architecture | 152K | XL（最大） | 35~50 |
| 08 backup-recovery | 67K | XL | 18~22 |
| 09 monitoring | 39K | L | 12~15 |
| 10 exception | 27K | M | 8~10 |

**全课估计 150~190 张主卡**（含少量 .deep）。一个技术点一张卡，宁拆薄不凑厚。

## 四、下一步

- 02 章为校准章（已落卡 + validate 0 error），作为全课节奏样板。
- 03~10 章按节奏表续产；每批落盘后跑 `python3 _pipeline/validate.py --strict`。
- 全课后用 `gen-recite-list.py` 出背诵清单。
