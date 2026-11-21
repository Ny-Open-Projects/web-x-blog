# 画面线理解：16-HDFS的API操作-访问权限问题

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\16-HDFS的API操作-访问权限问题【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:55, 02:45, 03:26, 04:19, 05:25, 06:18, 06:58, 07:36, 08:21, 09:07, 09:54, 10:54, 11:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 03:29:09

1) 这一组画面整体在讲如何通过修改Hadoop配置文件hdfs-site.xml启用文件权限控制，并演示了因权限不足导致的文件下载失败案例。

2) 按时间顺序列出每张画面的要点：
画面1：显示HDFS文件系统浏览器界面，列出根目录下的文件，包括a.txt、app、export、hello.txt、test、timer.txt、tmp、user等文件，所有文件的Owner和Group信息可见。
画面2：IDEA中显示Java代码，演示如何通过FileSystem对象下载HDFS文件到本地，代码中使用了URI("hdfs://node01:8020")。
画面3：SecureCRT终端中显示hdfs-site.xml配置片段，包含dfs.replication=3、dfs.permissions.enabled=false、dfs.namenode.checkpoint.edits.dir配置，以及执行了chmod命令修改timer.txt权限。
画面4：SecureCRT终端中显示cd进入hadoop-3.1.1/sbin目录，执行了ls命令列出脚本文件，随后执行了jps命令查看进程，显示了NameNode、DataNode等进程。
画面5：SecureCRT终端中显示cd进入etc/hadoop目录，ls命令列出配置文件，其中hdfs-site.xml被高亮选中。
画面6：SecureCRT终端中显示scp命令将hdfs-site.xml复制到node02和node03节点，随后cd ..并执行ls命令。
画面7：SecureCRT终端中显示在node02节点上执行jps命令，输出了DataNode进程信息。
画面8：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“Process finished with exit code -1”。
画面9：SecureCRT终端中显示启动SecondaryNameNode、NameNode、ResourceManager、NodeManager等进程，随后执行hdfs dfs -chmod命令。
画面10：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“AccessControlException: Permission denied: user=ift, access=READ, inode='timer.txt':root:supergroup:rw-------”。
画面11：IDEA中显示Java代码，演示下载文件，但运行结果提示测试失败，错误信息显示“AccessControlException: Permission denied: user=ift, access=READ, inode='timer.txt':root:supergroup:rw-------”。
画面12：HDFS文件系统浏览器界面，显示文件列表，其中timer.txt的Owner为root。
画面13：HDFS文件系统浏览器界面，显示文件列表，其中timer.txt的Owner为root。
画面14：SecureCRT终端中显示hdfs-site.xml配置片段，其中dfs.permissions.enabled被修改为true，随后执行了scp命令将配置文件复制到node02和node03节点。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面3：
```xml
<value>node01:50070</value>
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
<value>file:///export/servers/hadoop-3.1.1/datafs/nm/snn/edits</value>
</property>
```
画面5：
```bash
[root@node01 hadoop-3.1.1]# ls
capacity-scheduler.xml httpfs-log4j.properties mapred-site.xml
configuration.xml httpfs-site.xml ssl-client.xml.example
core-site.xml kms-acls.xml ssl-server.xml.example
hadoop-env.cmd kms-log4j.properties user_ec_policies.xml.template
hadoop-env.sh kms-site.xml yarn-env.cmd
hadoop-metrics2.properties log4j.properties yarn-env.sh
hadoop-policy.xml mapred-env.cmd yarn-service-log4j.properties
hdfs-site.xml mapred-queues.xml.template yarn-site.xml
```
画面6：
```bash
"hd fs-site.xml" 65L, 2031C written
[root@node01 hadoop]# scp hdfs-site.xml node02:$PWD
100% 2031 2.0KB/s 00:00
[root@node01 hadoop]# scp hdfs-site.xml node03:$PWD
100% 2031 2.0KB/s 00:00
[root@node01 etc]# ls
abc.txt a.txt bin dates etc include lib libexec LICENSE.txt logs NOTICE.txt README.txt sbin share
```
画面14：
```xml
<value>node01:50070</value>
<property>
<name>dfs.replication</name>
<value>3</value>
</property>
<property>
<name>dfs.permissions.enabled</name>
<value>true</value>
</property>
<property>
<name>dfs.namenode.checkpoint.edits.dir</name>
<value>file:///export/servers/hadoop-3.1.1/datafs/nm/snn/edits</value>
</property>
```

4) PPT 标题、架构图/流程图的结构、表格数据：
无

5) 画面里出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无
