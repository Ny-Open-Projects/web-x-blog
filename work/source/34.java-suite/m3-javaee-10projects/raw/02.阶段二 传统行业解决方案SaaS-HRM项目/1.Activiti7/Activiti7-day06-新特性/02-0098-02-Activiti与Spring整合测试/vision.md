# 画面线理解：02-Activiti与Spring整合测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day06-新特性
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day06-新特性\02-Activiti与Spring整合测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 02:49, 03:27, 04:21, 05:13, 06:50, 08:13, 10:02, 11:20, 12:40, 15:46, 16:43, 18:30, 19:12
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:30:56

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
    <aop:advisor advice-ref="txAdvice" pointcut="execution(* com.ithema.service.impl.*.*(..))"/>
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
