# 画面线理解：06-IDEA中制作流程定义png文件的中文乱码问题

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\06-IDEA中制作流程定义png文件的中文乱码问题_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:23, 00:32, 00:36, 00:38, 00:48, 00:52, 00:56, 01:10, 01:46, 02:00, 02:39, 02:54, 03:21
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 11:22:05

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中创建、导出并配置 Activiti 流程引擎的 BPMN 流程图，以及编写测试类来启动流程引擎。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 IntelliJ IDEA 中的项目结构，选中了 holiday.bpmn 文件，右侧是流程图编辑器，流程图包含 StartEvent、两个 UserTask 和 EndEvent。
画面2: 展示 PPT 页面，标题为“5.1.1.3 新建流程(Eclipse 工具)”，内容说明了在 Eclipse 中新建流程的方法。
画面3: 展示 PPT 页面，标题为“IDEA 工具中的操作方式”，内容说明第一步是将 holiday.bpmn 文件改为 holiday.xml，图示显示了修改前的流程图。
画面4: 展示 PPT 页面，标题为“第四步”，内容说明点击 Export To File 图标。
画面5: 展示“Save diagram as image”对话框，路径为“G:\Activiti7开发计划\Activiti7-day02\资料”，文件名为“diagram”，格式为“png”。
画面6: 展示 Windows 桌面，右键点击“我的电脑”，弹出菜单。
画面7: 展示 Windows 桌面，右键点击“我的电脑”，弹出菜单，鼠标悬停在“属性”上。
画面8: 展示“我的电脑”窗口，路径为“D:\idea\Install\IDEA 2017.1.5\bin”，选中了“idea64.exe”文件。
画面9: 展示“idea64.exe”文件的属性窗口，显示了 JVM 参数，其中包含“-Dfile.encoding=UTF-8”。
画面10: 展示 IntelliJ IDEA 中的“holiday.xml”文件内容，包含完整的 BPMN XML 结构。
画面11: 展示 IntelliJ IDEA 中的“ActivitiTest.java”文件，右键菜单显示“Run ActivitiTest”选项，代码中包含创建 ProcessEngine 的语句。
画面12: 展示 IntelliJ IDEA 中的“ActivitiTest.java”文件，代码中包含创建 ProcessEngine 的语句，注释说明了配置文件的加载方式。
画面13: 展示“idea64.exe”文件的属性窗口，显示了 JVM 参数，其中包含“-Dfile.encoding=UTF-8”。
画面14: 展示 IntelliJ IDEA 中的 BPMN 流程图编辑器，流程图包含 StartEvent、两个 UserTask 和 EndEvent，右侧是 BPMN 元素面板。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面10:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:activiti="http://activiti.org/bpmn" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd">
  <process id="holiday" isExecutable="true" name="请假流程" processType="None">
    <startEvent id="1" name="请假流程开始" />
    <userTask id="2" name="填写请假单" activiti:assignee="wang" activiti:exclusive="true" />
    <userTask id="3" name="领导审批" activiti:assignee="zhang" activiti:exclusive="true" />
    <sequenceFlow id="1" sourceRef="1" targetRef="2" />
    <sequenceFlow id="2" sourceRef="2" targetRef="3" />
    <sequenceFlow id="3" sourceRef="3" targetRef="4" />
    <endEvent id="4" name="请假流程结束" />
  </process>
</definitions>
```

画面10 (BPMNPlane 部分):
```xml
<bpmd:BPMDiagram documentation="background=#FFFFFF;count=1;horizontalCount=1;orientation=0;width=842.4;" xmlns:bpmd="http://activiti.org/bpmn">
  <bpmd:BPMDiagram>
    <bpmd:BPMDiagram>
      <bpmd:BPMDiagram>
        <bpmd:BPMDiagram>
          <bpmd:BPMDiagram>
            <bpmd:BPMDiagram>
              <bpmd:BPMDiagram>
                <bpmd:BPMDiagram>
                  <bpmd:BPMDiagram>
                    <bpmd:BPMDiagram>
                      <bpmd:BPMDiagram>
                        <bpmd:BPMDiagram>
                          <bpmd:BPMDiagram>
                            <bpmd:BPMDiagram>
                              <bpmd:BPMDiagram>
                                <bpmd:BPMDiagram>
                                  <bpmd:BPMDiagram>
                                    <bpmd:BPMDiagram>
                                      <bpmd:BPMDiagram>
                                        <bpmd:BPMDiagram>
                                          <bpmd:BPMDiagram>
                                            <bpmd:BPMDiagram>
                                              <bpmd:BPMDiagram>
                                                <bpmd:BPMDiagram>
                                                  <bpmd:BPMDiagram>
                                                    <bpmd:BPMDiagram>
                                                      <bpmd:BPMDiagram>
                                                        <bpmd:BPMDiagram>
                                                          <bpmd:BPMDiagram>
                                                            <bpmd:BPMDiagram>
                                                              <bpmd:BPMDiagram>
                                                                <bpmd:BPMDiagram>
                                                                  <bpmd:BPMDiagram>
                                                                    <bpmd:BPMDiagram>
                                                                      <bpmd:BPMDiagram>
                                                                        <bpmd:BPMDiagram>
                                                                          <bpmd:BPMDiagram>
                                                                            <bpmd:BPMDiagram>
                                                                              <bpmd:BPMDiagram>
                                                                                <bpmd:BPMDiagram>
                                                                                  <bpmd:BPMDiagram>
                                                                                    <bpmd:BPMDiagram>
                                                                                      <bpmd:BPMDiagram>
                                                                                        <bpmd:BPMDiagram>
                                                                                          <bpmd:BPMDiagram>
                                                                                            <bpmd:BPMDiagram>
                                                                                              <bpmd:BPMDiagram>
                                                                                                <bpmd:BPMDiagram>
                                                                                                  <bpmd:BPMDiagram>
                                                                                                    <bpmd:BPMDiagram>
                                                                                                      <bpmd:BPMDiagram>
                                                                                                        <bpmd:BPMDiagram>
                                                                                                          <bpmd:BPMDiagram>
                                                                                                            <bpmd:BPMDiagram>
                                                                                                              <bpmd:BPMDiagram>
                                                                                                                <bpmd:BPMDiagram>
                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                <bpmd:BPMDiagram>
                                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                                <bpmd:BPMDiagram>
                                                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                                                <bpmd:BPMDiagram>
                                                                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                                                                <bpmd:BPMDiagram>
                                                                                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                                                                                <bpmd:BPMDiagram>
                                                                                                                                                                                                  <bpmd:BPMDiagram>
                                                                                                                                                                                                    <bpmd:BPMDiagram>
                                                                                                                                                                                                      <bpmd:BPMDiagram>
                                                                                                                                                                                                        <bpmd:BPMDiagram>
                                                                                                                                                                                                          <bpmd:BPMDiagram>
                                                                                                                                                                                                            <bpmd:BPMDiagram>
                                                                                                                                                                                                              <bpmd:BPMDiagram>
                                                                                                                                                                                                                <bpmd:
