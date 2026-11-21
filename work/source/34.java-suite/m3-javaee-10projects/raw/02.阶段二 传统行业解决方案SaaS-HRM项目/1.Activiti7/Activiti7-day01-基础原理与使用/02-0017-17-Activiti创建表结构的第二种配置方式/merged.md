# 17-Activiti创建表结构的第二种配置方式

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\17-Activiti创建表结构的第二种配置方式_【海量资源尽在 ubkz.com】.mp4
- 时长 3分10秒（音频 190s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们说了如果说你不希望直接再去创建一个dbcp的数据源然后再去注入这个data source如果你不希望用使用这种方式其实你可以把这里头的各个属性直接copy拿过来就可以了但是你要注意我们刚才在测试的时候这个属性都是有问题的对吧那是什么原因导致的各位注意就是要改一个名字就可以了你发现这里头有很多jdbc开头的这样的一些属性
[00:28] 比如说我们这个地方就直接改成叫JDBC的driver而原来叫做driver class name而我们的这个URL这个也要改一下叫JDBC URL那我们的这个username也要改一下叫JDBC username对吧那这个password也给改一下叫JDBC password好了这样呢其实我们也就做完了这个工作这样
[00:55] 真正跑起来的时候我们就不需要上面的这个data source的配置了不需要它我们可以这样一起给各位也测一下这个效果我们这个时候就直接比如说把这个去掉然后在这个后边再去给它添加一个鞋杆柄子这样就可以跑起来了当然我要跑这个工作我可以我让它看到明显的效果我可以这样先把这个整库都删掉
[01:24] 然后再去创建对吧这样的话我们一刷新这里边就不会有这个表情号了对吧然后再回到我们这边重新去执行因为你看我这里要用的是ProcessEngineConfiguration01对吧所以我这边这个代码目前来看的话不需要做任何的改动好我们只是改动了activityconfigure.xml里头的配置项现在这个DataSource不住相当于是把这个DataSource所依赖的数据库的
[01:53] 连接信息给它直接注入进来一样也是可以支持的好这个地方我们重新再跑一下对吧其实我们在测试成功之后咱们再去刷一下这个库各位您发现这种方式其实也可以刚才我们在讲这个部分的时候咱们同学只要注意一点细节对吧就是你如果不想用对的硕士其实也没问题但是你要做的就是这里头的Google属性稍微要改个名对吧
[02:28] 改个名要不然不是直接原模一样给它加入进来那我们通常情况下各位还是可以选择用这种方式对吧这种方式直接注入数据源的好处是什么它的好处就是我们相当于做数据源的可以专心一致去搞自己的数据源对吧把数据源做好我们将来我们的activityactivity的这个process engine configuration
[02:55] 只要直接去使用我们的Dead Source数据源就可以了所以呢我在这里面更加推荐使用我们的第一种方式更加推荐各位使用我们的第一种方式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

