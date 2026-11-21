# 画面线理解：09-Activiti7整合开发的步骤

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\09-Activiti7整合开发的步骤_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:04, 00:15, 00:28, 00:59, 03:23, 03:30, 03:52, 04:21, 04:29, 04:45, 05:41, 06:21, 06:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:07:26

1) 这一组画面整体在讲如何使用 Activiti 工作流引擎，包括 BPMN 标准、流程定义、部署、启动实例、查询任务、办理任务和流程结束等核心概念。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 PPT 页面，标题为“2) 流程定义”，内容说明使用 activiti 流程建模工具（activity-designer）定义业务流程，bpmn 文件是业务流程定义文件，通过 xml 定义业务流程。
画面2: 展示 PPT 页面，标题为“2.2 Activiti 如何使用”，内容为“1) 部署 activiti”，下方显示一段 XML 代码片段：
<bpmm:BPMMEdge bpmnElement="flow1" id="BPMMEdge_flow1">
  <bpmm:waypoint x="465.0" y="177.0"/>
  <bpmm:waypoint x="512.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow2" id="BPMMEdge_flow2">
  <bpmm:waypoint x="335.0" y="177.0"/>
  <bpmm:waypoint x="360.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow3" id="BPMMEdge_flow3">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow4" id="BPMMEdge_flow4">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow5" id="BPMMEdge_flow5">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow6" id="BPMMEdge_flow6">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow7" id="BPMMEdge_flow7">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow8" id="BPMMEdge_flow8">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow9" id="BPMMEdge_flow9">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow10" id="BPMMEdge_flow10">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow11" id="BPMMEdge_flow11">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow12" id="BPMMEdge_flow12">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow13" id="BPMMEdge_flow13">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow14" id="BPMMEdge_flow14">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow15" id="BPMMEdge_flow15">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow16" id="BPMMEdge_flow16">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow17" id="BPMMEdge_flow17">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow18" id="BPMMEdge_flow18">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow19" id="BPMMEdge_flow19">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow20" id="BPMMEdge_flow20">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow21" id="BPMMEdge_flow21">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow22" id="BPMMEdge_flow22">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow23" id="BPMMEdge_flow23">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow24" id="BPMMEdge_flow24">
  <bpmm:waypoint x="663.0" y="177.0"/>
  <bpmm:waypoint x="663.0" y="177.0"/>
</bpmm:BPMMEdge>
<bpmm:BPMMEdge bpmnElement="flow25" id="BPMMEdge_flow25">
  <bpmm:waypoint x="6
