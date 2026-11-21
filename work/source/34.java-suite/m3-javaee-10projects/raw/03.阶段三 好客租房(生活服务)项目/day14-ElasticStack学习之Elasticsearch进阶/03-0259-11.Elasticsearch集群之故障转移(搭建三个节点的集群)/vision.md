# 画面线理解：11.Elasticsearch集群之故障转移（搭建三个节点的集群）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day14-ElasticStack学习之Elasticsearch进阶
- 源文件：03.阶段三 好客租房(生活服务)项目\day14-ElasticStack学习之Elasticsearch进阶\11.Elasticsearch集群之故障转移（搭建三个节点的集群）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 01:15, 01:29, 01:41, 02:00, 02:13, 02:34, 03:04, 03:31, 03:50, 04:23, 05:17, 05:43, 06:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:49:40

1) 这一组画面整体在讲什么（一句话）：
演示如何通过添加新节点并配置 node.master 为 true 来测试 Elasticsearch 集群的故障转移功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中“2.4. 故障转移”章节，说明测试故障转移需要向集群添加节点并将所有节点的 node.master 设置为 true。
画面 2: 在终端中执行命令 `docker stop es-node01 es-node02` 停止两个节点服务。
画面 3: 在终端中执行 `cd` 命令切换目录，准备进行后续操作。
画面 4: 在终端中执行 `cd node03/` 进入 node03 目录。
画面 5: 在终端中执行 `cp node01 node02/` 命令复制 node01 的配置文件到 node02 目录。
画面 6: 在终端中执行 `cd data/` 进入 data 目录。
画面 7: 在终端中执行 `rm -rf nodes/` 删除 nodes 目录。
画面 8: 在终端中执行 `cd node03/` 进入 node03 目录。
画面 9: 在终端中执行 `vim elasticserach.yml` 打开配置文件进行编辑。
画面 10: 在终端中执行 `vim elasticserach.yml` 打开配置文件进行编辑。
画面 11: 在终端中执行 `vim elasticserach.yml` 打开配置文件进行编辑。
画面 12: 展示 PDF 文档中“2.4. 故障转移”章节，说明测试故障转移需要向集群添加节点并将所有节点的 node.master 设置为 true。
画面 13: 在浏览器中打开 Elasticsearch Head 插件，准备进行索引操作。
画面 14: 在浏览器中打开 Elasticsearch Head 插件，显示集群中各节点的分片分布情况。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
docker stop es-node01 es-node02
```
画面 3:
```
cd
```
画面 4:
```
cd node03/
```
画面 5:
```
cp node01 node02/
```
画面 6:
```
cd data/
```
画面 7:
```
rm -rf nodes/
```
画面 8:
```
cd node03/
```
画面 9:
```
vim elasticserach.yml
```
画面 10:
```
vim elasticserach.yml
```
画面 11:
```
vim elasticserach.yml
```
画面 12:
无直接代码，但有文字说明：
```
为了测试故障转移，需要再向集群中添加一个节点，并且将所有节点的node.master设置为true。
```
画面 13:
无直接代码，但有文字说明：
```
"acknowledged":true,"shards_acknowledged":true,"index":"haoke"
```
画面 14:
无直接代码，但有文字说明：
```
haoke
size: 5908 (1.57K)
docs: 0 (0)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 12:
标题：“2.4. 故障转移”
内容：
- 我们需要知道分片是一个 Lucene 实例，并且它本身就是一个完整的搜索引擎。应用程序不会和它直接通信。
- 分片可以是主分片 (primary shard) 或者是复制分片 (replica shard)。
- 索引中的每个文档属于一个单独的主分片，所以主分片的数量决定了索引最多能存储多少数据。
- 复制分片只是主分片的一个副本，它可以防止硬件故障导致的数据丢失，同时可以提供读请求，比如搜索或者从别的 shard 取回文档。
- 当索引创建完成的时候，主分片的数量就固定了，但是复制分片的数量可以随时调整。
- 为了测试故障转移，需要再向集群中添加一个节点，并且将所有节点的 node.master 设置为 true。

画面 14:
标题：“Elasticsearch”
内容：
- 显示了集群中各节点的分片分布情况：
  - node01: 分片 0, 1, 4, 5
  - node02: 分片 0, 2, 3, 5
  - node03: 分片 1, 2, 3, 4

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）
