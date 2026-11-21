# 画面线理解：12-sqoop导入-hdfs

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\12-sqoop导入-hdfs【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:41, 02:08, 02:53, 03:36, 04:52, 05:23, 06:58, 07:37, 08:20, 09:42, 10:18, 11:06, 11:57, 12:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 09:44:40

1) 这一组画面整体在讲如何使用 Sqoop 工具列举 MySQL 数据库中的所有数据库和表。

2) 按时间顺序列出每张画面的要点：
   画面1（序号1）：
   - 展示了课程 PPT 的第 4.5 节“Sqoop 的数据导入”。
   - PPT 内容包括“列举出所有的数据库”和“查看某一个数据库下面的所有表”。
   - 展示了命令行操作的步骤：
     命令行查看帮助：
     bin/sqoop list-databases --help
     列出 win7 主机所有的数据库：
     bin/sqoop list-databases --connect jdbc:mysql://192.168.1.1:3306/ --username root --password root
   - 展示了 SecureCRT 连接窗口，提示在 Windows 的 MySQL 数据库中执行命令。
   - 左侧导航栏显示了课程目录结构，包括“4.5、Sqoop 的数据导入”等小节。

   画面2（序号2）：
   - 展示了 Windows 桌面，桌面上有“黑马程序员”和“博学谷”的标志。
   - 桌面图标包括：sqoop-1.4.7.tar.gz、mysql.exe、java/jdk.jar 等。

   画面3（序号3）：
   - 展示了 SecureCRT 连接窗口，显示了 MySQL 数据库中的所有数据库列表。
   - 列出的数据库包括：
     my_store_db
     mybatis01
     mysql
     mytravel
     performance_schema
     springdb
     store_db
     test
     travel
     travel2
     userdb
     userdb2
     web05db
     web06db
     web12db
     web14db
     web17db 02
     web46db

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
   画面1：
   命令行查看帮助：
   bin/sqoop list-databases --help
   列出 win7 主机所有的数据库：
   bin/sqoop list-databases --connect jdbc:mysql://192.168.1.1:3306/ --username root --password root

   画面3：
   my_store_db
   mybatis01
   mysql
   mytravel
   performance_schema
   springdb
   store_db
   test
   travel
   travel2
   userdb
   userdb2
   web05db
   web06db
   web12db
   web14db
   web17db 02
   web46db

4) PPT 标题、架构图/流程图的结构、表格数据：
   画面1：
   - PPT 标题：4.5、Sqoop 的数据导入
   - 子标题：“导入工具”单入表从 RDBMS 到 HDFS。表中的每一行被视为 HDFS 的记录。所有记录都存储为文本文件的文本格式（或者 Avro、sequence 文件等二进制数据）。
   - 子标题：“列举出所有的数据库”
   - 子标题：“查看某一个数据库下面的所有表”
   - PPT 左侧导航栏结构：
     4. Sqoop 数据迁移
       4.1. 概述
       4.2. sqoop1 与 sqoop2 的对比
       4.3. 工作机制
       4.4. sqoop 类及原理
         4.4.1. sqoop 原理
         4.4.2. 修改配置文件
         4.4.3. 加入额外的依赖包
         4.4.4. 验证数据
       4.5. Sqoop 的数据导入
         4.5.1. 列举出所有的数据库
         4.5.2. 查看某一个数据库下面的所有表
         4.5.3. 导入数据到 HDFS
         4.5.4. 导入数据到 HDFS 且开启分隔符

5) 无。
