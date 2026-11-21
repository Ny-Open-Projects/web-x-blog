# 15-发起申请：步骤分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\15-发起申请：步骤分析_【海量资源尽在 ubkz.com】.mp4
- 时长 8分50秒（音频 531s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经完成了审批列表还有审批详情的相应的查询工作那接下来呢就是完成最后的两个功能咱们先来看第一个也是比较难的一个就叫做发起我们的流程申请那发起申请呢咱们可以一起来分析一下就是我们这个整个业务应该怎么去做以及涉及到的表的一些操作那我们回到页面上从起点一起来看一下
[00:31] 找到页面那我们就以请假流程为例点击请假那在这边呢可以填写上我们的请假信息那可以填写请假的开始时间结束时间请假究竟有几天以及我们请假的一些事由那接下来呢打开F2我们点击提交来看一下发送相关参数那点击提交之后咱们可以看到发送了一个请求
[00:58] 那相关参数呢在底下呢都已经给我们罗列出来了没错吧那我把这个相关参数放到一张截图上我们开始进行分析那这个是我们的请假流程我们就是以请假流程为例那我当一点击请假的时候它就把这些参数呢发送到了我们的Controller当中controllerc-1-t-r-o-l-1-e-rcontroller
[01:30] 那这边呢我有一个小小的问题是这样的那请假流程可能涉及到类似这些参数那可能还有我们的加班可能还有离职等等的流程那不同的流程它传递的参数是不一样的那不知道各位还有印象吗我们最终是不是把这些数据给它保存到了我们拓展的这个流程的POC data这个数据字段当中啊那里面是不是把请假
[02:01] 发送到的所有数据以JSON字符创的形式保存下去没错吧所以呢在我们这边你发送过来我们的Controller接收的时候咱们不用自己定义一个新的对象我们直接用map来接收其实就好了Controller我们map接收参数map接收参数之后接下来把我们这个通过Controller把我们接收的这些参数是不是可以把它调用到Service当中来完成我们的
[02:34] 最终业务处理SERVICE这是我们的survey层去完成我们的相关业务处理那在我们这个业务处理survey当中我们应该怎么做呢这个是需要和各位一定要注意的地方那首先呢就是咱们这边要对应的数据库呢有两类数据库没错吧那第一类呢是我们的IHIM系统系统数据库好了那接下来第二类对应的是我们activity
[03:06] 对应的数据库没错吧那我们的这回一个申请的一个流程那我们同时又要操作咱们IHM相关的数据库表以及activity相关的数据库表这些应该各位都知道没错吧那我们就开始那对于思维层来说首先咱们要做的事情就是对我们IHM数据库里面的这两张表来进行处理第一个就是我们的数据库当中的咱们来看一下
[03:38] instance这张表回到这张图上里面保存我们的保存我们的业务流程数据那除了这张表之外呢还有一张表就是我们这边的明细的这张表任务明细表业务任务明细的这个数据要把它保存到上边这张表里那接下来呢activity数据库这些表呢并不需要我们进行额外的关注
[04:18] 我们可以调用ATM提供的API完成数据库操作那这个API里面就包含我们启动流程包含我们任务节点的一个完成处理它就会自动的对数据库进行操作那这个是我们数据库要对应的这些表那接下来呢那在我们Service层当中要做的事情究竟有
[04:48] 多少呢我们一起来分析一下那首先呢就是在这边我们要对咱们自己的数据库进行操作没错吧那自己的数据库要有PLC Intents对象要有我们Task Intents对象这些是不是我们就需要构造啊所以在我们这边咱要做的事情呢第一件事情就是构造我们的业务数据那构造业务数据重点构造的就是PLC Intents以及我们这边可能会有
[05:19] OC task instance这是构造我们的相应业务数据好了业务数据我们构造好了之后那接下来我们就开始着手当然先别保存我们最后去保存数据库其实也可以啊那我们接下来就开始着手干嘛呢就是对activity数据库来进行操作那我们都知道我们这边呢其实就是要发起流程发起流程其实调用activity提供的API就可以了
[05:52] 那我们究竟调用的是哪个流程呢数据库里面请假流程我们还有加班流程离职流程等等都有那我们怎么就能定位到你现在是一个请假流程各位能够看到传递的参数是不是有一个process key所以我们接下来就是根据CESS key去查询我们的流程定义其实查询的是底下activity表
[06:17] 因为只有在activity表章中我们才能查询出我们具体要去执行哪一个流程定义没错吧那查询好了之后接下来第三件事我们就开始着手开启流程那注意这个开启流程也是通过activity提供的API来完成的API操作很简单一句话的事好了那接下来开启了流程之后那接下来第四个事情
[06:45] 第四个事情是这样的我们开启流程并不等于我现在已经执行了第一个节点因为各位应该还记着那不管是哪个流程咱们第一个节点是不是都叫做提交申请啊那么刚才开启流程只是在第一个开始的这个阶段那么提交是不是还应该有提交申请的第一个咱们用户任务啊所以咱们这边呢还有接下来的投注第四个就是执行第一个
[07:17] 用户任务Task那就叫Task吧这个是什么呢就是我们的用户申请好了那接下来那这样一来呢咱们前四步呢就已经都准备好了那前四步其实正常你执行完成之后咱们就能够在列表当中得到这么一条审批记录但是当前审批人有吗当前审批人是不是没有啊也就意味着你现在提交了申请那
[07:51] 接下来的审批人究竟是谁我们的数据库表里面是不是还没有啊那没有怎么办也就意味着我们在这边还要做第五个操作那获取下一个用户任务那获取下一个用户任务主要目的就是获取我们的候选人数据那得到这些候选人数据是不是给他设置到我们自己的
[08:23] 流程定义当中啊没错吧那这样一来我们保存了之后保存了之后是不是就可以在流程定义里面能够看到我们下一个节点究竟由谁来执行我们页面就能够方便查询没错吧所以对于我们这回完成的流程申请而言其实就是这么几个步骤而已

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中发起请假申请，追踪其在后端（Controller、Service、Activiti 流程引擎）的处理流程，并通过数据库查看相关数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 iHRM 系统的“员工请假”页面，日历视图中显示了请假日期（如 2019-09-02）。
画面 2: 在请假申请表单中，填写了请假类型为“请假”，申请单位为“按天”，开始时间为“2019-09-02 00:00:00”，结束时间为“2019-09-03 00:00:00”，请假时长为“1”，申请理由为“xxxxxxxx”。
画面 3: 浏览器开发者工具中显示，提交请假申请的 POST 请求（URL: http://127.0.0.1:8085/api/user/process/startProcess）返回了 404 Not Found 错误。
画面 4: 在记事本中粘贴了用于发起请假申请的 JSON 数据，内容为：
{
  "applyUnit": "技光",
  "duration": "1",
  "emailTime": "2019-09-02 00:00:00",
  "holidayType": "1",
  "processKey": "process_leave",
  "processId": "1",
  "reason": "xxxxxxxx",
  "startTime": "2019-09-02 00:00:00",
  "userId": "118178950026271668"
}
画面 5: 在 SQLyog 数据库工具中，查看了 `proc_instance` 表，但数据为空。
画面 6: 在 Typora 中绘制了流程图，显示“Controller”组件。
画面 7: 在 Typora 中绘制了流程图，显示“Controller”接收参数后调用“Service”组件。
画面 8: 在 Typora 中绘制了流程图，显示“Controller”调用“Service”，并指向“ihrm系统数据库”和“activiti数据库”。
画面 9: 在 SQLyog 数据库工具中，查看了 `proc_instance` 表的结构，包含字段如 `process_id`, `user_id`, `proc_apply_time`, `proc_state`, `proc_task_instance_id` 等。
画面 10: 在 Typora 中绘制了流程图，显示了多个窗口（SQLyog、iHRM、Typora、项目文件夹等）的布局。
画面 11: 在 Typora 中绘制了流程图，显示“Controller”调用“Service”，并标注了“ihrm系统数据库”和“activiti数据库”。
画面 12: 在 PPT 中显示了“1.4 离职流程分析”章节，其中包含“业务流程概述”和流程图，流程图显示了“当事人发起离职申请”→“直属领导审批”→“人事部审批”→“人事负责人审批”→“财务部审批”的顺序。
画面 13: 在 iHRM 系统中，页面显示了“审批”页面，但内容为空。
画面 14: 在 Typora 中绘制了流程图，显示“Controller”调用“Service”，并标注了“ihrm系统数据库”和“activiti数据库”，并添加了文字说明：
1. 构造业务数据 ProcInstance
2. 根据 processKey 查询流程定义
3. 开启流程（activitiAPI调用）
4. 执行第一个用户任务(Task)，用户申请
5. 获取下一个用户任务，获取执行候选人数据，设置到ProcInstance中

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
{
  "applyUnit": "技光",
  "duration": "1",
  "emailTime": "2019-09-02 00:00:00",
  "holidayType": "1",
  "processKey": "process_leave",
  "processId": "1",
  "reason": "xxxxxxxx",
  "startTime": "2019-09-02 00:00:00",
  "userId": "118178950026271668"
}

画面 9:
proc_instance 表结构：
Field          Type          Collation     Null     Key     Default     Extra     Privileges     Comment
process_id     varchar(45)  utf8_general_ci  NO      PRI     NULL     (NULL)     select,insert,update,references     流程实例ID
process_key    varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程定义key
process_type   varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程类型
process_state  varchar(3)   utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程状态
user_id        varchar(3)   utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请人ID
proc_apply_time datetime     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请时间
proc_task_instance_id varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     任务实例ID
proc_end_time   datetime     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程结束时间
proc_data       longtext     utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程数据
department_id   varchar(40)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     部门ID
user_name       varchar(40)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     申请人姓名
proc_instance_id varchar(45)  utf8_general_ci  NO      NULL     NULL     (NULL)     select,insert,update,references     流程实例ID

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12:
标题：1.4 离职流程分析
子标题：业务流程概述
流程图结构：
- 开始 → 当事人发起离职申请 → 直属领导审批 → 人事部审批 → 人事负责人审批 → 财务部审批 → 结束
表格数据：
- 无表格数据，仅包含流程描述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

