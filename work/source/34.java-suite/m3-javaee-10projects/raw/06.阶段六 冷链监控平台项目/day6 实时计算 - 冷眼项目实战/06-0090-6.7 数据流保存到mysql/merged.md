# 6.7 数据流保存到mysql

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day6 实时计算 - 冷眼项目实战
- 源文件：06.阶段六 冷链监控平台项目\day6 实时计算 - 冷眼项目实战\6.7 数据流保存到mysql_【海量资源尽在 666java.com】.mp4
- 时长 13分58秒（音频 839s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,下面我们来开发把数据结果集也就是数据流存储到MySQL那么它实际上是在AddSync里边调用的那么我们在这里边实际上需要开发一个叫SyncToMySQL的一个类那么首先我们创建我们的Java的类叫SyncToMySQL而这个类呢它需要ExtendExtend我们的ReachSync function
[00:29] RigThink function它的数据流里边的数据类型是messageEntity那么此时我们需要复写我们的一个方法这个方法包括open close还有一个我们的invoke方法override invoke那open的意思是说当我拿到一个数据的时候
[01:04] 当我拿到数据集数据流里边的一个message in title的时候那么我首先我要进行一个连接我的数据库然后呢evoke就是我要执行我的一个数据结果那close当然我就需要把我的连接数据库的这种资源给它释放掉比如说像我们的connection或者说像我们的prepared statement这些我们都给它释放掉这是我们在我们这个方这个类里边要做的一些事情
[01:33] 那首先我们来创建或者说添加一些我们的一些参数而这些参数实际上是GDPC的一些参数设置GDPC参数那这个参数来讲包括我们的一个private connection等于空然后呢private prepared statement也等于空下面的话是我们的这个
[02:13] 数据库的一些属性这些数据库的属性包括我们的数据库的 username也可以我们的password那接着是我们数据库的driver就是GDPC它的一个驱动driver等于什么呢com.mycircle.gdpc.driver这是我们的GDPC的一个驱动的字符try然后
[03:04] 下面我们再写我们的UIL这个URL是我们连接MySQL数据库的时候我们需要写的一个属性比如说实际上是什么GDPC 双斜杠我们的不是双斜杠是MySQL然后此时我们是双斜杠IP地址0.143然后3306
[03:34] 然后呢再加上我们的数据库codecode我们可以再加上我们其他的一些参数比如说像allowallow什么呢allowmultiquaries等于 true并且我们要用我们的useunicode等于 true然后呢我们还可以再加上我们的这个字符出来的连接
[04:09] 这种字符集的话是属于叫做calric encoding-utf-8这是我们在这里边要添加的一个当然我们还可以再加上其他的一些属性其他的属性信息比如说像我们的这个useSSL等于false并且呢
[04:40] 并且我们的这个usss等于false并且我们要使用all to reconnection等于true这是我们的这几个参数而这几个参数来讲的话是让它定义好我们的数据库我们数据库的连接GDPC连接驱动那下一步的话其实我们是需要定义我们的一个叫
[05:09] 第一我们的一个circle语句而这个circle语句是需要进行拼接的一个circle语句它是通过我们的当前的数据流里给的message entity这个数据集来拼接成我们的一个数据的数据库的一个插入或者说替换的或者replace into的这样的一个circle语句那么这个circle语句我们可以定义一个circle类型的circle类型因为是拼接的话所以说我们用string buffer吧circle等于newstring
[05:40] 然后在我们创建的时候我们当然我们可以在这里边我们设置我们的这个数据库的拼接的语句但是我现在呢实际上是我只是把它放到我们这个sql语句放到哪呢放到我们的这个构造函数里边来加的那么我先看现在看一下我们这个一个是open一个close一个invoke那么我们加我们的加我们的那个什么呢构造函数public
[06:10] public mysync,sync to mycircle然后在这里边的时候我拼接构造我的circle语句在这个地方我构造circle语句那么我们在我们的open里边我们要添加什么呢我们要添加我们的连接的一些属性这种连接属性包括我们的class.forName就发什么name呢driver对吧我们用的是
[06:43] for driver class的,然后connection等于driverManager.getConnectiongetConnection里面包括我们的URL,我们的user,包括我们password,密码,用户名和密码,都是连接的。
[07:03] 那么我们再准备我们的prepared statement等于connection.prepared statement。
[07:13] 这个时候我们要把我们的circle.g来放进来。
[07:17] 这个就是我们在open的时候我们要进行这个预处理的搜索语句那close的时候啊close相对来讲也比较简单一些如果我们的它的主要作用是关闭数据关闭数据的这个资源而这种关闭数据资源的时候我们就是如果我们的prepared statement不等于空那其实我们要把prepared statement然后关闭close对吧那如果是我们的这个connection呢
[07:46] 不等于空我们要把我们的connection也给它关闭ifconnection不等于空那么我们要把connection给关闭OK这就是我们在close里边那重要的是我们在invoke里边来添写的那么invoke里边添加的时候呢我们可以使用的是什么呢我们要第一我们要构造构造
[08:19] prepare的就是实际上是给prepareprepare的statement添加添加数据是吧那么这个数据从哪来呢数据是value那第二部分来讲的话其实就是我们的prepare的一个statement的执行执行色彩绘OK这样的话其实是是可以的对不对这样可以来讲的话
[08:54] 那我们现在还有两个啊一个是我们的构造我们的circle一句构造circle一句相对来讲比较简单但是比较繁琐prepared void然后circle要get circle的话我们实际上是有spin的screw的appendappend什么呢replace into我们的数据库表明vvmessage real time
[09:33] 然后呢我们再加上我们的meter code然后呢meter idmeter name那么一直添加添加完这些字段之后呢我们就有一个valuesvalues加上问号比如说我们在我们的这个方法里边一直添加到最后
[10:13] 在中间我只是给它省略了一下那么我们实际的时候我们需要把我们这个字段给它都补全上我为了在这儿为了给大家节省时间我们在这儿其实不需要写那么多了比如说在这里写host id或者说host的一个code或者是host name等等这是我们的这个circle一句那在这里边的话我直接就调用这个circle一句就行了那我有了circle一句之后
[10:50] 我们需要给我们的这个statement来添加我们的数据集那添加数据集我可以在这里面写那我为了稍微这个好看一点或者结构化一点我给它添加一个一个方法set这个statement然后呢它的参数是message entitymessage entity的这个value然后我们要prepare的statement
[11:25] .setString这个setString1的第一个字段是我们的value.getMeterCode这个这个这个它没有向上把我们的异常给它暴露出来那同样道理我们一直是这个填写prepare的getStringMeter.setString
[12:00] 然后第二个字段的话是value.getmeterid那么一直写一直写到最后我们到把我们所有的字段全部添加进来prepared.setstring然后是第23个字段我记得是value.getuntimed在中间其实是
[12:38] 省略了很多直接把这个给添加上去就行了我在这里边我在这个invoke方法里边我就直接set这个statementset a statement实际上有一个value这个参数这样的话其实就可以了那我们从就简单的回顾一下我们当前的这个方法其实就是把我们的数据流中的一个message entity这种数据类型的数据然后呢把它
[13:09] 用GDPC连接的方式存储到我们的MySQL数据库里面而MySQL数据库我们连接的时候我们用了三个方法因为它是extend我们的richsync function这个类那么三个方法一个是open方法一个是close方法一个是invoke方法open方法它要连接我们的MySQL数据库那close的话是把我们的资源给它释放掉
[13:34] 那invoke的话就是执行我们的circle语句那在这里边的话我们需要拼接我们的circle语句以及给我们的circle语句的这个statementprepared statement然后给它添加我们的参数数值就是从数据流里边拿到的这个数值那么这个就把我们的数据存储到我们的mycircle里边去了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
package com.ithema.cold.Flink;

import com.ithema.cold.common.entity.MessageEntity;
import org.apache.Flink.streaming.api.functions.sink.RichSinkFunction;

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
import org.apache.Flink.streaming.api.functions.sink.RichSinkFunction;

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
//从redis中获取消息并和Kafka流进行合并
DataStream<MessageEntity> outStream = stream.map(new MessageAggregate());
//写入mysql
outStream.addSink(new SinkToMySQL());
//写入Kafka
FlinkKafkaProducer<String> mProducer = new FlinkKafkaProducer<String>(druid_topic, new SimpleStringSchema(), properties);
outStream.addSink(mProducer);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

