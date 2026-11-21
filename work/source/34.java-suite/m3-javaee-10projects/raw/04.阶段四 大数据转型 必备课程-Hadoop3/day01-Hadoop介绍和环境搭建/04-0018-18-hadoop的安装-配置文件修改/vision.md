# 画面线理解：18-hadoop的安装-配置文件修改

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\18-hadoop的安装-配置文件修改【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:51, 02:45, 03:13, 05:00, 07:38, 08:53, 09:16, 09:55, 10:49, 11:26, 12:25, 13:39, 14:32
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:44:18

1) 这一组画面整体在讲什么（一句话）：
配置 Hadoop 集群环境，包括修改核心配置文件、设置环境变量和创建必要的目录结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Hadoop 配置文件 configuration.xml 的开头部分，包含 XML 声明和 Apache 许可证信息。
画面2：展示 Hadoop 环境脚本 hadoop-env.sh 的部分内容，包含设置 HADOOP_OS_TYPE 和 HADOOP_OPTS 的逻辑。
画面3：展示 Typora 中的 Hadoop 安装文档，内容为“hadoop-env.sh”和“hdfs-site.xml”的配置说明。
画面4：展示 hdfs-site.xml 文件中配置 namenode 和 datanode 的数据目录。
画面5：展示 hdfs-site.xml 文件中配置 dfs.replication 和 dfs.permissions.enabled。
画面6：展示 Typora 中的 Hadoop 安装文档，内容为“mapred-site.xml”的配置说明。
画面7：展示 mapred-site.xml 文件中配置 mapreduce 的内存和任务参数。
画面8：展示 Typora 中的 Hadoop 安装文档，内容为“yarn-site.xml”的配置说明。
画面9：展示 yarn-site.xml 文件中配置 YARN 的日志聚合和资源参数。
画面10：展示 Typora 中的 Hadoop 安装文档，内容为“创建数据和临时文件夹”和“分发安装包到其它机器”的步骤。
画面11：在 SecureCRT 中执行命令，创建 Hadoop 各个组件所需的目录。
画面12：在 SecureCRT 中尝试从镜像站点下载 Hadoop 安装包，但连接被拒绝。
画面13：在 SecureCRT 中设置环境变量，包括 JAVA_HOME、HADOOP_HOME 和 PATH。
画面14：在 SecureCRT 中在 node03 上执行 source /etc/profile 命令，使环境变量生效。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. See accompanying LICENSE file.
<!-- Put site-specific property overrides in this file. -->
</configuration>
```

画面2：
```bash
export HADOOP_OS_TYPE=$(uname -s)
case $HADOOP_OS_TYPE in
Darwin*)
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.realm="
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.kdc="
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.security.krb5.conf="
;;
```

画面3：
```bash
export JAVA_HOME=/export/servers/jdk1.8.0_141
```

画面4：
```xml
<configuration>
<property>
<name>dfs.namenode.name.dir</name>
<value>file:///export/servers/hadoop-3.1.1/data/namenode/namenodedatas</value>
</property>
<property>
<name>dfs.namenode.handler.count</name>
<value>10</value>
</property>
<property>
<name>dfs.datanode.data.dir</name>
<value>file:///export/servers/hadoop-3.1.1/data/datanode/datanodedatas</value>
</property>
<property>
<name>dfs.namenode.http.address</name>
<value>node01.hadoop.com:50070</value>
</property>
</configuration>
```

画面5：
```xml
<property>
<name>dfs.replication</name>
<value>3</value>
</property>
<property>
<name>dfs.permissions.enabled</name>
<value>false</value>
</property>
<property>
<name>dfs.namenode.checkpoint.edits.dir</name>
<value>file:///export/servers/hadoop-3.1.1/data/dfs/nn/snn/edits</value>
</property>
<property>
<name>dfs.namenode.secondary.http-address</name>
<value>node01.hadoop.com:50090</value>
</property>
<property>
<name>dfs.namenode.checkpoint.dir</name>
<value>file:///export/servers/hadoop-3.1.1/data/dfs/snn/name</value>
</property>
```

画面6：
```xml
<configuration>
<property>
<name>mapreduce.framework.name</name>
<value>yarn</value>
</property>
<property>
<name>mapreduce.map.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.reduce.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.map.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.reduce.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.task.io.sort.mb</name>
<value>256</value>
</property>
<property>
<name>mapreduce.task.io.sort.factor</name>
<value>100</value>
</property>
<property>
<name>mapreduce.reduce.shuffle.parallelcopies</name>
<value>25</value>
</property>
<property>
<name>mapreduce.jobhistory.address</name>
<value>node01.hadoop.com:10020</value>
</property>
</configuration>
```

画面7：
```xml
<property>
<name>mapreduce.reduce.memory.mb</name>
<value>1024</value>
</property>
<property>
<name>mapreduce.reduce.java.opts</name>
<value>-Xmx512M</value>
</property>
<property>
<name>mapreduce.task.io.sort.mb</name>
<value>256</value>
</property>
<property>
<name>mapreduce.task.io.sort.factor</name>
<value>100</value>
</property>
<property>
<name>mapreduce.reduce.shuffle.parallelcopies</name>
<value>25</value>
</property>
<property>
<name>mapreduce.jobhistory.address</name>
<value>node01.hadoop.com:10020</value>
</property>
```

画面8：
```xml
<property>
<name>yarn.nodemanager.vmem-check-enabled</name>
<value>false</value>
</property>
<property>
<name>yarn.nodemanager.resource.memory-mb</name>
<value>1024</value>
</property>
<property>
<name>yarn.nodemanager.resource.detect.hardware.capabilities</name>
<value>true</value>
</property>
<property>
<name>yarn.nodemanager.local-dirs</name>
<value>file:///export/servers/hadoop-3.1.1/data/nodemanager/nodemanagerDatas</value>
</property>
<property>
<name>yarn.nodemanager.log-dirs</name>
<value>file:///export/servers/hadoop-3.1.1/data/nodemanager/nodemanagerLogs</value>
</property>
<property>
<name>yarn.nodemanager.log.retain-seconds</name>
<value>10000</value>
</property>
```

画面9：
```xml
<property>
<name>yarn.nodemanager.remote-app-log-dir</name>
<value>/export/servers/hadoop-3.1.1/data/remoteAppLogs</value>
</property>
<property>
<name>yarn.nodemanager.remote-app-log-dir-suffix</name>
<value>logs</value>
</property>
<property>
<name>yarn.nodemanager.aux-services</name>
<value>mapreduce_shuffle</value>
</property>
<property>
<name>yarn.log-aggregation.retain-seconds</name>
<value>18144000</value>
</property>
<property>
<name>yarn.log-aggregation.retain-check-interval-seconds</name>
<value>86400</value>
</property>
<property>
<name>yarn.app.mapreduce.am.resource.mb</name>
<value>1024</value>
</property>
```

画面10：
```text
3. 创建数据和临时文件夹
mkdir -p /export/servers/hadoop-3.1.1/data/dfs/nn/snn/edits
mkdir -p /export/servers/hadoop-3.1.1/data/namenode/namenodedatas
mkdir -p /export/servers/hadoop-3.1.1/data/datanode/datanodedatas
mkdir -p /export/servers/hadoop-3.1.1
