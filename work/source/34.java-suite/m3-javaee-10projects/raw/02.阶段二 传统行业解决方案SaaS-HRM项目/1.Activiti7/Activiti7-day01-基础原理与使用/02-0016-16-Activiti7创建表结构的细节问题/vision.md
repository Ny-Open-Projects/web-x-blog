# 画面线理解：16-Activiti7创建表结构的细节问题

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\16-Activiti7创建表结构的细节问题_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:37, 01:21, 01:49, 02:45, 03:56, 05:27, 06:18, 06:26, 06:57, 07:21, 08:04, 08:27, 08:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:12:15

1) 这一组画面整体在讲如何通过 Spring 配置文件初始化 Activiti 流程引擎并自动创建数据库表结构。

2) 按时间顺序列出每张画面的要点：
画面1：MySQL Workbench 界面，连接到本地数据库，左侧显示 information_schema 数据库结构，右侧查询编辑器为空。
画面2：MySQL Workbench 界面，光标在查询编辑器中，准备输入 SQL。
画面3：MySQL Workbench 界面，查询编辑器中输入了 SQL 语句：
drop database activiti;
create database activiti;
画面4：IntelliJ IDEA 界面，打开 activiti1 项目，显示 activiti.cfg.xml 文件内容，其中包含数据源配置和流程引擎配置，下方终端显示测试通过。
画面5：IntelliJ IDEA 界面，显示 ActivitiTest.java 文件，其中 testGenTable 方法注释说明了流程引擎配置的创建方式，下方终端显示测试失败。
画面6：IntelliJ IDEA 界面，显示 activiti.cfg.xml 文件，光标在 processEngineConfiguration01 bean 的 databaseSchemaUpdate 属性上。
画面7：IntelliJ IDEA 界面，显示 activiti.cfg.xml 文件，光标在 processEngineConfiguration01 bean 的 databaseSchemaUpdate 属性上，下方终端显示测试失败。
画面8：PPT 页面，标题为“3.3.3 ActivitiTest”，内容说明通过 createProcessEngineConfigurationFromResource 方法可以使用不同的 beanName。
画面9：PPT 页面，标题为“3.3.7 数据库表的命名规则”，内容说明 Activiti 表以 ACT_ 开头，第二部分是两个字母标识，如 ACT_RE_* 表示 repository，ACT_RU_* 表示 runtime，ACT_ID_* 表示 identity，ACT_GE_* 表示 general。
画面10：IntelliJ IDEA 界面，显示 ActivitiTest.java 文件，代码中使用了 createProcessEngineConfigurationFromResource 方法，参数为 activiti.cfg.xml 和 processEngineConfiguration01。
画面11：MySQL Workbench 界面，查询编辑器中输入了 SQL 语句：
drop database activiti;
create database activiti;
画面12：IntelliJ IDEA 界面，显示 activiti.cfg.xml 文件，光标在 processEngineConfiguration01 bean 的 databaseSchemaUpdate 属性上，下方终端显示测试通过。
画面13：PPT 页面，标题为“此时我们查看数据库，创建了 25 张表，结果如下：”，下方列出数据库表名，如 act_re_procdef、act_ru_event_subscr 等。
画面14：IntelliJ IDEA 界面，显示 activiti.cfg.xml 文件，光标在 processEngineConfiguration01 bean 的 databaseSchemaUpdate 属性上，下方终端显示测试通过。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
drop database activiti;
create database activiti;

画面4：
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver" />
        <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
        <property name="username" value="root" />
        <property name="password" value="root" />
    </bean>
    <!-- activiti单运行时的processEngine配置对象(processEngineConfiguration)，使用单启动方式
        默认情况下，beanId为processEngineConfiguration
    -->
    <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
        <property name="dataSource" ref="dataSource"/>
        <property name="databaseSchemaUpdate" value="true"/>
    </bean>
</beans>

画面5：
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

public class ActivitiTest {

    @Test
    public void testGenTable(){
        //1.创建ProcessEngineConfiguration对象，第一个参数：配置文件名称，第二个参数：processEngineConfiguration beanId
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml", "processEngineConfiguration");
        //2.创建ProcessEngine对象
        ProcessEngine processEngine = configuration.buildProcessEngine();
        //3.输出processEngine对象
        System.out.println(processEngine);
    }
}

画面6：
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver" />
        <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
        <property name="username" value="root" />
        <property name="password" value="root" />
    </bean>
    <!-- activiti单运行时的processEngine配置对象(processEngineConfiguration)，使用单启动方式
        默认情况下，beanId为processEngineConfiguration
    -->
    <bean id="processEngineConfiguration01" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
        <property name="dataSource" ref="dataSource"/>
        <property name="databaseSchemaUpdate" value="true"/>
    </bean>
</beans>

画面10：
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

public class ActivitiTest {

    @Test
    public void testGenTable(){
        //1.创建ProcessEngineConfiguration对象，第一个参数：配置文件名称，第二个参数：processEngineConfiguration beanId
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml", "processEngineConfiguration01");
        //2.创建ProcessEngine对象
        ProcessEngine processEngine = configuration.buildProcessEngine();
        //3.输出processEngine对象
        System.out.println(processEngine);
    }
}

画面12：
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd">
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver" />
        <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
        <property name="username" value="root" />
        <property name="password" value="root" />
    </bean>
    <!-- activiti单运行时的processEngine配置对象(processEngineConfiguration)，使用单启动方式
        默认情况下，beanId为processEngineConfiguration
    -->
    <bean id="processEngineConfiguration01" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
        <property name="dataSource" ref="dataSource"/>
        <property name="databaseSchemaUpdate" value="true"/>
    </bean>
</beans>

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面8：PPT 标题为“3.3.3 ActivitiTest”，内容说明通过 createProcessEngineConfigurationFromResource 方法可以使用不同的 beanName。
画面9：PPT 标题为“3.3.7 数据库表的命名规则”，内容说明 Activiti 表以 ACT_ 开头，第二部分是两个字母标识，如 ACT_RE_* 表示 repository，ACT_RU_* 表示 runtime，ACT_ID_* 表示 identity，ACT_GE_* 表示 general。
画面13：PPT 标题为“此时我们查看数据库，创建了 25 张表，结果如下：”，下方列出数据库表名，如 act_re_procdef、act_ru_event_subscr 等。

5) 无。
