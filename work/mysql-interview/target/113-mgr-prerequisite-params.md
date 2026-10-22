# 113 MGR 部署前置：插件与五个必配变量

> 分类：架构/复制 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**group_replication_group_name** / **local_address** / **group_seeds** / **XXHASH64** / **binlog_checksum=NONE**
> 原文锚点：第 777~840 段「安装组复制插件……把 binlog_checksum 配置成空才能起效，配置组复制组的名字、本地地址和种子节点」

## 一句话总述
MGR 是插件式架构：先 `INSTALL PLUGIN group_replication`，再配 **组名（UUID）、本地通信地址、种子节点、写集算法、binlog 校验关闭** 五件事，缺一件起不来。

## 面试官视角
- **考察意图**：是不是只看过 MGR 原理图，没真正拉起过集群——拉过的人一定被 `binlog_checksum` 和 33061 端口坑过。
- **P5** 知道要装插件、要有组名 / **P6** 能说清 `local_address`（本节点通信地址）与 `group_seeds`（种子节点列表）的区别 / **P7** 会补「通信端口必须**独立于 3306**，否则起不来」和「`single_primary_mode` 运行时不可改且集群内必须一致」。
- **红旗**：「种子端口用 3306」；「组名随便写个字符串」；「各节点参数可以不一样」。
- **惊艳点**：`group_replication_group_name` 必须是合法 **UUID**，随便写一串 a 起不来（原文为演示方便用了一串 a，实际必须 UUID 格式）—— 验证：用 `SELECT UUID();` 生成（8.0.36 `[经验]`）。

## 主问答
**Q：搭一个三节点 MGR，配置文件里必须写哪些东西？**
**A：**
1. **先给结论**：插件 + 组名 + `local_address` + `group_seeds` + 写集算法 `transaction_write_set_extraction=XXHASH64` + `binlog_checksum=NONE`。
2. **再给机制**：`local_address` 是**本节点**对外通信的地址（如 `192.168.1.91:33061`），`group_seeds` 是**加入集群时联系的种子列表**；写集算法用于冲突检测，`binlog_checksum=NONE` 是因为 8.0 默认 CRC32 与组复制的事件校验不兼容。
3. **最后给边界**：通信端口**不能复用 3306**（官方要求独立端口），且各节点的 `single_primary_mode`、`group_name` 必须一致——`single_primary_mode` 在集群运行时**不可修改**。
**加分层**：第一个节点用 `group_replication_bootstrap_group=ON` 引导，起完**必须设回 OFF**，否则重启会分裂出第二个组（脑裂）。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | MGR 是内置的吗 | 概念 | 插件 | 换题 |
| L2 | 组名能随便写吗 | 基础 | 必须 UUID | 判 P5 |
| L3 | local_address 与 seeds 区别 | 机制 | 本节点 vs 种子列表 | 判 P6 |
| L4 | 为什么关 binlog_checksum | 边界 | CRC32 与组复制校验不兼容 | 判 P6+ |
| L5 | bootstrap 用忘关会怎样 | 实战 | 重启分裂出第二个组 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| 5.7.17 引入；8.0 起成熟（验证 8.0.36） | **8.0.21 起 `binlog_checksum=NONE` 不再强制**（组复制支持带校验的事件）；`transaction_write_set_extraction` 在 8.0.26 起被标记过时 | 5.7 讲五件套；8.0.21+ 说明该约束已放宽 |

## 关键代码
```sql
-- 生成合法组名（不要手写一串 a）
SELECT UUID();
INSTALL PLUGIN group_replication SONAME 'group_replication.so';
SET GLOBAL group_replication_group_name = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'; -- 用真实 UUID 替换
SET GLOBAL group_replication_local_address = '192.168.1.91:33061';
SET GLOBAL group_replication_group_seeds  = '192.168.1.91:33061,192.168.1.92:33061';
SET GLOBAL group_replication_bootstrap_group = ON;   -- 仅第一个节点，起完设回 OFF
START GROUP_REPLICATION;
```

## ⚠️ 原文纠错
原文为演示方便把组名写成「一串 a」，**实际必须是合法 UUID**（`SELECT UUID()` 生成），否则插件拒绝启动；已在主问答与惊艳点双处纠正。原文「这个端口不能用 3306，这里使用 33061」表述正确，已保留并强化为硬约束。机翻「nauUID / transitionwatersetextension / vlogch / 组布阵 / 主复制」还原为 **group_replication_group_name** / **transaction_write_set_extraction** / **binlog_checksum** / **组复制**。

## 总结与追问预判
- 五件套 + 独立端口 + bootstrap 用完即关，是 MGR 起不来的三大原因。
- 下一题：见 114（节点加入与监控）、103（MGR 原理与单主多主）。
