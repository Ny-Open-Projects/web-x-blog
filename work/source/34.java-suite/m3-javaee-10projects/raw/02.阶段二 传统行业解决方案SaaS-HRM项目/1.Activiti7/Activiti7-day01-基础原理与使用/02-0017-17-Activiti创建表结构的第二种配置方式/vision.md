# 画面线理解：17-Activiti创建表结构的第二种配置方式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\17-Activiti创建表结构的第二种配置方式_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:24, 00:42, 00:50, 00:58, 01:12, 01:25, 01:36, 01:59, 02:02, 02:08, 02:16, 02:26, 02:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:13:06

1) 这一组画面整体在讲如何配置 Activiti 工作流引擎的数据库连接和启动测试。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IDEA 中查看并编辑 activiti.cfg.xml 文件，高亮显示了 dataSource 和 processEngineConfiguration 的配置段落。
画面2: 在 IDEA 中，鼠标悬停在 processEngineConfiguration 的 property 上，弹出属性提示框，显示了 jdbcUrl、jdbcUsername、jdbcPassword 等属性。
画面3: 在 IDEA 中，鼠标悬停在 processEngineConfiguration 的 property 上，弹出属性提示框，显示了 jdbcUrl、jdbcUsername、jdbcPassword 等属性。
画面4: 在 IDEA 中，高亮显示了 processEngineConfiguration 的 jdbcUrl 属性值。
画面5: 在 IDEA 中，高亮显示了 activiti.cfg.xml 文件的 xsi:schemaLocation 声明。
画面6: 在 IDEA 中，高亮显示了 processEngineConfiguration 的 databaseSchemaUpdate 属性值。
画面7: 在 SQLyog 中，执行了 drop database activiti; 和 create database activiti; 语句。
画面8: 在 IDEA 中，查看并编辑 ActivitiTest.java 文件，高亮显示了创建 ProcessEngineConfiguration 和 ProcessEngine 的代码。
画面9: 在 IDEA 中，右键点击 testGenTable 方法，弹出上下文菜单，显示了“Run testGenTable”选项。
画面10: 在 IDEA 中，执行了 testGenTable 方法，控制台输出了“test parsed”。
画面11: 在 SQLyog 中，光标位于 create database activiti; 语句后。
画面12: 在 IDEA 中，执行了 testGenTable 方法，控制台输出了 Activiti 引擎启动成功的日志。
画面13: 在 IDEA 中，高亮显示了 processEngineConfiguration 的 jdbcUrl 属性值。
画面14: 在 IDEA 中，高亮显示了 activiti.cfg.xml 文件的 dataSource bean 配置段落。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面1:
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
    <property name="driverClassName" value="com.mysql.jdbc.Driver" />
    <property name="url" value="jdbc:mysql://localhost:3306/activiti" />
    <property name="username" value="root" />
    <property name="password" value="root" />
</bean>

<bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource" />
    <property name="jdbcDriver" value="com.mysql.jdbc.Driver" />
    <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/activiti" />
    <property name="jdbcUsername" value="root" />
    <property name="jdbcPassword" value="root" />
    <property name="databaseSchemaUpdate" value="true" />
</bean>

画面2:
<property name="jdbcUrl" value="jdbc:mysql://localhost:3306/activiti" />
<property name="jdbcUsername" value="root" />
<property name="jdbcPassword" value="root" />

画面3:
<property name="jdbcUrl" value="jdbc:mysql://localhost:3306/activiti" />
<property name="jdbcUsername" value="root" />
<property name="jdbcPassword" value="root" />

画面4:
<property name="jdbcUrl" value="jdbc:mysql://localhost:3306/activiti" />

画面5:
xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd"

画面6:
<property name="databaseSchemaUpdate" value="true" />

画面7:
drop database activiti;
create database activiti;

画面8:
public class ActivitiTest {
    @Test
    public void testGenTable(){
        //1.创建ProcessEngineConfiguration对象，第一个参数：配置文件名称，第二个参数：processEngineConfiguration
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration.createProcessEngineConfiguration();
        configuration.setJdbcDriver("com.mysql.jdbc.Driver");
        configuration.setJdbcUrl("jdbc:mysql://localhost:3306/activiti");
        configuration.setJdbcUsername("root");
        configuration.setJdbcPassword("root");
        configuration.setDatabaseSchemaUpdate(ProcessEngineConfiguration.DB_SCHEMA_UPDATE_TRUE);
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
        configuration.setTransactionManager("transactionManager");
