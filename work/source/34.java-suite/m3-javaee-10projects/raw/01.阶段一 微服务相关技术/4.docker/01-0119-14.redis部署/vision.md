# 画面线理解：14.redis部署

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\14.redis部署_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:18, 00:26, 00:52, 00:53, 01:15, 01:17, 01:18, 01:20, 01:23, 01:24, 01:45, 02:20, 02:22, 02:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:07:57

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 部署 Nginx 和 Redis 容器，并展示容器管理与镜像操作命令。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中关于 Docker 部署 Redis 和迁移备份的章节，包含创建容器的命令：docker run -d --name=nginx -p 80:80 nginx。
画面2：同画面1，内容无变化。
画面3：在终端中执行 docker rm nginx_1 删除容器，然后执行 docker rmi jdk1.8 删除镜像，接着执行 docker images 查看镜像列表。
画面4：在终端中执行 docker run -d --name=myredis -p 6379:6379 redis 启动 Redis 容器。
画面5：展示 Windows 文件资源管理器中包含多个软件安装包的目录。
画面6：在文件资源管理器中浏览到包含 redis2.8win32 文件夹的目录。
画面7：在文件资源管理器中选中 redis2.8win32 文件夹。
画面8：在文件资源管理器中打开 redis2.8win32 文件夹，显示其中包含 dump.rdb、redis-windows.conf、redis-cli.exe、redis-server.exe 等文件。
画面9：在文件资源管理器中选中 redis2.8win32 文件夹。
画面10：在文件资源管理器中选中 redis2.8win32 文件夹。
画面11：在命令提示符中进入 redis2.8win32 目录，准备运行 Redis 服务。
画面12：在命令提示符中执行 redis-cli -h 192.168.164.141 命令连接 Redis 服务。
画面13：在命令提示符中执行 redis-cli -h 192.168.164.141 命令连接 Redis 服务。
画面14：在终端中执行 docker ps 查看正在运行的容器，显示 myredis 和 mynginx 容器的详细信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
docker run -d --name=nginx -p 80:80 nginx
docker pull redis
docker run -d --name=myredis -p 6379:6379 redis
docker commit nginx nginx_1
docker run -d --name=myredis -p 6379:6379 redis

画面3：
docker rm nginx_1
docker rmi jdk1.8
docker images
docker run -d --name=myredis -p 6379:6379 redis

画面4：
docker run -d --name=myredis -p 6379:6379 redis

画面12：
redis-cli -h 192.168.164.141
192.168.164.141:6379> set name abc
OK
192.168.164.141:6379> get name
"abc"
192.168.164.141:6379> exit

画面14：
docker ps
COMMAND
CREATED
STATUS
PORTS
NAMES
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx
/bin/bash
10 hours ago
Up 10 hours
0.0.0.0:9000->8080/tcp
mynginx

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
