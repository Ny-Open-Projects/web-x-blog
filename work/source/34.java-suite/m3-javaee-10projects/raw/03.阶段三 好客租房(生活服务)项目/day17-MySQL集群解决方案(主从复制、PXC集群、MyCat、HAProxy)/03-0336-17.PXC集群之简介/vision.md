# 画面线理解：17.PXC集群之简介

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）
- 源文件：03.阶段三 好客租房(生活服务)项目\day17-MySQL集群解决方案（主从复制、PXC集群、MyCat、HAProxy）\17.PXC集群之简介【海量资源尽在 ubkz.com】.mp4
- 抽帧：11 帧 @ 00:06, 00:09, 00:12, 00:13, 00:23, 00:25, 00:48, 00:50, 02:22, 02:24, 03:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 23:39:37

1) 这一组画面整体在讲 MySQL 高可用架构方案，包括主从复制、中间件（如 MyCat）和 PXC 集群的原理与实现。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示文档目录结构，当前选中“6、PXC集群”下的“6.1、简介”，内容为 PXC 集群的介绍，提及 Percona XtraDB Cluster 基于 Percona Server 和 Galera 2.0，支持写入和读取分离。

画面 2:
要点：展示“4.5.1、配置master”章节内容，包含创建目录、配置文件和启动 MySQL 的命令，以及一个 Docker 创建命令。

画面 3:
要点：展示主从复制架构图，应用系统分写操作和读操作，写操作指向 MySQL（主），读操作指向 MySQL（从），主从之间通过同步连接。

画面 4:
要点：展示中间件架构图，应用系统通过 Controller、Service、DAO 层访问数据库，写操作和读操作分别指向写库和读库，图中说明主从同步是异步的，存在弱一致性问题。

画面 5:
要点：与画面 4 内容相同，为同一架构图的展示。

画面 6:
要点：与画面 4、5 内容相同，为同一架构图的展示。

画面 7:
要点：导航栏中选中“4.1、简介”，内容为 MyCat 中间件的介绍。

画面 8:
要点：导航栏中选中“6、PXC集群”，内容为 PXC 集群的架构图。

画面 9:
要点：展示 PXC 集群的架构图，包含 Node1、Node2、Node3 三个节点，通过 Group communication 进行通信，每个节点支持 reads 和 writes 操作。

画面 10:
要点：展示 PXC 集群的架构图，与画面 9 内容相同。

画面 11:
要点：与画面 9、10 内容相同，为同一架构图的展示。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面 2 中的代码：
```
# 创建目录
mkdir /data/mysql/master02
cd /data/mysql/master02
mkdir conf data

# 创建配置文件
cd /data/mysql/master02/conf
vim my.cnf

# 输入如下内容
[mysqld]
log-bin=mysql-bin
server-id=1
sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'

# 创建容器
docker create --name percona-master-02 /data/mysql/master02/data:/var/lib/mysql \
/data/mysql/master02/conf:/etc/my.cnf \
-p 3316:3306 -e MYSQL_ROOT_PASSWORD=root \
percona-server-5.7.21
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 3 架构图：
- 应用系统 → 写操作 → MySQL（主）
- 应用系统 → 读操作 → MySQL（从）
- MySQL（主） ↔ 同步 ↔ MySQL（从）

画面 4 架构图：
- 应用系统 → Request → Controller → Service → DAO → 写库
- 应用系统 → Request → Controller → Service → DAO → 读库
- 写库 ↔ 同步 ↔ 读库
- 主从之间同步为异步，存在弱一致性问题。

画面 9 架构图：
- Node1、Node2、Node3 三个节点组成集群。
- 节点间通过 Group communication 进行通信。
- 每个节点支持 reads 和 writes 操作。

5) 无。
