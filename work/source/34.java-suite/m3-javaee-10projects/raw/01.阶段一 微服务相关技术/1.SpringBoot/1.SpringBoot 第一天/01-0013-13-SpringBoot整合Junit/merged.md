# 13-SpringBoot整合Junit

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\13-SpringBoot整合Junit_【海量资源尽在 ubkz.com】.mp4
- 时长 8分24秒（音频 504s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 接下来我们来介绍Spring Boot整合其他框架之前我们介绍过我们说现在有很多的企业都使用Spring Boot来快速的构建Spring的项目那么其实这个快速很大一部分程度上就体现在Spring Boot能够很方便的去整合一些其他的第三方的框架因为它提供了起步的依赖方便我们导入坐标它也提供了一些自动的配置
[00:30] 可以简化我们对于配置文件的书写那么在这一小节中我们将整合很多的框架来体验一下Spring Boot整合其他框架到底有多快有多方便那么首先我们来说第一个Spring Boot整合GUnit来进行单元测试这个非常的简单之前我们在学习Spring的时候也是整合过GUnit的导入一些坐标然后写一个测试类
[00:59] 并且在测试类上加一些注解之前我们说用Spring整合的时候我们需要加两个注解一个是Raw Face加入一些Junit4的启动然后加一个Context就是找到Spring的核心配置文件的注解然后写测试方法就OK了那么Spring Boot跟它的过程其实差不多我们来看一下首先第一个我们创建一个Spring Boot的工程然后引入一个
[01:28] 起步的依赖就是stutter-test那么这个依赖我们是见过的之前我们在快速构建Spring Boot项目它自带的就有这么一个test的依赖那么在接下来编写一个测试类当然如果是May1的项目我们应该把它写到test的那个包里边或者说那个文件夹下OK那么写好了之后呢接下来我们去在这个类上也需要加这么两个注解一个是Runways注解
[01:56] 它里边写的参数是SpringRunner.class跟之前的Spring可不太一样然后第二个呢我们可以去加一个注解叫做SpringBootTest这么一个注解这个注解是来标识当前这个类呢它是一个测试的用力的这个类然后指定一个引导类的这么一个路径即可最后呢就该写你的测试方法里边的代码都是一样的那么接下来我们在程序里边去演示一下打开ID
[02:25] 在这个地方我们新创建这么一个模块好 还是快速构建的方式下一步写一个包名com.it黑码然后这个artifact id我们叫sprintboot-test好 那么再下一步好 直接finish这样就完成了其实现在你发现我们没有勾选任何的一个
[02:53] 起步的依赖没有去勾选对吧我连web的那个起步依赖都没有勾选啊没有勾选之后呢我们来看一下这个POM文件来看这个POM文件里边你看现在是不是自己带着这个test的这个起步依赖的starter-test的OK那么有了这个依赖之后呢并且呢在Spring Boot快速构建的项目里边它还会帮我把这个测试用力这个类啊也帮我写好了我什么都不用干当然这个地方呢我们还是有一点地方是需要说一下的
[03:23] 所以我把这个删了我们手动的来写一下这么一个把这个包呢给它删掉删掉之后呢我们在这个启动类这个地方我们写一个类比如说以后呢我们可能要写各种的业务类user Service将来测试呢大部分时候是对于业务类来进行测试的那么既然是个业务类呢我们就给它标明是一个Service好那么在这里边我们也提供一个public void比如说叫做add这么一个方法
[03:54] 当然这个方法我们就不去实现了我们直接输出一下那么这个类呢就写好了接下来我们测试一下这个add这个方法那么要写测试呢我们需要找到测试这个包然后Java下边我们来写对应的一个测试用例好我们就写一个包com.it黑马.test那么就下面起名叫做user Service这个类名user Service的测试类
[04:23] 一般这个测试用力的类呢都这样起名你要测哪个类你就前面是哪个类然后呢接下来就是一个test那么写完了之后这个地方写一个文档注释表示是一个user Service的测试类好那么这个注释也写完了接下来加注解第一个呢就是runways当然这两个不分顺序好它呢写spring runner第二class
[04:50] 弄完了之后接下来加一个spreyboot test并且呢需要去指定一个classes等于当前我们这个引导类这个类的字解码文件好加进来其实呢就是这一串把它复制一下放这个地方好嘞这个代码呢就写完了写完了之后呢你接下来就该写怎么测试你就怎么测试比如说我们要去注入
[05:18] 我们对应的user Service对吧好user Service然后呢加一个注解all to weird弄完了之后呢我们写一个方法public void比如说test add好你要测试这个add方法那你就test add就可以了然后呢你直接去写一个比如说user Service.add方法调用一下当然这个方法呢将来会打印一个字幕串这个字幕串呢就是add三个点
[05:46] 那么接下来我们就来运行一下运行之前不要忘记这是个测试方法需要加一个add test这么一个注解OK写完了之后我们运行一下看一下这么一个效果稍等它正在启动你看好你看这个add点点点是不是就打印出来了没有任何的问题OK那么第一个事我们就说完了说完了之后这个代码写起来还是比较容易的
[06:16] 那么第二个事如果你这个包啊你这个当前测试用力的这个包是这个主要的主包的就是在引导类的这个主包的子包或者说跟它一样那么我们里边这个classes是不需要指定的比如说我们来演示一下为了演示一下呢我们在这个地方把这个包呢我们给它复制一下复制一下我们新创建这么一个package比如说我跟它一样
[06:45] 一样了之后呢接下来你看这里边是不是有个子包子包呢我们把这个类呢我们再复制一份好放这里边来放这里边来之后呢我们现在来看我们新写的这个现在我就把这个classes给它删掉删掉删掉之后呢括号也不用写了那么直接我们就可以来运行因为它们两个的包是一样的自动会去这个包下面找有没有这个引导类好稍等一下你看现在启动是不是也是没有问题的但是如果这个包呢
[07:13] 它不是当前这个主包的子包或者跟它一样的话比如说这个test包那么如果它也不加这一串的话就会报错了那么首先这个地方呢这个地方不是错这是编译说找不着这么一个Service因为这个user Service这个bin呢会在启动的时候才会去自动创建而它不会报这个错这个错只是一个idea的语法检查这个不用管然后呢我们直接来启动这个
[07:40] 启动这个呢就会真正的去报错了你看是不是就报错了OK吧他说找不到这么一个Spring Boot Configuration这么一个注记好这个地方呢稍微注意一下这个事情因为呢我们使用使用自动创建出来的项目就是我们用快速的构建的项目他这个Spring Boot Test是没有加那个对应的我们这一串东西的没有制定这个引导类的class文件的这个地方要注意为什么他没有加呢
[08:10] 是因为它这个包和这个包是一模一样的OK那么对于Spring Boot来整合Junit进行单元测试我们就介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中整合 JUnit 进行单元测试，包括添加依赖、编写测试类和测试方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: PPT 页面，标题为“Spring Boot 整合其他框架”，内容包括案例需求“Spring Boot整合JUnit,”和实现步骤：① 搭建Spring Boot工程；② 引入starter-test起步依赖；③ 编写测试类；④ 添加测试相关注解（@RunWith(SpringRunner.class) 和 @SpringBootTest(classes = 启动类.class)）；⑤ 编写测试方法。
画面 2: IntelliJ IDEA 主界面，显示项目结构，当前打开的是 pom.xml 文件，但内容为空。
画面 3: IntelliJ IDEA 编辑器，显示测试类 SpringbootTestApplicationTests.java 的内容，其中包含 @RunWith(SpringRunner.class) 和 @SpringBootTest 注解。
画面 4: IntelliJ IDEA 编辑器，显示 pom.xml 文件内容，其中包含 <dependencies> 和 <build> 标签，具体依赖为 spring-boot-starter-test。
画面 5: IntelliJ IDEA 编辑器，显示 UserService.java 文件内容，包含一个 add() 方法。
画面 6: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，光标位于 @Test 注解上方，准备编写测试方法。
画面 7: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @RunWith(SpringRunner.class) 和 @SpringBootTest 注解。
画面 8: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @SpringBootTest(classes = SpringbootTestApplication.class) 注解。
画面 9: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写 @Autowired private UserService userService; 字段。
画面 10: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，已编写测试方法 testAdd()，并运行测试，控制台显示测试通过。
画面 11: IntelliJ IDEA 编辑器，显示 SpringbootTestApplication.java 文件，包含 main 方法。
画面 12: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试方法 testAdd() 已编写完成。
画面 13: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试方法 testAdd() 已编写完成。
画面 14: IntelliJ IDEA 编辑器，显示 UserServiceTest.java 文件，测试失败，错误信息为“Could not find an 'annotation' declaration”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
案例：需求
Spring Boot整合JUnit,
案例：实现步骤
① 搭建Spring Boot工程
② 引入starter-test起步依赖
③ 编写测试类
④ 添加测试相关注解
• @RunWith(SpringRunner.class)
• @SpringBootTest(classes = 启动类.class)
⑤ 编写测试方法

画面 4:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.itheima</groupId>
    <artifactId>Spring Boot-test</artifactId>
    <version>1.0-SNAPSHOT</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.1.0.RELEASE</version>
        <relativePath/>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>

画面 5:
package com.itheima.springboottest;
@Service
public class UserService {
    public void add() {
        System.out.println("add");
    }
}

画面 6:
@Test
public void testAdd() {
    // TODO
}

画面 7:
@RunWith(SpringRunner.class)
@SpringBootTest
public class UserServiceTest {

}

画面 8:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {

}

画面 9:
@Autowired
private UserService userService;

画面 10:
@Test
public void testAdd() {
    userService.add();
}

画面 11:
package com.itheima.springboottest;
@SpringBootApplication
public class SpringbootTestApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringbootTestApplication.class, args);
    }
}

画面 12:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

画面 13:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

画面 14:
@RunWith(SpringRunner.class)
@SpringBootTest(classes = SpringbootTestApplication.class)
public class UserServiceTest {
    @Autowired
    private UserService userService;

    @Test
    public void testAdd() {
        userService.add();
    }
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“Spring Boot 整合其他框架”，内容包括案例需求和实现步骤。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求完成）

