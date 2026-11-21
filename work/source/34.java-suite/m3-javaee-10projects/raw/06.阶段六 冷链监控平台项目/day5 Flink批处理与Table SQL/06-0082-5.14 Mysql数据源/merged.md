# 5.14 Mysql数据源

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.14 Mysql数据源_【海量资源尽在 666java.com】.mp4
- 时长 12分42秒（音频 763s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好下面呢我们开发一个稍微复杂一点的例子那么这个例子里边我们使用mycircle的表里边的数据作为我们的数据源那么我们的Flink程序需要加入的或者需要加载的是一些新的一些dependency的一个jar 包那么需要加载什么呢第一它需要加载我们Flink的connector也就是说它的group id是org.
[00:30] apache.Flink那么它的artifact id呢叫Flink-gdbc下滑线2.12当前这个2.1的scala的版本那么它的version呢我们当前的version版本是1.9.1那么另外一个需要依赖的是我们的mycircle gdbc的驱动它的group id是叫mycircle它的artifact id的叫做mycircle
[01:01] -connector-java然后它的版本呢我们当前使用的是5.1.48这个版本OK我们把这两个jar 包给它添加进来那么下一步我们就可以添加我们的java程序那么这个java程序呢叫做table gdbc这样的一个类那么我们在这里边我们需要先添加一下我们的注释我们的目标是什么呢将
[01:33] mycircle数据添加或者说转换成flinktableOK那么我们先添加我们的命函数那第一步我们应该做什么定义或者设置我们的执行环境那对于我们的mycircle数据库里面来讲它的数据是有源的还是有界的还是无界的它是一个有界的对不对
[02:06] 作为邮件数据来讲的话我们需要定义的是什么是一个batch是一个批处理的一个environment那么所以我们在这儿我们先定义一个execution environment因为它等于什么呢它等于execution environment的一个方法叫getexecution environment方法那么第二步来讲的话我要定义我的batch tableenvironment那么这个batch table environment我们怎么定义它呢等于
[02:40] Batch Table Environment的create方法啊,调用它的create方法,然后它的参数呢,就是我们当前的这个environment,OK,我们订阅了环境变量了,那么下一步的话,我们需要把我们MySQL数据库里边的数据加载进来,那么我们先看一看MySQL数据库里边,那么我们现在有一个数据库,而这个数据库里边的有一张表,那么是user的表在我们的Ti701这个数据库里边,那么它的字段呢,非常简单,一个叫ID,一个叫
[03:09] 一个叫Age那么Uter Name是一个String类型的ID和Age都是整形的那我现在就可以添加我们的数据的类型那么我要定义数据类型定义数据类型我们怎么定义呢定义数据类型在Flink里边它有一个类叫Type Information这个类Type Information它指的是我们的数据的字段的类型
[03:41] 那么我们定义一个数组型的在这里边的话我定义一个数组它等于什么呢等于new type information这样的一个这样的一个类那么我创建这个实例的时候它的基础的类在哪呢叫basical type information它的类型我们可以看到它里边有好多类型比如说像我们的street类型的或者data类型的
[04:11] 或者instant类型long型的int类型的等等好几个类型那么对于我们第一个来讲的话我们使用的是int type对吧我们第一个字段是idid是个int型的那么第二个字段呢我们使用的是string类型的是吧第三个字段呢也是一个int类型的OK我们现在就定义好了我们的数据类型定义完数据类型之后呢我们可以定义我们的GDPC的一个参数
[04:46] GDPC参数那么这个GDPC参数我们用什么来定义呢我们有一个Java就Flink里边Flink API里边它有一个类叫GDPC input format这个类这个类的话我们需要创建一个GDPC input format然后由此来build一个我们的GDPC input format
[05:18] 然后在这里边的时候我可以定义我们的参数了这个参数里边我们可以看到有db url有driver name有password然后有执行query等等这些东西大家如果做过这种mycircle数据库开发的是不是比较熟悉那么首先的话我可能需要set driver name那么mycircle driver name是什么呢com.mycircle.gdbc.driver对吧
[05:47] 这是我们的MySQL gdbc的一个驱动的名字那么下一步的时候我要set db ur那么db ur是什么gdbc然后冒号MySQL冒号双斜杠我们的数据库的ip地址然后端口然后紧跟着就是我们的数据库的名字数据库名字是什么test01然后再加上我们的character
[06:20] ch a r a c t e r characterincoding等于utf8小写的utf8ok那此时我们已经把我们的db的url给填接上了那下一步的话我们就set我们的username那么username我们的数据库的用户名root然后再set我们的password数据库的密码密码123456
[06:51] OK那我们现在添加完这些之后紧接着我还可以添加我的query就是查询的我的查询的语句我们刚才的数据库表非常简单我select from我们的我们的user那么数据库这相应的我们的类型或者说查询的一个语句它的参数我们都添加完了那么我们还需要设置一个什么呢设置一个
[07:22] RowTypeRowType的话是一个返回类型那么这个返回类型是一个什么呢我们需要在我们刚才定义的数据类型里边再添加一个了RowTypeInfoOK这个RowTypeInfo的话它是一个什么东西呢我们等于NewRowTypeInfo它的参数就叫刚才我们定义的这个数组OK那此时我们就相应的是说把我们的MySQL数据库里边进行
[07:52] 查询返回值的数据类型给它填兼完了那么我们再加上一个finish表示整个的GDPC参数的设置已经完成了那下一步的话我们就可以定义我们一个数据源了定义数据源data source那么data source我们的source等于什么呢等于我们的env.create input那么这个create input就可以把我们的GDPC的一些参数给它
[08:25] 添加进来了OK我们定义好了我们的数据源下一步我们将要把我们的数据源注册成为一个一个表比如说我们的Batch table environment由它来注册成一个我们的表那么这个表来讲的话它的数据是从哪来呢从我们的Data source里边来那么表的名字比如说叫My table然后它的数据类型呢数据来源呢是sourceOK
[08:56] 那此时我们就注册成了注册Flink table那么我们定义完了我们Flink table之后下一步的话我们就执行我们的查询我们基于这个table来进行一个查询那这个查询的话我们查询结果返回的是一个table返回的是我们的table我们他返回了table之后呢我们等于他等于我们的table
[09:37] Batch Table Environment然后执行Circle Query那么这个Circle Query是什么我SelectingFrom我们的MyTable大家注意这个地方的查询的话是查询刚才我注册成的一个表也就是说我先把我的MyCircle数据库里边的数据语言添加到我们的MyCircle添加到我们的Flink的一个
[10:06] 表里边然后接着我在我的Flink的这个表空间里边查找或者说查询我们的这个数据那么下一步的话我们就将数据库给它返回对吧返回查询结果我们datasetresultresult它result等于什么呢等于我们的bathtable environment.to dataset我们就把我们的这个查询的一个
[10:41] 结果然后下一个就是我们的这个类这个类的话就是一个row.classok此时我们就执行完查询结果了最后我们就把我们的结果输出result.printok它执行了print其实也执行了我们的execution也就是也执行了我们Flink的执行程序那么我们来运行一下看看效果ok
[11:24] 他已经从我们的数据库里边拿到了我们的数据那么我们再来回顾一下我们整个过程第一定义了我们的环境变量这个环境变量是我们的batch或者说叫做dataset的一个环境变量那么第二步来讲的话我定义我们的GDPC参数和定义我们这个GDPC参数返回的一个类型这个类型来讲的话其实是Basic type information那第三步来讲的话
[11:52] 我需要定义我们的这个数据源也就是说给我们Flink table定义它的数据源这个数据源是一个datasource类型的这个datasource呢它是Flink API里面的一个datasource那么有了这个数据源之后下一步的时候我就把我的这个数据源注册成为我们一个Flink table
[12:15] 下一步我们就从我们刚才注册的这个Flink table里边把我们的数据查询出来那么查询的结果呢我们返回到一个dataset里边去然后把它输出打印打印的结果就是从我们从数据库里边拿到的一个结果好我们今天给大家介绍的这个从mycircle数据库里边拿到我们数据然后转换注册成一个Flink表的一个讲解就到这谢谢大家

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Flink 中通过 Table API 读取 MySQL 数据表并执行 SQL 查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构和 pom.xml 文件，其中包含 Flink Table API 相关的依赖项。
画面 2: 在项目中右键点击，弹出创建新文件的菜单，准备创建 Java 类。
画面 3: 在 src/main/java/com/itheima/cold.Flink/table 包下创建了 TableJob.java 文件。
画面 4: 在 TableJob.java 中导入 Flink 的 ExecutionEnvironment 和 BatchTableEnvironment。
画面 5: 定义执行环境 ExecutionEnvironment 和 BatchTableEnvironment。
画面 6: 定义数据类型 TypeInformation，声明了 INT、STRING、INT 三种字段类型。
画面 7: 创建 JDBCInputFormat 的构建器，准备设置数据库连接参数。
画面 8: 通过 IDE 的自动补全功能，选择并设置 JDBCInputFormat 的参数。
画面 9: 完成 JDBCInputFormat 的配置，包括数据库 URL、用户名、密码和查询语句。
画面 10: 通过 IDE 的自动补全功能，选择并设置 DataSource。
画面 11: 调用 batchTableEnvironment.registerDataSet 注册数据源。
画面 12: 通过 IDE 的自动补全功能，选择并设置 Table 的类型。
画面 13: 定义数据源 DataSource。
画面 14: 完成数据源的定义，准备执行 SQL 查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-streaming-java_${scala.binary.version}</artifactId>
    <version>${Flink.version}</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-table-api-java-bridge_${scala.binary.version}</artifactId>
    <version>${Flink.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.Flink</groupId>
    <artifactId>Flink-table-planner_${scala.binary.version}</artifactId>
    <version>${Flink.version}</version>
</dependency>
```

画面 3:
```java
package com.itheima.cold.Flink.table;
```

画面 4:
```java
import org.apache.Flink.api.java.ExecutionEnvironment;
import org.apache.Flink.table.api.java.BatchTableEnvironment;
```

画面 5:
```java
ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
BatchTableEnvironment batchTableEnvironment = BatchTableEnvironment.create(env);
```

画面 6:
```java
TypeInformation[] fieldTypes = new TypeInformation[] {
    BasicTypeInfo.INT_TYPE_INFO,
    BasicTypeInfo.STRING_TYPE_INFO,
    BasicTypeInfo.INT_TYPE_INFO
};
```

画面 7:
```java
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
```

画面 8:
```java
.setTableName("users")
.setQuery("select * from users")
.setRowTypeInfo(rowTypeInfo)
.finish();
```

画面 9:
```java
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
    .setDBUrl("jdbc:mysql://172.17.0.143:3306/test01?characterEncoding=utf8")
    .setUserName("root")
    .setPassword("123456")
    .setQuery("select * from users")
    .setRowTypeInfo(rowTypeInfo)
    .finish();
```

画面 10:
```java
DataSource source = env.createInput(jdbcInputFormat);
```

画面 11:
```java
batchTableEnvironment.registerDataSet("mTable", source);
```

画面 12:
```java
Table table = batchTableEnvironment.sqlQuery("select * from mTable");
```

画面 13:
```java
TypeInformation[] fieldTypes = new TypeInformation[] {
    BasicTypeInfo.INT_TYPE_INFO,
    BasicTypeInfo.STRING_TYPE_INFO,
    BasicTypeInfo.INT_TYPE_INFO
};
RowTypeInfo rowTypeInfo = new RowTypeInfo(fieldTypes);
JDBCInputFormat jdbcInputFormat = JDBCInputFormat.buildJDBCInputFormat()
    .setDBUrl("jdbc:mysql://172.17.0.143:3306/test01?characterEncoding=utf8")
    .setUserName("root")
    .setPassword("123456")
    .setQuery("select * from users")
    .setRowTypeInfo(rowTypeInfo)
    .finish();
DataSource source = env.createInput(jdbcInputFormat);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

