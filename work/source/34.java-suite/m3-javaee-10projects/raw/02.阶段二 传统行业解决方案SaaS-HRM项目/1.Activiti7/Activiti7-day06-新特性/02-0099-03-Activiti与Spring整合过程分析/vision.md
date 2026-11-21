# 画面线理解：03-Activiti与Spring整合过程分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\03-Activiti与Spring整合过程分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:42, 01:50, 02:07, 02:23, 03:23, 03:45, 03:56, 04:21, 05:03, 05:16, 06:27, 07:40, 08:36
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:31:50

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
