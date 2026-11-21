# 16-shiro认证与授权：基于ini的用户认证

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day05 JWT的权限控制与Shiro入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day05 JWT的权限控制与Shiro入门\16-shiro认证与授权：基于ini的用户认证_【海量资源尽在 ubkz.com】.mp4
- 时长 15分50秒（音频 950s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的看了一下Shadow内部结构我们得知对于我们来说使用Shadow其实就是关注它的Subject以及Rule还有我们如何把Rule放到Security Manager当中去使用那接下来我们就可以一起写一些入门的一些案例来看一下Shadow它内部究竟是如何做到认证如何做到授权还有我们的Rule应该如何去进行编写那当然了我们这回的案例会比较简单
[00:29] 咱们只是做一个简单的入门重点是看一下它授权的逻辑以及认证的逻辑它内部是怎么进行流转的好了那接下来呢我们就可以自己去玩一个shared入门的一个程序那对于这个shared入门程序来说呢我们这边是使用它完全脱离开web容器的这么一种编程方式单主使用shared那它叫做基于INI的这么一种搭建方式那我们要做的第一件事呢就是可以搭建这么一个简单的环境
[00:58] 去配置上坐标接着配置一个share自己内部的一个ini配置文件那完成它的认证授权和自定义任务这么一个过程好了在这边呢我打开我的idea去创建一个我们新的project去完成share的一个简单的测试好了这个project呢我就创建一个空的因为你的代码呢不太多也没有什么父子级关系好了点击next给它起一个名字呢我就叫做share test
[01:27] 好了可以选择一个我存放的位置啊我就把它放到Workspace下HRM当中就放到这个文件夹下吧好了给它起一个名字呢叫做Shared TextTestOK点击Finish就在当前工程打开了好了那我们现在已经创建好了一个新的空的工程那接下来呢我们可以在这个工程下去创建一个小的模块那这个模块我们是用Maven模块来做的
[02:09] OK好了我们这边的group id呢cn.itcastartifact id呢就叫做shareall就叫shareall-demo吧shareall-demo下滑线demoNext好了放的位置也没什么问题也没什么问题finish好了工程创建好了之后呢我们需要引入当前工程的这个坐标那这个坐标呢或者它的依赖在我们今天给各位提供的这个资料当中有一个专门的shareall资料
[02:41] 里面有share的相应的配置文件share它的一个官方文档还有一些share比较好用的一些简单的介绍那我们找到share的这个依赖control c直接放过来就可以了OK那依赖也已经添加进来了那接下来呢我们在这个工程当中需要去简单的配置一个share的配置文件那这个share的配置文件里面要写什么注意因为我们share它要可能要完成用户认证不是说过它要登录吗
[03:11] 那登录可能要连接数据库啊但是呢我们这个案例重点是为了看它内部的一个执行流程那操作数据库这个过程我就给它省略了那所以这些数据从哪来呢可以配置到sharewell的ini配置文件当中所以呢我在resource下去创建第一个我的配置文件那这个配置文件呢当然你想叫什么名字都可以我这边呢就叫做sharewell-auth当然这个名字如果觉得不好听的话咱们可以随便起比如说就叫做sharewell
[03:43] Gantest-1.ini好了这个Sherlock Gantest-1.ini里面我们要写究竟要写什么内容注意它这个有自己的固定的格式在里面首先呢中括号users那这个users里面定义的是我们的测试的用户数据好了这边呢可以写点注释啊就是模拟从数据库查询用户好了它的一个书写格式数据格式
[04:17] 它这个数据格式是这样的就是用户名等于密码好了所以对于我们来说呢可以构造几个比如说有张三这是一个用户他的密码123456好了接着呢有李四好了他的密码比如说654321OK那这样一来我第一个测试的这个案例已经把当前的数据库的这些数据库密码用户名密码给他搞定了那接下来呢我们就可以
[04:46] 完成基本的用户认证的这么一个单元测试好了呢这个单元测试写到哪其实无所谓我就写到test包下了好了创建一个我们自己的测试类出来把它放到cn.cn.itcast.m好了叫就叫shadow吧起一个名字我们叫做shadow test01叫01了
[05:18] 好了那这个里面的Sheryl进行测试的时候我们用的是这unit单元测试来做我们先来看一下我们要测试用户认证这是我们要做的第一件事那测试用户认证认证什么意思认证起的不就等于是用户叫做登录吗那需要跟各位做一个简单的他这个用户登录上面的步骤的一个说明步骤的一个说明区别于传统的用户登录
[05:46] 那在share当中用户登录需要调用它登录的一个方法来做那在share当中如何进行登录我们回到讲义一起来看一下刚才这张图刚才这张图里面说过了不管是认证不管是它的授权是不是全部都是通过subject来完成用户登录的这么一个过程所以对于share当中的认证来说想方设法的通过subject完成登录操作
[06:12] OK这个我们做了一个简单的声明那我们简单的来看一下对于整个我们操作这个认证它的一个简单的代码的一个执行顺序首先呢第一件事我们这边呢有自己的数据库自己构造的这个配置文件那这个配置文件呢我们需要想办法加载那Sherlock它提供了一个方法它主要目的其实就是根据我们的配置文件好了可以创建出第一个对象也就是Security Manager
[06:47] 注意它这个security manager是通过工厂的方式来做的所以我们通过配置文件得到的其实是一个工厂FACTORY得到工厂那得到了工厂之后剩下的事情就不难了通过工厂获取security manager好了接着第三件事我们就是想方设法的我们构造subject那构造了subject接下来第四件事因为我们都知道因为我们都知道
[07:19] 对于这个subject来说它是不是应该创它是不是应该是security manager里面或者管理的所有的subject所以对于我们当前的这个security manager来说应该把它绑定到我们当前的运行环境上所以将注意这个第三步第四步写错了第三步将security manager绑定到当前运行环境
[07:49] 好了接着才是从当前运行当中从当前运行环境中去构造subject好了这个就是我们的第四步好了第五步就是说呢第五步第五步第四步第五步好了第五步是这样的有了subject我们就开始进行登录了但是通过shadow进行登录的时候呢需要借助shadow它提供的一个叫做用户数据或者用户凭证所以我们需要构造shadow登录的
[08:19] 数据这个什么意思就是你用户登录不是有用户密码吧就把用户密码给他搞定让他去登录好了那接着最后第六件事就是真正的完成主体登录好了那接下来呢我们就开始把这几个啊做一个代码上的一个书写当然了如果步骤都有了那其实代码就比较简单了好了我们可以写一个ETA test配置一个方法public void就叫test login
[08:52] 因为是用来做认证的当然了我们在进行代码编写的时候以第一步根据配置文件去创建Security Manager Factory好那这一步如何去做呢其实不难也比较简单我们可以通过Sherlock提供一个对象这个对象叫做Init叫做Init Security Manager FactoryInit Security Manager
[09:23] 那这个magic factory里面呢可以接收我们的配置文件的class pass路径所以我这边class pass冒号share我的第一个配置文件呢叫做写到什么位置呢叫做-test-01抱歉我复制一下OK那这样一来呢我们就能够得到这么一个对象当然了我们这个对象呢现在这个对象写的还是不对啊我们用它的附接口的形式来去描述
[09:59] 别选测包用的是share提供的附结构的形式好了里面就能得到security manager了好了这边呢我就叫做factory f-a-c-t-y-yok好了抱歉啊各位就是说呢咱们如果在当前这个工程里面去完成这个代码编写的特别是这个security manager这个security manager需要这个坐标的一个补充那默认的引的这个坐标是不对的好了各位来看我把这个新的坐标呢已经导进来了
[10:40] 导进来之后你会发现就不会报错了其实这个是一个这个idea一个小小的一个问题就是说有shadow的时候这个supreme manager有重名的现象所以他就以错了所以刚才报了一个错误好了第一步我们搞定了之后接着我们关注第二步就是通过工厂获取真正的supreme manager那这一步比较简单直接factory打点getintense即可就能得到我们supreme manager我们最关键的这个安全管理器
[11:05] 好了那接着第三步就是将Security Manager绑定到当前现场绑定到当前现场上错了绑定到当前的运行环境上那绑定到当前运行环境上借助的是一个工具类叫做Security Utils那Security Utils打点setSecurity Manager好了那接着把Security Manager放进去那当前运行环境就已经有了Security Manager那接着我们还去做第四步就是从当前运行环境当中获取Subject
[11:37] 那获取subject呢也是比较简单的由于你当前已经绑定了这么一个supreme manager当前环境里有所以我们就可以从当前环境当中获取你的subject所以它有个方法get subject直接获取就可以了好了subject已经有了那接着我们来看一下我们看一下是不是有一个第六步叫做主体登录
[12:05] 那主体登录是什么意思其实就是借助这个subject完成登录操作subject打点叫做login那在进行login的时候呢各位它里面接收的是一个association
[12:18] 这么一个token那这个token其实是我们的用户认证数据那我们的认证数据还没有所以接下来第五步就是构造它的登录数据但是说的更加严谨一点呢其实是用户的认证数据那这个用户认证数据它login方法接收的是一个authentication这么一个token那这个authentication token呢它其实是一个接口那它有很多的实现方式
[12:44] 那我们现在用它比较经典的一个实现方式叫做什么就叫做user name password token好了等于new一个user name password tokenOK那接着对于我们用户登录来说它是不是可以输入用户名秘码输入用户名输入密码接着是不是完成登录啊那其实呢我们可以模拟比如说我当前用户输入了死俊user name等于好了我们有一个叫张三好了死俊
[13:15] 这是用户输入的当然我们是为了模拟password123456那好了接下来呢我们就可以去想方设法的构造username password token那怎么去构造呢很简单这玩意儿它有构造方法第一个参数就是username第二个就是password你传递过来所以对于我们来说username拿过来好了password拿过来OK这样一来我们就可以通过token完成登录的
[13:49] 这么一个操作那当然了我们现在用户登录已经搞定了那用户登录搞定了之后接下来呢就是说你当前登录究竟是登录成功还是登录失败了这个就不知道了所以第七件事我们可以做一个简单的验证就是验证用户是否是否登录成功那如果登录成功之后呢我们可以比如说呢叫做
[14:20] 获取登录成功的数据那这个应该怎么办那验证用户是否登录成功呢其实比较简单我们这边可以打印出来好了用户是否登录成功好了等于加上所有的只要你登录了之后所有内容都可以通过subject打点get的方式来获取那我们这边的subject打点is
[14:48] 哎错了所有的方式都可以通过subject去获取啊好了第一个方法is also ticketkitted这个玩意儿代表的是否登录成功那好了接着我们获取登录数据那获取登录数据也比较简单刚才说过了所有内容都在subject里面所以subject打点它有一个pro simple哎就是它那这个玩意儿其实就是获取安全数据也就是我们登录成功保存的数据默认保存的其实就是我们的用户名
[15:15] 那好了我们一起验证一下注意密码呢是123456我们执行一把来看张三123456登录成功等于触张三那如果我把这个密码写错了我们再来看好了各位来看这回就抛出了一个异常那这个异常呢其实就是告诉我们我的用户名和密码不匹配那站边呢说了一个是张三did not match那一个期望的一个密码的一个管理吧密码吧OK那这样一来我们就完成了这个整个用户
[15:47] 登录认证的这么一个操作

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中使用Shiro框架进行用户认证，包括创建项目、配置依赖、编写测试代码和处理认证失败。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT，标题为“4.4 Shiro的入门”，子标题“4.4.1 搭建基于ini的运行环境”，并显示了Maven依赖配置代码。
画面2：在IntelliJ IDEA中创建新项目，选择“Empty Project”。
画面3：IntelliJ IDEA项目创建完成后的初始界面。
画面4：显示了项目中的pom.xml文件内容，包含Shiro和JUnit的依赖配置。
画面5：黑屏，可能是视频切换或暂停。
画面6：展示课程PPT，标题为“4.4.1 用户认证”，并显示了ini配置文件内容。
画面7：展示多个窗口，包括PDF文档、IDEA项目、SQL日志等，用于说明Shiro的认证流程。
画面8：在IntelliJ IDEA中编写ShiroTest01.java测试类，导入Shiro相关包。
画面9：IDEA提示“不兼容的类型”，建议将变量类型改为InSecurityManagerFactory。
画面10：在ShiroTest01.java中，将SecurityManager设置到当前运行环境。
画面11：运行测试时出现异常，提示“UnknownError”。
画面12：在ShiroTest01.java中，创建UsernamePasswordToken对象并调用subject.login方法。
画面13：在IDEA中，使用Ctrl+Alt+Shift+L格式化代码。
画面14：测试失败，显示“SLF4J: Failed to load class 'org.slf4j.impl.StaticLoggerBinder'”和“org.apache.shiro.authc.IncorrectCredentialsException”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
<dependencies>
    <dependency>
        <groupId>org.apache.shiro</groupId>
        <artifactId>shiro-core</artifactId>
        <version>1.3.2</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
        <scope>test</scope>
    </dependency>
</dependencies>

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>shiro_demo</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>

画面6：
[users]
#模拟从数据库查询的用户
#数据格式：用户名-密码
zhangsan=123456
lisi=654321

画面8：
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.junit.Test;
public class ShiroTest01 {

画面9：
Factory<SecurityManager> factory = new IniSecurityManagerFactory( inResourcePath: "classpath:shiro-test-1.ini");

画面10：
SecurityManager securityManager = factory.getInstance();
SecurityUtils.setSecurityManager(securityManager);

画面12：
String username = "zhangsan";
String password = "123456";
UsernamePasswordToken token = new UsernamePasswordToken(username,password);
subject.login(token);

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：标题“4.4 Shiro的入门”，子标题“4.4.1 搭建基于ini的运行环境”。
画面6：标题“4.4.1 用户认证”，内容包括“认证：身份认证/登录，验证用户是不是拥有相应的身份”。
画面7：展示多个窗口，包括PDF文档、IDEA项目、SQL日志等，用于说明Shiro的认证流程。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

