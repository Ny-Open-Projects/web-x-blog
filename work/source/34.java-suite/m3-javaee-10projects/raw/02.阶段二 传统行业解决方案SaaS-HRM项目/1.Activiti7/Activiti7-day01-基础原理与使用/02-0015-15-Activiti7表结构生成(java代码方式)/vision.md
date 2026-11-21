# 画面线理解：15-Activiti7表结构生成（java代码方式）

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\15-Activiti7表结构生成（java代码方式）_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 01:18, 02:42, 03:29, 04:03, 05:10, 06:25, 09:58, 13:02, 15:20, 16:13, 16:47, 17:05, 18:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:11:22

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IDEA 中创建 Activiti 项目，配置数据库连接，编写测试类并运行以自动创建 Activiti 数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：打开 MySQL Workbench，连接到本地数据库，显示数据库列表，包括 activiti、crm、test 等。
画面 2：在 IDEA 中新建项目，项目名为 activi001，路径为 G:\Activiti\开发计划\Activiti\day01\代码。
画面 3：在 Windows 资源管理器中，显示 Activiti 项目文件夹，选中名为“代码”的文件夹。
画面 4：在 IDEA 中打开 pom.xml 文件，显示项目依赖配置，包括 activiti-engine、activiti-spring、activiti-bpm-model 等。
画面 5：在 IDEA 中继续编辑 pom.xml，添加了 activiti-cloud-services-api 和 mysql-connector-java 依赖。
画面 6：在 IDEA 中弹出“Copy”对话框，将 log4j.properties 文件复制到项目 resources 目录下。
画面 7：在 IDEA 中打开 activiti.cfg.xml 文件，显示 Spring 配置文件的 XML 声明和命名空间。
画面 8：在 IDEA 中编辑 activiti.cfg.xml，配置数据源和 ProcessEngineConfiguration。
画面 9：显示 PPT 页面，标题为“3.3.6.5 编写程序”，内容是创建 ProcessEngineConfiguration 并调用 buildProcessEngine() 方法。
画面 10：在 IDEA 中编写并运行 ActivitiTest 测试类，控制台输出日志，显示创建数据源和数据库表。
画面 11：在 MySQL Workbench 中，显示数据库连接状态，准备执行 SQL。
画面 12：在 IDEA 中，控制台日志显示创建表 ACT_RU_EXECUTION。
画面 13：在 IDEA 中，控制台日志显示创建表 ACT_RU_VARIABLE。
画面 14：在 IDEA 中，显示 ActivitiTest 测试类代码，注释说明了创建 ProcessEngineConfiguration 和 ProcessEngine 的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 的 pom.xml 片段：
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring</artifactId>
    <version>7.0.0.0</version>
    <packaging>jar</packaging>
    <name>activiti-spring</name>
    <description>Activiti Spring integration</description>
    <properties>
        <slf4j.version>1.6.6</slf4j.version>
        <log4j.version>1.2.17</log4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-engine</artifactId>
            <version>7.0.0.0</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring</artifactId>
            <version>7.0.0.0</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-bpm-model</artifactId>
            <version>7.0.0.0</version>
        </dependency>
    </dependencies>
</project>
```

画面 5 的 pom.xml 片段：
```xml
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-cloud-services-api</artifactId>
    <version>7.0.0.0</version>
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
<!-- log start -->
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

画面 7 的 activiti.cfg.xml 片段：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
</beans>
```

画面 8 的 activiti.cfg.xml 片段：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/activiti"/>
        <property name="username" value="root"/>
        <property name="password" value="root"/>
    </bean>
    <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.ProcessEngineConfigurationImpl">
        <property name="dataSource" ref="dataSource"/>
        <property name="databaseSchemaUpdate" value="true"/>
    </bean>
</beans>
```

画面 9 的 PPT 内容：
```java
//创建ProcessEngineConfiguration
ProcessEngineConfiguration configuration = ProcessEngineConfiguration
        .createProcessEngineConfigurationFromResource("activiti.cfg.xml")
//通过ProcessEngineConfiguration创建ProcessEngine，此时会创建数据库
ProcessEngine processEngine = configuration.buildProcessEngine();
System.out.println(processEngine);
```

画面 10 的 ActivitiTest.java 代码：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

public class ActivitiTest {

    @Test
    public void testGenTable() {
        //1. 创建ProcessEngineConfiguration配置
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml");
        //2. 通过ProcessEngineConfiguration创建ProcessEngine
        ProcessEngine processEngine = configuration.buildProcessEngine();
        //3. 调用processEngine创建数据库表
        System.out.println(processEngine);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9：PPT 标题为“3.3.6.5 编写程序”，内容为创建 ProcessEngineConfiguration 并调用 buildProcessEngine() 方法，下方有注释说明“activiti 数据库创建，通过改变 activiti.cfg.xml 中的配置，可以执行不同的数据表处理策略”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
