# 7.10 JDBC查询Druid数据

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day7 统计分析
- 源文件：06.阶段六 冷链监控平台项目\day7 统计分析\7.10 JDBC查询Druid数据_【海量资源尽在 666java.com】.mp4
- 时长 10分56秒（音频 657s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好 下面我们来介绍使用这种GDPC来查询Apache Dread因为我们通过前面的方式来查询可以了解到我们通过API接口或者是我们通过客户端那本质上来讲的话都是调用Dread的一个服务那么Dread服务Dread自己写了个API能查询数据库那为什么我们不能自己也写个程序也访问Dread的数据呢其实答案是一样的答案是可以的答案来讲的话为什么会能够访问
[00:30] 就是因为Apache Droid它用了一个叫Apache Callset的一个数据的一个管理框架或者换句话说我们把数据存储在某一个地方存储在某一个地方的时候呢那其实是中间用了Apache Callset来管理它那我给大家简单的画一下这个过程那简单的来讲的话是说画的不太准确但是呢应该是这么一个意思就是说我们
[01:07] 有一些数据这个地方是我们的数据对吧这些数据是Apache Dread的数据Dread的数据那我们有一个程序这个程序呢叫做Dread对吧无论是Dread的这个Dcircle的客户端还是我们的这种叫做什么呢叫做Web管理端那它本质上来讲的话是它要
[01:47] 调用我们的一个接口它调用后台的服务那么后台服务呢给它返回相应的一个结果对不对但是这个数据是一个存储它通过什么方式来达到这样的一个效果呢那它其实就是在这儿有一个叫Avetica叫Apache的Call SetCall Set这个中间层它通过这个中间层
[02:30] 来达到了数据的一个访问和数据的一个返回而Apache的call set的有一个客户端这个客户端呢或者说这个调用程序就叫做Apache call setcall set的Aviteca它其实就是Apache call set的Aviteca所以说Droid的客户端它访问了我们的
[03:06] 阿帕奇call set的Avetica然后Avetica它访问我们的数据那同样道理我们自己的应用我们的应用是不是也可以这样做呢我们的应用和阿帕奇Droid的它这个应用它其实是类似的对不对那我们的应用也可以这样调用所以说我们这儿就通过我们这种方式来访问我Droid的数据
[03:38] 那么我们使用Apache Call Set的Avetica GTBC的驱动来访问Apache Droid获得这种数据我们看一看这个程序如何来开发本身这个Droid的demo就是一个最简单的或者最基本的Mainware的一个工程那么我们来看一看POM文件我们需要在POM文件里边添加我们的Avetica的一个引用
[04:07] 就是dependency然后呢我们需要添加dependency的一个引用这种group id叫org.apache.这种call setcall set的这种ivtk然后它的artifact id呢是ivtk-call然后需要再添加一个worthy
[04:39] 而这个worthy呢是1.15.0那么它会把我们的这个Aptica的jar 包给添加进来那下一步的话我们就需要添加一个Java的一个类com.it黑马.demo.droid.wiki然后我们添加一个我们的这个命函数那么
[05:13] 我们如果开发GDPC程序我们需要几个步骤第一个步骤来讲的话是设置设置GDPC的参数第二步的话我们需要设置或者说我们需要执行circle语句第三步我们显示返回结果OK那么我们来看一看第一个
[06:00] 我们的GDP参数那首先呢我们可以定义我们的URL而这个URL就是和我们写其他的GDPC的URL是一样只不过它的区别在于在这的时候我们使用的是Avetica的GDPC的URL它是属于GDPC冒号Avetica冒号remote冒号URL等于http
[06:32] 然后我们的服务器的IP和端口172.17.0.143然后冒号80828082是我们的broker的一个端口我们也可以使用这个888848这个端口然后用dry的v2-circle-ivtk
[07:03] 这是我们的GDPC的URL那么下一个的话我们是需要设置我们的propertiesproperties等于newproperties这和我们开发其他的GDPC是一样的然后我们再添加一个circle这个circle是什么呢circle我们可以直接是selectingfromwikipedia
[07:35] 然后order by双下划线time然后dsc limit 10而这个serve语句呢其实是在我们的这个dread里面能够直接就执行我们来看一下我们的这个dreadok这个serve语句实际上是没有问题的通过dread的这个管理端的页面是能够直接返回结果的那么我们的gdbc查询也会查询这个
[08:11] 这个sql语句那下一步的话我们就执行我们的gdbc的查询了那首先我们再定义一个connection等于driver managerget connection而这个connection的参数一个是url一个是我们的properties那第二个的话是这个是我们的连接对吧数据库连接那第二个的话是我们的返回值
[09:11] 我们使用resultsetresultset等于connection.create statement然后执行execute query circleOK此时我们就执行了我们的这个circle语句那么下一步的话我们要返回我们的显示我们的这个查询结果对吧我们要对于一个
[09:44] result set来讲的话我们可以使用while result set点next然后它不断的循环然后呢我们把我们的这个结果给它展现出来而我们看一下这个结果里边有什么东西呢比如说有city name啊或者说有comment啊这是我们的每一条记录里边包含的我们直接把我们的配置给它显示出来result system out的present land点result set
[10:18] 我们用getString这个方法然后呢配置OK这个时候我们的开发就开发完了我们来执行一下OK此时的时候我们就能得到了我们的这个结果了这个结果就是查询的J的里边这张表里边的10条记录然后呢把字段是配置的给它显示出来

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码连接 Apache Druid 数据库并执行 SQL 查询。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程PPT内容，介绍 Apache Calcite 是一个动态数据管理框架，包含多个常用典型数据库系统的经典模块，省略了一些关键功能，如数据存储、数据处理逻辑和元数据存储，并给出示例代码片段。
画面2：在PPT中绘制了“Apache Druid”与“数据 druid数据”之间的双向箭头，表示 Druid 的数据管理能力。
画面3：在PPT中添加了“我们能应用”框，并在中间层标注“apache Calcite”和“apache calcite Avatica”，说明应用通过 Calcite 和 Avatica 与 Druid 数据交互。
画面4：展示 IntelliJ IDEA 中的 `pom.xml` 文件内容，添加了对 `org.apache.calcite.avatica` 依赖。
画面5：展示 `Wiki.java` 文件的初始状态，准备编写代码。
画面6：在 `Wiki.java` 文件中添加了注释“//1. 设置jdbc的参数”和“//2. 执行sql语句”。
画面7：在 `Wiki.java` 文件中编写了设置 JDBC URL 和 Properties 的代码。
画面8：在 `Wiki.java` 文件中，为 `Properties` 类添加了 `import java.util.Properties;`。
画面9：在 `Wiki.java` 文件中，为 `Connection` 类添加了 `import java.sql.Connection;` 和 `import java.sql.DriverManager;`。
画面10：在 `Wiki.java` 文件中，为 `DriverManager` 类添加了 `import java.sql.DriverManager;`。
画面11：在 `Wiki.java` 文件中，编写了 SQL 查询语句 `select * from wikipedia order by _time desc limit 10`。
画面12：在浏览器中打开 Apache Druid 的查询界面，显示了查询结果。
画面13：在 `Wiki.java` 文件中，编写了遍历 ResultSet 并打印结果的代码。
画面14：在 `Wiki.java` 文件中，编写了获取列标签并打印的代码，编译成功。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面4：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithems.demo</groupId>
    <artifactId>druid-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.apache.calcite.avatica</groupId>
            <artifactId>avatica-core</artifactId>
            <version>1.18.0</version>
        </dependency>
    </dependencies>
</project>
```

画面7：
```java
String url = "jdbc:avatica://http://172.17.0.143:8888/druid/v2/sql/avatica/";
Properties properties = new Properties();
```

画面11：
```java
String sql = "select * from wikipedia order by _time desc limit 10";
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面2：
- “Apache Druid” 框通过双向箭头指向 “数据 druid数据” 框。

画面3：
- “Apache Druid” 框通过双向箭头指向 “apache Calcite” 框。
- “apache Calcite” 框通过双向箭头指向 “数据 druid数据” 框。
- “我们能应用” 框通过单向箭头指向 “apache Calcite” 框。

5) 无

