# 画面线理解：07.MongoDB复制集之故障转移

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\07.MongoDB复制集之故障转移【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 00:45, 01:12, 01:29, 01:54, 02:59, 03:23, 03:58, 04:22, 05:21, 05:38, 06:18, 07:19, 07:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:05:19

1) 这一组画面整体在讲什么（一句话）：
演示 MongoDB 副本集故障转移过程，包括手动停止节点、观察状态变化、验证仲裁节点作用及数据一致性。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示终端初始状态，提示符为 root@0fe207830106:#
画面 2: 显示 MongoDB 副本集状态，其中 rs0:PRIMARY> 提示符，输出包含 "configVersion": 1, "self": true 等信息。
画面 3: 用户在终端执行命令：docker exec -it mongo01 /bin/bash，进入容器。
画面 4: 显示 MongoDB 副本集状态，其中 "stateStr": "(not reachable/healthy)"，并提示 "Connection refused"。
画面 5: 显示 Typora 编辑器中的 Markdown 文档，标题为“讲义.md”，内容为“1.6、故障转移”和“1.7、增加arbitrer节点”，其中包含 Docker 命令：
docker create --name mongo04 -p 27020:27017 -v mongo-data-04:/data/db mongo:4.0.3 --replSet "rs0" --bind_ip_all
docker start mongo04
在节点上执行
rs0:PRIMARY> rs.addarbitrator("172.16.55.185:27020")
画面 6: 显示 MongoDB 副本集状态，其中 "state": 2, "stateStr": "SECONDARY"。
画面 7: 用户在终端执行命令：docker stop mongo02 和 docker ps，查看容器状态。
画面 8: 显示 MongoDB 副本集状态，其中 "stateStr": "(not reachable/healthy)"，并提示 "Connection refused"。
画面 9: 显示 MongoDB 副本集状态，其中 "stateStr": "(not reachable/healthy)"，并提示 "Connection refused"。
画面 10: 用户在终端执行命令：db.user.insert({ _id: 1003, name: "wangwu" })，并查询数据。
画面 11: 用户在终端执行命令：docker stop mongo03 和 docker ps，查看容器状态。
画面 12: 显示 MongoDB 副本集状态，其中 "stateStr": "(not reachable/healthy)"，并提示 "Connection refused"。
画面 13: 显示 MongoDB 副本集状态，其中 "stateStr": "(not reachable/healthy)"，并提示 "Connection refused"。
画面 14: 显示 Typora 编辑器中的 Markdown 文档，内容与画面 5 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
docker create --name mongo04 -p 27020:27017 -v mongo-data-04:/data/db mongo:4.0.3 --replSet "rs0" --bind_ip_all
docker start mongo04
在节点上执行
rs0:PRIMARY> rs.addarbitrator("172.16.55.185:27020")

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5: PPT 标题为“讲义.md”，内容为“1.6、故障转移”和“1.7、增加arbitrer节点”，其中包含 Docker 命令和操作步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
