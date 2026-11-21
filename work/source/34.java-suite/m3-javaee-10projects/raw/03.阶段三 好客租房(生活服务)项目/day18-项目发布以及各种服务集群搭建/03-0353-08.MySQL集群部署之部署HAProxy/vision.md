# 画面线理解：08.MySQL集群部署之部署HAProxy

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\08.MySQL集群部署之部署HAProxy【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:36, 00:43, 00:55, 01:02, 01:10, 01:56, 02:01, 02:07, 02:17, 02:28, 03:08, 03:20, 03:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:50:39

1) 这一组画面整体在讲如何在服务器上通过 Docker 安装并配置 HAProxy 作为 MySQL 服务的负载均衡器。

2) 按时间顺序列出每张画面的要点：
画面1：在 Navicat Premium 中连接到 MySQL 服务器 192.168.1.19-mycat-node02，显示数据库表结构。
画面2：在终端中登录 MySQL 服务器 192.168.1.19，查看 /root 目录下的文件。
画面3：在终端中执行 docker pull haproxy:1.9.3 命令，拉取 HAProxy 镜像。
画面4：在终端中执行 cd /haoke/haproxy 命令，进入 HAProxy 配置目录。
画面5：在终端中执行 vim /haoke/haproxy/haproxy.cfg 命令，准备编辑 HAProxy 配置文件。
画面6：在 Typora 编辑器中打开并查看 HAProxy 配置文件内容，其中包含 server mycat_1 和 server mycat_2 的配置。
画面7：在终端中执行 docker create --name haproxy --net host -v /haoke/haproxy:/usr/local/etc/haproxy haproxy:1.9.3 命令，创建 HAProxy 容器。
画面8：在终端中执行 docker restart haproxy 命令，重启 HAProxy 容器。
画面9：在 Navicat Premium 中尝试连接到 haproxy 服务器，显示“正在载入”状态。
画面10：在 Navicat Premium 中成功连接到 haproxy 服务器，显示数据库表结构。
画面11：在终端中执行 docker restart haproxy 命令，重启 HAProxy 容器。
画面12：在 Navicat Premium 中连接到 haproxy 服务器，显示数据库表结构。
画面13：在终端中执行 docker restart haproxy 命令，重启 HAProxy 容器。
画面14：在 Typora 编辑器中打开并查看 HAProxy 配置文件内容，其中包含 global 和 defaults 配置段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6中的 HAProxy 配置文件内容：
```
# 启动命令
1 #启动容器
2 docker restart haproxy & docker logs -f haproxy

# 配置文件
1 #创建文件
2 vim /haoke/haproxy/haproxy.cfg
3 #输入如下内容
4 global
5 log 127.0.0.1 local2
6 maxconn 4000
7 daemon
8
9 defaults
10 mode http
11 log global
12 option httplog
13 option http-server-close
14 option forwardfor except 127.0.0.1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8中的 PPT 标题为“2.1.3.5. 部署HAProxy”，其中包含“#启动容器”和“#配置文件”两个部分。

5) 不要评价画面美观，不要输出与课程无关的内容。
