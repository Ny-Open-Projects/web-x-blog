# 画面线理解：11.MongoDB分片集群之架构

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\11.MongoDB分片集群之架构【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:16, 00:48, 01:21, 01:36, 01:53, 02:26, 02:58, 03:30, 03:31, 04:03, 04:35, 04:44, 04:45, 04:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:07:10

1) 这一组画面整体在讲 MongoDB 分片集群的架构组成与数据分布机制。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示“2.3、架构”章节，包含组件说明表和架构图。架构图显示：App Server → Router (mongos) → Config Servers (replica set) → Shard (replica set)。
画面 2: 与画面 1 相同，无新增要点。
画面 3: 与画面 1 相同，无新增要点。
画面 4: 架构图更新，新增了“2 or more Shards”部分，显示两个 Shard (replica set)。
画面 5: 与画面 4 相同，无新增要点。
画面 6: 与画面 4 相同，无新增要点。
画面 7: 用红色圆圈高亮了“Shard (replica set)”部分。
画面 8: 用红色圆圈高亮了“Config Servers (replica set)”部分。
画面 9: 展示“2.4、集群中数据分布”章节，架构图保持不变，下方文字说明“Mongos本身并不持久化数据...”。
画面 10: 用红色圆圈高亮了“Mongos...”文字部分。
画面 11: 用红色圆圈高亮了“Mongos...”文字部分。
画面 12: 架构图恢复为画面 4 的状态，无高亮。
画面 13: 架构图恢复为画面 4 的状态，无高亮。
画面 14: 用红色圆圈高亮了“App Server”部分。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
无。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
标题：2.3、架构
架构图结构：
- App Server → Router (mongos) → Config Servers (replica set) → Shard (replica set)
- 两个 Router (mongos) 通过双向箭头连接 Config Servers (replica set)。
- 两个 Shard (replica set) 通过双向箭头连接 Config Servers (replica set)。
表格数据：
| 组件 | 说明 |
| :--- | :--- |
| Config Server | 存储集群所有节点、分片数据路由信息。默认需要配置3个Config Server节点。 |
| Mongos | 提供对外应用访问，所有操作均通过mongos执行。一般有多个mongos节点，数据迁移和数据自动平衡。 |
| Mongod | 存储应用数据记录。一般有多个Mongod节点，达到数据分片目的。 |

5) 无。
