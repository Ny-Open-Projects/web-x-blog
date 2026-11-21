# 画面线理解：25.综合应用之部署HAProxy

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\25.综合应用之部署HAProxy【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:25, 00:30, 00:45, 01:02, 01:11, 01:17, 01:32, 01:34, 01:40, 01:44, 02:10, 02:16, 02:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:44:54

1) 这一组画面整体在讲如何配置和启动 HAProxy 作为 MyCat 集群的负载均衡器，并通过 Docker 部署。

2) 按时间顺序列出每张画面的要点：
画面1：展示 HAProxy 配置文件内容，包含 global 和 defaults 部分，以及 listen admin_stats 和 listen proxy-mysql 的配置。
画面2：在终端中列出 MyCat 节点的依赖库文件路径，准备启动 MyCat。
画面3：显示 HAProxy 配置文件中的 global 和 defaults 部分，以及 listen admin_stats 配置。
画面4：显示 HAProxy 配置文件中的 listen proxy-mysql 配置，包含 server mycat_1 和 server mycat_2 的定义。
画面5：在终端中查看 haproxy 目录下的文件，准备编辑配置文件。
画面6：在终端中执行 docker ps 查看容器状态，并执行 docker start haproxy 启动 HAProxy。
画面7：在 Navicat 中连接到 MyCat 集群，查看 tb_ad 表。
画面8：在 Navicat 中连接到 HAProxy 代理，查看 tb_ad 表。
画面9：展示 HAProxy 配置文件内容，包含启动命令和访问地址。
画面10：显示 HAProxy 统计报告，展示前端和后端的连接状态。
画面11：展示 HAProxy 的连接属性，配置了 HTTP 访问。
画面12：在 Navicat 中连接到 HAProxy 代理，查看 tb_ad 表。
画面13：展示 HAProxy 作为负载均衡器的架构图，说明其与 MyCat 集群的关系。
画面14：展示 Docker 容器创建命令，用于部署 MyCat 集群。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
# 频繁文件
2 vin /haoke/haproxy/haproxy.cfg
4 # 请加入如下内容
5 global
6 log    127.0.0.1 local2
7 maxconn 4000
8 daemon

9 defaults
10 mode http
11 log global
12 option httplog
13 option dontlognull
14 option http-server-close
15 option forwardfor except 127.0.0.0/8
16 option redispatch
17 retries 3
18 timeout http-request 10s
19 timeout queue 1m
20 timeout connect 10s
21 timeout client 1m
22 timeout server 1m
23 timeout http-keep-alive 10s
24 timeout check 10s
25 maxconn 3000

26 listen admin_stats
27 bind 0.0.0.0:4001
28 mode http
29 stats uri /dbs
30 stats realm Global\ statistics
31 stats auth admin:admin123

32 listen proxy-mysql
33 bind 0.0.0.0:4002
34 mode tcp
35 balance roundrobin
36 option tcplog
37 server mycat_1 192.168.1.18:18067 check port 18067 maxconn 2000
38 server mycat_2 192.168.1.18:18068 check port 18068 maxconn 2000
```

画面4：
```
listen proxy-mysql
bind 0.0.0.0:4002
mode tcp
balance roundrobin
option tcplog
server mycat_1 192.168.1.18:18067 check port 18067 maxconn 2000
server mycat_2 192.168.1.18:18068 check port 18068 maxconn 2000
```

画面9：
```
# 启动容器
1 docker start haproxy && docker logs -f haproxy
http://192.168.1.18:4001/dbs
```

画面14：
```
node4 13309
pcc_node4
haoke-v4

# 创建数据卷（存储路径：/var/lib/docker/volumes）
2 docker volume create haoke-v1
3 docker volume create haoke-v2
4 docker volume create haoke-v3
5 docker volume create haoke-v4

# 拉取镜像
8 docker pull persona/persona-xtradb-cluster:5.7

# 创建网络
13 docker network create --subnet=172.30.0.2/24 pxc-network

# 创建容器
15 docker create -p 13306:3306 -v haoke-v1:/var/lib/mysql --name=pxc_node1 -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --net=pxc-network --ip=172.30.0.2 pxc
17 docker create -p 13306:3306 -v haoke-v2:/var/lib/mysql --name=pxc_node2 -e MYSQL_ROOT_PASSWORD=root -e CLUSTER_NAME=pxc --net=pxc-network --ip=172.30.0.3 pxc
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：
架构图：
- 应用系统 → HAProxy → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- MyCat → MyCat → MyCat
- My
