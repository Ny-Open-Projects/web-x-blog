# 13-sqoop导入-hive

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\13-sqoop导入-hive【海量资源尽在 ubkz.com】.mp4
- 时长 6分44秒（音频 404s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习将关系表的数据导入Hive那么要做这么一件事首先第一步我们需要将一个jar 包导到这个Scoop的Lab下面哪个jar 包呢在这个Hive它的一个lib下面有一个Hive.exe点架来我们来找一下那么回到我们这个服务器在Export Service下面Apache然后Hive进来进来之后进入lib
[00:30] 在这里有一个有一个什么呢有一个Hive exe我们来找一下Hive向上翻Hive exe来看一下看到了在这个位置我们需要把它拷贝过来拷贝到哪里去呢我们来看一下要拷贝scope的lib下面去来我们来做一下拷贝一个Hive exe.com.exe的servicescopelib下面
[01:03] 好考过来好考过来之后呢接下来我们就可以执行了来回到我们刚才这个scope下面接下来我们来执行一个命令这个命令是这样的在这个把这个数据导到Hive之前呢我们先要在这个mycircle里边呢先要在这个这个Hive里边呢创建对应的数据库和对应的表那我们先进到Hive里面去来在这里我们export Service apache
[01:32] 好在这里输个binhive进到Hive的一个命令行进来之后呢我们在这里呢需要建一个数据库create databasescope to Hive好先在这里建一个数据库好建完数据库之后呢接下来我们再创建一张表再去使用这个数据库然后再创建一张表use稍等我来一下叫usescope to Hive
[02:09] 好然后呢在这里边创建一张表create external创建一个web表这个表的名字叫emp-Hive这个表呢有1 2 3 4 5 5个字段然后它的行分格符呢这个地方呢是-001这个-001呢其实是Hive中末的一个分格符这个分格符非常特殊我们是通过键盘的通过一次键盘的一个敲击呢是打不出这个字符的所以说呢这个我们来
[02:38] 创建这张表拿到这里走这个表的名字记着叫EMPHEV来稍等这个表创建成功了好创建成功之后呢我们来开始进行数据的导入怎么导呢向下看第三步我们来开始导入来看这个这个名BIN SCOPE我们要导入那么这个地方连接我们这个数据库而且连接这个这台主机上面这个数据库用户名ROT密码ROT
[03:10] 这个表呢叫EMPEMP这个表那这个EMP表的话呢这个行分格符是-001好 重点是在后面这个地方我们导入Hive是--Hive import表示我要导入到Hive上面去好 Hive的table就是Hive的表呢Hive上面的表是谁呢是scope2hive这个数据库下面的这张表注意这个是我们mycircle的表而这个是Hive的表
[03:39] 这个杠杠haveoverwrite呢表示数据覆盖而这个delete target的dr表示如果目标目录已经存在把它删掉最后这个杠m1呢表示启动一个map taskok这是整个命令我们把它复制一下来我们来运行那么运行的时候呢我们需要进到这个scope里边来在这里直接回车稍等我们让它来执行好稍等它开始启动
[04:11] myproduce好了我们的程序执行结束结束完之后呢它已经导到我们的Hive里面了我们去Hive中查看一下好进入这个里面我们来Hive里面我们先呢去show一些table4好在这里有一个emp have表我们来查一下看数据有没有过来select from emp have走稍等哎你看数据是不是全部导进来了
[04:45] 这个数据呢其实就是我们原始里边EMP中的数据OK这个导入成功那接下来我们再继续看好那么导入完之后呢我们通过查看发现已经有数据了而刚才导入的时候呢我们是先创建一个数据库然后在这个数据库里面呢创建一张表那接下来我们看另外一种方式我们可以另外一种方式呢导入到还有表里边让它自动去创建对应的表怎么做呢
[05:13] 我们来看这个命令这个命令呢前面都一样scope import连接这台主机的这个数据库用户名密码这个表呢是empconnect注意这个表换了然后呢这个地方是导入这个myprotos和启动一个注意最后这句话这句话呢我要导到Hive的数据库这个数据库的名字是scope to Hive把这个命令一执行了它就可以
[05:43] 自动给我们创建对应的表那我们来试一下我们来试一下走在这里我们还是在这个score里边执行走稍等好执行完毕执行完毕之后呢我们再回到Hive中查看一下suitables你会发现呢在这个数据库下面创建了一个表这个表的名字叫empconnect而我们在mycircle里边
[06:15] 我们这个表也叫EMP Connector那咱看看它的数据Select新FromEMP-CONN走你会发现数据全过来了说明呢我们这种方式更简单一点你不需要提前创建表它呢自动给你创建对应的表而且结构都是一样的OK这是另外一种导入方式好那么关于呢它这个导入HAL表呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Sqoop 将 MySQL 数据库中的表数据导入到 Hive 中，并展示创建 Hive 表和查询数据的过程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程 PPT 页面，标题为“导入关系表到HIVE”，内容包括“第一步：拷贝jar包”和“第二步：准备Hive数据库与表”，并列出相关命令。
画面2：显示终端窗口，列出 HBase 相关的 JAR 包文件名。
画面3：终端中执行命令将 Hive-exec-3.1.1.jar 复制到 Sqoop 的 lib 目录下。
画面4：终端中进入 apache-Hive-3.1.1-bin 目录并列出其内容。
画面5：PPT 页面，高亮显示“第二步：准备Hive数据库与表”中的创建数据库命令。
画面6：PPT 页面，高亮显示创建外部表的 SQL 语句。
画面7：PPT 页面，展示“第三步：开始导入”和“第四步：Hive表数据查看”的命令和查询语句。
画面8：终端中执行 Sqoop 导入命令，显示警告信息（缺少 HBase、HCatalog、Accumulo、ZooKeeper 环境变量）。
画面9：终端中执行 Hive 命令，创建数据库、使用数据库、创建外部表、查看表和查询数据。
画面10：终端中执行 Hive 查询语句，显示查询结果（5 行数据）。
画面11：PPT 页面，展示“第三步：开始导入”的命令。
画面12：终端中执行 Sqoop 导入命令，显示日志信息（HiveImport 初始化、加载数据、导入完成）。
画面13：终端中执行 Hive 查询语句，显示查询结果（5 行数据）。
画面14：PPT 页面，展示“第四步：Hive表数据查看”的查询语句和“导入关系表到Hive并自动创建Hive表”的命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
cp /export/servers/apache-Hive-3.1.1-bin/lib/Hive-exec-3.1.1.jar
/export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/lib

画面3：
cp Hive-exec-3.1.1.jar /export/servers/sqoop-1.4.7.bin_hadoop-2.6.0/lib/

画面4：
bin binary-package-licenses conf hostlog jdbc lib LICENSE NOTICE RELEASE NOTES.txt scripts

画面5：
Hive (default)> create database sqoopothive;
Hive (default)> use sqoopothive;
Hive (sqoopothive)> create external table emp.Hive(id int,name string,deg string,salary int ,dept string) row format delimited fields terminated by '\001';

画面7：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --fields-terminated-by '\001' --Hive-import --Hive-table sqoopothive.emp_hive --Hive-overwrite --delete-target-dir -m 1

画面11：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --fields-terminated-by '\001' --Hive-import --Hive-table sqoopothive.emp_hive --Hive-overwrite --delete-target-dir -m 1

画面14：
bin/sqoop import --connect jdbc:mysql://192.168.1.7:3306/userdb --username root --password root --table emp --Hive-import --Hive-database sqoopothive

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备Hive数据库与表
第三步：开始导入
第四步：Hive表数据查看

画面5：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备Hive数据库与表
第三步：开始导入
第四步：Hive表数据查看

画面7：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备Hive数据库与表
第三步：开始导入
第四步：Hive表数据查看

画面11：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备Hive数据库与表
第三步：开始导入
第四步：Hive表数据查看

画面14：
标题：导入关系表到HIVE
子标题：
第一步：拷贝jar包
第二步：准备Hive数据库与表
第三步：开始导入
第四步：Hive表数据查看
第五步：导入关系表到Hive并自动创建Hive表

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

