# 画面线理解：14.MongoDB分片集群之集群使用以及操作

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\14.MongoDB分片集群之集群使用以及操作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 00:54, 02:02, 03:05, 03:27, 04:04, 04:43, 05:04, 05:37, 06:13, 06:47, 07:20, 09:10, 10:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:09:13

1) 这一组画面整体在讲如何在 MongoDB 分片集群中创建数据库、集合、配置分片规则并插入测试数据。

2) 按时间顺序列出每张画面的要点：
画面1: 连接 MongoDB Shell，显示版本信息和安全警告。
画面2: 查看集群状态，显示数据库信息和分片配置。
画面3: 执行 sh.shardCollection 命令，为 test.order 集合设置分片规则。
画面4: 在主节点上执行 db.order.find()，查询数据并显示结果。
画面5: 显示 MongoDB 启动日志和监控服务提示。
画面6: 从主节点退出并重新连接到分片节点 rs_shardsvr2。
画面7: 在 rs_shardsvr2 节点上执行 db.order.find()，查询数据并显示结果。
画面8: 显示 Typora 中的文档，内容为分片集群的配置和操作步骤。
画面9: 在 config 数据库中执行 show tables，查看系统表。
画面10: 查询 databases 和 collections 的信息，确认分片状态。
画面11: 显示 Typora 中的文档，内容为分片集群的配置和操作步骤。
画面12: 显示 Typora 中的文档，内容为使用 Docker 启动配置节点的命令。
画面13: 显示 Typora 中的文档，内容为使用 Docker 启动分片节点的命令。
画面14: 显示 Typora 中的文档，内容为分片集群的配置和操作步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3:
```javascript
sh.shardCollection("test.order", {"_id": "hashed"})
```
画面4:
```javascript
db.order.find()
```
画面6:
```bash
mongo 172.16.55.185:37003
```
画面7:
```javascript
db.order.find()
```
画面8:
```javascript
#启用分片
sh.enableSharding("test")

#设置分片规则，按照_id的hash进行区分
sh.shardCollection("test.order", {"_id": "hashed"})

#插入测试数据
use test
for (i = 1; i <= 1000; i=i+1){
    db.order.insert({"id": i, 'price': 100+i})
}

#分别在2个shard集群中查询数据进行测试
db.order.count()
```
画面9:
```javascript
use config
show tables
```
画面10:
```javascript
db.databases.find()
db.collections.find()
```
画面12:
```bash
docker create --name mongo-configsvr1 -p 17001:27019 -v mongoconfigsvr-data-01:/data/configdb mongo:4.0.3 --configsvr --replset "rs_configsvr" --bind_ip_all
docker create --name mongo-configsvr2 -p 17002:27019 -v mongoconfigsvr-data-02:/data/configdb mongo:4.0.3 --configsvr --replset "rs_configsvr" --bind_ip_all
docker start configsrv01 configsrv02 configsrv03
```
画面13:
```bash
docker create --name mongos -p 6666:27017 --centritypoint mongo:4.0.3 --configsvr rs_configsvr --bind_ip_all
docker start mongos
docker exec -it mongos bash
mongo 172.16.55.185:6666
sh.addShard("rs_shardsvr1/172.16.55.185:37000,172.16.55.185:37001,172.16.55.185:37002")
sh.addShard("rs_shardsvr2/172.16.55.185:37003,172.16.55.185:37004,172.16.55.185:37005")
sh.enableSharding("test")
sh.shardCollection("test.order", {"_id": "hashed"})
use test
for (i = 1; i <= 1000; i=i+1){
    db.order.insert({"id": i, 'price': 100+i})
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8: PPT标题为“分片集群的配置和操作步骤”，内容包括启用分片、设置分片规则、插入测试数据、查询数据等。
画面12: PPT标题为“使用 Docker 启动配置节点”，内容包括创建配置节点的命令。
画面13: PPT标题为“使用 Docker 启动分片节点”，内容包括创建分片节点的命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
