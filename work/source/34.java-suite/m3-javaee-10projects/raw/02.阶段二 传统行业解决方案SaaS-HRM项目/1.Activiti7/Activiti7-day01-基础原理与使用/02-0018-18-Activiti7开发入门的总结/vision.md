# 画面线理解：18-Activiti7开发入门的总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\18-Activiti7开发入门的总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:05, 00:08, 03:29, 03:42, 07:23, 07:27, 07:38, 08:47, 09:41, 09:42, 09:44, 09:49, 10:01
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:13:40

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中配置并测试 Activiti 工作流引擎的运行环境，包括查看数据库表结构、编写测试代码和配置文件。

2) 按时间顺序列出每张画面的要点：
画面1：展示 IntelliJ IDEA 中打开的 activiti.cfg.xml 文件，右侧有“Configure application context”提示，下方有“StandaloneProcessEngineConfig”相关代码片段。
画面2：空白文档编辑界面，光标在起始位置。
画面3：空白文档编辑界面，光标在起始位置。
画面4：显示 PPT 页面，标题为“黑马程序员”，内容为“此时我们查看数据库，创建了 25 张表，结果如下：”，并列出多个表名。
画面5：空白文档编辑界面，光标在起始位置。
画面6：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“Idea中安装Activiti Designer”的提示。
画面7：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，包含创建 ProcessEngineConfiguration 对象的注释。
画面8：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，下方有“Event Log”窗口显示执行日志。
画面9：空白文档编辑界面，光标在起始位置。
画面10：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“Idea中安装Activiti Designer”的提示。
画面11：IntelliJ IDEA 中打开的 ActivitiTest.java 文件，显示测试方法 testGenTable() 的代码，下方有“Event Log”窗口显示执行日志。
画面12：IntelliJ IDEA 中打开的 activiti.cfg.xml 文件，显示配置内容，包括 <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.StandaloneProcessEngineConfiguration"> 及其内部属性。
画面13：空白文档编辑界面，光标在起始位置。
画面14：空白文档编辑界面，光标在起始位置，下方有“Eclipse安装Activiti Designer”和“Idea中安装Activiti Designer”的提示。

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
