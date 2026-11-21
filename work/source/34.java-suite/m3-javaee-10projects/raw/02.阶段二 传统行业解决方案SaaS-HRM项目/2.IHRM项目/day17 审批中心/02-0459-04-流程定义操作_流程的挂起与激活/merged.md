# 04-流程定义操作：流程的挂起与激活

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\04-流程定义操作：流程的挂起与激活_【海量资源尽在 ubkz.com】.mp4
- 时长 5分19秒（音频 320s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好我们现在呢已经完成了这个流程定义对象的列表查询那接下来呢咱们继续那我们接下来呢就是通过单元测试的形式和各位简单的来看一下对于这个流程定义我们能够查出来我们同样可以对这个流程设置一下它的状态把状态设置为挂起或者激活那这个呢同样我们用单元测试的形式一起来试一下好了测试流程的
[00:33] 挂起与激活好了那这边呢etatestpublic with id其一个方法咱们就叫做suspenddok那对于这个流程的挂起或者流程的激活我们同样也是使用repository Service来进行的一个操作
[00:59] 那我们操作的时候呢很简单reported Service打点里面呢有很多方法比如说呢有 suspenda process definite by id definition by id就是根据 id 我们来进行挂起那比如说呢还可以根据咱们的 key 来进行挂起等等等等那当然了这边呢还有一个方法is process definition suspend
[01:28] 这个代表的是当前的一个流程是否是一个挂起状态哎就是这么一个简单的说明那对于我们而言要想去完成流程的挂起我们可以根据这个流程的ID来进挂起OK那我们的ID是什么呢刚才咱们查到的数据库里面这边有哎就是这一长串Ctrl C把它拿到这边Ctrl V Copy过来
[01:58] 那接下来呢我们一起来执行一把看一下最终它的状态是什么我们再回到数据库来看一下目前的这个状态是不是1没错吧那接着我们执行一把来走好了这个执行的操作呢相对呢会有一点点慢各位咱们耐心等待一下吧
[02:30] 好了各位现在呢已经执行成功了没有任何问题执行成功我们回到数据库再来刷新一下刚才是1刷新走现在这个状态呢是不是就变成2了没错吧OK好了咱们操作的是POCDF这个表那注意当前呢这个状态是2表示的其实就是是一个挂起的一个状态来我把这个数据库啊等等写到这边
[03:02] 数据库的表名称流程定义这个表好了其中呢有这么一个状态字段那这个状态字段如果是一表示的是一个激活状态如果状态那如果是二表示的是一个挂起状态OK那刚才呢我们做到的事情是把一转化为二把它设置为挂起了那如果想把这个挂起呢
[03:39] 抱歉刚才写错位置了写到底下那如果想由一个挂起状态把它转成激活状态那我怎么做呢好了这边是流程的流程挂起那除了流程挂起之外我们还可以进行流程激活那流程激活怎么办呢Repository Service打点注意这个方法也很简单挂起呢叫做Suspend那激活呢就叫做Active
[04:11] report Service ACTI active叫做process definition by a同样是by id我们把这一段control c拿到这边control vok好了那接下来我们再来运行一下走而这个测试呢会有点慢啊我先暂停一下好了现在呢我的单元测试已经执行成功了
[04:46] 那接下来呢我们回到数据库来看一下那刚才呢我们数据的状态字段改成了2了那由于我设置了一个激活操作那接下来我刷新一下是不是同样又变回1了好了这个就是跟各位来看到的那对于Repository Service可以进行我们流程定义的列表查询
[05:11] 可以进行我们流程根据ID进行挂起根据ID进行激活

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中通过测试类调用 Activiti 工作流引擎的 RepositoryService，查询并挂起指定的流程定义。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 在 IntelliJ IDEA 中，展示 `ProcessTest.java` 文件，其中包含 `@Autowired` 注解的 `repositoryService` 字段。
- 代码中定义了 `findall1()` 方法，用于创建 `ProcessDefinitionQuery` 查询对象，并设置租户 ID 为“体智播客”，然后获取最新版本的流程定义列表并打印大小。
- 代码中定义了 `testSuspend()` 方法，用于挂起流程定义。

画面 2:
- 代码中 `testSuspend()` 方法的注释部分显示了流程定义状态的枚举值：`SUSPENSION_STATE_`、`1.激活状态`、`2.挂起状态`。
- 代码中 `testSuspend()` 方法的实现部分显示了挂起流程定义的调用语句。

画面 3:
- 代码中 `testSuspend()` 方法的注释部分显示了流程定义状态的枚举值：`SUSPENSION_STATE_`、`1.激活状态`、`2.挂起状态`。
- 代码中 `testSuspend()` 方法的实现部分显示了挂起流程定义的调用语句。

画面 4:
- 代码中 `testSuspend()` 方法的注释部分显示了流程定义状态的枚举值：`SUSPENSION_STATE_`、`1.激活状态`、`2.挂起状态`。
- 代码中 `testSuspend()` 方法的实现部分显示了挂起流程定义的调用语句。

画面 5:
- 控制台输出了 Spring Boot 应用启动的日志信息，包括环境变量、配置文件加载、数据库连接等。

画面 6:
- 控制台输出了 Spring Boot 应用启动的日志信息，包括环境变量、配置文件加载、数据库连接等。

画面 7:
- 展示了数据库表 `act_re_procdef` 的结构，其中包含 `ID_`、`REV_`、`NAME_`、`KEY_`、`VERSION_`、`DEPLOYMENT_ID_`、`RESOURCE_NAME_`、`DGRM_ID_`、`CATEGORY_`、`DESCRIPTION_`、`TENANT_ID_`、`HAS_START_FORM_KEY_`、`HAS_GRAPHICAL_FORMDEF_`、`SUSPENSION_STATE_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、`DERIVED_FROM_ID_`、`DERIVED_FROM_VERSION_`、

