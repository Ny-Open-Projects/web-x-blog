# 02-流程定义的概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\02-流程定义的概述_【海量资源尽在 ubkz.com】.mp4
- 时长 3分0秒（音频 180s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了,我们一个一个来看首先呢,咱们要看第一块那在我们讲义上呢,叫做流程定义的一个管理那首先需要跟各位介绍一下什么叫做流程定义那是这样,在activity当中呢如果我们部署一个流程上去之后其实也就意味着我们定义了一个流程那这些流程全部在什么位置进行展示呢咱们可以一起打开activity数据库我们来看一下
[00:30] 那这个是activity的数据库那打开之后找到对应的表那我们都知道部署一个之后呢部署一个流程之后它会体现在这个deployment这个表当中好了那这个是我们之前部署的这边有一个名字叫做传制播客各位应该还能看到那除了这个表之外呢相应的还有一些表比如说上边有一个叫做battery那这个battery里面存放的全部都是你当前这个流程它的完整的X秒
[01:02] 这个就是我们的XML文件能看到吗那除了这个之外还有一个你上传一个流程并且部署进去之后你就定义了一个流程定义对象其实咱们可以把它理解成一个对象那这个对象存放到什么地方也是在表当中好了我们一起来找一下它叫做PROdefinition就是它PROC Definition这个是一个流程定义的这么一个对象那其实就是我们
[01:33] 自己制作的流程相关的一些配置信息在里面那有了这个流程定义之后才会有后续的发起流程挂起流程激活流程等等等等这一系列的处理所以呢这个流程定义呢可以理解为Active里面比较重要的这么一个环节好了呢这个咱们看过了之后那同时我们这边讲以上也说过了
[01:58] 在这间课程呢我们已经把一个BPMN文件上传到服务器当中那上传过去之后就会把相应的数据保存到一个一个表里同时我们已经完成了一个流程定义那说的官方一点呢它叫做Process Definition那接着呢我们就可以通过Activity为我们提供的一些API去完成这个流程定义相关的查询
[02:28] 它的一些比如说挂起激活等等的业务处理那在我们这边呢主要来看两个方面第一个方面就是我们查询所有已经部署或者已经定义的这些流程这是我们要做的第一件事那接下来第二件事就是对已经有的这个流程完成一个挂起或者完成一个激活操作那这个就是我们接下来对流程定义
[02:57] 要完成的两件事

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过数据库查询和编辑 BPMN 流程定义（Process Definition），并展示其 XML 内容。

2) 按时间顺序列出每张画面的要点：
画面1: 打开数据库表“act_re_procdef”，查看流程定义列表，当前选中“SpringBpmnDeployment”。
画面2: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面3: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面4: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面5: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面6: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面7: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面8: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面9: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面10: 在左侧导航树中选中“act_re_procdef”表，切换到“act_re_procdef”表，选中“process_leave”流程定义。
画面11: 切换到 PPT 页面，标题为“1 流程定义管理”，子标题“1.1 流程定义列表查询”，并展示数据库查询结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6-8 中的 XML 内容：
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:activiti="http://activiti.org/bpmn" xmlns:flowable="http://flowable.org/bpmn">
  <process id="process_leave" name="请假流程" isExecutable="true">
    <startEvent id="startEvent1" name="开始" />
    <userTask id="userTask1" name="提交请假申请" activiti:assignee="${user}" />
    <userTask id="userTask2" name="审批请假申请" activiti:assignee="${user}" />
    <endEvent id="endEvent1" name="结束" />
    <sequenceFlow id="flow1" sourceRef="startEvent1" targetRef="userTask1" />
    <sequenceFlow id="flow2" sourceRef="userTask1" targetRef="userTask2" />
    <sequenceFlow id="flow3" sourceRef="userTask2" targetRef="endEvent1" />
  </process>
</definitions>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面11 中的 PPT 内容：
标题：1 流程定义管理
子标题：1.1 流程定义列表查询
表格数据：
| ID | NAME | KEY | VERSION | DEPLOYMENT_ID_ | RESOURCE_NAME |
|----|------|-----|---------|----------------|---------------|
| 6602012-11e4-11e9-0000000000000000 | process_leave | process_leave | 1 | 6602012-11e4-11e9-0000000000000000 | process_leave.bpmn |

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

