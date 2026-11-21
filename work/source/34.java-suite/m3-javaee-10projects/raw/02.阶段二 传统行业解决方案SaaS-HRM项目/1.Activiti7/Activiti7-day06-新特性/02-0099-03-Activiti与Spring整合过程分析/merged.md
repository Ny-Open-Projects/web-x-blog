# 03-Activiti与Spring整合过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\03-Activiti与Spring整合过程分析_【海量资源尽在 ubkz.com】.mp4
- 时长 8分44秒（音频 524s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好,下面我们一起来分析一下我们的这个执行流程那Activity与Spring整合加载并且呢我们刚才跑出了这个执行之后我们看到了相关的这个表对吧以及我们的Report Service的这个对象那现在我们可以一起给各位来介绍一下我们的这个整个运行的过程是什么样的那首先呢我们
[00:33] 一起来看一下我们的这个activity与Spring整合的这个配置文件在整合的这个配置文件中我们可以看到其实整个这个过程最关键的这个代码就是这一行配置那就是我们的流程引擎的这个对象我们的这个流程引擎对象是这样被创建出来的是Process Engine Factor BIM它是通过我们的工厂
[01:03] 它是通过我们的工厂方式这个是通过我们的工厂方式创建出来创建出我们的叫做Process EngineProcess Engine的对象这个是我们在这里边实现的效果是这样的那我们真正在这里边你会发现呢我们的这个Process Engine的这个对象它又需要去
[01:32] 注入一个Process Engine Configuration这样的一个对象而我们注入的这个对象又是从哪里头来的呢那我们可以进一步来看一下我们这一次真正注入的这个对象又是从哪个地方来的那我们的这个对象呢它是Process Engine Configuration它是这样的这就是我们在这里边所看见的我们的Process Engine
[02:02] configure a 型的这个对象看小微啊我把它复制下来啊我把它截下来啊这样来做这是我们的这个process configure a 型的这个对象啊好我们再放到这边来啊各位这时候呢我们基本上就可以看到我们这一次呢真正啊在这里边相当于我们的这个process engine这个对象又能够被创建出来那他必须要知道
[02:34] 那必须要知道我们连我们真正将来连接数据库的data source是什么对不对这是必须要知道的这是一个点除了这个点我们将来我们的事务管理器这个是要知道的对不对我们对于数据库是直接创建表还是是job还是correct对吧还是jobcorrect这个要说清楚对不对那通过这个process engine configuration这个对象的注入
[03:03] 那我们这边的基本上啊就完成了这几个工作啊那再下一步走呢对吧那我们的data source这个对象有没有呢那各位可以看到我们在顶上部分呢各位就可以看到啊这就是我们所配置的这个data source而在这个data source部分我们已经说得非常清楚我们的数据库连接的用户名和密码都已经非常清楚吧那这样的话就基本上啊给各位
[03:31] 说清楚DD Source这个真正的注入就在于它对不对这样我们就完成了我们的DD Source的注入当然我们的Transaction Manager真正的也是在这个部分有一个Transaction Manager的对象那就在这个地方这样的话我们将来就可以去注入我们的Transaction Manager这个对象好就在这个部分Countryway扔过来
[03:59] 那我们注入Transaction Manager对象那这样也就给各位说清楚了对不对那在这个部分就是注入我们的Transaction Manager好那当我们整个这个流程都跑通的时候那我们刚才呢在这边就写了我们的这个JUnit的单元测试对不对
[04:20] 通过这个jUnit单元测试的这两行代码那其实我们就可以完成我们Spring配置文件的加载对不对而我们Spring配置文件在加载的时候它就相当于这是我们做我们Spring配置文件加载的工作这个地方就去加载我们的Spring配置文件当我们的Spring配置文件一旦被加载它里面所配置的这样的一些并对象
[04:49] 就会被实力化对不对从而完成我们的一些对象创建工作这就是整个流程当Process Engine如果都已经创建出来的话那我们相关的这样的一些Service对象是不是就可以很轻松的拿到也就是比如说我在这里头给各位再贴出一个如果我要去创建一个Repository Service的对象那我们这边就可以很轻松的去得到我们的
[05:19] report得到我们的report Service因为report Service需要用到我们的这个我们的这个process engine的这个对象是不是他要用到他他需要用到这个process engine的这个对象这个大致情况就是这样的我把这个地方给各位他在里面呢需要用到我们的process engine的这个对象是不是
[05:48] 这样我们基本上就完成了整个的这个说明那这个地方其实是我们的第一个工作对吧首先我们相当于一上来呢去加载Spring配置文件当我们加载Spring配置文件的时候于是就要去做我们Process Engine的这个创建对不对当我们的Process Engine创建的时候它里面呢又需要去依赖我们的Process Engine Configuration的这个对象所以我们这里头就有第二个工作
[06:17] 那第二个工作一旦做完于是我们将来就需要去做我们的data source的注入还要去做我们的transaction manager的注入最后我们呢说你就可以拿到我们想要的这个Service了这是我们的第五个工作啊那有了这个Service对象将来你程序里头要去做部署也好做任务的运行也好啊做任务的执行这些都没有问题啊
[06:44] 这是我们在这里面给各位讲了一下我们从解决你的加载配置文件到我们的这个Processor EngineFactory Beam对象创建它又依赖于Processor Engine Configuration而Configuration又需要去依赖于Data Source走接着往后走又它又需要依赖于Transaction Manager当这些对象完全都给你提供出来的时候
[07:08] 那整个我们的Process Engine这个对象就可以完全创建出来而当我们的Process Engine创建好了那我们的第五个步骤那就可以去进一步由Process Engine去调用它的这个GetRepositoryService从而得到我们的RepositoryService这样的一个编对象整个这个过程啊就算是给各位啊分析完成那再说一嘴就是我们为什么要去给各位讲这个部分啊
[07:37] 就是特别给各位去讲一下activity与我们的Spring整合那是因为现在我们的Spring用的是非常多的对吧有一些公司它将来会选择activity直接与Spring整合当然现在还有一种情况就是我们的Spring boot也比较火所以后面我们也会去讲另外一种情况就activity与Spring boot来实现整合我们在现有的公司的层面
[08:07] 主要就是考虑这两种方式对吧一种呢就是我们的这个activity直接与sprint整合然后将来直接去用我们之前所用的这一套原生的这个API成了就可以完成我们的这个流程控制对不对这是一种方式啊除了这种方式呢我们还有一种方式就是呢使我们的activity与我们的sprintboot来整合开发啊那这个后续我们再给各位介绍
[08:35] 大致上我的这个Spring与Activity分析的过程给各位就介绍到这里面

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 与 Spring 整合的执行流程，通过分析配置文件和测试代码展示各组件间的依赖关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示教材页面，介绍 Activiti 与 Spring 整合的执行流程分析，图示说明了 processEngineConfiguration、processEngine、repositoryService 等对象的依赖关系。
画面2：在 IntelliJ IDEA 中打开 activiti-spring.xml 配置文件，显示了 Spring 容器中定义的多个 bean，包括 processEngine、repositoryService、runtimeService、taskService、historyService 和 transactionManager。
画面3：在 PowerPoint 中展示代码片段，说明通过工厂方式创建 processEngine 对象，并指向 activiti-spring.xml 文件。
画面4：在 PowerPoint 中展示代码片段，说明通过工厂方式创建 processEngine 对象，并指向 activiti-spring.xml 文件。
画面5：在 PowerPoint 中展示代码片段，聚焦于 processEngineConfiguration bean 的配置，包含 dataSource、transactionManager 和 databaseSchemaUpdate 属性。
画面6：在 IntelliJ IDEA 中打开 activiti-spring.xml，显示了 Spring 的 XML 命名空间和 dataSource bean 的配置。
画面7：在 IntelliJ IDEA 中打开 activiti-spring.xml，显示了 processEngineConfiguration bean 的配置，包含 dataSource、transactionManager 和 databaseSchemaUpdate 属性。
画面8：在 PowerPoint 中展示代码片段，用红色圆圈和箭头标注了 processEngineConfiguration bean 中的 dataSource、transactionManager 和 databaseSchemaUpdate 属性。
画面9：在 IntelliJ IDEA 中打开 ActivitiSpringIntegrationTest.java，展示使用 @RunWith(SpringJUnit4ClassRunner.class) 和 @ContextConfiguration(locations = "classpath:activiti-spring.xml") 注解的测试类。
画面10：在 IntelliJ IDEA 中打开 ActivitiSpringIntegrationTest.java，展示测试方法 testDeploymentObj()，该方法通过 @Autowired 注解注入 repositoryService。
画面11：在 PowerPoint 中展示代码片段，用红色箭头标注了 @ContextConfiguration 注解和 processEngineConfiguration bean 的配置。
画面12：在 PowerPoint 中展示代码片段，用红色箭头标注了 @ContextConfiguration 注解、processEngineConfiguration bean 的配置、dataSource bean 的配置和 transactionManager bean 的配置。
画面13：展示教材页面，介绍 Activiti 与 Spring 整合的执行流程分析，图示说明了 processEngineConfiguration、processEngine、repositoryService 等对象的依赖关系。
画面14：在 PowerPoint 中展示代码片段，用红色箭头标注了 @ContextConfiguration 注解、processEngineConfiguration bean 的配置、dataSource bean 的配置和 transactionManager bean 的配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```xml
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>

<bean id="processEngine" factory-bean="processEngineFactoryBean" factory-method="getProcessEngine"/>
<bean id="repositoryService" factory-bean="processEngineFactoryBean" factory-method="getRepositoryService"/>
<bean id="runtimeService" factory-bean="processEngineFactoryBean" factory-method="getRuntimeService"/>
<bean id="taskService" factory-bean="processEngineFactoryBean" factory-method="getTaskService"/>
<bean id="historyService" factory-bean="processEngineFactoryBean" factory-method="getHistoryService"/>
```

画面2：
```xml
<bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>

<bean id="repositoryService" factory-bean="processEngine" factory-method="getRepositoryService"/>
<bean id="runtimeService" factory-bean="processEngine" factory-method="getRuntimeService"/>
<bean id="taskService" factory-bean="processEngine" factory-method="getTaskService"/>
<bean id="historyService" factory-bean="processEngine" factory-method="getHistoryService"/>
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource"/>
</bean>
```

画面5：
```xml
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>
```

画面6：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xsi:schemaLocation="
            http://www.springframework.org/schema/beans
            http://www.springframework.org/schema/beans/spring-beans.xsd
            http://www.springframework.org/schema/tx
            http://www.springframework.org/schema/tx/spring-tx.xsd
            http://www.springframework.org/schema/aop
            http://www.springframework.org/schema/aop/spring-aop.xsd">

    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/activiti"/>
        <property name="username" value="root"/>
        <property name="password" value="root"/>
        <property name="maxActive" value="3"/>
        <property name="maxIdle" value="1"/>
    </bean>

    <bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
        <property name="dataSource" ref="dataSource"/>
        <property name="transactionManager" ref="transactionManager"/>
        <property name="databaseSchemaUpdate" value="drop-create"/>
    </bean>

    <bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
        <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
    </bean>
</beans>
```

画面7：
```xml
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql://localhost:3306/activiti"/>
    <property name="username" value="root"/>
    <property name="password" value="root"/>
    <property name="maxActive" value="3"/>
    <property name="maxIdle" value="1"/>
</bean>

<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>

<bean id="processEngine" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration"/>
</bean>
```

画面8：
```xml
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="transactionManager" ref="transactionManager"/>
    <property name="databaseSchemaUpdate" value="drop-create"/>
</bean>

<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
    <property name="url" value="jdbc:mysql://localhost:3306/activiti"/>
    <property name="username" value="root"/>
    <property name="password" value="root"/>
    <property name="maxActive" value="3"/>
    <property name="maxIdle" value="1"/>
</bean>

<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource"/>
</bean>
```

画面9：
```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:activiti-spring.xml")
public class ActivitiSpringIntegrationTest {

    @Autowired
    private RepositoryService repositoryService;

    @Test
    public void testDeploymentObj() {
        // 拿到一个repositoryService对象
        System.out.println("repositoryService");
    }
}
```

画面10：
```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:activiti-spring.xml")
public class ActivitiSpringIntegrationTest {

    @Autowired
    private RepositoryService repositoryService;

    @Test
    public void testDeploymentObj() {
        System.out.println("repositoryService");
    }
}
```

画面11：
```java
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:activiti-spring.xml")
public class ActivitiSpringIntegrationTest {

    @Autowired
    private RepositoryService repositoryService;

    @Test
    public void testDeploymentObj() {
        System.out.println("repositoryService");
    }
}
```

画面12：
```java
@RunWith(SpringJUnit4

