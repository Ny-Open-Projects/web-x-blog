# 画面线理解：8-Hive的安装-Hive配置

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\8-Hive的安装-Hive配置【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:40, 00:54, 01:13, 01:40, 02:08, 02:25, 02:33, 02:40, 03:11, 03:28, 03:38, 03:58, 04:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:47:39

1) 这一组画面整体在讲什么（一句话）：
在 Linux 系统中配置和修改 Hive 环境变量文件 hive-env.sh，以适配 Hadoop 环境并调整 JVM 堆内存大小。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了课程视频的抽帧画面，左侧是课程目录结构，包含“Hive 基础”、“Hive 的元数据管理”等章节。
- 右侧是文本编辑器，显示了“第三步：修改hive的配置文件”和“第四步：进入mysql的客户端然后进行授权”的说明。
- 文本编辑器中包含以下代码：
  ```
  grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
  flush privileges;
  ```
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

画面 2：
- 展示了 SecureCRT 会话窗口，用户在节点 node03 上执行了命令：
  ```
  [root@node03 ~]# ls /export/servers/
  apache-hive-3.1.1-bin/ hadoop-3.1.1/ jdk1.8.0_141/ zookeeper-3.4.9/
  [root@node03 ~]# cd /export/servers/apache-hive-3.1.1-bin/
  [root@node03 conf]# ls
  bin  binar-package  licenses  conf  examples  hostlog  jdb  lib  LICENSE  NOTICE  RELEASE_NOTES.txt  script
  beeline-log4j2.properties  hive-default.xml.template  hive-env.sh.template  hive-log4j2.properties.template
  hive-exec-log4j2.properties.template  ivysettings.xml  llap-cli-log4j2.properties.template  llap-daemon-log4j2.properties.template
  parquet-logging.properties
  [root@node03 conf]# cp hive-env.sh.template hive-env.sh
  ```

画面 3：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 hive-env.sh 文件内容：
  ```
  # if [ -z "$SDEBUG" ]; then
  # export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
  -XX:+UseParNewGC -XX:+UseGCOverheadLimit"
  # else
  # export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
  -XX:+UseGCOverheadLimit"
  # fi
  # The heap size of the jvm stared by hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for hive server.
  ```
- 窗口底部显示了编辑状态：46, 0-1 78%。

画面 4：
- 展示了 SecureCRT 会话窗口，显示了空的终端界面，仅包含提示符“^C”和“^C”。
- 顶部显示了多个会话标签，包括 192.168.174.120、192.168.174.120、192.168.174.120（第三个为未激活状态）。

画面 5：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 hive-env.sh 文件内容：
  ```
  # The heap size of the jvm stared by hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for hive server.
  # Set HADOOP_HOME to point to a specific hadoop install directory
  HADOOP_HOME=/export/servers/hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  # export HIVE_CONF_DIR=
  # Folder containing extra libraries required for hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：48, 18 Bot。

画面 6：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 hive-env.sh 文件内容：
  ```
  # The heap size of the jvm stared by hive shell script can be controlled via:
  # export HADOOP_HEAPSIZE=1024
  # Larger heap size may be required when running queries over large number of files or partitions.
  # By default hive shell scripts use a heap size of 256 (MB). Larger heap size would also be
  # appropriate for hive server.
  # Set HADOOP_HOME to point to a specific hadoop install directory
  HADOOP_HOME=/export/servers/hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  export HIVE_CONF_DIR=/export/servers/apache-hive-3.1.1-bin/conf
  # Folder containing extra libraries required for hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：54L, 2413C written。
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

画面 7：
- 展示了 SecureCRT 会话窗口，显示了编辑后的 hive-site.xml 文件内容：
  ```
  # Set HADOOP_HOME to point to a specific hadoop install directory
  HADOOP_HOME=/export/servers/hadoop-3.1.1/
  # Hive Configuration Directory can be controlled by:
  # export HIVE_CONF_DIR=
  export HIVE_CONF_DIR=/export/servers/apache-hive-3.1.1-bin/conf
  # Folder containing extra libraries required for hive compilation/execution can be controlled by:
  # export HIVE_AUX_JARS_PATH=
  ```
- 窗口底部显示了编辑状态：54L, 2413C written。
- 同时显示了两个 SecureCRT 会话窗口，分别连接到 192.168.174.120 和 192.168.174.120（第二个窗口为未激活状态）。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1：
```
grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
flush privileges;
```

画面 2：
```
[root@node03 ~]# ls /export/servers/
apache-hive-3.1.1-bin/ hadoop-3.1.1/ jdk1.8.0_141/ zookeeper-3.4.9/
[root@node03 ~]# cd /export/servers/apache-hive-3.1.1-bin/
[root@node03 conf]# ls
bin  binar-package  licenses  conf  examples  hostlog  jdb  lib  LICENSE  NOTICE  RELEASE_NOTES.txt  script
beeline-log4j2.properties  hive-default.xml.template  hive-env.sh.template  hive-log4j2.properties.template
hive-exec-log4j2.properties.template  ivysettings.xml  llap-cli-log4j2.properties.template  llap-daemon-log4j2.properties.template
parquet-logging.properties
[root@node03 conf]# cp hive-env.sh.template hive-env.sh
```

画面 3：
```
# if [ -z "$SDEBUG" ]; then
# export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
-XX:+UseParNewGC -XX:+UseGCOverheadLimit"
# else
# export HADOOP_OPTS="$SHADOOP_OPTS -XX:NewRatio=12 -Xms10m -XX:MaxHeapFreeRatio=40 -XX:MinHeapFreeRatio=15
-XX:+UseGCOverheadLimit"
# fi
#
