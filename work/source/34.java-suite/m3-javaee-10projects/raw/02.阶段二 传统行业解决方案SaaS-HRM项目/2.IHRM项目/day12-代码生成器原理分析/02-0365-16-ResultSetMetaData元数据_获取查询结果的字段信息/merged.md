# 16-ResultSetMetaData元数据：获取查询结果的字段信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\16-ResultSetMetaData元数据：获取查询结果的字段信息_【海量资源尽在 ubkz.com】.mp4
- 时长 10分8秒（音频 609s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 刚才和各位简单的看了一下参数元数据接下来就是元数据里面最后一种类型就是结果级元数据这个结果级元数据是通过查询之后得到的result set获取到的所以叫做result set metadata它的主要目的其实就是获取到查询结果相应的一些数据比如说我们通过一个搜索语句来进行一个举例说明比如说就是它
[00:29] 那slack星一执行我得到了所有的内容得到了很多的内容那得到了很多内容我们这样一来就能够得到你当前查询出来的所有的列你这个词后一句所有的列名也能够得到每一列它的类型它的属性能理解吧所以对于这个呢是也是在Metadata里面用的比较普遍或者广泛的一种结果一种一种元数据那这种元数据一般应用到什么地方呢
[00:58] 这个result set结果级元数据一般应用在很多的我们ORM框架里面比如说my-based框架比如说havenly的框架里面都有这种结果级元数据在里面因为各位会发现我直接有了结果级元数据之后比如说我这个ID什么什么968它其实代表的就是用户的ID那这样一来ID字段你有了
[01:24] 那其实这个ID字段应该代表的就是某一个实体类里面的ID属性那它是不是通过反射直接复制啊所以这种元数据一般大量应用在这种OM框架当中能理解吧OK那好了对于这个结果级元数据它有很多个方法当然了这个方法我只是罗列了一些用的比较多的还是跟之前一样如果各位感兴趣的话可以参考给各位下发的这个JPI文档OK那好了我们简单的写一个案例一起来看一个
[01:55] 就是看一下这个result setmetadata应该如何去使用好了这边呢回到我的代码部分右键创建一个测试类测试结果级元数据OK这个结果级元数据是通过result set获取并且它的主要目的就是获取查询结果的相应信息OKata testpublic
[02:42] 算了这段我不想写了我抄一下能原谅我是吧OKConnection链接拿过来好了接下来呢这边Circle语句拿过来因为我们这个结果结论数据呢是真真正正的要发送查询得到相应的数据得到相当内容OK好了那这边把这些没用的都删掉把这些没用的都粘掉好了那这其实就是我们刚才的这段代码只不过呢我写了定义了Circle语句定义了PrepareSemin
[03:21] prepare statement的对象那对站位符进行复制那接下来我们开始进行真正的查询查询比较简单pstmt打点我叫acute queryOK那这样一来就发送了查询得到我们的result set那好了有了result set注意这一回我们可以通过result set打点get myto date那这样一来我们得到的其实就是结果结果数据
[03:54] OK有了结果局原数据那就好玩了那MetalData里面比如说呢我们可以获取查询的字段个数那注意我这个slash from BS user其实代表的是查询字段这里面所有的字段是不是都要查询出来啊OK那如何去做MetalData打点get column count
[04:23] OK那这样一来有了column count那接下来呢比如说我想看一下你查询出来的这个结果当中的这个列这个列名究竟叫什么那这个列名如何获取呢同样可以通过metadata打点get count name的形式来做注意get count name那get column name那这个name你会发现它有一个参数你究竟查询的是第几列那比如说我想查询第一列我就写1其实就可以了
[04:51] 那有的朋友说我如果想要查询所有的链那我应该怎么办呢那很简单注意你这不是有的总的自断个数了吗那总自断个数那我们可以做一个for循环int i等于1i小于等于比如说叫做count i++OK那好了接下来countCtrl CCtrl V
[05:26] 那这样一来呢它开始一个一个的进行获取那注意我这边就是根据i来进行获取了注意在这个原数据获取数据的过程获取column name的时候i的索引是从1开始的千万别写错OK这边sot打印一下column name列名OK那当然了除了这几个方法之外呢还有很多的方法还有一个常用的比如说column type对应的类型对应的类型
[06:03] 那我们一起来看一下打点get column type同样也把爱传进去加上column type写点注释OK当然除了这个之外呢还有比如说呢class namemetadata打点get classget class哦抱歉get column class name列的类型名字
[06:54] OK那我们再来打印一下看一下它获取的对不对啊那这边我想跟各位说一下这个字段类型是指的是Circle的字段类型Circle类型里面的那这个ClassName指的是获取Java的这个类型那对于Circle类型来说呢可能代表的是WhatchaWhatcha2或者其他的类型那对于的翻译成Java来说是不是就是死菌呀能理解吧各位OK那接着我们一起来看一下
[07:29] 它究竟能不能获取到这些数据来走好了各位来看首先IDcolumnNamecolumnType这个circle类型其实是对的其实是对的但是这个咱们一会儿再跟各位简单的解释一下那其实呢这个columnNamecolumnType咱们可以这样去做它有一个叫做columnTypeName那这个Type呢它代表的含义其实在
[08:05] 在这个metadata当中它是通过数字的形式来进行一个体现比如说12它其实代表的就是瓦刹比如说还有一些4代表的是一个数字比如说93其实代表的是data time这些那我们用这个数字看的不太直观所以这边呢可以用type name来获取它真正代表的含义能理解什么意思吧所以这边应该用死菌来进行获取这种比较方便一些其实这个12也是对的也是对的只不过它是用数字的形式来表示的
[08:33] 能理解吧OK那好了我们再去执行一下看一下OK各位就会发现了ID代表的是Whatch那代表的是Street好了MobileWhatch代表的是Street好了Int代表的是Integer好了Datatime代表的是TimeStream没错吧OK那这样一来其实我们就已经看到了这个结果结源数据它能够做的事情其实就是获取到你查询出来的这每一列它的名称
[09:05] 它代表的Circle的类型它代表的可以翻译成Java的类型其实除了这些还有其他的一些细节那对于这些细节各位有兴趣的话参照API自己去看就可以了OK那到目前为止呢其实我们这个数据库原数据的内容就跟各位都说过了那数据库原数据我们关注的它是什么其实就是能够通过我们Java的一些操作获取数据库定义的一些结构上面的内容比如说能够得到数据库它所有的库的名称
[09:35] 可以得到某一个库当中所有表的名称可以得到某一个表里面所有列的名称也可以得到你发送每一个sql的参数的所有情况也能得到你执行某一个sql语句返回的结果集当中的它究竟有多少列列的一些相关属性如果说能够运用到这些元数据或者运用好这些元数据的话能够帮助我们加深对框架的影响
[10:01] 能够帮助我们完成最终的我们这个代码生成器的一个搭建工作OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码获取数据库查询结果集的元数据信息，包括列名和列类型。

2) 按时间顺序列出每张画面的要点：
画面1：展示数据库表结构，查询 `bs_user` 表数据，用于后续测试。
画面2：展示 PPT 内容，讲解 `ResultSetMetaData` 的概念和常用方法。
画面3：展示项目结构，重点是 `application.yml` 配置文件。
画面4：展示 `ResultSetMetaDataTest.java` 文件，准备测试代码。
画面5：展示 `ParameterMetaDataTest.java` 文件，用于测试参数元数据。
画面6：展示 `ResultSetMetaDataTest.java` 文件，编写 SQL 和 PreparedStatement。
画面7：在 `ResultSetMetaDataTest.java` 中调用 `rs.getMetaData()`。
画面8：在 `ResultSetMetaDataTest.java` 中获取列数 `getCount()`。
画面9：在 `ResultSetMetaDataTest.java` 中使用 `for` 循环遍历列。
画面10：在 `ResultSetMetaDataTest.java` 中添加打印列名的代码。
画面11：在 `ResultSetMetaDataTest.java` 中添加打印列类型的方法 `getColumnTypeName()`。
画面12：运行测试，输出列名及其 Java 类型。
画面13：运行测试，输出列名及其 SQL 类型。
画面14：展示 PPT 内容，页面为空，可能为过渡或结束页。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3 - application.yml：
```yaml
#微服务注册到Eureka
Eureka:
  client:
    Service-url: http://localhost:6868/Eureka
  server:
    port: 9002
spring:
  #服务名配置
  application:
    name: ihrm_system #指定服务名
  #数据库配置
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
    #jpa
    database: MySQL
    show-sql: true
    open-in-view: true
    redis:
      host: 127.0.0.1
      port: 6379
    jwt:
      config: 
```

画面5 - ParameterMetaDataTest.java：
```java
@Before
public void init() throws Exception {
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306/ihrm?useUnicode=true&characterEncoding=utf8";
    String username = "root";
    String password = "111111";
    Properties props = new Properties();
    props.put("remarksReporting","true");//获取数据库的备注信息
    props.put("user",username);
    props.put("password",password);
    //1.获取连接
    Class.forName(driver);//注册驱动
    connection = DriverManager.getConnection(url,props);
}
```

画面6 - ResultSetMetaDataTest.java：
```java
String sql = "select * from bs_user where id=?";
PreparedStatement pstmt = connection.prepareStatement(sql);
pstmt.setString(parameterIndex, "1", "1863705482939731968");
```

画面7 - ResultSetMetaDataTest.java：
```java
ResultSetMetaData metaData = rs.getMetaData();
```

画面8 - ResultSetMetaDataTest.java：
```java
int count = metaData.getColumnCount();
```

画面9 - ResultSetMetaDataTest.java：
```java
for(int i=1;i<count;i++){
```

画面10 - ResultSetMetaDataTest.java：
```java
String columnName = metaData.getColumnName(i);
System.out.println(columnName);
```

画面11 - ResultSetMetaDataTest.java：
```java
String columnType = metaData.getColumnTypeName(i);
System.out.println(columnName+"---"+columnType);
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：PPT 标题为“3.4 结果集元数据”，内容包括 `ResultSetMetaData` 的定义和常用方法。
画面14：PPT 标题为“1.4 数据库之元数据”，内容为空。

5) 无。

