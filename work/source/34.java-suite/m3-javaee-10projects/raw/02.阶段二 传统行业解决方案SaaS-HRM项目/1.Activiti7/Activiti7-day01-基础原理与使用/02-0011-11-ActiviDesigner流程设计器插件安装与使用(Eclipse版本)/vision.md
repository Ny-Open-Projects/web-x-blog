# 画面线理解：11-ActiviDesigner流程设计器插件安装与使用(Eclipse版本)

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\11-ActiviDesigner流程设计器插件安装与使用(Eclipse版本)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:07, 00:34, 01:28, 02:02, 02:23, 02:58, 03:43, 04:39, 08:21, 09:00, 10:26, 12:33, 13:20, 13:42
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:09:04

1) 这一组画面整体在讲如何在 Eclipse 中安装 Activiti Designer 插件并创建和编辑 BPMN 2.0 流程图。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程 PPT 页面，标题为“3.3.2.1 Eclipse 工具下插件安装方式 1”，内容说明插件安装参考“activiti 开发环境配置.docx”中的“Eclipse 插件安装”章节。
画面2：在 Eclipse 中点击“Install New Software...”选项，弹出“Install”界面，提示用户点击“Add...”按钮。
画面3：在“Available Software”界面中，工作区设置为“http://www.activiti.org/designer/update/”，并勾选“Show only the latest versions of available software”和“Hide items that are already installed”选项。
画面4：桌面显示“联合出品”页面，包含“传智播客”和“黑马程序员”两个机构的标志。
画面5：显示 Eclipse 安装目录，包含“configuration”、“dropins”、“features”、“plugins”、“p2”、“.eclipseproduct”、“.eclipse.ini”和“eclipse.exe”等文件夹和文件。
画面6：在“features”文件夹中显示两个插件文件：“org.activiti.designer.feature_5.18.0.201508180939.jar”和“org.eclipse.graphiti.feature_0.11.4.v2015011492.jar”。
画面7：在 Eclipse 中点击“File”菜单，弹出下拉菜单，包含“New”、“Open File...”、“Import...”等选项。
画面8：在 Eclipse 中点击“File”菜单，弹出下拉菜单，包含“New”、“Open in New Window”、“Open Type Hierarchy”、“Show in Local Terminal”、“Copy”、“Paste”、“Delete”、“Remove from Content”、“Build Path”、“Source”、“Refactor”、“Import...”、“Export...”、“Assign Working Sets...”、“Coverage As”、“Run As”、“Debug As”、“Profile As”、“Validate”、“Restore from Local History...”、“Team”、“Compare With”和“Properties”等选项。
画面9：在 Eclipse 中打开“holiday.bpmn”文件，显示 BPMN 2.0 流程图，包含“StartEvent”、“UserTask”和“EndEvent”等元素。
画面10：在 Eclipse 中显示 BPMN 2.0 流程图，包含“StartEvent”、“UserTask”和“EndEvent”等元素。
画面11：在 Eclipse 中打开“Preferences”对话框，显示“Save Actions”设置，包括“Create process definition image other saving the diagram”、“Overlay process information on the process image”、“Position the overlay in corner”、“Include the process key (BPMN ID)”、“Include the diagram’s filename”、“Include the date/time of saving the diagram”、“Include the revision from the version control system if available”等选项。
画面12：桌面显示“联合出品”页面，包含“传智播客”和“黑马程序员”两个机构的标志。
画面13：在 Eclipse 中打开“holiday.bpmn”文件，显示 BPMN 2.0 流程图的 XML 代码。
画面14：在 Eclipse 中显示“holiday.bpmn”文件的空白编辑界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面13：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.omg.org/spec/BPMN/2.0/MODEL" xmlns:activiti="http://activiti.org/bpmn" xmlns:bpmn="http://www.omg.org/spec/BPMN/2.0" xmlns:flowable="http://flowable.org/bpmn">
  <bpmn:process id="MyProcess" name="My process" isExecutable="true">
    <bpmn:startEvent id="startEvent1" name="Start" activiti:formKey="startFormKey">
    </bpmn:startEvent>
    <bpmn:userTask id="userTask1" name="填写请假单" activiti:formKey="userTaskFormKey">
    </bpmn:userTask>
    <bpmn:userTask id="userTask2" name="领导审批" activiti:formKey="userTaskFormKey">
    </bpmn:userTask>
    <bpmn:endEvent id="endEvent1" name="End" activiti:formKey="endFormKey">
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="flow1" sourceRef="startEvent1" targetRef="userTask1">
    </bpmn:sequenceFlow>
    <bpmn:sequenceFlow id="flow2" sourceRef="userTask1" targetRef="userTask2">
    </bpmn:sequenceFlow>
    <bpmn:sequenceFlow id="flow3" sourceRef="userTask2" targetRef="endEvent1">
    </bpmn:sequenceFlow>
  </bpmn:process>
</bpmn:definitions>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“3.3.2.1 Eclipse 工具下插件安装方式 1”，内容说明插件安装参考“activiti 开发环境配置.docx”中的“Eclipse 插件安装”章节。
画面9：BPMN 2.0 流程图包含“StartEvent”、“UserTask”和“EndEvent”等元素，其中“StartEvent”指向“UserTask”，“UserTask”指向“EndEvent”。
画面10：BPMN 2.0 流程图包含“StartEvent”、“UserTask”和“EndEvent”等元素，其中“StartEvent”指向“UserTask”，“UserTask”指向“EndEvent”。
画面11：在“Preferences”对话框中，显示“Save Actions”设置，包括“Create process definition image other saving the diagram”、“Overlay process information on the process image”、“Position the overlay in corner”、“Include the process key (BPMN ID)”、“Include the diagram’s filename”、“Include the date/time of saving the diagram”、“Include the revision from the version control system if available”等选项。

5) 不要评价画面美观，不要输出与课程无关的内容。
