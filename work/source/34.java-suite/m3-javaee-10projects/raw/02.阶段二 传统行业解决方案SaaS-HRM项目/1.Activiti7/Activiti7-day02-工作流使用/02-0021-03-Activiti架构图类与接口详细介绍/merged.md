# 03-Activiti架构图类与接口详细介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\03-Activiti架构图类与接口详细介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 12分20秒（音频 740s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们通过对于activity这个架构图的一个讲解我们应该能够感受到只要我们有了这一堆Service接口之后我们将来对于activity的后续的操作应该基本上就简单很多了因为有了这些Service我们再去实现对这些表的操作我们将来只需要去学会这些Service的使用就可以了
[00:29] 对吧那要注意就是我在这里特别提醒一下我们的这个Service在我们的activity7这个版本里面它已经把identity Service和我们的form Service两个都已经删除了那这个各位要了解一下如果你使用的是activity7的最新版的话你要注意一下当然我们很多公司在开发的时候我看用五和六还是比较多的对吧
[00:58] 那我们的这个期呢也是一种趋势对吧我们讲课的时候学习的时候就学它的这个最新版这个也是有原因的因为任何一个技术呢你最先掌握了对吧那将来你在这个在这个行业里头将来就更加容易立足对吧然后我们的真正开发的时候用它的低版本这个其实没有任何的问题那我们接着再往后去讲
[01:27] 就是来一起看一下我们的这个activity接下来我们将从这几个方面就是一个是我们的activityconfigure.xml这个配置文件另外一方面就是从我们的这个configuration以及我们的这个process engine以及我们的Service从这四个方面开始来给各位做一下介绍那activity.cfg.xml作为我们的这个activity的一个默认的配置文件
[01:57] 那将来呢我们有两种方式啊来创建我们的这个Process Engine Configuration对吧那我们一起来看一下啊其中第一种方式呢就是呢我们不借助于不借助于啊我们的这个Spring直接使用的是当机的方式开始运行对吧我们用的是Dynaline Process Engine Configuration用这种方式除了这种方式呢我们还有另外的一种方式
[02:24] 这种方式就是要求我们开始要考虑与Spring整合的方式来做我们直接进到这边来因为刚才这一段我们都已经介绍过了我们就直接进入到Spring Process Engine Configuration这种方式就要求我们必须与Spring整合之后才可以去使用的一种方式如果咱们细心的同学你会发现
[02:51] 我们的这个activity.cfg.xml它本身呢你发现它本身这个配置文件本身就是Spring的这个配置文件对吧也就是告诉各位我们的这个activity和我们的这个Spring整合将来搞配置文件的话其实我们有这个配置文件其实也就可以了像我们这里头这个bin的写法对吧都跟我们的Spring配置文件的写法是一致的
[03:17] 然后我们再回到这边来这是各位要去先了解一下我们如果说将来要去实现activity与Spring整合的话那我们将来可能要用到整合有专门的一个叫Spring Process Engine Configuration有这样的一段这个后面我们会详细给各位去讲这个整合的步骤我们
[03:42] 对于具体的整合的配置现在我暂时就不去使劲给各位介绍因为后面我们再去专门做Spring与Activity整合的时候还会给各位去介绍的所以这一段我们先大家了解一下就可以了然后通过我们的介绍各位可以看到我们的这一堆Service将来也都在这里头直接就配好了配好后
[04:12] 我们再去使用的话应该说我们将来要去用这些Service的话在Spring中直接可以通过AtaAutoVal来实现我们的注入对吧注入一个RepositoryService我将来直接就可以使用这一点我只是先给各位做一个大概的简介然后后面等我们做Spring与Activity整合再详细给各位介绍好我们
[04:41] 这是关于我们的activityconfigure.xml如何来创建我们的这个processengineconfiguration对吧两种方式一种是通过当机standard run processprocessengineconfiguration一种是通过借助于我们的split来实现那我们呢再给各位学一个小的点吧那就是关于我们的这个processengine如何来创建
[05:11] 我们的这个Process Engine在创建的时候相当于是一个工作流的引擎是一个门面的接口那我们创建它除了我们开始在这边给各位介绍的Activity Test的点加这种方式除了我们早期的这种方式第一种方式就是我们早期所介绍的这种方式通过Configuration点Build Process Engine通过这种方式除了这种方式之外我们其实还有一种方式
[05:41] 这第二种方式我们写起来的时候就相当于更加简便一些我们也可以做一个简单的测试来看一下效果比如说public void我就写一个叫test还是叫generate table好各位你注意一下我们在这个地方先把我们早期的数据库还是一样的要给它job database先给它清掉
[06:10] 然后我们再通过create database再把它创建出来sati vi ti activity下面我们再执行看一下效果先去把它删掉然后我们再去重新把这个库创建出来这时候你再去刷新的话我们这个库里头就没有任何的表了好我们下面就再次回到我们的加码代码在这边我们就直接
[06:37] 用一行代码来创建我们的process engine这样的一个对象那如果你要把它创建出来我们这个时候就需要用到有一个叫做process engineprocess engine之点里头就有一个叫get default process engine那如果你要用这一行代码就可以搞定我们的这个process engine的这个对象的创建成为了
[07:05] 达到也一样可以去创建我们的这25张表那我们要做到这个效果我们这边呢就有几点是默认的啊要具备的几个条件啊如果说你不具备这个条件的话那对不起你应该是啊你应该是不能够使用这个最简最简洁的方式来创建我们的这个数据库的表那这个条件是什么啊第一个
[07:32] 就要求了我们对应的配置activity的配置名称activiti配置文件名称就必须是叫做activitiactivity.cfg.xml这是第一个条件第二个条件是我们必须要做到我们的activity在这个里头它的名称不能随便瞎写
[07:59] 它的名称呢要求我们还得回到我们的这个0还得回到我们的就默认的Process Engine Configuration这样的一个名称第二个呢就是我们的这个叫做叫做binbin的IDbin的ID那肯定是要让它等于一个这样的名称这是两个条件如果做到了这两个条件那我们呢真正
[08:28] 将来在测试表生成的时候你就可以直接使用Process Engine去调用它的GetDefaultProcessEngine通过这一行代码也可以搞定我们的表的生成我们可以一体来测试一下执行的效果好现在我们就可以看到这边不断的在生成我们的表结构对吧好整个这个过程就已经结束了对吧那这样基本上我们就完成了我们这个工作
[08:59] 而且最后呢因为我们这边呢在这里头要去输出我们的这个activity的这个process engine的对象对吧这个最后一行呢咱们其实就可以看到将我们的这个对象啊就已经输出了对吧输出了这个对象啊好我们再回到我们的这个表结构来看一下啊应该呢就会创建出我们想要的这个表对吧这就是啊我们在这边呢给各位啊又提供了一种途径对吧这种途径呢就要求我们在写
[09:27] 写这个配置文件的时候以及配置文件里头这个process engine configuration的时候那咱们必须按照这个要求去做对吧否则呢那你将不能够创建成功啊不能比如说这个代码运行的时候它是不会成功的啊它会告诉你啊比如说这个文件找不着或者是什么呢或者是我们对应的这个bin的ID不叫这个名字它也找不着明白是吧这是我们啊搞的这个
[09:54] 搞得刚才在这里面给activity这个详细啊介绍了一下啊然后呢我们底下的这个各种Service呢我们其实在之前我在给各位讲的时候也给各位大致做了一个演示啊后面我们可以根据自己的实际情况对吧如果说你呢想用runtime Service那你可以通过process engine调用它的getRuntimeService来实现比如说要用reportable的Service也是一样的啊
[10:22] 那Repository的Service是Ictivity的资源管理类Runtime是我们流程运行的管理类Task是任务的管理类或者是History是我们历史的管理类那总之就是我们在这边如果说将来你想操作我们后续的这些相关的表你比如说我要操作HIT开头的这一堆表那我们应该肯定用的是History Service来解决我们的问题那如何去使用我们的每一个Service我直接
[10:51] 在这边开始也给各位介绍过那我们可以通过我们的 processengine.get比如说history Service那这样你就可以得到一个我们的history Service就可以拿到了所以说整个这个过程也是非常简单对吧也非常简单这样我们就拿到了一个历史任务的Service那有了history的Service将来后续你就可以去调用它内部所提供出来的各个方法然后就可以去操作我们后面activity的
[11:21] 相关的这个流程的历史信息就是这个意思啊也非常的简单那通过刚才的这一段啊我们主要是给各位啊介绍了我们不同的不同的这个Service啊应该如何去得到以及我们每一个Service在这里头它真正所起到的这个作用啊那我们呢重点要求各位呢要掌握这四个Service就可以了最终最后的这个叫做manager Service这个是
[11:49] 本身是activity的流程引擎的管理管理类本身是需要用到的也就是说我们activity本身如果要去做它activity本身的一些管理那我们就需要用到这个叫做manager Service所以说一般情况下我们呢是在开发的时候用的很少那基本上我们对于我们的这个activity的这个架构图和我们底下的每一个相关的这个类
[12:18] 就给各位介绍到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
是 activiti 的资源管理类，提供了管理和控制流程发布包和流程定义的操作。使用工作流建模工具设计的业务流程图需要使用此 Service 将流程定义文件的内容部署到计算机。
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

