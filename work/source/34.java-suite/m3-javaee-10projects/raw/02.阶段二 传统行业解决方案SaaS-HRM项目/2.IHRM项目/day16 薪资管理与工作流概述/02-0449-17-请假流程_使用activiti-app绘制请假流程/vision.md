# 画面线理解：17-请假流程：使用activiti-app绘制请假流程

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\17-请假流程：使用activiti-app绘制请假流程_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:58, 01:15, 01:50, 03:23, 05:34, 07:37, 08:19, 08:33, 09:08, 11:26, 13:02, 13:17, 13:37, 14:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:55:29

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Activiti 工作流引擎的图形化编辑器中创建和配置一个请假审批流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 在 Activiti 编辑器主界面，拖拽一个“Identity management”组件到画布上。
画面 2: 选中并调整“Identity management”组件的大小和位置。
画面 3: 弹出“Create a new business process model”对话框，准备创建新流程模型。
画面 4: 展示课程 PPT 页面，标题为“4.2 流程制作工具”，内容介绍制作流程的几种方式，包括“手写xml文件”、“基于IDEA中的activiti插件”、“通过java编辑或生成xml文件”、“基于Activiti官方提供的activiti-app工具包”。
画面 5: 在 Activiti 编辑器中，已绘制出请假流程的初始图形，包含“提交申请”、“HR初审”、“复审”三个任务节点和一个“领导审批”分支。
画面 6: 选中“复审”任务节点，准备进行属性配置。
画面 7: 弹出“Assignment”对话框，用于配置任务的分配方式，当前选中“Identity store”选项卡，候选组字段显示为“${PROCESS_LEAVE_APPLY_USERS}”。
画面 8: 在“Assignment”对话框中，切换到“Fixed values”选项卡，准备设置固定值。
画面 9: 选中“复审”任务节点，弹出其属性面板，正在配置“Multi-instance”（多实例）相关属性，其中“Cardinality (Multi-instance)”字段被选中。
画面 10: 弹出“Sequence flow condition”对话框，用于设置流程分支的条件表达式。
画面 11: 弹出“Save model”对话框，用于保存当前流程模型，其中“Name”字段为“请假”，“Key”字段为“qj”，“Description”字段为“测试请假流程”。
画面 12: 保存后，流程图界面显示“V1 请假”，并显示“创建者”和“最后更新时间”信息。
画面 13: 显示桌面，桌面上有“黑马程序员”和“博学谷”的标志。
画面 14: 在 Notepad++ 编辑器中打开并显示了“bpmn20.xml”文件的内容，该文件是流程图的 XML 定义。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4: 无代码或配置。
画面 5: 无代码或配置。
画面 6: 无代码或配置。
画面 7: 无代码或配置。
画面 8: 无代码或配置。
画面 9: 无代码或配置。
画面 10: 无代码或配置。
画面 11: 无代码或配置。
画面 12: 无代码或配置。
画面 13: 无代码或配置。
画面 14: 以下为 XML 内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:camunda="http://camunda.org/schema/1.0/bpmn" id="Definitions_1" targetNamespace="http://www.activiti.org/bpmn20" exporter="Activiti" exporterVersion="7.1.0">
  <bpmn:process id="Process_1" isExecutable="true" name="请假">
    <bpmn:startEvent id="StartEvent_1" name="开始" />
    <bpmn:sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="Task_1" />
    <bpmn:userTask id="Task_1" name="提交申请" />
    <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="Task_2" />
    <bpmn:userTask id="Task_2" name="HR初审" />
    <bpmn:sequenceFlow id="Flow_3" sourceRef="Task_2" targetRef="Task_3" />
    <bpmn:userTask id="Task_3" name="复审" />
    <bpmn:sequenceFlow id="Flow_4" sourceRef="Task_3" targetRef="Gateway_1" />
    <bpmn:exclusiveGateway id="Gateway_1" name="决策点" />
    <bpmn:sequenceFlow id="Flow_5" sourceRef="Gateway_1" targetRef="Task_4" />
    <bpmn:userTask id="Task_4" name="领导审批" />
    <bpmn:sequenceFlow id="Flow_6" sourceRef="Task_4" targetRef="EndEvent_1" />
    <bpmn:endEvent id="EndEvent_1" name="结束" />
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">
      <bpmndi:BPMNShape id="StartEvent_1_di" bpmnElement="StartEvent_1">
        <di:Bounds height="40.0" width="40.0" x="100.0" y="100.0" />
        <di:Bounds height="40.0" width="40.0" x="100.0" y="100.0" />
        <di:Bounds height="40.0" width="40.0" x="100.0" y="100.0" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_1_di" bpmnElement="Task_1">
        <di:Bounds height="80.0" width="100.0" x="100.0" y="-1.54322144732192E-15" />
        <di:Bounds height="80.0" width="100.0" x="100.0" y="-1.54322144732192E-15" />
        <di:Bounds height="80.0" width="100.0" x="100.0" y="-1.54322144732192E-15" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_2_di" bpmnElement="Task_2">
        <di:Bounds height="28.0" width="28.0" x="83.73590275949999" y="164.0" />
        <di:Bounds height="28.0" width="28.0" x="83.73590275949999" y="164.0" />
        <di:Bounds height="28.0" width="28.0" x="83.73590275949999" y="164.0" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_3_di" bpmnElement="Task_3">
        <di:Bounds height="28.0" width="28.0" x="178.21450214502145" y="164.0" />
        <di:Bounds height="28.0" width="28.0" x="178.21450214502145" y="164.0" />
        <di:Bounds height="28.0" width="28.0" x="178.21450214502145" y="164.0" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Gateway_1_di" bpmnElement="Gateway_1">
        <di:Bounds height="40.0" width="40.0" x="250.0" y="100.0" />
        <di:Bounds height="40.0"
