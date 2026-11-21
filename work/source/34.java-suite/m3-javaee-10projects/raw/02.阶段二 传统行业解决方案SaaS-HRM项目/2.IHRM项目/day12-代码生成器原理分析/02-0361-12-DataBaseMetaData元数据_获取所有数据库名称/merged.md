# 12-DataBaseMetaData元数据：获取所有数据库名称

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\12-DataBaseMetaData元数据：获取所有数据库名称_【海量资源尽在 ubkz.com】.mp4
- 时长 4分34秒（音频 274s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那其实可以获取数据库基本信息呢这个其实应用的场景不太大那接下来呢我们再去看一下其他的方式好了接下来呢我们就开始去试一下获取数据库列表获取数据库的列表什么意思呢列表是这样的我准备啊直接传递我这个数据库127.0.13306
[00:33] 那接着我想获取一下这里面有多少个真真正正的数据库也就是我想把这些数据库列表全部都给我获取出来主要拿数据库名称可以吧所以接下来呢我们来看一下如何去做当然对于这个功能呢其实不难其实不难那接着我们来看一下首先呢这边呢我们ETA testpublic viewid test test02了那接着我们这边要做的事情首先呢第一件事是也是搞一个链接出来
[01:05] 那有了链接之后是不是也要获取原数据啊那对于这些内容呢我想说我可不可以把这个内容给它抽取一下来个ata before初始化一下那这样一来我写代码就轻松一些嘛不用写这些重复的那些工作了好了我主要目的就是获取一个链接抽取到最上方OK然后呢在我这个init方法当中让它自动帮我把链接获取到因为这个不是我们的重点OK这边呢用treadcatch处理一下
[01:43] 算了就直接死肉吧抛出最大了OK那这样一来抽取好了抽取好了之后我们这边关注我们这个数据库列表那数据库列表首先的第一件事也是获取原数据这个都是一模一样的我们通过原数据接下来要想方设法的得到所有的数据库列表抛出一场那这个数据库列表我们就是第二个操作那这个数据库列表如何去做呢metadata打点打点它有一个方法叫做get
[02:19] catalogok那他他选的是一个 result set那好了接下来呢result set 各位应该都不陌生我们可以直接通过 vail 循环的形式来对他进行一个处理rs.next 循环便利吗ok 好了这边 sot 我们来打印一下这rs 看一下他究竟是什么那最后呢千万别忘了这个rs 呢需要 close当然我们这个链接呢也需要 closecoconnection 打点 closeok
[02:55] 注意这边呢咱们使用debug的形式来看一下它究竟是什么内容可以吧好了那接着我们debug走好了各位来看目前呢已经进入到这个debug程序当中了我们也拿到了查询结果的第一条数据RS那这个RS在这边有显示我们可以打开一起简单的来看一下那对于这个RS我们要看什么注意看的其实是叫做fields这个程序fields
[03:28] 那这个Fields各位会发现RS里面它只有一条记录这个一条记录里面它的名称叫做什么呢叫做TableCat那注意注意那我们之前操作数据库的时候只要看一下Fields它有多少个我们是不是就可以通过RS打点Get的方式来进获取了所以我们都知道这回RS里面只有一条内容那我们来看一下
[03:58] RS打点get我就用死菌的形式去获取那我们现在它只有一条我们这边写1是不即可啊那接着我们一起运行一下看一下这回拿到的是什么内容哎各位会发现各位发现我发送查询catalog它其实得到的就是所有数据库它的名称没错吧我数据库名称呢就有informationsgamer好了hrmlotto等等等等我们可以对比一起来看一下
[04:27] 没错吧OK那这样一来其实我们就已经获取了数据库所有的列表

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库的基本信息和数据库列表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示测试类 DatabaseMetaDataTest 中的 test01 方法，用于获取数据库基本信息，包括驱动、URL、用户名、密码，并通过 DriverManager 获取连接，再调用 connection.getMetaData() 获取 DatabaseMetaData 对象，最后打印数据库用户名、是否支持事务、数据库产品名。
画面2：展示在 SQLyog 中查看数据库列表，弹出的数据库列表包含多个数据库名，如 information_schema、test、mysql 等。
画面3：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.supportsTransactions()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面4：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面5：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面6：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面7：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面8：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面9：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面10：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面11：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面12：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面13：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。
画面14：在 IntelliJ IDEA 中，光标位于 test01 方法的 System.out.println(metaData.getDatabaseProductName()); 行，IDE 提示可以按 Ctrl+Shift+Enter 选择建议或插入点。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```java
/**
 * 获取数据库基本信息
 */
@Test
public void test01() throws Exception {
    String driver = "com.mysql.jdbc.Driver";
    String url = "jdbc:mysql://127.0.0.1:3306?useUnicode=true&characterEncoding=utf8";
    String username = "root";
    String password = "111111";

    Properties props = new Properties();
    props.put("remarksReporting", "true"); //获取数据库的备注信息
    props.put("user", username);
    props.put("password", password);

    //1.获取连接
    Class.forName(driver); //注册驱动
    Connection connection = DriverManager.getConnection(url, props);

    //2.获取元数据
    DatabaseMetaData metaData = connection.getMetaData();

    //3.获取数据库基本信息
    System.out.println(metaData.getUserName()); //是否支持事务
    System.out.println(metaData.supportsTransactions()); //是否支持事务
    System.out.println(metaData.getDatabaseProductName()); //数据库产品名
}
```

画面2：
无代码，仅展示数据库列表。

画面3：
无代码，仅展示 IDE 提示。

画面4：
无代码，仅展示 IDE 提示。

画面5：
无代码，仅展示 IDE 提示。

画面6：
无代码，仅展示 IDE 提示。

画面7：
无代码，仅展示 IDE 提示。

画面8：
无代码，仅展示 IDE 提示。

画面9：
无代码，仅展示 IDE 提示。

画面10：
无代码，仅展示 IDE 提示。

画面11：
无代码，仅展示 IDE 提示。

画面12：
无代码，仅展示 IDE 提示。

画面13：
无代码，仅展示 IDE 提示。

画面14：
无代码，仅展示 IDE 提示。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

