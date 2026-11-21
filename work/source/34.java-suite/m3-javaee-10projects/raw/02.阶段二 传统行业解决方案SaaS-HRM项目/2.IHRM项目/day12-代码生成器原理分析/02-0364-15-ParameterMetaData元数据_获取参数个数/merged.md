# 15-ParameterMetaData元数据：获取参数个数

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\15-ParameterMetaData元数据：获取参数个数_【海量资源尽在 ubkz.com】.mp4
- 时长 5分15秒（音频 316s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们这个数据库原数据简单的说过了之后那接下来呢就是一个参数原数据那这个参数原数据呢一般呢用的范围比较小并且呢它支持的比较真实的方法呢也不多那首先需要跟各位说一下这个参数原数据呢叫做Parameter Metadata那是在经过了Prepare Segment也就是预编一对象处理数据或者处理我们Circle参数之后得到的这么一个原数据对象
[00:30] 通过这个原数据对象能够获取到你参数你circle参数里面的一个参数的个数参数的类型还有参数的其他的一些描述当然了这里面的方法它有很多但是据我个人测试并且参照了一些网站的一些说法它的参数原数据里面它可以使用的方法或者比较准确的方法就这么一个叫做getParameterCount它主要是为了获取参数的个数
[00:57] 那这个玩意Parameter Metadata也就是参数元数据主要目的就是对于一个Circle里面的一些占位符参数编译的过程当中得到一些它的一些真实信息那这个呢应用长久比较少我们可以简单的来看一下如何去用其实就可以了OK好了这边我拷一下这个名称创建一个我们参数元数据的一个测试类右键创建一个classtest测试参数元数据
[01:38] 它主要是通过ParameterStatement对象获取主要目的就是获取在Circle参数中的一些属性信息当然了一般来说用的这个用的比较少ETA testPublic VUID testOK那当然了我这些test方法里面呢既然要有Circle的一些参数其实就可以真真正正的写一个Circle与去发送一个查询
[02:15] 往里面添加一些参数来做了那比如说呢我要完成的就拿这个user来举例吧我就要发生一条搜索语句slag新from bs下滑线user好了where id等于一个值比如说我就查第一条那我的正常搜索语句写到这边没错吧OK那好了我就按照这种方式咱们一起来看一下如何去做搜索语句先写到这OK那首先上边呢跟之前一样我先去搞到connection注意这个connection我就
[02:49] 跟这边一样了直接拿到的就是这个IHMO这个数据库链接OK这个语句写起来也比较简单也不难也不难我们一起来看下讲义吧我直接从讲义上就拿过来了OK靠过来印下包Connection那各位能够看到各位能够看到首先呢这是一条Circle语句后面有一个站位符那我经过预编译对这个Circle语句进行一个编译的过程那接着对这个站位符进行复制没错吧
[03:40] OK那这样一来那这样一来我们就可以通过注意这上面是我们的基本伺候语句的写法接下来我们就开始去获取参数元数据那这个参数元数据如何去获取其实就可以借助我们的prepare statement来做了这边把这个异常处理一下prepare statement打点get parameter metadata这样一来就能获取到参数元数据那获取到了参数元数据那接下来metadata打点get parameter count
[04:20] 这样一来其实就能够得到我所有的参数的个数我们可以打印一下来看一下效果来走好了我现在一共就一个参数没错吧所以这个方式也是没什么问题的但是我想说啊这个mental date里面除了这个get parameter metal除了这个get parameter count之外它还有很多个方法这些方法呢比如说呢有得到它的渣滓类型的还有知道它的
[04:52] 在circle的类型还有java的类型等等等等很多种方法比如说还有得到它的小数位数但是那几个方法都不太准确所以对于这个参数元数据来说我们一般用只用第一个就这个看一下它有多少个参数可以吧所以这个方法呢咱们作为一个了解各位知道就可以了一般用的比较少OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 PreparedStatement 获取参数元数据（ParameterMetaData），并演示了如何使用 getParameterCount 方法获取 SQL 语句中占位符参数的个数。

2) 按时间顺序列出每张画面的要点：
画面1: 展示课程 PPT 的目录结构，当前选中“3.3 参数元数据”。
画面2: PPT 页面显示“3.3 参数元数据”章节内容，介绍 ParameterMetaData 是由 PreparedStatement 通过 getParameterMetaData 方法获取，主要提供占位符参数个数和 SQL 类型等信息。
画面3: 展示 IntelliJ IDEA 中的项目结构，选中了“ParameterMetaDataTest.java”文件，右键菜单显示了“Run Tests in 'cn.itcast.metadata.test'”等选项。
画面4: PPT 页面显示“3.3 参数元数据”章节内容，下方有“黑马程序员”的水印。
画面5: 展示 IntelliJ IDEA 中的项目结构，选中了“ParameterMetaDataTest.java”文件，代码编辑器中显示了该类的开头部分。
画面6: 展示 SQLyog 数据库管理工具界面，显示了“bs_user”表的数据，其中包含 id、username、password 等字段。
画面7: 展示 IntelliJ IDEA 中的“DatabaseMetaDataTest.java”文件，代码中定义了连接数据库的 URL、用户名、密码等配置。
画面8: PPT 页面显示“3.3 参数元数据”章节内容，下方有“黑马程序员”的水印。
画面9: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中定义了 init 方法用于建立数据库连接，并在 test 方法中使用 PreparedStatement。
画面10: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法使用了 PreparedStatement 的 setString 方法设置参数值。
画面11: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法使用了 PreparedStatement 的 setString 方法设置参数值，光标位于 setString 方法的参数位置。
画面12: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法注释了 setString 方法，添加了获取参数元数据的代码。
画面13: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法添加了获取参数元数据的代码，并在控制台输出了参数个数。
画面14: 展示 IntelliJ IDEA 中的“ParameterMetaDataTest.java”文件，代码中 test 方法添加了获取参数元数据的代码，并在控制台输出了参数个数。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7:
```java
import java.util.Properties;

//测试数据库连接
public class DatabaseMetaDataTest {
    private Connection connection,

    @Before
    public void init() throws Exception {
        String driver = "com.mysql.jdbc.Driver";
        String url = "jdbc:mysql://127.0.0.1:3306/thrm?useUnicode=true&characterEncoding=utf8";
        String username = "root";
        String password = "111111";

        Properties props = new Properties();
        props.put("remarksReporting", "true");//获取数据库的备注信息
        props.put("user", username);
        props.put("password", password);

        //1.获取连接
        Class.forName(driver);//注册驱动
        connection = DriverManager.getConnection(url, props);
    }
```

画面9:
```java
//sql = SELECT * FROM bs_user WHERE id = '1063705482939731968'
@Test
public void test() throws Exception {
    String sql = "select * from bs_user where id=?";
    PreparedStatement pstmt = connection.prepareStatement(sql);
    pstmt.setString(1, "1063705482939731968");
}
```

画面10:
```java
//sql = SELECT * FROM bs_user WHERE id = '1063705482939731968'
@Test
public void test() throws Exception {
    String sql = "select * from bs_user where id=?";
    PreparedStatement pstmt = connection.prepareStatement(sql);
    pstmt.setString(parameterIndex: 1, "1063705482939731968");
}
```

画面12:
```java
//获取参数元数据
ParameterMetaData metaData = pstmt.getParameterMetaData();
int count = metaData.getParameterCount();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

画面4: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

画面8: PPT 标题为“3.3 参数元数据”，内容为“参数元数据（ParameterMetaData）：是由 PreparedStatement 对象通过 getParameterMetaData 方法获取而来，主要是针对 PreparedStatement 对象和其预编译的 SQL 命令语句提供一些信息，ParameterMetaData 提供占位符参数的个数，获取指定位置占位符的 SQL 类型等等。以下有一些关于 ParameterMetaData 的常用方法：getParameterCount：获取预编译 SQL 语句中占位符参数的个数。”

5) 不要评价画面美观，不要输出与课程无关的内容。

