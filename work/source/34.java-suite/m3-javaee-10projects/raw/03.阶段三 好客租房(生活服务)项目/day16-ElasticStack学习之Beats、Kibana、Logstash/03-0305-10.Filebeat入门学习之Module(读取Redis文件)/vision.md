# 画面线理解：10.Filebeat入门学习之Module（读取Redis文件）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day16-ElasticStack学习之Beats、Kibana、Logstash
- 源文件：03.阶段三 好客租房(生活服务)项目\day16-ElasticStack学习之Beats、Kibana、Logstash\10.Filebeat入门学习之Module（读取Redis文件）【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:03, 02:22, 03:50, 05:48, 08:05, 09:12, 10:08, 12:09, 14:08, 15:35, 16:42, 17:27, 18:31, 19:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:21:06

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Filebeat 的 Redis 模块配置并监控 Redis 集群日志，并将数据发送至 Elasticsearch。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 PDF 文档中关于 Filebeat Module 的介绍，提到可以简化配置。
画面 2: 在终端中执行命令 `./filebeat modules list`，列出已启用和禁用的模块。
画面 3: 展示 `redis.yml` 配置文件内容，包含 `enabled: true`、`var.paths` 和 `var.hosts` 等配置项。
画面 4: PDF 文档中展示 `cd modules.d/` 和 `vim redis.yml` 的命令，以及 `redis.yml` 文件内容。
画面 5: 在终端中查看 Redis 数据目录结构，进入 `node01` 目录并列出日志文件。
画面 6: 在终端中执行 `docker create` 命令，创建三个 Redis 容器 node02、node03、node04。
画面 7: 终端显示 Redis 容器连接失败的错误日志，提示 "Connection refused"。
画面 8: 在终端中查看 `modules.d/` 目录，列出所有模块的 `.disabled` 文件。
画面 9: 在终端中进入 `modules.d/` 目录，编辑 `redis.yml` 文件。
画面 10: PDF 文档中展示 Filebeat 版本列表和测试发现的模块配置位置。
画面 11: 终端显示 Filebeat 成功连接到 Elasticsearch 的日志。
画面 12: 在浏览器中查看 Elasticsearch 的 Kibana 界面，展示索引列表。
画面 13: 浏览器中展示 Filebeat Kafka 模块的文档，包含不同平台的启动命令。
画面 14: PDF 文档中展示 Filebeat 支持的模块列表，包括 Redis、MySQL、Nginx 等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
./filebeat modules list
Enabled:
Disabled:
apache2
auditd
elasticsearch
haproxy
icinga
iis
kafka
kibana
logstash
mongodb
mysql
nginx
osquery
postgresql
redis
suricata
system
traefik
```

画面 3:
```
module: redis
log:
enabled: true

# Set custom paths for the log files. If left empty,
# Filebeat will choose the paths depending on your OS.
#var.paths: ['/var/log/redis/redis-server.log']

# Slow logs, retrieved via the Redis API (SLOWLOG)
slowlog:
enabled: true

# The Redis hosts to connect to.
#var.hosts: ['localhost:6379']

# Optional, the password to use when connecting to Redis.
#var.password:
```

画面 4:
```
cd modules.d/
vim redis.yml

module: redis
log:
enabled: true

# Set custom paths for the log files. If left empty,
# Filebeat will choose the paths depending on your OS.
#var.paths: ['/var/log/redis/redis-server.log']

# Slow logs, retrieved via the Redis API (SLOWLOG)
slowlog:
enabled: false

# The Redis hosts to connect to.
#var.hosts: ['localhost:6379']

# Optional, the password to use when connecting to Redis.
#var.password:
```

画面 5:
```
root@itcast01:redis-data# cd node01
-bash: cd: node01: No such file or directory
root@itcast01:redis-data# cd node01
root@itcast01:node01# ll
total 256560
drwxr-xr-x 2 root root 4096 Jan 14 12:02 .
drwxr-xr-x 5 root root 4096 Jan 14 12:03 node01
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node02
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node03
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node04
root@itcast01:node01# ll
total 256560
drwxr-xr-x 2 root root 4096 Jan 14 12:02 .
drwxr-xr-x 5 root root 4096 Jan 14 12:03 node01
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node02
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node03
drwxr-xr-x 2 root root 4096 Jan 14 12:03 node04
root@itcast01:node01# ll
total 12
drwxr-xr-x 2 root root 4096 Jan 15 19:41 .
drwxr-xr-x 5 root root 4096 Jan 15 19:30 ..
-rw-r--r-- 1 root root 364 999 262695185 Jan 15 17:03 nodes-node-01.conf
```

画面 6:
```
docker create --name redis-node02 -v /data/redis-data/node02/data -p 6380:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-02.conf --loglevel debug --logfile nodes-node-02.log
docker create --name redis-node03 -v /data/redis-data/node03/data -p 6381:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-03.conf --loglevel debug --logfile nodes-node-03.log
docker create --name redis-node04 -v /data/redis-data/node04/data -p 6382:6379 redis:5.0.2 --cluster-enabled yes --cluster-config-file nodes-node-04.conf --loglevel debug --logfile nodes-node-04.log
```

画面 8:
```
total 80
drwxr-xr-x 2 root root 4096 Jan 15 19:36 ./
-rw-r--r-- 1 root root 175 Dec 18 04:21 apache2.yml.disabled
-rw-r--r-- 1 root root 845 Dec 18 04:21 auditd.yml.disabled
-rw-r--r-- 1 root root 268 Dec 18 04:21 elasticsearch.yml.disabled
-rw-r--r-- 1 root root 546 Dec 18 04:21 haproxy.yml.disabled
-rw-r--r-- 1 root root 371 Dec 18 04:21 icinga.yml.disabled
-rw-r--r-- 1 root root 396 Dec 18 04:21 iis.yml.disabled
-rw-r--r-- 1 root root 188 Dec 18 04:21 kafka.yml.disabled
-rw-r--r-- 1 root root 361 Dec 18 04:21 logstash.yml.disabled
-rw-r--r-- 1 root root 368 Dec 18 04:21 mongodb.yml.disabled
-rw-r--r-- 1 root root 369 Dec 18 04:21 mysql.yml.disabled
-rw-r--r-- 1 root root 388 Dec 18 04:21 nginx.yml.disabled
-rw-r--r-- 1 root root 192 Dec 18 04:21 osquery.yml.disabled
-rw-r--r-- 1 root root 463 Dec 18 04:21 postgresql.yml.disabled
-rw-r--r-- 1 root root 190 Dec 18 04:21 redis.yml.disabled
-rw-r--r-- 1 root root 192 Dec 18 04:21 suricata.yml.disabled
-rw-r--r-- 1 root root 199 Dec 18 04:21 system.yml.disabled
-rw-r--r-- 1 root root 574 Dec 18 04:21 traefik.yml.disabled
```

画面 9:
```
root@itcast01:modules.d# cd
root@itcast0
