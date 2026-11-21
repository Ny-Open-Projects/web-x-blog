# 10-Hive的基本操作-数据库的创建和删除

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\10-Hive的基本操作-数据库的创建和删除【海量资源尽在 ubkz.com】.mp4
- 时长 6分13秒（音频 373s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们就来学习Hive的基本操作Hive的基本操作也就是在Hive这个客户端里面写一些类似于Circle的一些命令然后对我们数据仓库的数据进行分析和处理那么咱们先看第一个创建数据库创建数据库我们刚才用过就是Create DatabaseIf not exist, myHive如果myHive不存在那我就去创建这个数据库
[00:29] 这个条件呢可以加也可以不加加上了主要是防止这个数据库已经存在的情况比如说呢在这里你看在这里有个mytest2比如说我再创建一个created database然后呢它已经存在我写mytest2走那这个时候它就报错那我加了这个条件之后呢它就可以防止出现这么一个错误这个use myhive呢不用说了就是选择我使用这个数据库
[01:00] 接下来呢我对我操作一些表呢是对这个数据库中的表进行操作好那么接下来还有一个问题是我们刚才创建的这些数据库它都存在HDFS的什么位置呢这里注意这里其实有一个有一个配置这个配置呢叫have matstock warehouse dr这个是配置一个一个数据原数据的一个存放位置存放目录那么这个呢里边呢
[01:29] 其实就是我们HAVE数据库的一个位置默认是在哪里呢是在user下面HAVE一个warehouse我们来找一下吧在这里呢我们来访问我们的HDFS好打开我们的HDFS在这里呢默认是在user下面有一个HAVEHAVE一个warehouse你看这里边是不是就是我刚刚创建的一些数据库你会发现数据库呢其实就是一个文件夹那点开了你看这里边有一张表
[01:59] 那表呢也是一个文件夹这个表里边是没有数据的所以说呢默认是在这个目录那我们可不可以自己指定一个目录呢当然可以我们可以在创建数据库的时候呢用一个location用个location来指定它的位置来我们来做一下好在这里呢我们来createcreate database然后呢后面呢跟上一个数据库的名字location我们来试一下比如说my
[02:31] have2location后面跟上比如说我要放在根目录下面有个myhave2走加个分号结尾好 没问题没问题之后呢我们在这里呢做一个刷新嘛在根目录下面好 做一个刷新走看看这里边是不是一个myhave2OK 这就是一个指定它的存储位置好了还呢可以去修改数据库
[02:59] 所谓的修改数据库就是用alter database这个它主要是修改数据库的一些属性比如说数据库的一些创建时间但是它的原数据的信息是不可更改的比如说数据库的名字数据库所在的位置等等这是不能改的这个里边用一个alter database加上一个set db properties这么一个命令OK 大家可以自己操作一下
[03:26] 还有一个呢就是查看数据库的一个详情这个呢这个有时候也挺有用的来我们来试一下比如说呢我想去看一下我们刚才这个myhive它的一个详情我们给它dse database然后后面给它myhive好这个地方你看它列出了一个什么呢列出了一个数据库的名字然后呢后面跟上数据库所在的位置还有呢它的一个用户
[03:56] 这个应该是一个用户的类型这是一个用户的类型这是表示用户用户的名字是Rotan好这么一个信息还有呢这个地方呢还可以呢查看更详细的信息就是中间呢加个extended我们来看一下好在这里加一个加一个extended加个这么一个东西这个地方呢应该是extend应该是1D走写错了
[04:27] EXTENEDOK走一下这地方写错了写错了EXTENEDOK好了那这个呢这个信息呢和刚才差不多是因为我这里边还没有内容那这个呢也是它的一个输出的一个信息好那么既然呢还可以去删除数据库这个删除数据库呢有个drop database后面跟上数据库的名字比如说呢我现在呢想把这个mine
[04:59] 我们来看一下show database色我想把这个myhive2删了那就是drop后面给上database然后后面myhive2注意删的时候你看它出了一个问题什么问题呢它说呢这个Hive这个数据库不存在其实这个报错呢应该不用管我们再来看它删了没有走你看这个地方已经删了所以这个异常了不用管好那么这个删完之后呢
[05:29] 注意如果说呢这个数据库中呢有这个内容或者有表那这个时候呢是不能删的那如果说有表的话我还想删除怎么办呢有一个叫强制删除强制删除呢在这个命令的后面加一个叫CASC就是CSCSK的加上这么一个关键字那它呢就可以把这个数据库整个就删除了但大家呢尽量不要去用这个因为这个呢强制删除相当于你的数据呢
[06:00] 整个就丢失了OK这是他对数据库的一些基本操作我们呢只需要记住一个就是第一个创建数据库基本上就OK了好那么关于数据库的一个操作呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 Hive 基本操作，包括创建、修改、查看和删除数据库，以及创建表的语法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Hive 基本操作章节，包含创建数据库的 SQL 语句 `create database if not exists myhive;` 和 `use myhive;`，以及说明 `Hive.metastore.warehouse.dir/name` 由 `Hive-site.xml` 中属性指定。
画面 2: 在 SecureCRT 中执行 `show databases;` 查看数据库，然后尝试创建已存在的数据库 `mytest2`，提示错误 `Database mytest2 already exists`。
画面 3: 浏览器打开 Google 搜索页面，显示搜索建议和相关网页预览。
画面 4: 浏览器访问 HDFS 的 Web UI，显示 `/user` 目录下的 `Hive` 文件夹。
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
<name>Hive.metastore.warehouse.dir</name>
<value>/user/Hive/warehouse</value>
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

