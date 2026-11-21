# 11-DataBaseMetaData元数据：获取数据库基本信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\11-DataBaseMetaData元数据：获取数据库基本信息_【海量资源尽在 ubkz.com】.mp4
- 时长 11分35秒（音频 695s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们接下来呢就开始针对刚才说过的三种原数据一个一个来看一下如何去做首先呢就是第一个通过Connection获取的数据库原数据当然了我们是翻译的数据库原数据它的全称呢其实就是Database Metal DateMetal Date代表就是原数据的意思好了这个是由Connection对象获取而来的主要是封装的数据库
[00:25] 本身的一些综合的一些信息比如说数据库的一些名称版本号你输入的用户名和数据库的密码等等当然除了刚才说的这些还有一些更加高级的一些用法比如说可以通过Database Metadata可以获取整个数据库所有的表可以获取表当中的所有的字段等等所以针对咱们数据库原数据而言Database Metadata它的功能其实就是比较强大的
[00:53] OK那针对这些呢它有很多的方法这些方法呢咱们一会儿一个一个简单的来看一下我这边就不跟各位一个一个去读了那这个有点浪费时间那好了接下来呢我们就可以一起写一点点程序来看一下数据库原数据应该如何获取我们应该如何使用它哎来在这边呢我们跟之前一样首先呢也是写一个搭建环境的这么一个过程那对于搭建环境呢其实我们这边呢就是通过JDBC的形式
[01:23] 获取一个Connection那通过Connection的方法得到Metadata所以这边呢我需要补充一个依赖就是我们的MySQL驱动那有了驱动之后才能获取到我们的Connection对象没错吧OK好了接下来呢我们回到代码部分打开碰文件好了MySQL驱动呢刚才我们已经把它引入进来了所以接下来呢我们直接写一些代码来测试一下数据库它的原数据好了同样的我也写到Test这个目录下
[01:55] 右键创建一个classsin.itcast.这回呢就叫metadata.test好了给它起一个名称呢我就叫做databasemetadata.testok测试库原数据ok好了接下来呢我们这边etatestpublic vid test01好了这个测试我们要测试点什么呢咱们就测试一些获取
[02:30] 数据库基本信息的因为我们刚才说过了这个数据库原数据呢database metadata它其实是一个功能比较强大的这么一个原数据所以呢通过它来说呢它也是我们一个原数据里面一个比较重要的一环所以对于我们来说呢这里面呢除了获取数据库基本数据信息之外还能获取到其他的那这些呢可能跟我们写我们的代码生成器有关所以把这些基本内容都跟各位补充一下所以讲这一块内容可能稍微花费一点点时间
[02:59] OK好了那接下来在这里面我们应该如何去做那获取数据库的基本信息通过的是Database Battle Date那这个玩意怎么获取的刚才我们说过了是不是首先第一步要获取链接那获取了链接之后接着第二件事才是去获取我们的原数据好了接着第三件事根据原数据获取数据库的基本信息所以这些代码所以这个操作步骤比较简单
[03:30] 比较简单但是代码呢可能会有点点麻烦或者一些啰嗦OK好了第一个获取链接那针对这个获取链接呢这玩意儿其实如果各位经常写Java或者咱们经过不断的学习第一个接触操作数据库的就是原生的GDPC操作吧所以对于这个驱动获取数据库链接来说呢class.forname注册驱动好了接着在这边呢我们可能还要涉及到一些其他内容比如说呢
[04:06] 叫做connection叫做driver manager.getconnectiongetconnection我们就可以获取一个链接了当然了获取链接的过程当中这边需要这么几个参数这几个参数首先我们需要死菌类型的driver还需要死菌类型的url还需要死菌类型的叫做username还需要死菌类型的pass
[04:48] 好了那这边呢我先把把这个基本的写到去上方吧好了接下来呢我们driver大家说我之前说过了我们现在使用的是mycircle数据库所以驱动com.mycircle.jd.jdbc.driver好了urlurl后呢这边我就用我本地的数据库了我们打开本地的数据库就是当前我这个数据库OK好了接着回到idea那我这个url地址呢
[05:23] GDBC冒号mycircle冒号好了杠杠127.0.0.1冒号3306这是我们的数据库地址OK当然如果你想写的更加完整一点我从咱们之前的代码这边call一下call一下主要是为了加上后面这些字符集的一个处理好了各位
[05:50] 需要注意的是我直接指定的是我数据库的根地址没有指定我用具体用是哪一个没错吧所以它其实代表的就是我们这个数据库的根地址在这边那通过数据库根地址呢其实我能够得到数据库里面的所有的数据库的这些内容当然它也可以受到整个的基本数据OK好了那接着我的用户名root好了我的密码
[06:19] 123456那接下来呢我们可以把这个代码简单的补充一下driver驱动好了这边呢class.follow name注册驱动之后呢我们可以获取链接获取链接呢可以看一下它有很多的方法这些方法呢这些方法呢第一个直接把我们的用户名密码还有地址传进来这种方式是我们常见的一种方式那除了这种方式之外还有一种就是把一些数据呢封装到properties配置文件里
[06:51] 这两种哪一种都可以当然了我们这边用的是property配置文件的主形式所以在这边我去创建一个property配置文件等于new一个properties好了接着我这个properties开始往里put值点put其实put的这些值基本都比较简单了好了第一个useruser name好了第二个properties点put好了第二个就存着我们的密码就可以了
[07:29] OK那好了接着接着那我们借助的是properties的这种方式往里存那往里存的时候首先这边第一个参数UIL第二个就是我们properties的一个文件OK那接着我想跟各位来声明一下为什么我要有这种方式存其实这种方式存这么写跟刚才三个参数那种写法是一样的主要要这么写的考虑其实就是说呢在获取原数据的时候我们可以指定一个参数
[07:58] 这个remarking reporting主要目的就是为了获取数据库的备注如果咱们用传统那种写法的话数据库备注获取的会是空那这个如何配置呢同样也是purpose.put那put的名称叫做remarksreporting这个主要目的把它设置为处啊抱歉把它设置为处这个主要目的呢就是为了保证获取数据库的备注信息
[08:33] 如果你不是不设置的话在某些数据库里面可能会是空啊ok 好了这样一来我驱动就已经搞定了这边有异常我处理一下我就直接搞最大的哎 其他异常没问题那接着链接咱们已经搞定了那有了链接之后就是获取原数据那获取原数据比较简单我们直接可以通过connection打点get dataget
[09:04] MetalMetalData那这样一来我们就能够得到这个DatabaseMetalData好了这个MetalData我们获取到了之后我们就可以获取想要的一些内容比如说呢MetalData打点Get就一顿Get就行了那这里面呢就有很多的内容就有很多的内容比如说呢我们可以拿一个数据库的用户名GetUserNameSOT打印出来
[09:39] 那除了获取用户名之外呢还可以获取其他的内容比如说呢可以获取它是否支持事物打点getspottingget不是getspottingspottingsupportstransactionsok这个是获取是否支持事物当然除了这些内容之外呢还有很多的其他的一些
[10:13] 基本数据的一种获取方式在我这边呢都给各位罗列出来比如说Eso Read Only是否是只读还有获取驱动的版本号等等这些全部都属于基本的一些内容当然还能获取Database Product Name.getDatabase Product Name就是获取我们数据库的类型它的名称好了都把这些呢打印出来一起来看一下效果
[10:46] 好了这边都配置好了之后来启动走那这边报了一个空置针是吧来看一下哪有问题这个问题哦在这儿就是说我们properlyput的时候呢全部都用string往里传植啊不应该直接写出OK好了那接下来我们再来试一下走哎各位来看现在呢其实我已经把基本的信息已经打印出来了我们这边呢是root
[11:24] 访问的是本地的数据库好了是否支持是确实支持让我们的数据库是买四个口没错吧OK那这样一来其实我们就玩了一个最简单的获取了数据库基本信息OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 的 DatabaseMetaData 接口获取数据库的基本信息，包括数据库产品名、版本号、用户名、驱动版本号、是否支持事务等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT内容，标题为“3.2 数据库元数据”，子标题“3.2.1 概述”，介绍DatabaseMetaData是Connection对象通过getMetaData方法获得，封装了数据库基本信息，并列出常用方法如getDatabaseProductName、getUserName等。
画面2：在IDEA中，项目结构显示，正在创建一个新类，同时展示pom.xml中已添加的freemarker依赖。
画面3：在IDEA中，创建了名为DatabaseMetaDataTest的测试类，开始编写测试方法test01。
画面4：在IDEA中，编写代码，准备获取数据库连接，注释为“//1. 获取元数据”。
画面5：切换到另一个项目ihm_parent，展示application.yml文件。
画面6：在SQLyog中，显示数据库列表，包括test、test1、test2等。
画面7：在IDEA中，编写代码，准备获取数据库连接，注释为“//1. 获取元数据”。
画面8：在IDEA中，编写代码，设置数据库连接参数，包括驱动、URL、用户名、密码。
画面9：在IDEA中，编写代码，获取数据库元数据对象。
画面10：在IDEA中，编写代码，调用getUserName方法获取用户名。
画面11：在IDEA中，编写代码，调用supportsTransactions方法检查是否支持事务。
画面12：在IDEA中，编写代码，调用getCatalogs方法获取数据库目录。
画面13：在IDEA中，运行测试，测试失败，提示java.util.Hashtable.put异常。
画面14：在IDEA中，修正代码后运行测试，测试通过，输出结果为true和MySQL。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```xml
<dependency>
    <groupId>org.freemarker</groupId>
    <artifactId>freemarker</artifactId>
    <version>2.3.28</version>
</dependency>
```

画面8：
```java
String driver = "com.mysql.jdbc.Driver";
String url = "jdbc:mysql://127.0.0.1:3306?useUnicode=true&characterEncoding=utf8";
String username = "root";
String password = "111111";
Properties props = new Properties();
props.put("remarksReporting", "true"); //获取数据库的备注信息
props.put("user", username);
props.put("password", password);
```

画面9：
```java
Class.forName(driver); //注册驱动
Connection connection = DriverManager.getConnection(url, props);
DatabaseMetaData metaData = connection.getMetaData();
```

画面10：
```java
String userName = metaData.getUserName();
```

画面11：
```java
boolean supportsTransactions = metaData.supportsTransactions();
```

画面12：
```java
String[] catalogs = metaData.getCatalogs();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“3.2 数据库元数据”，子标题“3.2.1 概述”，内容包括DatabaseMetaData的定义和常用方法列表。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

