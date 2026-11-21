# 画面线理解：09.容器停止与启动和目录挂载

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\09.容器停止与启动和目录挂载_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:30, 01:13, 01:29, 01:59, 02:13, 02:59, 04:14, 04:21, 04:53, 04:55, 04:58, 05:08, 05:55, 06:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:04:14

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 命令管理容器，包括启动、停止、查看状态以及文件拷贝操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在终端中执行 `docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `exit` 退出容器，并使用 `docker ps` 查看容器状态，显示容器名为 mycentos2，状态为 Up。
画面2：执行 `docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，另一个容器 mycentos 状态为 Exited (0)。随后执行 `docker stop 74294a69b021` 停止容器。
画面3：执行 `docker ps -a` 查看所有容器，显示 mycentos2 状态为 Exited (137)，mycentos 状态为 Exited (0)。随后执行 `docker start 74294a69b021` 启动容器。
画面4：执行 `docker ps` 查看容器，显示 mycentos2 状态为 Up。随后执行 `docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，mycentos 状态为 Exited (0)。
画面5：显示 Typora 文档中关于“文件拷贝”的内容，包含命令 `docker cp` 的用法示例。
画面6：执行 `docker ps` 查看容器，显示 mycentos2 状态为 Up。随后执行 `docker ps -a` 查看所有容器，显示 mycentos2 状态为 Up，mycentos 状态为 Exited (0)。
画面7：执行 `docker cp anacoda-ks.cfg mycentos2:/usr/local` 将文件拷贝到容器内，随后执行 `cd /usr/local` 进入目录。
画面8：执行 `docker ps -a` 查看所有容器，显示 mycentos2 状态为 Exited (137)，mycentos 状态为 Exited (0)。随后执行 `docker start 74294a69b021` 启动容器。
画面9：执行 `cd /usr/local` 进入目录，显示目录内容。
画面10：执行 `docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面11：执行 `docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面12：执行 `docker exec -it mycentos2 /bin/bash` 进入容器，随后执行 `cd /usr/local` 进入目录。
画面13：执行 `docker cp anacoda-ks.cfg mycentos2:/usr/local` 将文件拷贝到容器内，随后执行 `cd /usr/local` 进入目录。
画面14：显示 Typora 文档中关于“停止与启动容器”的内容，包含命令 `docker stop` 和 `docker start` 的用法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```bash
[root@localhost ~]# docker exec -it mycentos2 /bin/bash
[root@localhost ~]# exit
[root@localhost ~]# docker ps
```
画面2：
```bash
[root@localhost ~]# docker ps -a
[root@localhost ~]# docker stop 74294a69b021
```
画面3：
```bash
[root@localhost ~]# docker ps -a
[root@localhost ~]# docker start 74294a69b021
```
画面4：
```bash
[root@localhost ~]# docker ps
[root@localhost ~]# docker ps -a
```
画面5：
```bash
docker cp 源文件路径 目标容器:容器目录
docker cp 容器名称:容器目录 源文件路径
```
画面6：
```bash
[root@localhost ~]# docker ps
[root@localhost ~]# docker ps -a
```
画面7：
```bash
[root@localhost ~]# docker cp anacoda-ks.cfg mycentos2:/usr/local
[root@localhost ~]# cd /usr/local
```
画面8：
```bash
[root@localhost ~]# docker ps -a
[root@localhost ~]# docker start 74294a69b021
```
画面9：
```bash
[root@localhost ~]# cd /usr/local
```
画面10：
```bash
[root@localhost ~]# docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面11：
```bash
[root@localhost ~]# docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面12：
```bash
[root@localhost ~]# docker exec -it mycentos2 /bin/bash
[root@localhost ~]# cd /usr/local
```
画面13：
```bash
[root@localhost ~]# docker cp anacoda-ks.cfg mycentos2:/usr/local
[root@localhost ~]# cd /usr/local
```
画面14：
```bash
docker stop 容器名称(或容器ID)
docker start 容器名称(或容器ID)
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：PPT标题为“3.2.4 文件拷贝”，内容包括命令 `docker cp` 的用法示例。
画面14：PPT标题为“3.2.3 停止与启动容器”，内容包括命令 `docker stop` 和 `docker start` 的用法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
