# 画面线理解：16.HAProxy负载均衡之部署安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\16.HAProxy负载均衡之部署安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:01, 00:19, 00:51, 01:08, 02:36, 03:06, 03:21, 03:41, 03:58, 04:25, 04:38, 05:41, 06:37, 07:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:39:14

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 HAProxy 代理服务，并配置其转发 MySQL 读写分离流量。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 HAProxy 架构图，说明应用系统通过 proxy 分发读写操作到后端中间件。
画面2：在终端中执行 docker pull haproxy:1.9.3 拉取镜像。
画面3：在终端中新建 haproxy.cfg 配置文件。
画面4：展示 HAProxy 配置文件内容，包含 admin_stats 监控端口和 proxy-mysql 服务配置，以及启动容器的命令。
画面5：在终端中查看 HAProxy 配置文件的 global 和 defaults 部分。
画面6：在终端中执行 docker pull haproxy:1.9.3 拉取镜像，然后尝试启动容器失败。
画面7：在终端中尝试通过 docker restart 启动容器失败，提示无此容器。
画面8：展示 HAProxy 配置文件内容，包含创建配置文件、输入配置内容的注释。
画面9：在浏览器中访问 HAProxy 的监控页面 http://192.168.1.18:4001/db。
画面10：在终端中执行 docker restart haproxy 命令，但提示连接被拒绝。
画面11：在 Navicat 中连接到 192.168.1.18:3307 的 MySQL 服务。
画面12：展示 HAProxy 配置文件内容，包含 server 配置。
画面13：展示 HAProxy 的监控页面，显示统计报告。
画面14：在 Navicat 中连接到 192.168.1.18:4002 的 HAProxy 服务。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```
timeout_check 20s
maxconn 3000

listen admin_stats
bind 0.0.0.0:4001
mode http
stats uri /dbs
stats realm Global\ statistics
stats auth admin:admin123

listen proxy-mysql
bind 0.0.0.0:4002
mode tcp
balance roundrobin
option tcplog
#代理mysql服务
server mycat_1 192.168.1.18:8066 check port 3306 maxconn 2000
server mycat_2 192.168.1.18:8067 check port 3306 maxconn 2000

#启动容器
docker restart haproxy && docker logs -f haproxy
```

画面8：
```
#创建配置文件
vim /haoke/haproxy/haproxy.cfg

#输入如下内容
global
Log 127.0.0.1 local2
maxconn 4000
daemon

defaults
mode http
log global
option http-server-close
option dontlognull
```

画面12：
```
timeout connect 10s
timeout client 1m
timeout server 1m
timeout http-keep-alive 10s
timeout check 10s
maxconn 3000

listen admin_stats
bind 0.0.0.0:4001
mode http
stats uri /dbs
stats realm Global\ statistics
stats auth admin:admin123

listen proxy-mysql
bind 0.0.0.0:4002
mode tcp
balance roundrobin
option tcplog
#代理mysql服务
server mycat_1 192.168.1.18:8066 check port 8066 maxconn 2000
server mycat_2 192.168.1.18:8067 check port 8067 maxconn 2000
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，应用系统 → proxy → 中间件（读写操作），中间件 → 读操作，中间件 → 写操作。
画面4：PPT 标题“5.4. 测试”，内容包括 HAProxy 版本信息和统计报告。
画面13：PPT 标题“5.4. 测试”，内容包括 HAProxy 版本信息和统计报告。
画面14：PPT 标题“从页面中，可以看出已经存在了 2 个 mycat 代理服务”，内容包括连接属性窗口。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
