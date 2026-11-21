# 画面线理解：06.搭建Spark集群（实施部署）

- 阶段：07.阶段七 探花交友项目
- 章节：day06 探花交友-Spark快速入门
- 源文件：07.阶段七 探花交友项目\day06 探花交友-Spark快速入门\06.搭建Spark集群（实施部署）_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:40, 01:06, 01:36, 02:10, 02:59, 04:31, 04:53, 05:39, 06:02, 06:42, 08:08, 09:13, 10:35
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 20:21:06

1) 这一组画面整体在讲什么（一句话）：
在三台服务器上配置并启动 Spark 集群，包括 SSH 密钥免密登录、解压安装包、配置环境变量和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：执行 ssh-copy-id 命令，将本地公钥复制到 node2 和 node3，用于免密登录。
画面2：展示 Typora 中的 Spark 快速入门文档，内容为 Spark 安装步骤，包括创建目录、解压 tar 包、移动配置文件等。
画面3：在终端中执行 cd /itcast/ 命令，进入 itcast 目录。
画面4：在终端中执行 tar -xvf spark-2.4.3-bin-hadoop2.7.tar.gz 命令，解压 Spark 安装包。
画面5：在终端中执行 tar 命令，解压 Spark 安装包中的数据文件。
画面6：在终端中查看 spark-env.sh 文件内容，显示 Apache Spark 的许可证信息。
画面7：在终端中执行 mv spark-env.sh.template spark-env.sh 和 mv slaves.template slaves 命令，将模板文件重命名为配置文件。
画面8：在终端中执行 vim /etc/profile 命令，编辑系统环境变量配置文件。
画面9：在终端中执行 vim /etc/profile 命令，编辑系统环境变量配置文件，设置 JAVA_HOME、CLASSPATH 和 PATH。
画面10：在终端中执行 vim /etc/profile 命令，编辑系统环境变量配置文件，设置 JAVA_HOME、CLASSPATH 和 PATH。
画面11：在终端中执行 cd spark/sbin 命令，进入 Spark 的 sbin 目录。
画面12：在 Typora 中展示 Spark 快速入门文档，内容为启动 Spark 集群的命令。
画面13：桌面显示“黑马程序员”和“博学谷”的标志。
画面14：在 Typora 中展示 Spark 快速入门文档，内容为启动 Spark 集群的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
# 创建安装目录，3台机器都要创建
mkdir /itcast
# 上传spark-2.4.3-bin-hadoop2.7.tar.gz 到目录，进行解压
tar -xvf spark-2.4.3-bin-hadoop2.7.tar.gz
mv spark-2.4.3-bin-hadoop2.7 spark
# 配置环境变量
cd spark/conf
mv spark-env.sh.template spark-env.sh
vim spark-env.sh
# 在上面插入如下信息
export JAVA_HOME=/usr/local/src/java/jdk1.8.0_141 #jdk地址
export SPARK_MASTER_HOST=node1 #指定master的主机名
export SPARK_MASTER_PORT=7077 #master的端口

画面7：
[root@itcast conf]# mv spark-env.sh.template spark-env.sh
[root@itcast conf]# mv slaves.template slaves

画面8：
if [ $UID -gt 199 ] && [ "/usr/bin/id -gn" = "/usr/bin/id -un" ]; then
umask 022
else
umask 022
fi
for i in /etc/profile.d/*.sh; do
if [ -r "$i" ]; then
if [ "${#i}" != "$i" ]; then
else
"$i" > /dev/null 2>&1
fi
fi
done
unset i
unset -f pathmunge
#set java environment
JAVA_HOME=/usr/local/src/java/jdk1.8.0_141
CLASSPATH=.:$JAVA_HOME/lib/tools.jar
PATH=$JAVA_HOME/bin:$PATH
export JAVA_HOME CLASSPATH PATH

画面9：
#set java environment
JAVA_HOME=/usr/local/src/java/jdk1.8.0_141
CLASSPATH=.:$JAVA_HOME/lib/tools.jar
PATH=$JAVA_HOME/bin:$PATH
export JAVA_HOME CLASSPATH PATH

画面11：
[root@itcast spark]# cd spark/sbin

画面12：
# 启动
cd /itcast/spark/sbin
./start-all.sh

画面14：
# 启动
cd /itcast/spark/sbin
./start-all.sh

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“Spark 快速入门.md”，内容包括 Spark 概述、为什么选择 Spark、Spark 的特点、环境准备、配置安装等章节。
画面12：PPT 标题为“Spark 快速入门.md”，内容包括 Spark 概述、为什么选择 Spark、Spark 的特点、环境准备、配置安装等章节。
画面14：PPT 标题为“Spark 快速入门.md”，内容包括 Spark 概述、为什么选择 Spark、Spark 的特点、环境准备、配置安装等章节。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
