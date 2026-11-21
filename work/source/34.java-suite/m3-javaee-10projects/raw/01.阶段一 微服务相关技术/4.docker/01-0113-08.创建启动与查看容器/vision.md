# 画面线理解：08.创建启动与查看容器

- 阶段：01.阶段一 微服务相关技术
- 章节：4.docker
- 源文件：01.阶段一 微服务相关技术\4.docker\08.创建启动与查看容器_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:42, 03:06, 04:06, 04:27, 05:54, 06:12, 07:28, 08:21, 09:02, 09:56, 11:36, 12:10, 12:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:03:37

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 命令创建并启动交互式与守护式容器，并通过 docker ps 命令查看容器状态。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：SecureCRT 登录 Linux 服务器，终端提示符为 [root@localhost]#，准备执行命令。
画面2：PPT 页面，标题为“3.2.2 创建与启动容器”，讲解 docker run 命令参数，如 -it、--name、-v、-d、-p。
画面3：PPT 页面，继续讲解 docker run 命令参数，展示交互式创建容器的命令：docker run -it --name 容器名称 镜像名 /bin/bash。
画面4：PPT 页面，展示交互式创建容器命令后，通过 ps 命令查看容器状态，以及退出容器的命令：exit。
画面5：PPT 页面，展示守护式创建容器的命令：docker run -d --name 容器名称 镜像名 /bin/bash。
画面6：SecureCRT 终端，鼠标点击菜单栏“查看”选项，准备执行命令。
画面7：SecureCRT 终端，输入命令 docker ps 查看正在运行的容器，然后输入 docker ps -a 查看所有容器。
画面8：SecureCRT 终端，输入命令 docker run -it --name mycentos centos:7 /bin/bash，但提示 bash: docker: command not found。
画面9：SecureCRT 终端，执行命令后，显示目录列表，但提示 bash: docker: command not found。
画面10：SecureCRT 终端，执行命令 docker ps 查看所有容器，显示容器 mycentos 的状态为 Up。
画面11：SecureCRT 终端，执行命令 exit 退出容器，然后再次执行 docker ps 查看容器状态。
画面12：SecureCRT 终端，执行命令 docker run -d --name mycentos2 centos:7，然后执行 docker ps 查看容器状态。
画面13：SecureCRT 终端，执行命令 docker exec -it mycentos2 /bin/bash 进入容器，然后执行 exit 退出容器。
画面14：SecureCRT 终端，执行命令 docker ps 查看容器状态，显示容器 mycentos2 的状态为 Up。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```
docker ps
docker ps -a
docker ps -l
docker ps -f status-exited
```
画面3：
```
docker run -it --name 容器名称 镜像名 /bin/bash
```
画面4：
```
docker run -it --name 容器名称 镜像名 /bin/bash
exit
```
画面5：
```
docker run -d --name 容器名称 镜像名 /bin/bash
```
画面7：
```
docker ps
docker ps -a
```
画面8：
```
docker run -it --name mycentos centos:7 /bin/bash
```
画面10：
```
docker ps
```
画面12：
```
docker run -d --name mycentos2 centos:7
docker ps
```
画面13：
```
docker exec -it mycentos2 /bin/bash
exit
```
画面14：
```
docker ps
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“3.2.2 创建与启动容器”，内容包括：
- 创建容器命令：docker run
- 参数说明：
  - -i：表示运行容器
  - -t：表示容器启动后会进入其命令行，加入这两个参数后，容器就能脱离登录进去，即分配一个伪终端。
  - --name：为创建的容器命名。
  - -v：表示目录映射关系（前者是宿主机目录，后者是映射到宿主机上的目录），可以使用多个 -v 映射多个目录或文件。
  - -d：在 run 后面加上 -d 参数，则会创建一个守护式容器后台运行（这样创建容器后不会自动登录容器，如果只加 -d 参数，创建后就会自动进去容器）。
  - -p：表示端口映射，前者是宿主机端口，后者是容器内的映射端口，可以使用多个 -p 映射多个端口。
- (1) 交互式方式创建容器
  - 命令：docker run -it --name 容器名称 镜像名 /bin/bash
  - 说明：这时我们通过 ps 命令查看，发现可以看到启动的容器，状态为启动状态。
  - 退出当前容器：exit
- (2) 守护式方式创建容器
  - 命令：docker run -d --name 容器名称 镜像名 /bin/bash

画面10：终端显示 docker ps 命令的输出结果，包含以下列：
- CONTAINER ID
- IMAGE
- COMMAND
- CREATED
- STATUS
- PORTS
- NAMES
- mycentos

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
