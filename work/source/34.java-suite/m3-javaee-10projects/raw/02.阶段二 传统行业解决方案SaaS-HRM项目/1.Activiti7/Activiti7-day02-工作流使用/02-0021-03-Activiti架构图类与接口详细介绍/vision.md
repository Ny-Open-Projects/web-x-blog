# 画面线理解：03-Activiti架构图类与接口详细介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\03-Activiti架构图类与接口详细介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 01:29, 02:19, 02:55, 03:46, 04:16, 04:58, 06:25, 07:52, 09:03, 09:36, 10:47, 11:35, 12:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:19:37

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎的配置文件 activiti.cfg.xml 结构、核心配置类 ProcessEngineConfiguration 的定义、以及如何通过 ProcessEngineConfiguration 创建 ProcessEngine 并获取各个服务（RepositoryService、RuntimeService、TaskService、HistoryService、ManagementService）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Activiti 引擎架构图，ProcessEngineConfiguration 依赖 activiti.cfg.xml，其下包含 RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService 七个服务。文字说明新版本中 IdentityService 和 FormService 已被移除，但老版本仍需了解。
画面2：展示 activiti.cfg.xml 文件的 XML 命名空间声明。
画面3：展示 4.2 ProcessEngineConfiguration 小节，说明其是流程引擎的配置类，用于创建 ProcessEngine。
画面4：展示 activiti.cfg.xml 文件中配置数据源和 ProcessEngineConfiguration 的 bean 定义。
画面5：展示 activiti.cfg.xml 文件中定义了 Spring 事务管理器和流程引擎 bean。
画面6：展示 activiti.cfg.xml 文件中定义了 RepositoryService、RuntimeService、TaskService、HistoryService、IdentityService 五个服务的 bean。
画面7：展示 4.2.3 创建 ProcessEngineConfiguration 小节，说明通过 ProcessEngineConfiguration.createProcessEngineConfigurationFromResource 方法创建配置，以及可以修改 bean 名称。
画面8：展示 MySQL 命令行界面，执行删除 activiti 数据库并创建 activiti 数据库的 SQL 语句。
画面9：展示 activiti.cfg.xml 文件中配置数据源和 ProcessEngineConfiguration 的 bean 定义。
画面10：展示 ActivitiTest 测试类中通过 ProcessEngineConfiguration 创建 ProcessEngine 的代码，并在控制台输出 ProcessEngine 对象。
画面11：展示 4.3.2 简单创建方式小节，说明通过 ProcessEngineConfiguration.createProcessEngineConfigurationFromResource 方法创建配置。
画面12：展示 ActivitiTest 测试类中通过 ProcessEngineConfiguration 创建 ProcessEngine 的代码，并在控制台输出 ProcessEngine 对象。
画面13：展示 4.4.3 RepositoryService 小节，说明其是资源管理服务，用于管理流程定义。
画面14：展示 4.4.5 TaskService 小节，说明其是任务管理服务，用于获取任务信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
ProcessEngineConfiguration
|
├── RepositoryService
├── TaskService
├── IdentityService
├── FormService
├── RuntimeService
├── ManagementService
└── HistoryService

画面2：
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd
       http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">

画面3：
class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">

画面4：
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
    <property name="username" value="root" />
    <property name="password" value="root" />
</bean>

<bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource" />
    <property name="databaseSchemaUpdate" value="true" />
</bean>

画面5：
<bean id="processEngineConfiguration"
      class="org.activiti.spring.SpringProcessEngineConfiguration">
    <!-- 数据源 -->
    <property name="dataSource" ref="dataSource" />
    <!-- 使用spring事务管理器 -->
    <property name="transactionManager" ref="transactionManager" />
    <!-- 数据库策略 -->
    <property name="databaseSchemaUpdate" value="drop-create" />
    <!-- activiti的定时任务开关 -->
    <property name="jobExecutorActivate" value="false" />
</bean>

<bean id="processEngine"
      class="org.activiti.spring.ProcessEngineFactoryBean">
</bean>

画面6：
<property name="processEngineConfiguration" />
</bean>

<bean id="repositoryService" factory-bean="processEngine"
      factory-method="getRepositoryService" />
<bean id="runtimeService" factory-bean="processEngine"
      factory-method="getRuntimeService" />
<bean id="taskService" factory-bean="processEngine"
      factory-method="getTaskService" />
<bean id="historyService" factory-bean="processEngine"
      factory-method="getHistoryService" />
<bean id="identityService" factory-bean="processEngine"
      factory-method="getIdentityService" />

画面7：
ProcessEngineConfiguration configuration
ProcessEngineConfiguration.createProcessEngineConfigurationFromResource("activiti.cfg.xml")

ProcessEngineConfiguration.createProcessEngineConfigurationFromResource(String resource, String beanName);

画面8：
drop database activiti;
Create database activiti;

画面9：
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
    <property name="username" value="root" />
    <property name="password" value="root" />
</bean>

<bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource" />
</bean>

画面10：
public class ActivitiTest {
    @Test
    public void testGenTable() {
        ProcessEngine processEngine = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml")
                .buildProcessEngine();
        System.out.println(processEngine);
    }
}

画面11：
//使用classpath下的activiti.cfg.xml文件中的配置创建processEngine
ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
System.out.println(processEngine);

画面12：
public class ActivitiTest {
    @Test
    public void testGenTable() {
        ProcessEngine processEngine = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml")
                .buildProcessEngine();
        System.out.println(processEngine);
    }
}

画面13：
4.4.3 RepositoryService
是 activiti 的资源管理类，提供了管理和控制流程发布包和流程定义的操作。使用工作流建模工具设计的业务流程图需要使用此 service 将流程定义文件的内容部署到计算机。
除了部署流程定义以外还可以：
查询流程定义和流程实例。
暂停或激活发布包，对应全部和特定流程定义。暂停意味着它们不能再执行任何操作了，激活是对应的反向操作。
获得多种资源，像是包含在发布包里的文件，或 引擎自动生成的流程图。
获得流程定义的 pojo 版本，可以用来通过 java 解析流程，而不必通过 xml。

画面14：
4.4.5 TaskService
是 activiti 的任务管理类，可以从这个类中获取任务的信息。

4.4.6 HistoryService
是 activiti 的历史管理类，可以查看历史信息，执行流程时，引擎会保存很多数据（根据配置），比如流程实例启动时间，任务的参与者，完成任务的时间，每个流程实例的执行路径，等等。这个服务主要通过查询功能来获得这些数据。

4.4.7 ManagementService
是 activiti 的引擎管理类，提供了对 Activiti 流程引擎的管理和维护功能，这些功能不在工作流驱动的应用程序中使用，主要用于 Activiti 系统的日常维护。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“4.1 activiti.cfg.xml”，架构图显示 ProcessEngineConfiguration 指向 activiti.cfg.xml，ProcessEngineConfiguration 下方有七个服务：RepositoryService、TaskService、IdentityService、FormService、RuntimeService、ManagementService、HistoryService。
画面7：PPT 标题为“4.2.3 创建 ProcessEngineConfiguration”，文字说明通过 ProcessEngineConfiguration.createProcessEngineConfigurationFromResource 方法创建配置。
画面11：PPT 标题为“4.3.2 简单创建方式”，文字说明通过 ProcessEngineConfiguration.createProcessEngineConfigurationFromResource 方法创建配置。
画面13：PPT 标题为“4.4.3 RepositoryService”，文字说明其是资源管理服务。
画面14：PPT 标题为“4.4.5 TaskService”、“4.4.6 HistoryService”、“4.4.7 ManagementService”，分别说明其是任务管理、历史管理、引擎管理服务。

5) 不要评价画面
