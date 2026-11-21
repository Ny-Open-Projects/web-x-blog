# 02-Activiti与Spring整合测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\02-Activiti与Spring整合测试_【海量资源尽在 ubkz.com】.mp4
- 时长 19分30秒（音频 1170s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:04] 那下面我们就一起啊来实现我们的activity与spleen整合开发啊那首先我们要做的工作呢是要将我们的activity与spleen整合相关的这个配置要做好那下面我们就开始来做这个配置的工作啊第一步我们呢可以去创建一个这样的activity的工程啊那可以这样来做啊我可以new一个fair project然后呢下一步对吧我们在这里边呢可以去写上啊
[00:33] comit黑码然后下一步再走的话就可以进入到acti vi viti比如说来一个activity06再走下一步这样的话我就可以把这个部分放入到我们的代码部分去比如说新特性我们的原代码放到这个文件夹里下去有一个我们的activity
[01:00] activity06的这样的一个项目对吧好这时候呢我再走啊finish然后我们可以我们可以啊呃他说这个目录不存在对吧那我们可以创建它就可以了啊好这样我呢再去new一个打开一个新的窗口啊那这个activity06的这个工程啊呃就创建出来了那我们现在在这边就可以做一件事情呢就是我们
[01:30] 要做的这个事情是我们的activity与我们的这个Spring整合对吧所以呢我们要做的工作就是activity与Spring整合相关的这个坐标要引入进来那各位思考那有哪样的有一些什么样的坐标可以引入进来了对吧那我们这次肯定需要引入的包括我们的activity7相关的坐标对吧
[02:00] 还会涉及到我们Spring相关的坐标对吧Spring相关坐标还有不同样的我们activity为了能够去与我们的这个Spring整合那肯定也需要有相关的这个整合包对不对当然我们这一次还需要连接我们的这个MySQL数据库所以呢我们还会有我们的MySQL相关的这个驱动包对吧MySQL的驱动包
[02:29] 好等等啊那下面我们呢就可以把相关的这个坐标引入进来啊我们一起来来看一下在我给各位的这个第六天的资料中啊我们可以去找在这个部分有一个基本素材啊因为对于我们来说啊这样的这个坐标呃相信我们在同学呢在做这个实际开发的过程中啊都已经明白啊这样的坐标呢其实不需要我们去背的对吧那我这边呢呃就快速的把这些坐标啊
[02:58] 额,挪到我们的这个工程中来啊那好现在呢我就呃拿过来了啊我们一起来看一下大致啊他在这里边主要包含了有哪样的一些坐标啊其中呢呃你看第一个部分这个部分是我们的这个呃activity的这个流程引擎对吧呃这个地方叫做activity engine啊这是我们的这个引擎啊也是我们认为啊非常关键的一个啊一个坐标对吧这是我们的流程引擎的包啊
[03:27] 还有像我们的activity与sprint整合的包这个包其实我是刚才也特别给各位介绍过是我们的activity与我们的sprint整合的一个包然后我们在这里面就可以看到这一段内容是我们的activity的BPMN和我们的activity BPMN Conventor这个主要是
[03:55] 你像这一段主要是给我们的这个BPMN文件啊以及它的这个转换工作相关的这个坐标对吧好这是我们的这一段啊这一段坐标是这样的然后呢我们再往后走那将来我们啊比如说如果我们还要去用activity7的其他的一些模块的话你还可以把这个包导入进来啊但这个我们可以提前放到这里面啊这可以吧
[04:21] 然后呢后面部分你像这个各位很熟悉啊是我们的这个MySQL驱动包对吧那这个部分是我们的这个JUnit Supreme整合对不对所需要的包啊而后面这个部分呢是我们的这个日志所对应的这个坐标对吧那再往后走是我们这一次用到的这个MyBedis的这个坐标啊好还有像我们的这个CommerceDB啊你像这个文件读写呢文件读写的这个包呢如果你不
[04:51] 不加的话其实应该也不会有问题啊那这样我们把我们这一次activity与sprint整合所需要用到的这个POM文件啊就给各位啊介绍到这里面那下面呢我们就开始来学习我们的activity与sprint整合真正相关的这个具体配置啊那这一次这个具体配置我们呢
[05:16] 主要用到了一个新的这个类这个新的类是叫做SpringProcessEngineConfiguration这一点呢是我们前面都没有用到的那这个类各位呢可以看出它是由我们的这个Activity这个包所提供出来的那我们下面呢就可以来分析一下我们的这个具体的这个Activity-Spring.xml这个文件
[05:45] 具体都要去做什么样的一些配置工作啊那我们再往后走那第一个部分我们可以看到啊它会去做我们的这个data source的配置对吧也就是说我们的数据源需要配置啊然后下一个工作是我们工作流引擎配置的一个bin啊那这个bin是我们第一次接触啊是logo activity supreme是supreme process engine configuration这样的一个类啊
[06:13] 这个各位稍微注意一下就可以了原来我们是Standard Run是单机版这一次我们主要是Activity与Spring整合这样的话我们专门搞出了一个这样的SpringProcessEngineConfiguration这样的一个类好这个类将来里面可以注入一个是注入DataSource这是我们的数据源
[06:40] 另外一个它还可以注入我们的TransactionManager来实现我们的事务管理然后呢有我们数据库的策略这个策略呢比如说我先呢可以是job-create这个策略代表的是我们如果数据库里头有相关的表的话那会实现先job table然后再去做create table这样的操作再往后走一个呢是我们的这个process engine
[07:09] fire.bind那这个步骤主要就是去创建我们的process engine这个对象的啊它里面会注入我们在上面所创建的这个process engine configuration的对象它会直接注入进来最后这个部分就是我们会借助于我们的这个工厂来工厂方法啊来实现我们的这个
[07:33] Service啊reportable Service, runtime Service, task Service啊等等这样的一些Service的创建工作大致情况就是这样的啊那这一段内容呢如果说我们要去给它手工编写出来啊这个应该啊也没什么问题但我们在这里边呢也可以直接用另外一种方式啊就是呢我今天在过位啊在这里边呢我给各位啊提供了有这样的一个XML文件啊
[08:03] 在这个XML文件中呢我们其实已经把这样的一些工作给各位都做好了那我们可以把这样的一个配置文件直接拿过来这个地方啊对于我们来说应该难度也不大你像数据员对吧你像这个部分是我们今天啊新涉及到的如果啊如果咱们有需要的话这个其实我敲出来没有什么问题啊但是这个我这边呢
[08:32] 就直接给它引入进来就可以了啊然后下一个就是我们的这个process engine factory bin通过这个工厂方法通过这个工厂bin对象啊我们就可以快速得到我们的process engine对象然后呢下边的这个步骤啊就是下面最后面的这个部分呢是我们在这里边呢通过我们的实力实力工厂啊通过我们的这个实力工厂方式
[09:00] 来生成我们的每一个Service对象那这样啊我在这边呢就不去过多的给各位介绍这个部分了啊那现在呢我可以直接把它啊加入到我们的这个resources目录下啊看见我扔到这里头来啊那这样我们就相当于做好了activity与sprint整合的这个配置配置文件啊好这个部分呢对于我们来说应该啊
[09:29] 各位可以看到这里面有很多报错的内容对吧那我们来看一下为什么会出这些问题我先看一下这个部分各位应该是我们现在刚刚已经更新了我们的这个pom.xml文件但我更新完之后我们并没有来刷新我们的mywinproject对吧那现在我可以直接在这里面刷新一下
[09:55] 那刷新一下当我们完成了我们的这个dependence依赖之后我们这个时候再去回头看我们的activity与sprint整合的这个配置文件应该呢这里面就应该要恢复正常才是正确的我们来看一下那我们这边所需要依赖的这一堆这一堆依赖都添加进来了我这时候可以重新重新打开我们再看一下好这个部分
[10:28] 这里头有一个叫one euro fund对吧我们找到这个问题到底在哪好过去注意一下目前我们可以看到这里面报的一个错这个错主要是说我们当前的这一次项目因为我们没有这个comit黑码的包导致出现了这个问题对吧那对于我们而言其实呢可以到这边去新建一个这样的package对吧
[11:04] 好,比如说我这个做法啊com.it黑码it黑码然后.Service.impl那这样应该说我这个包名就存在了吧当我这个包名存在过一回看到啊我们刚才在这里面所报的这个错立即就不见了对吧那这样的话应该说我呢就完成了我们的这个activity.respring整合
[11:31] 所需要用到的一些前期的配置工作但这个配置工作在这个部分Split和Activity整合的配置文件我没有去敲其实我们主要就是这个类SplitProcessEngineConfiguration这个类和ProcessEngineFactoringBin这样的两个类我们最后就是把这个事务给它配一下就可以了对吧整体上
[11:59] 没有什么太大的难度啊那我们做完这个工作呢现在我就可以来做我们的这个整合的测试啊那怎么样去说我们这一次整合工作是成功还是失败那这个地方啊我们可以很轻松的啊来做这个工作啊各位可以看一下啊首先呢我可以把我们的这个activity库给它删掉啊然后呢我们再去创建一个这样的库出来对不对
[12:25] 比如说我这个是再刷新一下各位可以看到我们的这个activity库就已经创建出来了但是这个库里面并没有我们任何的一个表的信息对吧那现在我可以呢在这里头讲我们的下一步操作这个下一步操作主要就是啊我们在这边呢可以去创建一个创建一个啊这样的类比如说我就搞出一个啊叫做com.it黑码然后呢我去搞一个这样的测试测试包底下啊
[12:55] 在测试包底下,我再去搞一个activity与sprint整合,比如说integration搞出一个测试类,可以吗?
[13:10] activity-sprint-integration-test搞一个类这个类放在test的文件夹下这样我们就可以实现
[13:26] Spring与我们的JUnit整合测试测试的主要目标我们说一下我们测试的目标是要完成我们的Aggregtivity与我们的Spring整合我们测试到底成不成功成功的标志主要是一个是看我们的
[13:54] 看我们的这个activity库中是否有相用的表对不对那些表是否可以出来这是一个另外一个呢我们也可以在这里面比如说我可以输出一个repository输出一个repository Service的对象当我们的这个对象可以正确输出的时候那我们就可以认为我们的activity也是不能整合
[14:24] 所生成的process engine以及我们在这里边通过我们的工厂通过我们的实例方法通过我们的实例方法通过process engine的这样的实例工厂的实例对象再去调用它的工厂方法对吧从而完成我们的reportedly Service的并对象创建这个地方如果可以的话那就证明我们已经成功了对吧
[14:53] 现在我可以做一个这样的工作我可以在这里面来一个叫做ata-auto-reel然后在这里面去将我们的reporeported Service对象注入进来如果这个过程没有任何问题的话我们就认为我们的工作已经完成对吧好具体可不可以我在这里面可以来一个sout来输出我们的比如说我们这里头
[15:22] 有一个叫部署对象这个具体的对象啊是叫做Repository Repo就是我们的Repository这个对象的输出啊就是这个对象吧好康小微那再来啊那这个地方各位要注意一下啊就是我们因为我们这一次这个方法是是卖方法这个地方有点问题对不对那我打算呢把这个调整一下可以吗我把这个呢
[15:50] 比如说直接搞出一个啊public void比如说叫做test的叫做test的我们的这个部署对象对吧deployment的对象的创建啊那这样应该可以了啊然后呢我们就可以再去做下一个工作就是呢在这里边去把我们的这个junit的单元测试引入进来啊那这样我们是否就可以完成我们的这个junit的测试呢
[16:20] 对吧因为我们要测试的目标是activity与sprint整合对吧那很明显我们现在还没有完成我们的这个工作那现在我可以在这里头来一个叫做runways来加载我们的sprint与junit整合的这样的一个类对不对好下一个步骤我们就可以用另外的一个注解叫做contestconfiguration然后来在这里头来一个加载我们的
[16:47] 加载我们的Spring配置文件所在的位置ClassPass底下的叫做acti viti activity-spring.xml对不对当我们完成这个工作这样我们基本上就可以来测试我们的这次整合是否成功如果成功的话刚才我们介绍过应该在这里面会刷出我们activity相关的那些表对不对
[17:14] 好现在我们可以来运行一下我们的代码啊好这边呢我们就可以我们这边呢就可以来看一下啊整个的过程啊都已经完成了对吧部署的对象是叫做我们的activity engine啊是这样的一个对象那这个过程到底啊是否成功对吧我们对象是输出了啊也就是说我们第一个第一个标志是已经成功的啊
[17:49] 还有一个标志要去看我们的这个activity库是否存在相关的表对吧那我们可以啊再去刷一下这个部分啊各位我们现在就可以看到啊在我们的这个activity库中啊又可以看到这些相关的表又重新啊被创建进来了那这样我们基本上啊就给各位啊演示了我们的这个activity与Spring整合测试
[18:16] 并且完成我们相应的效果总体上的步骤各位是否还记得我们要做的第一个工作是在 pom.xml 文件中引入相关坐标我们做的第二个工作是我们在这边要去做我们的activity和 spleen 整合对应的配置信息这个配置信息主要包括就是数据源的配置工作流引擎对象的配置以及我们
[18:46] 以及我们工作流引擎的配置最后一个就是我们的相关的这些Service的配置对吧这样基本上我们就完成任务了当然这个事务这一块的我们之前就配过那我们事务管理器这一块我就不啰嗦了这是我们整体上这个配置信息是这样的当我们完成这个配置信息之后下一个环节我们就应该是来做我们的整合测试这是我们整合测试
[19:15] 其实主要目标就是加载了我们的Splint配置文件对吧这样我们就可以创建出我们的Report to the Service然后呢就可以正确输出啊这是大致的步骤给各位做的一个小节啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中配置 Spring 与 Activiti 的集成环境，包括 Maven 依赖管理、Spring 配置文件编写和单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 打开 IntelliJ IDEA 项目，项目名为 activiti02，提示未配置 Spring。
画面 2: 编辑 pom.xml 文件，添加 Activiti 相关依赖。
画面 3: 在 pom.xml 中继续添加 Activiti 的依赖项。
画面 4: 在 pom.xml 中添加 MySQL 和 JUnit 依赖。
画面 5: 查看 PDF 文档中关于 Spring 配置的说明。
画面 6: PDF 文档中展示 Spring 配置文件的结构。
画面 7: 编辑 activiti-spring.xml 文件，配置数据源和流程引擎。
画面 8: 在 activiti-spring.xml 中配置数据库连接和流程引擎。
画面 9: 在 activiti-spring.xml 中配置事务管理器。
画面 10: 在 activiti-spring.xml 中添加 Spring AOP 事务配置。
画面 11: 编写 ActivitiSpringIntegrationTest.java 测试类，准备注入 RepositoryService。
画面 12: 在测试类中添加 @RunWith 和 @ContextConfiguration 注解。
画面 13: 在测试类中添加 @Test 注解并执行测试。
画面 14: 测试通过，输出“部署对象：repositoryService”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.ithema</groupId>
    <artifactId>activiti02</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <slf4j.version>1.6.6</slf4j.version>
        <log4j.version>1.2.12</log4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-engine</artifactId>
            <version>7.0.0.Beta1</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring</artifactId>
            <version>7.0.0.Beta1</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-bpmn-model</artifactId>
            <version>7.0.0.Beta1</version>
        </dependency>
    </dependencies>
</project>
```

画面 3:
```xml
<dependencies>
    <properties>
        <slf4j.version>1.6.6</slf4j.version>
        <log4j.version>1.2.12</log4j.version>
    </properties>
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-engine</artifactId>
        <version>7.0.0.Beta1</version>
    </dependency>
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-spring</artifactId>
        <version>7.0.0.Beta1</version>
    </dependency>
    <dependency>
        <groupId>org.activiti</groupId>
        <artifactId>activiti-bpmn-model</artifactId>
        <version>7.0.0.Beta1</version>
    </dependency>
</dependencies>
```

画面 4:
```xml
<dependency>
    <groupId>org.activiti.cloud</groupId>
    <artifactId>activiti-cloud-services-api</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>
<dependency>
    <groupId>aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.5.4</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.40</version>
</dependency>
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
```

画面 6:
```xml
<!-- 工作流引擎配置bean -->
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>

<!-- 流程引擎 -->
<bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>

<!-- 资源服务 -->
<bean id="repositoryService" factory-bean="processEngine" factory-method="getRepositoryService"/>
<bean id="runtimeService" factory-bean="processEngine" factory-method="getRuntimeService"/>
<bean id="taskService" factory-bean="processEngine" factory-method="getTaskService"/>
<bean id="historyService" factory-bean="processEngine" factory-method="getHistoryService"/>
```

画面 7:
```xml
<!-- 数据源 -->
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql://localhost:3306/activiti?"/>
    <property name="username" value="root"/>
    <property name="password" value="root"/>
    <property name="maxIdle" value="1"/>
</bean>

<!-- 工作流引擎配置bean -->
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>

<!-- 流程引擎 -->
<bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>

<!-- 资源服务 -->
<bean id="repositoryService" factory-bean="processEngine" factory-method="getRepositoryService"/>
<bean id="runtimeService" factory-bean="processEngine" factory-method="getRuntimeService"/>
<bean id="taskService" factory-bean="processEngine" factory-method="getTaskService"/>
<bean id="historyService" factory-bean="processEngine" factory-method="getHistoryService"/>
```

画面 9:
```xml
<bean id="transactionManager"
      class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource"/>
</bean>
```

画面 10:
```xml
<aop:config proxy-target-class="true">
    <aop:advisor advice-ref="txAdvice" pointcut="execution(* com.ithema.Service.impl.*.*(..))"/>
</aop:config>
```

画面 11:
```java
package com.ithema.test;
import org.activiti.engine.beans.factory.annotation.Autowired;
import org.springframework.util.SpringUtils;
import org.springframework.util.StringUtils;

public class ActivitiSpringIntegrationTest {
    @Autowired
    private RepositoryService repositoryService;

    public static void main(String[] args) {
        System.out.println("部署对象：" + repositoryService);
    }
}
```

画面 12:
```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(loader = org.springframework.test.context.support.AnnotationConfigContextLoader.class)
public class ActivitiSpringIntegrationTest {
    @Autowired
    private RepositoryService repositoryService;

    @Test
    public void test() {
        System.out.println("部署对象：" + repositoryService);
    }
}
```

画面 13:
```xml
<bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>

<bean id="repositoryService" factory-bean="processEngine" factory-method="getRepositoryService"/>
<bean id="runtimeService" factory-bean="processEngine" factory-method="getRuntimeService"/>
<bean id="taskService" factory-bean="processEngine" factory-method="getTaskService"/>
<bean id="historyService" factory-bean="processEngine" factory-method="getHistoryService"/>
```

画面 14:
```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:activiti-spring.xml")
public class ActivitiSpringIntegrationTest {
    @Autowired
    private RepositoryService repositoryService;

    @Test
    public void test

