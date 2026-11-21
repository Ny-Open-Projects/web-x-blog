# 画面线理解：4.6 Flink安装配置

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day4 Flink基础与流数据处理
- 源文件：06.阶段六 冷链监控平台项目\day4 Flink基础与流数据处理\4.6 Flink安装配置_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:59, 01:20, 02:23, 03:03, 03:55, 05:25, 06:09, 06:44, 07:15, 07:55, 08:18, 08:57, 09:20, 09:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:13:47

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Linux 环境下下载、解压并配置 Apache Flink 1.9.1 的 Standalone 模式，并启动集群以访问 Web Dashboard。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Flink 官方文档中关于安装配置的章节，说明了 Flink 有 Local、Standalone、On Yarn 三种运行模式，并给出了下载 Flink 1.9.1 的 wget 命令。
画面 2: 展示了 Apache Flink 官网的下载页面，确认了 Flink 1.9.1 是最新的稳定版本，并列出了可供下载的文件。
画面 3: 展示了下载的 Flink 1.9.1-bin-scala_2.12.tgz 文件在 Windows 资源管理器中的位置。
画面 4: 展示了 Flink Web Dashboard 的“Running Jobs”页面，但内容为空。
画面 5: 展示了 Flink Web Dashboard 的“Job Manager”页面，准备提交新作业。
画面 6: 在 Linux 终端中，显示了已下载的 Flink 1.9.1-bin-scala_2.12.tgz 文件，并执行了 tar 命令解压。
画面 7: 展示了 Flink 配置文件 flink-conf.yaml 的部分内容，包括 JobManager 和 TaskManager 的堆内存设置。
画面 8: 展示了 flink-conf.yaml 文件中关于 Kerberos 安全配置的部分。
画面 9: 在终端中，显示了正在执行的命令，但内容为空。
画面 10: 在终端中，执行了 start-cluster.sh 命令，启动了 Flink Standalone 集群。
画面 11: 展示了浏览器访问本地 IP 地址 172.17.0.143:8081 的页面，但显示的是一个商业网站的首页。
画面 12: 展示了 Flink Web Dashboard 的“Overview”页面，显示了可用任务槽位和运行作业状态。
画面 13: 展示了 Flink 官方文档中关于修改环境变量和配置文件 flink-conf.yaml 的说明。
画面 14: 展示了 flink-conf.yaml 文件中关于 JobManager 和 TaskManager 的 IP 地址、端口、堆内存等配置项。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```bash
[root@node2-vmb6 opt]# cd /opt
[root@node2-vmb6 opt]# wget -c http://mirrors.tuna.tsinghua.edu.cn/apache/flink/flink-1.9.1/flink-1.9.1-bin-scala_2.12.tgz
```
画面 6:
```bash
[root@node2-vmb6 opt]# tar xf flink-1.9.1-bin-scala_2.12.tgz
```
画面 7:
```yaml
# The heap size for the JobManager JVM
jobmanager.heap.size: 1024m

# The heap size for the TaskManager JVM
taskmanager.heap.size: 1024m

# The number of task slots that each TaskManager offers. Each slot runs one parallel pipeline.
taskmanager.numberOfTaskSlots: 1

# The parallelism used for programs that did not specify and other parallelism.
parallelism.default: 1
```
画面 8:
```yaml
# Flink Cluster Security Configuration

# Kerberos authentication for various components: Hadoop, ZooKeeper, and connectors
# may be enabled in four steps:
# 1. configure the local xdb.conf file
# 2. provide Kerberos credentials (either a keytab or a ticket cache w/ kinit)
# 3. Make the credentials available to various JAAS login contexts
# 4. configure the connector to use JAAS/SASL

# The below configure how Kerberos credentials are provided. A keytab will be used instead of
# a ticket cache if the keytab path and principal are set.
# security.kerberos.login.use-ticket-cache: true
# security.kerberos.login.keytab: /path/to/kerberos/keytab
```
画面 10:
```bash
[root@node2-vmb6 bin]# ./start-cluster.sh
Starting cluster.
Starting standalone session daemon on host node2-vmb6.yyy.
```
画面 13:
```bash
1) 修改环境变量，vi /etc/profile,添加以下内容
export FLINK_HOME=/opt/flink-1.9.1/
export PATH=$FLINK_HOME/bin:$PATH

2) 修改配置文件 flink-conf.yaml,
cd /opt/flink-1.9.1/conf
vim flink-conf.yaml

# 主要修改的位置有：
jobmanager.rpc.address: 172.17.0.143
taskmanager.numberofTaskSlots: 2
parallelism.default: 4
```
画面 14:
```yaml
# JobManager 的IP地址
jobmanager.rpc.address: 172.17.0.143

# JobManager 的端口号
jobmanager.rpc.port: 6123

# JobManager JVM heap 内存大小
jobmanager.heap.size: 1024m

# TaskManager JVM heap 内存大小
taskmanager.heap.size: 1024m

# 每个 TaskManager 提供的任务 slots 数量大小，默认为1
taskmanager.numberOfTaskSlots: 1
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.5 安装配置”，内容包括“Flink 的运行一般分为三种模式：Local、Standalone、On Yarn”。
画面 13: PPT 标题为“1.5 安装配置”，内容包括“1) 修改环境变量，vi /etc/profile,添加以下内容”和“2) 修改配置文件 flink-conf.yaml”。
画面 14: PPT 标题为“1.5 安装配置”，内容包括“# 主要修改的位置有：”和“# JobManager 的IP地址”等配置项。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
