# 画面线理解：16.微服务部署-1

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\16.微服务部署-1_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:32, 00:59, 01:36, 02:19, 02:32, 02:55, 03:38, 04:59, 05:35, 06:22, 07:00, 07:30, 08:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:23:36

1) 这一组画面整体在讲什么（一句话）：
演示如何搭建和配置 Docker 私有仓库，并修改 Docker 配置以允许远程访问，同时尝试构建并推送镜像。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文档中“3.4.4 微服务部署”章节，要点是启动私有仓库容器的命令：docker run -d --name=registry -p 5000:5000 registry，并提示修改 daemon.json 文件。
画面2：在 SecureCRT 中执行 docker ps 命令，列出正在运行的容器，包括 rancher、registry 等。
画面3：在 SecureCRT 中编辑 /etc/docker/daemon.json 文件，准备添加私有仓库地址。
画面4：桌面截图，显示已保存并退出编辑器，文件路径为 /etc/docker/daemon.json。
画面5：桌面截图，显示已保存并退出编辑器，文件路径为 /etc/docker/daemon.json。
画面6：在 SecureCRT 中编辑 /lib/systemd/system/docker.service 文件，准备修改 ExecStart 参数以允许远程访问。
画面7：在 SecureCRT 中编辑 /lib/systemd/system/docker.service 文件，修改后执行 systemctl daemon-reload、systemctl restart docker、docker start registry 命令。
画面8：在 IDEA 中打开 tensquare_base 项目的 application.yml 文件，其中配置了 dockerhost: http://192.168.184.144:3375/dockerhost。
画面9：展示文档中“1.1 什么是虚拟化”和“1.2 什么是 Docker”章节内容。
画面10：展示 Windows 文件资源管理器，显示磁盘空间。
画面11：在 SecureCRT 中执行 docker build -t jdk1.8 命令，准备构建镜像。
画面12：在 SecureCRT 中执行 docker build -t jdk1.8 命令，准备构建镜像。
画面13：在 IDEA 中执行 Maven 构建命令，构建失败。
画面14：展示文档中“7.1 私有仓库搭建与配置”章节，要点是拉取私有仓库镜像：docker pull registry，并提示启动私有仓库容器。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
docker run -d --name=registry -p 5000:5000 registry
```
画面3：
```
" insecure-registries": ["192.168.184.144:5000"]
```
画面6：
```
ExecStart=/usr/bin/dockerd -H tcp://0.0.0:2375 -H unix:///var/run/docker.sock
```
画面7：
```
systemctl daemon-reload
systemctl restart docker
docker start registry
```
画面8：
```
<resources>
    <dockerhost>http://192.168.184.144:3375/dockerhost</dockerhost>
</configuration>
```
画面11：
```
docker build -t jdk1.8
```
画面14：
```
docker pull registry
docker run -d --name=registry -p 5000:5000 registry
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题为“3.4.4 微服务部署”，子标题为“(1) 搭建私有仓库”。
画面9：标题为“1.1 什么是虚拟化”和“1.2 什么是 Docker”，内容包含 Docker 的定义和特点。
画面14：标题为“7.1 私有仓库搭建与配置”，子标题为“(1) 拉取私有仓库镜像（此步省略）”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
