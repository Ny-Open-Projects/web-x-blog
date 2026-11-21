# 画面线理解：11-sqoop安装

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\11-sqoop安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:30, 00:56, 01:17, 01:42, 02:26, 02:44, 03:23, 03:49, 04:17, 04:30, 04:48, 04:58, 05:12, 05:25
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:32:35

1) 这一组画面整体在讲什么（一句话）：
演示如何在Linux服务器上安装并配置Sqoop工具，包括下载解压、修改配置文件和添加依赖包。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Sqoop安装章节，列出下载地址和解压命令。
画面2：在SecureCRT中，用户正在传输sqoop-1.4.7.bin_hadoop-2.6.0.tar.gz文件。
画面3：在SecureCRT中，用户列出并进入sqoop解压后的目录。
画面4：在SecureCRT中，用户进入sqoop的scripts目录。
画面5：在SecureCRT中，用户进入sqoop的conf目录。
画面6：在SecureCRT中，用户进入Hadoop的mapreduce目录。
画面7：在SecureCRT中，显示Hadoop环境变量配置文件的开头部分。
画面8：在SecureCRT中，用户正在编辑Hadoop环境变量配置文件，设置HIVE_HOME。
画面9：在SecureCRT中，用户完成编辑并保存了sqoop-env.sh配置文件。
画面10：在SecureCRT中，用户正在使用rz命令传输文件，弹出Zmodem传输窗口。
画面11：展示PPT页面，说明Sqoop需要添加mysql和java-json的依赖包，并给出验证启动命令。
画面12：展示PPT页面，说明Sqoop需要添加mysql和java-json的依赖包，并给出验证启动命令。
画面13：在SecureCRT中，用户进入sqoop的lib目录。
画面14：在SecureCRT中，用户执行sqoop-version命令，显示Sqoop版本信息和警告信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
http://archive.apache.org/dist/sqoop/1.4.7
http://archive.apache.org/dist/sqoop/1.4.7_bin_hadoop-2.6.0.tar.gz
http://archive.apache.org/dist/sqoop/1.99.6/sqoop-1.99.6-bin_hadoop200.tar.gz
我们这里使用sqoop1的版本，下载之后上传到/export/export/software目录下，然后进行解压
cd /export/servers/hadoop-3.1.1/conf

画面2：
rz waiting to receive.
Transferring sqoop-1.4.7.bin_hadoop-2.6.0 (1).tar.gz...

画面3：
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/bin/hive.cmd
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/createOnlyImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/customOverwriteImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/decimalMapImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/failingImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/fieldWithNewlineImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/incrementalHiveAppend10.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/incrementalHiveAppend20.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/incrementalHiveAppendEmpty.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/normalImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/numericImport.q
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/partitionImport.q

画面4：
sqoop-1.4.7.bin_hadoop-2.6.0/testdata/hive/scripts/partitionImport.q
[root@node03 software]# cd ../servers/
[root@node03 servers]# ls
apache-flume-1.8.0-bin
azkaban-solo-server-0.1.0-SNAPSHOT.tar.gz
azkaban-web-server-0.1.0-SNAPSHOT.tar.gz
azkaban-exec-server-0.1.0-SNAPSHOT.tar.gz
create-all-sql-0.1.0-SNAPSHOT.sql
sqoop-1.4.7.bin_hadoop-2.6.0
hadoop-3.1.1-bin
hive sql
taillog
zookeeper-3.4.9

画面5：
[root@node03 servers]# cd /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/
[root@node03 sqoop-1.4.7.bin_hadoop-2.6.0]# cd conf/
[root@node03 conf]# ls
oraop-site-template.cmd
sqoop-env-template.sh
sqoop-site.xml
sqoop-env.sh

画面6：
[root@node03 share]# cd hadoop/
[root@node03 hadoop]# s
-bash: s: command not found
[root@node03 hadoop]# ls
client common hdfs mapreduce tools yarn
[root@node03 mapreduce]# ls
hadoop-mapreduce-client-shuffle-3.1.1.jar
hadoop-mapreduce-client-3.1.1.jar
hadoop-mapreduce-client-core-3.1.1.jar
hadoop-mapreduce-client-hs-plugins-3.1.1.jar
hadoop-mapreduce-client-jobclient-3.1.1-tests.jar
hadoop-mapreduce-client-nativetask-3.1.1.jar

画面7：
# limitations under the License.
# included in all the hadoop scripts with source command
# should not be executable directly
# also should not be passed any arguments, since we need original $*
# Set Hadoop-specific environment variables here.
#Set path to where bin/hadoop is available
export HADOOP_COMMON_HOME=/export/servers/hadoop-3.1.1
#Set path to where hadoop-*core.jar is available
export HADOOP_MAPRED_HOME=/export/servers/hadoop-3.1.1
#Set the path to where bin/hbase is available
#export HBASE_HOME=

画面8：
# should not be executable directly
# also should not be passed any arguments, since we need original $*
# Set Hadoop-specific environment variables here.
#Set path to where bin/hadoop is available
export HADOOP_COMMON_HOME=/export/servers/hadoop-3.1.1
#Set path to where hadoop-*core.jar is available
export HADOOP_MAPRED_HOME=/export/servers/hadoop-3.1.1
#Set the path to where bin/hbase is available
#export HBASE_HOME=
#Set the path to where bin/hive is available
export HIVE_HOME=

画面9：
#Set the path to where bin/hive is available
export HIVE_HOME=/export/servers/apache-hive-3.1.1-bin
"sqoop-env.sh" 35L, 1435C written
[root@node03 conf]#

画面11：
mysql-connector-java-5.1.40.jar
java-json.jar
将这两个jar也添加到sqoop的lib目录下
4、验证启动
cd /export/servers/sqoop-1.4.6-cdh5.14.0
bin/sqoop-version

画面14：
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../hbase does not exist! HBase imports will fail.
Please set $HBASE_HOME to the root of your HBase installation.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../hcatalog does not exist! HCatalog jobs will fail.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../accumulo does not exist! Accumulo imports will fail.
Please set $ACCUMULO_HOME to the root of your Accumulo installation.
Warning: /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/bin/../zookeeper does not exist! Accumulo imports will fail.
Please set $ZOOKEEPER_HOME to the root of your Zookeeper installation.
2019-05-12 19:57:59,375 INFO sqoop: Sqoop: Running Sqoop version: 1.4.7
git commit id 2328971411f57f0cb683db79d44d195d88
Compiled by maugli on Thu Dec 21 15:59:58 STD 2017

4) 出现的 PPT 标题、架构图/流程图
