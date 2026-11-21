# 画面线理解：10-Hive的基本操作-数据库的创建和删除

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\10-Hive的基本操作-数据库的创建和删除【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:52, 01:38, 01:46, 02:16, 02:41, 02:53, 03:36, 04:06, 04:48, 05:11, 05:20, 05:32, 06:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 05:57:09

1) 这一组画面整体在讲什么（一句话）：
演示 Hive 基本操作，包括创建、修改、查看和删除数据库，以及创建表的语法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Hive 基本操作章节，包含创建数据库的 SQL 语句 `create database if not exists myhive;` 和 `use myhive;`，以及说明 `hive.metastore.warehouse.dir/name` 由 `hive-site.xml` 中属性指定。
画面 2: 在 SecureCRT 中执行 `show databases;` 查看数据库，然后尝试创建已存在的数据库 `mytest2`，提示错误 `Database mytest2 already exists`。
画面 3: 浏览器打开 Google 搜索页面，显示搜索建议和相关网页预览。
画面 4: 浏览器访问 HDFS 的 Web UI，显示 `/user` 目录下的 `hive` 文件夹。
画面 5: Typora 文档中展示创建数据库并指定位置的 SQL 语句 `create database myhive2 location '/myhive2';`，以及修改数据库的语句 `alter database myhive set dbproperties('createtime'='20180611');`。
画面 6: SecureCRT 中执行 `create database myhive2 location '/myhive2'`，成功创建数据库。
画面 7: SecureCRT 中显示 `create database myhive2 location '/myhive2'` 命令执行成功，耗时 0.133 秒。
画面 8: Typora 文档中展示查看数据库详细信息的 SQL 语句 `desc database myhive2;` 和 `desc database extended myhive2;`。
画面 9: Typora 文档中展示删除数据库的 SQL 语句 `drop database myhive2;`。
画面 10: Typora 文档中展示删除数据库的 SQL 语句 `drop database myhive2;`。
画面 11: SecureCRT 中执行 `desc database myhive;` 和 `desc database extended myhive;`，然后执行 `drop database myhive2;`。
画面 12: SecureCRT 中显示执行 `drop database myhive2;` 后的堆栈跟踪信息。
画面 13: Typora 文档中展示创建数据库表的语法 `CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name (...) PARTITIONED BY (...)`。
画面 14: Typora 文档中展示修改数据库的 SQL 语句 `alter database myhive set dbproperties('createtime'='20180611');`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```sql
create database if not exists myhive;
use myhive;
```
```xml
<name>hive.metastore.warehouse.dir</name>
<value>/user/hive/warehouse</value>
```

画面 5:
```sql
create database myhive2 location '/myhive2';
alter database myhive set dbproperties('createtime'='20180611');
```

画面 8:
```sql
desc database myhive2;
desc database extended myhive2;
```

画面 9:
```sql
drop database myhive2;
```

画面 11:
```sql
desc database myhive;
desc database extended myhive;
drop database myhive2;
```

画面 13:
```sql
CREATE [EXTERNAL] TABLE [IF NOT EXISTS] table_name
([col_name data_type [COMMENT col_comment], ...])
[COMMENT table_comment]
[PARTITIONED BY (col_name data_type [COMMENT col_comment], ...)]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“3. Hive 的基本操作”，子标题“3.1 创建数据库”。
画面 5: PPT 标题为“3.2 创建数据库并指定位置”和“3.3 修改数据库”。
画面 8: PPT 标题为“3.4 查看数据库详细信息”。
画面 9: PPT 标题为“3.5 删除数据库”。
画面 13: PPT 标题为“3.6 创建数据库表的语法”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
