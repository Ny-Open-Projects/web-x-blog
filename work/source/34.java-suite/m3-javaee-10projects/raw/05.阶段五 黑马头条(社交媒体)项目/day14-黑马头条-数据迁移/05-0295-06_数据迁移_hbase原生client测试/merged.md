# 06_数据迁移_hbase原生client测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day14-黑马头条-数据迁移
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day14-黑马头条-数据迁移\06_数据迁移_hbase原生client测试【海量资源尽在 666java.com】.mp4
- 时长 7分30秒（音频 451s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就继续往下讲刚才咱们是把这个HBase的一些相关的配置咱们已经弄完了主要是在Common这一块去做的然后下面咱们就来去创建项目这个项目主要是做迁移用的这是一个微服务这个咱们叫什么叫Migration就它呢它就是迁移的意思这个项目我已经创建完了你只需要在哪在当前的资料中去找到当前的什么它
[00:29] 然后是导进去那这个导了咱们导了好多次了啊这我又不再去强调了这时候我这项目已经拿过来了你可以看一下这里边的代码啊这里边几乎没有代码啊你看它只有一个引导类啊引导类然后呢是有一些初始化的一些东西啊我们可以看一看有哪些啊首先呢是一个com是吧这是Jackson的一些东西然后是买circle的嗯还有咱们的quad还有hbase还有Kafka就那么多好吧就那么多啊你把它搞搞进来就可以啊
[00:59] 然后咱们要再去看一看咱们下面就来去做一个测试主要测的是就是HBase主要测的就是HBase但这里边咱们一会估计还少一个这里边少一个Mongo一会咱们导入Mongo之后咱们再去引进来好吧这里边有一个测试咱们可以看一看有一个测试这个测试可以看一下这个测试比较简单我现在注入的就是最原生的那个什么HBase Client
[01:28] 然后下面是有一些的操作我们可以看一下有哪些第一个是创建表第二个是可以删除表第三个你可以去保存当然你也可以去查询你也可以去查询行咱们就说那么多下面咱们就具体去看一看这些该怎么去操作你可以查看一下当前的数据库list当前的这里边其实有几张表一个是前这个咱们真正业务的表
[01:59] 这个是实时测试的这也是测试的我后边都是测试的有那么多这时候我要想要去创建的时候是有这么个表叫HBaseTestTableName然后我把它干嘛我把它给删了好吧那先删了你看删除好用不好用你看这个名跟这个名字要保持一致看看是不是一样一样的话咱们就删除试一试这个方法你可以看一下
[02:25] 我现在注入的是HBaseClient然后呢就是delete table你直接把表名放到这就可以好吧现在咱们去执行一下走稍等正在加载环境啊好马上加载完成稍等一下啊这里边没有报错啊看看能不能删除成功好这个是原亮色是吧那这时候咱们可以去查看一下看看有没有删除目前的话是不是就少了一张表了我没问题啊
[03:03] 那这个删除咱们测完了没有事那咱们下面继续往下看啊下面咱们要去新增一张表那新增表的时候咱们之前去说概念的时候已经讲了啊这时候呢你需要去指定表名还有什么必须要指定列足OK这有一个什么这不有一个列足吗column family是吧然后这个东西呢就是你可以指定几个其实都行无所谓啊这个就是咱们真正装数据的地儿它里边可以包含很多个列是吧
[03:33] 这里边是可以传一个集合集合的意思就是说你可以传入多个多个列组OK那这样的话咱们就可以去创建表OK那咱们也可以去执行一下看看能不能创建成功走执行稍等这个稍微时间有点长好马上结束稍等正在加载这个环境应该是他前面也没有报错我们可以看一下能不能创建成功好那这个也是原谅色是吧那这时候咱们可以在这去查看
[04:10] 当前的list车表是不是就创建出来了我要没问题那创建完之后你说光创建其实没有用咱们需要去保存数据对吧这里边其实还有一个方法叫port dateport date我要去简单解释一下第一个就是当前的表你要指定哪个表然后第二个就是你的row key这个row key是啥之前讲过是吧这就是唯一的一个标识
[04:38] 唯一标识咱们查询的时候就是要通过表和它的唯一标识去查询数据所以说呢你要去指定表名还有rokey还有就是你存储要存到哪呢要存到一个这种列组里边所以说你要去指定一个列组好吧这是一个内容当然下面还有两个一个columns一个values这是啥呀很显然呢这就是啥呢这就是两个数组这就是列组里边所需要的列
[05:08] 和值就是说内幕它的值是张三A值是28当然这个你要去提供两个这样比较方便一些提供两个第一个是column第二个是values好吧这个对应上你这个你别到时候把28放到前边这样子就不太合适了为什么说不太合适你可以去看一下这个我的data里边你可以往下正的去调用的时候先去创建表是吧
[05:35] 当然这个表它就会去做一个判断先去获得表然后是获得数据获得数据的时候你看它就会干嘛它就会把当前的column去循环循环的时候同时会往这里边去put那put什么看put一个当前的什么i一个value也就是说它两个必须的是集合是保持一致才行这时候你就可以往当前列组里边去装入它的什么它的一个这种column和value这样的话就能追赢上了
[06:06] 好吧行那这个你注意一下写的时候你不能说我这边有三个元素这里边有两个元素那这个肯定会出问题好吧那咱们下面就来去测试一下看看能不能成功稍等看看看看这个数据有没有完成好那这个也完成了这个也没有报错它也有数据那你怎么去验证为什么会有说说会有数据下面咱们还有一个方法就是查询就查询这查询的话刚才说了你就要根据当前的表
[06:42] 跟你的Rowkey去查询你看我这个表是不是他呀这个Rowkey跟这个是不是对应上啊这时候呢你就可以在这打断点啊咱们可以看一下里面的数据但是你也可以放行可以去打印这个数据也行好吧那咱们就来去执行走好马上执行完了稍等往下好这个执行完了啊执行完之后呢你看这个数据呢其实就是当前的打印的数据啊你看他的那么TestRowkey01然后这里边有A值还有什么呢你可以看一下啊有Name是吧这个
[07:23] 这个值呢咱们已经装进去了没有问题啊那行那这个呢其实是最原生的一个HBase Client

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 Java 项目如何通过单元测试对 HBase 数据库进行表的创建、删除、数据写入和查询操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 `src/main/java/com/heima/migration/config/InitConfig.java` 文件。
画面2：显示 `InitConfig.java` 文件内容，包含 `@Configuration` 和 `@EnableScheduling` 注解，以及 `@ComponentScan` 指定扫描包。
画面3：显示 `HBaseTest.java` 文件，包含 `testCreateTable()`、`testDeleteTable()`、`testSaveData()` 和 `testFindRowKey()` 四个测试方法。
画面4：展示在 SecureCRT 中执行 HBase 命令的终端输出，显示了表的创建、删除和数据操作结果。
画面5：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中。
画面6：显示 `HBaseTest.java` 文件，光标位于 `testDeleteTable()` 方法中，下方终端显示测试通过日志。
画面7：展示在 SecureCRT 中执行 HBase 命令的终端输出，显示了表的创建、删除和数据操作结果。
画面8：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中，下方终端显示测试通过日志。
画面9：显示 `HBaseTest.java` 文件，光标位于 `testCreateTable()` 方法中，下方终端显示测试通过日志。
画面10：显示 `HBaseTest.java` 文件，光标位于 `testDeleteTable()` 方法中，下方终端显示测试通过日志。
画面11：显示 `HBaseTest.java` 文件，光标位于 `testSaveData()` 方法中，下方终端显示测试通过日志。
画面12：显示 `HBaseTest.java` 文件，光标位于 `testSaveData()` 方法中，下方终端显示测试通过日志。
画面13：显示 `HBaseTest.java` 文件，光标位于 `testFindRowKey()` 方法中，下方终端显示测试通过日志。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.heima.migration.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@ComponentScan({"com.heima.common.common.init","com.heima.common.mysql.core", "com.heima.common.hbase"})
@EnableScheduling
public class InitConfig {
}
```

画面3：
```java
columnFamily.add("test_cloum_family1");
columnFamily.add("test_cloum_family2");
boolean ret = hBaseClient.createTable(tableName: "hbase_test_table_name", columnFamily);
```

画面5：
```java
public void testCreateTable() {
    List<String> columnFamily = new ArrayList<>();
    columnFamily.add("test_cloum_family1");
    columnFamily.add("test_cloum_family2");
    boolean ret = hBaseClient.createTable(tableName: "hbase_test_table_name", columnFamily);
}
```

画面6：
```java
@Test
public void testDeleteTable() {
    hBaseClient.deleteTable(tableName: "hbase_test_table_name");
}
```

画面7：
```java
String []columns = {"name","age"};
String []values = {"shangsan","28"};
hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
```

画面10：
```java
@Test
public void testDeleteTable() {
    hBaseClient.deleteTable(tableName: "hbase_test_table_name");
}
```

画面11：
```java
@Test
public void testSaveData() {
    //String tableName, String rowKey, String familyName, String[] columns, String[] values
    String []columns = {"name","age"};
    String []values = {"shangsan","28"};
    hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
}
```

画面12：
```java
@Test
public void testSaveData() {
    //String tableName, String rowKey, String familyName, String[] columns, String[] values
    String []columns = {"name","age"};
    String []values = {"shangsan","28"};
    hBaseClient.putData(tableName: "hbase_test_table_name", rowKey: "test_row_key_001", familyName: "test_cloum_family1", columns, values);
}
```

画面13：
```java
@Test
public void testFindRowKey() {
    Result hbaseResult = hBaseClient.getHbaseResult(tableName: "hbase_test_table_name", rowKey: "test_row_key_001");
    System.out.println(hbaseResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

