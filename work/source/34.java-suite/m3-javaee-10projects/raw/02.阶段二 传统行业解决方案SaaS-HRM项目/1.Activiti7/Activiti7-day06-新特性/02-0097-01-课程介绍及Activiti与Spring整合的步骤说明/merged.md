# 01-课程介绍及Activiti与Spring整合的步骤说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\01-课程介绍及Activiti与Spring整合的步骤说明_【海量资源尽在 ubkz.com】.mp4
- 时长 4分44秒（音频 285s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:05] 那本次课程呢我们主要介绍的是Activity 7的一些新特性部分那这个部分呢我们将包含有Activity与我们的Spring来实现整合开发这是一部分还有一个是我们的这个Activity 7的一些现状的分析将会涉及还有就是我们Activity的新特性介绍以及我们的这个Activity 7与Spring Boot整合开发
[00:35] 那最后部分呢我们将会带着各位啊一起来做一个啊我们activity与我们的sprintboot整合之后的这个啊综合案例那就是我们的这个SaaSIHRM这样的一个能力资源的一个项目啊这个项目部分呢我们啊这一次课程中后续来给各位主要介绍的是我们的这个activity和sprintboot整合之后啊来实现我们的这个
[01:04] 流程化的管理这是大致的这个课程介绍时间的那好我们现在呢就进入到第一个部分是activity与我们的这个stream来实现我们的整合开发那要去做这个工作我们呢大体上给各位先来介绍一下我们大体的步骤这个步骤第一个是我们要去把整个这个环境搭起来对吧
[01:30] 那我们要做的工作就是activity与spleen整合所需要用到的一些依赖我们呢要在porm.xml中给它搞定啊这是第一部分第二个部分就是呢我们把这个所需要的依赖整合进来之后啊那我们将会进入到我们的这个基本的配置信息那就是activity和我们的spleen整合的一些配置操作啊那这次我们呢
[01:59] 这个配置跟上次比较我们的这一次主要用的是SpringProcessEngineConfiguration用这样的一个类来实现我们的activity与Spring框架整合来创建我们的这个ProcessEngine对象那各位也可以思考一下其实上一次我们前面的过程一直采用的是StandardLambProcessEngineConfiguration来创建我们的这样的一个Configuration的对象
[02:29] 有了configuration之后我们就可以很轻松的得到我们的process engine对象这是我们的第二个环节要做的是Spring与activity整合的具体的配置文件但这个配置文件我们起名字这一次我们用的是activity-spring.xml这个名字其实是不固定的这是我们要做的第二个工作
[02:56] 那第三个工作我们就可以来写我们的这个测试代码了那这个部分啊就是我们的这个测试代码我们这次测试代码主要是啊用我们的这个activity测试的是activity啊我们做的工作是spring与junit整合之后的这个写法啊也就是说这种写法也对于我们来说啊也不是很陌生对吧通过这种方式来加载我们的这个spring的配置文件啊
[03:25] 最后我们就可以来看一下我们的这个Repository Service是否可以正常的注入进来如果它可以正常的注入进来那我们就认为我们的Process Engine已经创建成功了并且可以通过它很轻松的得到我们的这个Repository Service有了Repository Service那我们后续
[03:53] 就可以去实现我们的这个activity的流程部署工作对吧好最后一个点呢是我们会去把我们整个这个环节啊给各位做一下分析啊那这是我们这一次所涉及到的应该是四个步骤啊第一个步骤是导入我们的这个paw.xml的坐标第二个步骤是解决我们的这个配置文件的问题第三个步骤是我们编码来实现啊
[04:21] 这是第二个步骤配置文件这是我们的第三个步骤编码来实现第四个步骤那就是呢我们来实现activity与splint整合整个的加载过程的分析这就是我们大致的这个步骤性的内容以及我们的这个课程介绍的点大致是这样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti7 与 Spring 的整合开发，包括依赖配置、Spring 配置文件编写及执行流程分析。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：标题页，显示“SaaS-IHRM 项目-Activiti7 新特性 工作流引擎”，机构为“传智播客-研究院”。
画面2：同画面1，无新增内容。
画面3：显示页脚信息“北京市昌平区建材城西路金燕龙办公楼一层 电话：400-618-9090”。
画面4：PPT标题“第1章 Activiti 与 Spring 整合开发”，子标题“1.1 Activiti 与 Spring 整合的配置”，展示部分 Maven 依赖配置。
画面5：展示 Maven 依赖配置，包含 org.activiti:activiti-engine 和 org.activiti:activiti-spring。
画面6：展示 Maven 依赖配置，包含 org.springframework:spring-test。
画面7：展示 Maven 依赖配置，包含 log4j 和 slf4j。
画面8：展示创建 Spring 与 Activiti 整合配置文件的 XML 结构，包含命名空间和 schemaLocation。
画面9：展示测试代码，使用 @RunWith(SpringJUnit4ClassRunner.class) 和 @ContextConfiguration。
画面10：展示测试方法 test01()，用于打印 repositoryService 对象。
画面11：重复画面4的 Maven 依赖配置。
画面12：重复画面6的 Maven 依赖配置。
画面13：展示 Maven 依赖配置，包含 org.mybatis:mybatis 和 org.apache.commons:commons-dbcp。
画面14：展示“1.2.2 执行流程分析”，包含 XML 配置片段，说明 Spring 配置文件加载 ProcessEngineConfiguration 对象，以及创建 ProcessEngineFactoryBean 对象的过程。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
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
</dependencies>

画面5：
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring</artifactId>
    <version>7.0.0.Beta1</version>
</dependency>

画面6：
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>5.0.7.RELEASE</version>
</dependency>

画面7：
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>${log4j.version}</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>${slf4j.version}</version>
</dependency>

画面8：
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans.xsd
           http://www.springframework.org/schema/context
           http://www.springframework.org/schema/context/spring-context.xsd
           http://www.springframework.org/schema/tx
           http://www.springframework.org/schema/tx/spring-tx.xsd">

画面9：
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = "classpath:activiti-spring.xml")
public class ActivitiTest {

    @Autowired
    private RepositoryService repositoryService;

画面10：
@Test
public void test01() {
    System.out.println("部署对象：" + repositoryService);
}

画面14：
<bean id="processEngineConfiguration" class="org.activiti.spring.SpringProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource" />
    <property name="transactionManager" ref="transactionManager" />
    <property name="databaseSchemaUpdate" value="true" />
</bean>

<bean id="processEngineFactoryBean" class="org.activiti.spring.ProcessEngineFactoryBean">
    <property name="processEngineConfiguration" ref="processEngineConfiguration" />
</bean>

<bean id="repositoryService" factory-method="getRepositoryService" factory-bean="processEngineFactoryBean" />
<bean id="runtimeService" factory-method="getRuntimeService" factory-bean="processEngineFactoryBean" />
<bean id="taskService" factory-method="getTaskService" factory-bean="processEngineFactoryBean" />
<bean id="identityService" factory-method="getIdentityService" factory-bean="processEngineFactoryBean" />
<bean id="managementService" factory-method="getManagementService" factory-bean="processEngineFactoryBean" />
<bean id="formService" factory-method="getFormService" factory-bean="processEngineFactoryBean" />

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：标题“第1章 Activiti 与 Spring 整合开发”，子标题“1.1 Activiti 与 Spring 整合的配置”。
画面7：文字说明“我们除了使用 StandaloneProcessEngineConfiguration 来创建 ProcessEngine 流程引擎对象。还可以通过 org.activiti.spring.SpringProcessEngineConfiguration 与 Spring 整合方式来创建 ProcessEngine 对象。”
画面8：文字说明“创建 spring 与 activiti 的整合配置文件：activiti-spring.xml（名称不固定）”。
画面14：文字说明“下面我们一起分析 Activiti 与 Spring 整合加载的过程。如下图所示：”，并展示 XML 配置片段，说明 Spring 配置文件加载 ProcessEngineConfiguration 对象，以及创建 ProcessEngineFactoryBean 对象的过程。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

