# 画面线理解：01-课程介绍及Activiti与Spring整合的步骤说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\01-课程介绍及Activiti与Spring整合的步骤说明_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:07, 01:14, 01:18, 01:50, 01:54, 01:58, 02:40, 03:05, 03:59, 04:15, 04:19, 04:21, 04:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:29:57

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
