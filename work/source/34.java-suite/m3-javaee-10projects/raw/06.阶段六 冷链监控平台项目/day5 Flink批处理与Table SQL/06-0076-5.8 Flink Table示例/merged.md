# 5.8 Flink Table示例

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.8 Flink Table示例_【海量资源尽在 666java.com】.mp4
- 时长 16分31秒（音频 992s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好下面呢我们给大家演示一下Flink table api和circle的操作那么我们首先呢我们先建一个package那么这个package就叫table然后在这个table package下面我们创建一个类叫做table test然后我们添加我们的main函数那么我们整个类的一个方法或者说整个类的一个功能我们先简单的给大家梳理一下那首先
[00:33] 我们第一步我们要做什么呢因为我们是一个table或者说是一个表那么这个表的这个数据库表比如说我们要定义mycircle数据库表那么我们首先要定义什么我们要定义数据类型或者叫数据模型或者叫数据结构都是一样的那么这个数据类型呢我们实际上是用了一个叫order表也就是说是一个订单表那么这个订单表呢其实是一个pojopojo类型的
[01:02] 那第二部分的话我们需要设置我们的Flink执行环境Flink执行环境第三步的话我们需要定义我们的table环境定义Flink的table执行环境那么第四步的话我们需要定义数据源或者叫输入源那第五步我们要将我们的输入源
[01:42] 转化成我们的table将数据转化转换转换成tableblink table那么第六步的话我们要执行table的查询操作那么第七步我们要执行blink程序OK那么我们在我们的main函数里边我们需要定义这么七个步骤那么第一部分来讲的话OK我们先定义第一部分第一部分是
[02:23] 我们的order的这个post就对象这个对象来讲的话是一个我们的订单针对一个订单的话我们最简单的需要什么呢我先定义publicstatic然后我们的classclass叫什么order然后这个classorder我们要有几个参数呢第一个参数是是一个我们的用户ID
[02:57] 比如说我们用浪性的Use那么第二个的话我们要定义什么我们定义它的购买的商品对吧对于一个订单来讲的话要有一个Product那么同时还要有一个什么购买的数量OK这么三个字段是我们针对定义的一个订单表那么我们需要做的是什么呢我们需要先创建一个Public的一个
[03:31] 构造函数而这个构造函数是无参的一个构造函数没有任何参数这么一个构造函数为什么要这样做因为我们的blink它如果想要处理比如说我们的数据语言把它转化成一个order或者是转化成一个我们的poj对象那么我们这个poj对象里边必须有一个必须有一个无参的构造函数OK那下一步的情况下
[04:03] 我们需要再定义我们有参的构造函数比如publicorder那么这个参数呢是我们的lang型的user然后还有个string型的product再来一个int型的amount数量ok我们给它复制this.user等于userthis.product等于product
[04:40] 那么this.amount等于amountOK我们的这个构造函数其实就我们这个poj对象就添加完了那么添加完之后呢下一步的时候我们要做的一个操作就是在我们的函数里边添加我们的Flink程序第一步定义执行环境对不对定义执行环境那么定义执行环境我们现在需要有几个执行环境一个执行环境是我们的
[05:15] 比如说我们的streamstream.execution.environment这个呢等于stream的一个execution.environment然后get.execution.environment那么第二个来讲的话我们需要定义stream的一个table.execution.environment比如说这个叫tenv那么它等于什么呢stream.table.execution.environment它来创建一个environment
[05:49] 创建一个环境也就是说我们的stream table environment是依赖于我们的stream execution environment的OK我们定义完了之后第二步的话我们要定义一个数据定义输入源输入源的数据那么我们输入源的数据我们可以简单的做一下比如说我们不用通过读取卡普卡数据了我们通过直接是用Java对象来创建
[06:20] 我们的输入源比如说data streamdata stream什么呢它类型是order然后我们定义一个order a我们等于inv.fromcollection这个collection的话我们就直接从java对象里面创建就可以了这个对象是irows.aslistok那么我们把我们的
[06:59] 对象先创建上这个对象是neworder然后neworder什么呢1user id是1然后product是什么呢比如说book1然后amount等于几呢3比如说就是user1他买了book1然后买了三个然后我们再定义neworderuser2他买了book2然后他的amount是4
[07:38] 那么user3他买了book3然后amount是2此时我们就创建了我们的delta stream了类型不对类型的话我们要是lang型的我们用1L 2L和3LOK那我们定义好了定义好了之后这个是我们的一个输入源我们还可以再定义另外一个输入源订单2订单B对于订单B来讲的话我们的用户是4
[08:20] 五六那么四呢他买了book4买了book5买了book6然后他的数量321OK我们制造了这两个订单然后下一步的时候我们要将我们的数据流转化成我们的一个table也就是转化成Flink table那么首先我们要定义一个tabletable a那么这个table a等于什么呢等于我们的teinv.from
[08:59] data stream也就是说我通过一个data stream来转化成一个Flink table那么order a然后它的字段字段有什么呢userproductproduct然后再加上一个amount这是我们针对于table a生成的就是用order a这个数据源来生成了table a那么紧接着我们用
[09:34] 那么生成了tableB那么这两个数据这两个tableflink table就是将数据流转换成Flink table我们现在有了两个table了下一步我们就执行查询操作我们定义一个table是result我们查询结果也是一个table它等于什么呢
[10:12] 它等于t因为点circle q那么就是下边就是一个直行的一个查询查询的circle语句这个circle语句比如说selectselect fromfrom什么呢我们再加上t包a然后加上加上我们的条件条件是well注意这里边有两个空格没有两个空格它会
[10:47] 它会构成你circle语句是有问题的那么我要什么呢amountamount大于2然后就是从a表中的amount值大于2的那肯定就是1和2这两个用户对不对然后我们在unitunit2什么意思我们再加个空格因为要是添加或者说合并对不对合并什么呢合并selectingfrom
[11:17] 再加上我们的什么呢table b再加上where条件where amountamount小于2ok此时我们就得到了我们的查询语句我们执行了这个查询那下一步的时候我们就定义我们的输出就可以了对不对tenv.toappendStream也就是我把我们的这个结果呢
[11:51] 把我们的结果转换成一个del streamresult然后转换需要经过一个什么呢经过order的类型转换成order类型然后紧接着我们把它打印出来present我们再加上一个里边的present的一个标识吧我们给它打印出来然后我们还可以设置我们的定型度OK那此时我们就
[12:22] 开发完了我们的这个circle的程序了那紧接着我们再执行env.executeexecuteok然后我们有错有错我们先through这个exception我们through exception就ok了ok那此时我们就把我们程序开发完了那么我们简单的来看一眼
[12:49] 这个sugary句是说我要从第一个表里边我拿到了数据就是amount大于2的那么就是1和2那么我们还需要从第二张表里边拿到amount小于2的那么就是6所以说它的结果应该是126用户126那么我们执行一下看看这个结果是不是我们这样的我们来执行一下看一眼OK它在执行OK它执行完了执行完了我们看一看
[13:27] 它有三个输出输出的话是我们但是这个输出我们看不出来到底是一个什么意思我们需要重新的把我们的结果给它输出出来因为我们在我们的order类里边没有定义一个toString方法所以在这里边的时候它就没办法来打印出来那么它打印的就是我们不可识别的那么我们需要generate然后override一个toString的一个方法
[13:57] 那么在这里的情况下我们就可以给他添加一个什么呢瑞汤什么瑞汤欧的类型的那么这个奥德类型的是什么呢比如说u字等于加上u字然后再加哈加什么加上我们的product等于再加上一个product然后再加上我们的
[14:38] amount等于再加上amountOK最后再加上一个加上一个什么加上一个大括号OK此时我们就能够打印出来了我们再重新执行一下OK它在执行我们看一看中间它打印出来的东西OK第一个是order等于6的对不对第二个order等于1的我们说原来我们看到的
[15:22] 满足条件的就是1 2和6那么第一个第六个都有了126没错这是我们得到的一个正确的一个结果我们从这里面可以看到几个方面啊第一个来讲的话我们的DataStreamJava的这种集合类可以直接给DataStream复制那么第二个来讲的话我们从中可以看到我们通过一个DataStream把它转化成一个Flink的一个table那第三步是
[15:52] 我们需要能够了解到我们执行circle语句然后执行circle语句之后我们还可以通过一个table把它转化成一个datastream然后最后执行那么在这里边还有一个额外的一个小收获就是我们想要把某一个类给它toString的时候我们的这个toString里边的这个类的我们要重写一下
[16:19] 否则情况下他打印出来的就是不是我们想要的一个或者我们不可识别的一个字段一个数值一个字符好我们的示例就演示到这谢谢大家

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中编写一个 Flink Table API 的 Java 示例程序，包括定义数据结构、设置执行环境、定义输入数据、转换成 Table、执行 SQL 查询并打印结果。

2) 按时间顺序列出每张画面的要点：
画面 1: 显示了 Maven 项目的 pom.xml 文件内容，其中配置了 Apache Flink 的快照仓库和依赖。
画面 2: 显示了 TableTest.java 文件的开头，注释列出了程序的六个步骤。
画面 3: 在注释中添加了“定义输入数据”。
画面 4: 在注释中添加了“将数据转换成 table”。
画面 5: 在注释中添加了“执行 Table 查询操作”。
画面 6: 在注释中添加了“执行 SQL 查询”。
画面 7: 在 main 方法中开始定义执行环境，使用 StreamExecutionEnvironment。
画面 8: 在 main 方法中定义了 DataStream<Order> orderA。
画面 9: 在 main 方法中定义了 Table tableA 和 Table tableB。
画面 10: 在 main 方法中开始编写 SQL 查询语句。
画面 11: 在 main 方法中完成了 SQL 查询语句，并添加了 print() 操作。
画面 12: 程序运行，控制台输出了 Flink 的启动日志。
画面 13: 程序运行结束，控制台输出了 Flink 的关闭日志。
画面 14: 在 Order 类中重写了 toString() 方法，并定义了构造函数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<repositories>
    <repository>
        <id>apache.snapshots</id>
        <name>Apache Development Snapshot Repository</name>
        <url>https://repository.apache.org/content/repositories/snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
    <repository>
        <id>oss</id>
        <name>oss</name>
        <url>https://oss.sonatype.org/content/repositories/snapshots/</url>
        <releases>
            <enabled>false</enabled>
        </releases>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.apache.Flink</groupId>
        <artifactId>Flink-java</artifactId>
        <version>${Flink.version}</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Flink</groupId>
        <artifactId>Flink-streaming-java_2.12</artifactId>
        <version>${Flink.version}</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.Flink</groupId>
        <artifactId>Flink-clients_2.12</artifactId>
        <version>${Flink.version}</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

画面 2-14:
```java
package com.ithema.cold.Flink.table;

import java.util.Arrays;

public class TableTest {

    // 1. 定义数据结构， Order POJO
    // 2. 设置 Flink 执行环境
    // 3. 定义 FlinkTable 执行
    // 4. 定义输入数据
    // 5. 将数据转换成 table
    // 6. 执行 Table 查询操作
    // 7. 执行 SQL 查询

    public static void main(String[] args) {

        // 1. 定义执行环境
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        StreamTableEnvironment tEnv = StreamTableEnvironment.create(env);

        // 2. 定义输入数据
        DataStream<Order> orderA = env.fromCollection(Arrays.asList(
                new Order(user: 1L, product: "book1", amount: 2),
                new Order(user: 1L, product: "book2", amount: 3),
                new Order(user: 1L, product: "book3", amount: 2),
                new Order(user: 1L, product: "book4", amount: 3)
        ));

        DataStream<Order> orderB = env.fromCollection(Arrays.asList(
                new Order(user: 1L, product: "book1", amount: 1),
                new Order(user: 1L, product: "book2", amount: 2),
                new Order(user: 1L, product: "book3", amount: 1)
        ));

        // 3. 将数据转换成 Table
        Table tableA = tEnv.fromDataStream(orderA, "user, product, amount");
        Table tableB = tEnv.fromDataStream(orderB, "user, product, amount");

        // 4. 执行 SQL 查询
        Table result = tEnv.sqlQuery("SELECT * from " + tableA + " where amount > 2 union all " +
                "select * from " + tableB + " where amount > 2");

        // 5. 执行 SQL 查询
        tEnv.toAppendStream(result, Order.class).print("sinkIdentifier: " + "sinkIdentifier");

    }
}

public static class Order {
    public Long user;
    public String product;
    public int amount;

    public Order() {}

    public Order(Long user, String product, int amount) {
        this.user = user;
        this.product = product;
        this.amount = amount;
    }

    @Override
    public String toString() {
        return "Order{" +
                "user=" + user +
                ", product=" + product +
                ", amount=" + amount +
                '}';
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

