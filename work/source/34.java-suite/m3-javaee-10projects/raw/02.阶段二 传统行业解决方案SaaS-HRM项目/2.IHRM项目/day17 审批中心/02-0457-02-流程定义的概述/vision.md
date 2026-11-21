# 画面线理解：02-流程定义的概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day17 审批中心
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day17 审批中心\02-流程定义的概述_【海量资源尽在 ubkz.com】.mp4
- 抽帧：11 帧 @ 00:28, 00:32, 00:42, 00:52, 00:57, 01:00, 01:02, 01:03, 01:06, 01:27, 01:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 18:01:01

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
