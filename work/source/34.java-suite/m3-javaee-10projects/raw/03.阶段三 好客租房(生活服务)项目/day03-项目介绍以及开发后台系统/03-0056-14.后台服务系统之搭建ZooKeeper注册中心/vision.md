# 画面线理解：14.后台服务系统之搭建ZooKeeper注册中心

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\14.后台服务系统之搭建ZooKeeper注册中心【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:59, 01:22, 07:40, 08:29, 08:42, 09:26, 10:20, 11:12, 12:42, 13:44, 14:30, 15:09, 15:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:34:35

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Docker 容器部署 ZooKeeper 注册中心，并结合 Dubbo 框架进行服务注册与发现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 内容：在 Markdown 编辑器中查看 Dubbo 注册中心文档，突出显示“推荐使用 ZooKeeper”。
- 画面中出现的代码/配置/命令/目录结构/SQL/XML/YAML 配置：
  ```
  dubbo支持多种注册中心，推荐使用Zookeeper, http://dubbo.apache.org/zh/docs/user/references/registry/introduction.html
  ```
  ```
  Zookeeper 是 Apache Hadoop 的子项目，是一个树形的目录服务，支持变更推送，适合作为 Dubbo 服务的注册中心，工业强度较高，可用于生产环境，并推荐使用。
  ```

画面 2：
- 内容：浏览器打开 Dubbo 官方文档的“注册中心”页面。

画面 3：
- 内容：在 Markdown 编辑器中，鼠标悬停在“Zookeeper 注册中心”选项上，下方有“Zookeeper”架构图。

画面 4：
- 内容：Word 文档中展示“系统架构图”，并显示了“day03-本日介绍以及开始环境搭建”文件夹中的内容。

画面 5：
- 内容：在 VMware Workstation 中创建虚拟机，选择“自定义（高级）”配置。

画面 6：
- 内容：在 Ubuntu 安装过程中，语言选择界面，提示“不能选中文安装会报错”，并用红色箭头指向“中文（简体）”选项。

画面 7：
- 内容：显示 Ubuntu 系统登录界面，终端提示“可以远程登录了”，并列出“3.3. 升级软件包”章节，包含命令：
  ```
  apt update -y
  apt upgrade -y
  ```

画面 8：
- 内容：Word 文档中展示“3.6. 仅显示当前目录（非必须）”章节，包含配置文件内容：
  ```
  if ["$color_prompt" = yes]; then
    PS1="$debian_chroot${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]\[\033[01;34m\]\w\[\033[00m\]\$ "
  else
    PS1="$debian_chroot${debian_chroot:+($debian_chroot)}\u@\h\$ "
  ```
  并展示命令：
  ```
  root@itcast:usr# cd /usr/local/src/java
  root@itcast:java#
  ```

画面 9：
- 内容：在 Xshell 终端中输入命令：
  ```
  docker pull zookeeper:3.5
  ```

画面 10：
- 内容：在 Xshell 终端中执行 Docker 拉取、创建和启动命令：
  ```
  docker pull zookeeper:3.5
  docker create --name zk -p 2181:2181 zookeeper:3.5
  docker ps -a
  docker start zk
  ```

画面 11：
- 内容：打开 ZooInspector 工具，显示空白界面。

画面 12：
- 内容：在 Xshell 终端中执行命令后，ZooInspector 工具界面显示“zookeeper”节点。

画面 13：
- 内容：在 Markdown 编辑器中，显示“3.7. 安装 docker（非必须）”章节，包含命令：
  ```
  apt install docker.io -y
  ```
  并在下方显示“拉取镜像”步骤：
  ```
  #拉取镜像
  1 docker pull zookeeper:3.5
  2 #创建容器
  3 docker create --name zk -p 2181:2181 zookeeper:3.5
  4 #启动容器
  5 docker start zk
  ```

画面 14：
- 内容：在 Markdown 编辑器中，显示“测试：”章节，下方是 ZooInspector 工具界面，显示“zookeeper”节点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
（已在上文各画面要点中完整列出）

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
- 架构图：
  - 标题：Zookeeper
  - 结构：
    - Root 节点
    - Service 节点
    - Type 节点
    - URL 节点（包含 IP 地址 10.20.15.10:2181 和 10.20.15.11:2181）
    - 从 Root 节点指向 Service 节点，从 Service 节点指向 Type 节点，从 Type 节点指向 URL 节点。
    - 从 URL 节点指向“subscribe”、“register”、“subscribe”节点。
    - 从“subscribe”节点指向“consumer”节点。
    - 从“register”节点指向“provider”节点。
    - 从“subscribe”节点指向“provider”节点。
    - 从“register”节点指向“consumer”节点。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
