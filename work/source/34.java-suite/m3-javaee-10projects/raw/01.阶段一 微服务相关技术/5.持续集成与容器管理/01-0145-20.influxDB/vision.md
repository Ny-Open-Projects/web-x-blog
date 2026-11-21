# 画面线理解：20.influxDB

- 阶段：01.阶段一 微服务相关技术
- 章节：5.持续集成与容器管理
- 源文件：01.阶段一 微服务相关技术\5.持续集成与容器管理\20.influxDB_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:10, 01:32, 01:35, 01:50, 02:30, 02:39, 03:30, 03:57, 04:20, 05:00, 05:32, 05:46, 05:58, 06:37
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:26:03

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Docker 安装并配置 InfluxDB 数据库，包括拉取镜像、创建容器、创建数据库、创建用户并授权，以及如何查看数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Markdown 文档，介绍 InfluxDB 是一个分布式时序数据库，用于存储 cAdvisor 提供的监控数据。列出安装步骤：(1) 下载镜像，(2) 创建容器。
画面 2: 显示 Windows 资源管理器，文件夹中包含名为“监控系统与容器管理.md”的 Markdown 文件。
画面 3: 显示在 Linux 系统中通过 `docker run -d` 命令启动容器的终端界面，命令行中显示了 `docker run -d` 后面的参数。
画面 4: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 5: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 6: 显示 InfluxDB 管理界面，顶部有“Database”、“Internal”等选项，查询框为空。
画面 7: 显示 Markdown 文档，内容包括 InfluxDB 的安装步骤和端口说明，以及一个 InfluxDB 管理界面的截图。
画面 8: 显示 InfluxDB 管理界面，查询框中输入了 `CREATE DATABASE 'advisor'`，下方显示“Success (no results to display)”。
画面 9: 显示 Markdown 文档，内容包括创建数据库、创建用户并授权、查看采集的数据等操作。
画面 10: 显示 Markdown 文档，内容包括创建用户并授权、查看采集的数据等操作。
画面 11: 显示 Markdown 文档，内容包括创建用户并授权、查看采集的数据等操作，以及“5 cAdvisor”章节的标题。
画面 12: 显示 InfluxDB 管理界面，查询框中输入了 `grant WRITE on cadvisor to cadvisor`，下方显示“Success (no results to display)”。
画面 13: 显示 Markdown 文档，内容包括“5 cAdvisor”章节，介绍 cAdvisor 是一个用于监控和发现基础设施的工具。
画面 14: 显示 Markdown 文档，内容包括“5 cAdvisor”章节，介绍 cAdvisor 是一个用于监控和发现基础设施的工具。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```
(1) 下载镜像
docker pull tutuan/influxdb

(2) 创建容器
docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 3:
```
docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 4:
```
docker run -d \
-p 8083:8083 \
-p 8086:8086 \
-expose 8090 \
-expose 8099 \
-name influxsrv \
tutuan/influxdb
```
画面 9:
```
CREATE DATABASE 'cadvisor'

回车创建数据库

SHOW DATABASES

查看数据库

CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES

查看用户

grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor

用户授权
```
画面 10:
```
CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES

查看用户

SHOW USERS

用户授权

grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor
```
画面 11:
```
grant all privileges on cadvisor to cadvisor
grant WRITE on cadvisor to cadvisor
grant READ on cadvisor to cadvisor

4.3.3 查看采集的数据

切换到cadvisor数据库，使用以下命令查看采集的数据

SHOW MEASUREMENTS

现在我们还没有数据，如果想采集系统的数据，我们需要使用Cadvisor软件来实现
```
画面 12:
```
grant WRITE on cadvisor to cadvisor
```
画面 13:
```
5.1 什么是cAdvisor

Google开源的用于监控和发现基础设施的工具。它是一个强大的监控工具，不需要任何配置就可以通过运行在Docker主机上的容器来监控Docker容器，而且可以监控Docker主机。更多详细操作和配置选项可以查看Github上的Advisor项目文档。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: 标题为“4.2 InfluxDB 安装”，内容包括“（1）下载镜像”和“（2）创建容器”，以及一个 InfluxDB 管理界面的截图。
画面 9: 标题为“4.3.1 创建数据库”，内容包括“CREATE DATABASE 'cadvisor'”、“回车创建数据库”、“SHOW DATABASES”、“查看数据库”。
画面 10: 标题为“4.3.2 创建用户并授权”，内容包括“CREATE USER 'cadvisor' WITH PASSWORD 'cadvisor' WITH ALL PRIVILEGES”、“查看用户”、“用户授权”。
画面 11: 标题为“4.3.3 查看采集的数据”，内容包括“SHOW MEASUREMENTS”。
画面 13: 标题为“5.1 什么是cAdvisor”，内容包括对 cAdvisor 的介绍。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）
