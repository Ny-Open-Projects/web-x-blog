# 画面线理解：17-hadoop的安装-准备工作

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day01-Hadoop介绍和环境搭建
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day01-Hadoop介绍和环境搭建\17-hadoop的安装-准备工作【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:14, 01:20, 01:27, 01:33, 01:38, 02:04, 02:15, 03:03, 04:47, 04:59, 05:08, 05:17, 05:34, 05:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 02:41:18

1) 这一组画面整体在讲什么（一句话）：
演示 Hadoop 3.1.1 版本的安装过程，重点是上传解压、修改配置文件（core-site.xml 和 hdfs-site.xml）以及 YARN 的配置（yarn-site.xml）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Typora 文档，内容为“8.2 Hadoop的安装”章节，列出安装步骤：上传并解压、修改配置文件、分发安装包、格式化HDFS、启动集群。其中“上传并解压”步骤下有命令：cd /export/software 和 tar zxvf hadoop-3.1.1.tar.gz -C ../servers。
画面 2: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的客户端 jar 包路径列表。
画面 3: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的共享缓存管理器相关文档路径。
画面 4: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的 ResourceManager API 文档路径。
画面 5: SecureCRT 会话窗口，显示 Hadoop 3.1.1 的 ResourceManager 预留资源相关 API 文档路径。
画面 6: SecureCRT 会话窗口，显示在 node01 节点上，用户进入 /servers/hadoop-3.1.1/ 目录并列出其内容。
画面 7: Typora 文档，内容与画面 1 相同，展示“8.2 Hadoop的安装”章节。
画面 8: Notepad++ 编辑器界面，显示“Plugin Manager”菜单项，用于管理插件。
画面 9: Notepad++ 编辑器界面，显示远程连接到 192.168.174.100 的文件目录结构，包含多个 Hadoop 配置文件。
画面 10: Notepad++ 编辑器界面，显示 core-site.xml 文件内容，包含 Apache License 2.0 的声明和注释“Put site-specific property overrides in this file.”。
画面 11: Typora 文档，展示 core-site.xml 文件内容，其中包含 <property> 标签对，如 <name>fs.defaultFS</name> 和 <value>hdfs://node01:8020</value>。
画面 12: Typora 文档，展示 hdfs-site.xml 文件内容，包含 <property> 标签对，如 <name>dfs.namenode.name.dir</name> 和 <value>file:///export/hadoop/data/namenodedatas</value>。
画面 13: Typora 文档，展示 yarn-site.xml 文件内容，包含 <property> 标签对，如 <name>yarn.resourcemanager.address</name> 和 <value>node01:8032</value>。
画面 14: Notepad++ 编辑器界面，显示 core-site.xml 文件内容，与画面 10 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
1. 上传并解压
2. 修改配置文件
3. 分发安装包
4. 格式化HDFS
5. 启动集群
1. 上传并解压
1. 上传压缩包到/export/software目录
2. cd /export/software
3. tar zxvf hadoop-3.1.1.tar.gz -C ../servers
画面 6:
[root@node01 software]# cd ../servers/
[root@node01 servers]# cd hadoop-3.1.1/
[root@node01 hadoop-3.1.1]# ls
bin  etc  include  lib  LICENSE.txt  NOTICE.txt  README.txt  sbin  share
[root@node01 etc]# cd hadoop/
[root@node01 hadoop]#
画面 11:
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://node01:8020</value>
  </property>
</configuration>
画面 12:
<configuration>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///export/hadoop/data/namenodedatas</value>
  </property>
  <property>
    <name>dfs.blocksizet</name>
    <value>134217728</value>
  </property>
  <property>
    <name>dfs.namenode.handler.count</name>
    <value>18</value>
  </property>
</configuration>
画面 13:
<configuration>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>node01:8032</value>
  </property>
  <property>
    <name>yarn.resourcemanager.scheduler.address</name>
    <value>node01:8030</value>
  </property>
  <property>
    <name>yarn.resourcemanager.resource-tracker.address</name>
    <value>node01:8031</value>
  </property>
  <property>
    <name>yarn.resourcemanager.admin.address</name>
    <value>node01:8033</value>
  </property>
  <property>
    <name>yarn.resourcemanager.webapp.address</name>
    <value>node01:8088</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>node01</value>
  </property>
  <property>
    <name>yarn.scheduler.minimum-allocation-mb</name>
    <value>1024</value>
  </property>
</configuration>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
