# 画面线理解：14-Activiti7与SpringBoot整合-任务拾取&执行

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day07-审批中心模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day07-审批中心模块开发\14-Activiti7与SpringBoot整合-任务拾取&执行_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 00:38, 00:57, 01:27, 01:56, 02:43, 02:58, 03:16, 03:32, 04:14, 04:34, 04:44, 05:02, 06:08
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 12:43:02

1) 这一组画面整体在讲如何在 Activiti 工作流引擎中通过 Java 代码启动流程实例、查询并处理任务，并演示了任务的认领（claim）和完成（complete）操作。

2) 按时间顺序列出每张画面的要点：
画面1: 展示了启动流程实例的代码，使用 ProcessRuntime.start(ProcessPayloadBuilder).start()，并打印流程实例ID。
画面2: 代码与画面1相同，无新增要点。
画面3: 展示了 Activiti 流程定义的 BPMN XML 文件内容，包含两个用户任务（"first" 和 "second"）及一个排他网关。
画面4: 在 Java 代码中，通过 taskRuntime.claim(TaskPayloadBuilder.claim().withTaskId(task.getId()).build()) 对任务进行认领。
画面5: 代码中添加了对任务的认领操作，并显示了 TaskPayloadBuilder 的方法提示。
画面6: 展示了 PPT 内容，其中包含任务完成的代码示例：taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build()。
画面7: 代码中添加了任务完成的代码，并显示了 TaskPayloadBuilder 的方法提示。
画面8: 代码中添加了任务完成的代码，并显示了 TaskPayloadBuilder 的方法提示。
画面9: 代码中完整展示了任务的认领和完成操作，包括打印任务信息。
画面10: 代码中对任务的认领和完成操作进行了注释，并显示了 TaskPayloadBuilder 的方法提示。
画面11: 在代码中选中了 for 循环语句，并弹出了“Refactor”菜单。
画面12: 展示了 PPT 内容，其中包含任务完成的代码示例：taskRuntime.complete(TaskPayloadBuilder.complete().withTaskId(task.getId()).build()。
画面13: 展示了 PPT 内容，并在底部显示了“使用 TaskRuntime 接口的 tasks() 方法实现任务的查询。”
画面14: 展示了 PPT 内容，并在底部显示了“使用 TaskRuntime 接口的 tasks() 方法实现任务的查询。”

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3 XML 配置：
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/2.0.1/schema/xsd" xmlns:activiti="http://activiti.org/bpmn" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <process id="myProcess" name="myProcess" isExecutable="true" processType="None">
    <startEvent id="1" name="StartEvent" />
    <userTask id="2" name="first" activiti:exclusive="true" activiti:candidateGroups="activityTeam" />
    <userTask id="3" name="second" activiti:exclusive="true" activiti:candidateGroups="activityTeam" />
    <sequenceFlow id="1" sourceRef="1" targetRef="2" />
    <sequenceFlow id="2" sourceRef="2" targetRef="3" />
    <endEvent id="4" name="EndEvent" />
    <process>
      <bpmn:diagram documentation="background=FFFFFF;count=;horizontalCount=;orientation=;width=842;height=595">
        <bpmndi:BPMNDiagram id="BPMNDiagram_1">
          <bpmndi:BPMNPlane bpmnElement="1" id="BPMNPlane_1" background="FFFFFF" horizontalCount="1" orientation="horizontal" width="842" height="595">
            <bpmndi:BPMNShape bpmnElement="1" id="Shape_1" height="32.0" width="32.0" x="0.0" y="0.0">
              <bpmndi:BPMNLabel>
                <bpmndi:BPMNLabel>
                  <bpmndi:BPMNLabel>
                    <bpmndi:BPMNLabel>
                      <bpmndi:BPMNLabel>
                        <bpmndi:BPMNLabel>
                          <bpmndi:BPMNLabel>
                            <bpmndi:BPMNLabel>
                              <bpmndi:BPMNLabel>
                                <bpmndi:BPMNLabel>
                                  <bpmndi:BPMNLabel>
                                    <bpmndi:BPMNLabel>
                                      <bpmndi:BPMNLabel>
                                        <bpmndi:BPMNLabel>
                                          <bpmndi:BPMNLabel>
                                            <bpmndi:BPMNLabel>
                                              <bpmndi:BPMNLabel>
                                                <bpmndi:BPMNLabel>
                                                  <bpmndi:BPMNLabel>
                                                    <bpmndi:BPMNLabel>
                                                      <bpmndi:BPMNLabel>
                                                        <bpmndi:BPMNLabel>
                                                          <bpmndi:BPMNLabel>
                                                            <bpmndi:BPMNLabel>
                                                              <bpmndi:BPMNLabel>
                                                                <bpmndi:BPMNLabel>
                                                                  <bpmndi:BPMNLabel>
                                                                    <bpmndi:BPMNLabel>
                                                                      <bpmndi:BPMNLabel>
                                                                        <bpmndi:BPMNLabel>
                                                                          <bpmndi:BPMNLabel>
                                                                            <bpmndi:BPMNLabel>
                                                                              <bpmndi:BPMNLabel>
                                                                                <bpmndi:BPMNLabel>
                                                                                  <bpmndi:BPMNLabel>
                                                                                    <bpmndi:BPMNLabel>
                                                                                      <bpmndi:BPMNLabel>
                                                                                        <bpmndi:BPMNLabel>
                                                                                          <bpmndi:BPMNLabel>
                                                                                            <bpmndi:BPMNLabel>
                                                                                              <bpmndi:BPMNLabel>
                                                                                                <bpmndi:BPMNLabel>
                                                                                                  <bpmndi:BPMNLabel>
                                                                                                    <bpmndi:BPMNLabel>
                                                                                                      <bpmndi:BPMNLabel>
                                                                                                        <bpmndi:BPMNLabel>
                                                                                                          <bpmndi:BPMNLabel>
                                                                                                            <bpmndi:BPMNLabel>
                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                                                                                  <bpmndi:BPMNLabel>
                                                                                                                                                                                                    <bpmndi:BPMNLabel>
                                                                                                                                                                                                      <bpmndi:BPMNLabel>
                                                                                                                                                                                                        <bpmndi:BPMNLabel>
                                                                                                                                                                                                          <bpmndi:BPMNLabel>
                                                                                                                                                                                                            <bpmndi:BPMNLabel>
                                                                                                                                                                                                              <bpmndi:BPMNLabel>
                                                                                                                                                                                                                <bpmndi:BPMNLabel>
                                                                                                                                                                                                                  <bpmndi:BPMNLabel>
