# 18-Activiti7开发入门的总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\18-Activiti7开发入门的总结_【海量资源尽在 ubkz.com】.mp4
- 时长 10分5秒（音频 605s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们对于我们第一次学习activity我们大致给各位做一下整结我们来看一下这个也算是一个最基础的路门我们在这个里头给各位整结一下我们所介绍的一些内容第一个我们主要学习了什么是工作流比如说我们的一个请假的流程我们的调薪或者是调岗加薪的一个流程
[00:28] 那这个地方其实就是我们的工作流啊那工作流这里面我们又类似的介绍了几个概念啊一个是叫做工作流对吧还有工作流系统工作流系统啊还有我们的这个为了能够更好的去表达我们的这个工作流我们还介绍了啊BPMBPM对不对以及我们的BPM叫做我们的这个叫做business process
[00:58] 叫做业务process处理流程对吧业务处理流程这是一个或者是以我们的这个叫business processmodel and notice对吧介绍了这样的两个最基本的概念那其中像我们的这个BPMN是一个我们的流程就是我们的这个流程定义的一个标准的
[01:27] 标准的定义语言我们的这个叫做流程流程定义就是说我们昨天上次就是我们上次给各位介绍有一个叫做我们的这个叫做请假的流程这个请假的流程其中里头涉及到的就有我们比如说作为员工的话他应该是申请我们的请假单
[01:57] 申请我们的请假单或者叫填写填写请假单那它填写完了呢就会进入到我们的这个部门经理环节对吧然后再进入到我们的这个总经理环节当然在这要注意啊各个公司走的这个流程可能不太一致啊但是没关系我们将来唯一变化的就是我们的这个流程定义的图对不对最后比如说进入到我们的这个财务财务财务经理
[02:26] 去做传档对吧那这就是我们啊自己搞了一个流程搞了一个我们自己的流程但是这个流程呢要怎么样去做可以让它更加规范对不对所以呢我们在这一堂给各位啊就讲了一个叫做我们的这个叫做流程设计器对不对流程设计器那这个流程设计器作为一款啊我们的这个软件我们呢给各位分别讲了在Eclips里头我们怎么去怎么去安装对吧
[02:55] 安装我们的这个叫做activityactivity designer对吧activity designer还有一个就是我们ideal中ideal中又是如何去安装我们的这个activity designer对不对在装好之后我们这些软件装好之后我们都需要测试一下对吧测试一下测试是否已经安装成功对不对这都是我们已经做完的工作
[03:26] 然后下一个环节呢我们又接着给各位啊给各位讲了一下我们的这个activity真正开发的这个环境准备对吧那环境准备我们这一次还需要有我们的数据库我们用的是myseco数据库对吧然后呢我们在这个里头给各位啊应该是在这个过程中给各位讲了一个非常重要的点就是我们为什么为什么啊使用activity啊activity可以实现
[03:56] 可以实现啊业务代码不变更不变更那就可以啊就可以实现流程更新对吧其实我们整个这个过程呢我们讲的这些流程定义啊流程设计器啊这些标准的BPMM其实都是围绕这个环节在做对吧好那我们啊我们在这个地方给各位的答案就是他呢将来我们
[04:23] 真正我们的流程发生更新之后我们只是把流程定义给它改了对吧流程定义图做更新啊做更新然后呢流程定义图做完更新之后它里头读取各个节点的信息就先会读取到先读取节点信息先读取我们的节点信息到我们的数据库表吧数据库表中对吧那然后呢我们后续只要
[04:52] 后续只要针对我们的数据户表做操作就可以了后续就针对数据户表进行操作这样我们就可以实现流程快速更新只要对我们的数据户表做操作后面我们就给各位进一步介绍了我们的这个activity支持支持的这个数据户有哪些对吧有哪些
[05:23] 我们这次主要用的是MySQL数据库然后下一个环节我们就给各位介绍了既然你支持我们的MySQL数据库我们就讲了25张25张表的创建为什么说到这个点这是一个重点因为我们activity要工作activity要能够工作就必须就必须有
[05:51] 表结构的支撑对不对由它的这个表结构支撑表结构的支撑那我们如果25张表都没有那我们说你把这个流程定义图里头的过过节点信息读取到我们的数据库表里头那你连数据库表都没有那后续工作就开展不了对吧所以我们后面就紧接着给各位讲了使用Java使用Java代码
[06:19] 使用Java代码方式来生成我们的25张表结构对不对25张表那这个Java代码其中呢主要的这个具体我们的这个Java工程是怎么搞的第一步是我们的POM.xml文件对吧需要去需要引入需要引入相关的这个坐标对吧需要引入activity7开发相关的这个坐标这是一项
[06:49] 完了我们当把这个工作做好了我们第二个工作刚才我们说了是把我们的logo4jpropertiesproperties直接这个是一个日志文件添加进来对吧然后第三个工作我们在这个里头是创建了一个activity.cfg.xml注意这个是它的一个默认的默认的配置文件是activity默认的配置文件也可以是其他名称也可以
[07:19] 是其他名称这个过程呢因为我们真正写这个加密代码的时候你是在这个里头自己加载了这个配置文件的名字所以如果说这个名字是叫做abc.xml那我们这个人就应该写abc.xml就这个意思啊好我们这个时候再回到这个总结啊这是第三个环节当我们把这个文件都配好了我们第四个环节是不是就写加密代码就可以了
[07:47] 好我们的第四个环节啊就是呢写我们的这个交代码那写这个交代码其中啊我们这里头主要就是两个关键的类给各位再再次说一下啊一个是叫做process engineprocess engine configuration对吧configuration一个是这样的一个类啊好除了这个还有一个就是我们的一个叫做process engine的这个类是不是叫做process engine的process engine的这个类啊
[08:17] 主要就是创建这两个类的对象对吧我们把这两个类的对象一旦生成出来基本上25张表的工作就创建出来了那我们在这个activitycfg.xml这个文件中我们刚才做了些什么操作第一个我们是配置我们的数据源配置数据源当然我们后期又说了这个数据源其实也可以不用单独配置出来对吧也是可以成功的好这是
[08:47] 这是一个工作啊配置数据人还有一个工作就是叫做创建我们的这个叫做Process EngineConfiguration的对象对吧Configuration的对象那这个对象我们主要是使用托机的方式来创建使用托机方式托机方式创建那就是单独单独一台机器这种方式来创建那我们使用的这个对象是叫做StandardLambStandardLamb
[09:19] 叫做Process Engine Configuration使用这种方式使用这种方式来实现我们的创建我们的Standard Line Process Engine Configuration里头有一个很重要的属性这个属性就是决定我们是否需要去自动生成我们的25张表这个属性是叫做
[09:46] 叫做database schema update对吧我们需要将这个首先的值啊设置为true对不对设置为true好让它的这个值啊等于true对吧这样呢就可以实现我们自动去创建我们的25张表这个就是呢大致我们所介绍的支点啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中配置并测试 Activiti 工作流引擎的运行环境，包括查看数据库表结构、编写测试代码和配置文件。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IntelliJ IDEA 中打开的 activiti.cfg.xml 文件，右侧有“Configure application context”提示，下方有“StandaloneProcessEngineConfig”相关代码片段。
画面2：空白文档编辑界面，光标在起始位置。
画面3：空白文档编辑界面，光标在起始位置。
画面4：显示 PPT 页面，标题为“黑马程序员”，内容为“此时我们查看数据库，创建了 25 张表，结果如下：”，并列出多个表名。
画面5：空白文档编辑界面，光标在起始位置。
画面6：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“IDEA中安装Activiti Designer”的提示。
画面7：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，包含创建 ProcessEngineConfiguration 对象的注释。
画面8：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，下方有“Event Log”窗口显示执行日志。
画面9：空白文档编辑界面，光标在起始位置。
画面10：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“IDEA中安装Activiti Designer”的提示。
画面11：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，下方有“Event Log”窗口显示执行日志。
画面12：IntelliJ IDEA 中打开的 activiti.cfg.xml 文件，显示配置内容，包括 <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration"> 及其内部属性。
画面13：空白文档编辑界面，光标在起始位置。
画面14：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“IDEA中安装Activiti Designer”的提示。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
<bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
</bean>

画面7：
public class ActivitiTest {
    @Test
    public void testGenTable() {
        //1.创建ProcessEngineConfiguration对象，第一个参数：配置文件名称，第二个参数：processengineconfiguration
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml", beanName="process");
        //2.创建ProcessEngine对象
        ProcessEngine processEngine = configuration.buildProcessEngine();
        //3.输出processEngine对象
        System.out.println(processEngine);
    }
}

画面12：
<bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration">
    <property name="dataSource" ref="dataSource"/>
    <property name="jdbcDriver" value="com.mysql.jdbc.Driver"/>
    <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/activiti"/>
    <property name="jdbcUsername" value="root"/>
    <property name="jdbcPassword" value="root"/>
    <property name="databaseSchemaUpdate" value="true"/>
</bean>

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面4：
标题：黑马程序员
内容：此时我们查看数据库，创建了 25 张表，结果如下：
表格数据：
- act_ge_bytearray
- act_ge_property
- act_hi_actinst
- act_hi_comment
- act_hi_detail
- act_hi_eventsubscr
- act_hi_identitylink
- act_hi_procinst
- act_hi_taskinst
- act_hi_varinst
- act_id_group
- act_id_membership
- act_id_user
- act_re_procdef
- act_ru_eventsubscr
- act_ru_execution
- act_ru_identitylink
- act_ru_job
- act_ru_task
- act_ru_variable
- act_ru_id
- act_ru_id
- act_ru_id
- act_ru_id
- act_ru_id

5) 无

