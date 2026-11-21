# 画面线理解：5.8 Flink Table示例

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.8 Flink Table示例_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 01:08, 01:44, 02:10, 03:36, 05:07, 05:50, 06:50, 09:43, 10:25, 12:17, 13:19, 15:09, 16:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:25:17

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
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-java</artifactId>
        <version>${flink.version}</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-streaming-java_2.12</artifactId>
        <version>${flink.version}</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.flink</groupId>
        <artifactId>flink-clients_2.12</artifactId>
        <version>${flink.version}</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

画面 2-14:
```java
package com.ithema.cold.flink.table;

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
