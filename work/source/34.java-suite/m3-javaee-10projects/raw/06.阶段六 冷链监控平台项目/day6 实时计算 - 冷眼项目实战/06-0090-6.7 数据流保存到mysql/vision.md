# 画面线理解：6.7 数据流保存到mysql

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.7 数据流保存到mysql_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:45, 01:45, 02:05, 03:03, 05:45, 06:36, 07:13, 08:21, 08:45, 11:15, 12:06, 12:47, 13:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 17:33:30

1) 这一组画面整体在讲什么（一句话）：
编写一个 Flink 自定义 Sink，将消息数据写入 MySQL 数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 IntelliJ IDEA 中，右键点击 `SinkToMySQL.java` 文件，弹出上下文菜单，准备进行代码操作。
画面 2: 显示 `SinkToMySQL.java` 文件的初始状态，类定义为空。
画面 3: 在 `SinkToMySQL` 类中，添加了 `@Override` 注解的 `open`、`close` 和 `invoke` 方法的骨架。
画面 4: 在 `SinkToMySQL` 类中，声明了用于连接和操作数据库的私有成员变量：`Connection connection`、`PreparedStatement preparedStatement`、`String user`、`String pwd` 和 `String driver`。
画面 5: 在 `SinkToMySQL` 类中，为 `driver` 字段赋值为 `"com.mysql.jdbc.Driver"`，并开始定义 `StringBuffer sql` 变量。
画面 6: 在 `SinkToMySQL` 类中，声明了 `StringBuffer sql` 变量，并在 `open` 方法中准备初始化数据库连接。
画面 7: 在 `open` 方法中，使用 `Class.forName(driver)` 加载 MySQL JDBC 驱动。
画面 8: 在 `open` 方法中，使用 `DriverManager.getConnection(url, user, pwd)` 建立数据库连接，并创建 `PreparedStatement`。
画面 9: 在 `close` 方法中，检查并关闭 `PreparedStatement` 和 `Connection` 资源。
画面 10: 在 `invoke` 方法中，调用 `PreparedStatement` 的 `execute()` 方法执行 SQL。
画面 11: 在 `invoke` 方法中，调用 `setStatement` 方法设置参数。
画面 12: 在 `setStatement` 方法中，调用 `PreparedStatement` 的 `setString` 方法设置参数值。
画面 13: 在 `setStatement` 方法中，调用 `PreparedStatement` 的 `setString` 方法设置参数值。
画面 14: 在 `StreamingJob` 类中，展示了 `SinkToMySQL` 的使用方式，通过 `outStream.addSink(new SinkToMySQL())` 将数据流写入 MySQL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ithema.cold.flink;

import com.ithema.cold.common.entity.MessageEntity;
import org.apache.flink.streaming.api.functions.sink.RichSinkFunction;

public class SinkToMySQL extends RichSinkFunction<MessageEntity> {
}
```

画面 3:
```java
public class SinkToMySQL extends RichSinkFunction<MessageEntity> {
    @Override
    public void open(Configuration parameters) throws Exception {
        super.open(parameters);
    }

    @Override
    public void close() throws Exception {
        super.close();
    }

    @Override
    public void invoke(MessageEntity value, Context context) throws Exception {
    }
}
```

画面 4:
```java
import org.apache.flink.streaming.api.functions.sink.RichSinkFunction;

public class SinkToMySQL extends RichSinkFunction<MessageEntity> {
    //设置jdbc参数
    private Connection connection = null;
    private PreparedStatement preparedStatement = null;
    private String user = "cold";
    private String pwd = "cold123";
    private String driver = "com.mysql.jdbc.Driver";
```

画面 5:
```java
private String driver = "com.mysql.jdbc.Driver";
private protected
public PreparedStatement getPreparedStatement() {
    return preparedStatement;
}
```

画面 6:
```java
private StringBuffer sql = new StringBuffer();
```

画面 7:
```java
Class.forName(driver);
```

画面 8:
```java
connection = DriverManager.getConnection(url, user, pwd);
preparedStatement = connection.prepareStatement(sql);
```

画面 9:
```java
public void close() throws Exception {
    super.close();
    if(preparedStatement != null){
        preparedStatement.close();
    }
    if(connection != null){
        connection.close();
    }
}
```

画面 10:
```java
public void invoke(MessageEntity value, Context context) throws Exception {
    //TODO
    preparedStatement.execute();
}
```

画面 11:
```java
public void invoke(MessageEntity value, Context context) throws Exception {
    //TODO
    preparedStatement.execute();
}
private void setStatement(MessageEntity value) {
```

画面 12:
```java
private void setStatement(MessageEntity value) {
    preparedStatement.setString(1, value.getMotorcode());
    preparedStatement.setString(2, value.getMotorid());
}
```

画面 13:
```java
private void setStatement(MessageEntity value) {
    preparedStatement.setString(1, value.getMotorcode());
    preparedStatement.setString(2, value.getMotorid());
}
```

画面 14:
```java
//从redis中获取消息并和kafka流进行合并
DataStream<MessageEntity> outStream = stream.map(new MessageAggregate());
//写入mysql
outStream.addSink(new SinkToMySQL());
//写入kafka
FlinkKafkaProducer<String> mProducer = new FlinkKafkaProducer<String>(druid_topic, new SimpleStringSchema(), properties);
outStream.addSink(mProducer);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
