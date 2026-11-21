---
title: "用 IDEA 的 Activiti 设计器画出第一张流程定义图"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段二 传统行业解决方案SaaS-HRM项目]
tags: [Java, 项目实战]
---

# 用 IDEA 的 Activiti 设计器画出第一张流程定义图

流程引擎要转起来，手里得先有一张流程图：请假从哪个节点开始、中间经过谁审批、到哪里结束，这些信息要先落成一份流程定义文件，后面的部署与启动才有东西可用。装好 Activiti 设计器插件的 IDEA 就是干这件事的画板，这一步走完，产出一个 `holiday.bpmn`。

## 先给结论

- 前提是装好 Activiti 设计器插件，画板 Palette 提供 Connection、Event、Task、Gateway 等元素，往画布拖节点就能搭流程。
- 在 `resources` 下建 `diagram` 目录，右键新建 BpmnFile 起名 `holiday`，默认扩展名就是 `.bpmn`。
- `.bpmn` 本质是 XML 文件，画布上的图形是插件解析 XML 后渲染出来的视图。
- 每个流程定义必须有唯一的 id，部署后按 key 启动实例靠的就是它；name 只是给人看的显示名。
- 任务节点要指定 assignee（任务负责人），否则流程走到这一步没有负责人，任务无人认领。

## 一、画图在整条链路里的位置

入门体验一共五步，画流程定义只是第一环：

```mermaid
flowchart LR
    A["绘制流程定义 bpmn"] --> B["部署流程定义进库"]
    B --> C["启动流程实例"]
    C --> D["任务负责人查询任务"]
    D --> E["处理任务直到流程结束"]
```

图上从左到右是一条完整的业务线：图先画出来，部署进数据库，然后才能启动。启动相当于发起一张请假单，张三填单，李四以部门经理身份审批，王五以总经理身份审批，每个人都要先查询自己的待办任务再处理。后面课程里启动实例用 `startProcessInstanceByKey`、完成任务用 `taskService.complete`，这两个动作能找到目标，靠的就是画图时定下的 id 和每个节点的 assignee。

## 二、画板与新建文件

**第一，认识 Palette。** 设计器画板上的元素按类分组：Connection 是连线，Event 是事件（开始、结束都在这一组），Task 是任务，Gateway 是网关，另有 Container、边界事件、中间事件。请假这种简单流程只会用到 Event、Task 和连线。

**第二，新建文件。** 在 `resources` 下建一个 `diagram` 目录，用来集中放流程文件，右键目录选 New 里的 BpmnFile，起名 `holiday`，扩展名默认就是 `.bpmn`，确认后直接进入流程设计页面。Eclipse 里的入口略有不同，产物一样，都是一份 bpmn 文件。

## 三、把请假流程画出来

搭建过程没有技巧，就是拖节点、改名字、连线：

1. 从 Event 组拖一个 StartEvent 到画布，name 改成「开始」；不想看到英文就直接写汉字，工具不做限制。
2. 从 Task 组拖三个 UserTask，依次改名为「填写请假申请单」「部门经理审批」「总经理审批」。
3. 从 Event 组拖一个 EndEvent，name 改成「结束」。
4. 用 Connection 把五个节点从头到尾串起来。

有两个细节值得单独说。**一是对齐。** IDEA 的设计器没有对齐辅助线，节点摆得正不正基本靠眼睛；Eclipse 版在拖动时会提示是否对齐，这点确实更好用。**二是属性。** 选中画布空白处，属性面板里给流程定义设 id 与 name，课程里设的是 `Id: holiday`、`Name: 请假流程`，`Is Executable` 保持 true；再逐个选中任务节点，把 assignee 分别设为 `zhangsan`、`lisi`、`wangwu`，对应填单人、部门经理、总经理三个人。

流程结构画完是这个样子：

```mermaid
flowchart LR
    S["开始"] --> T1["填写请假申请单 zhangsan"]
    T1 --> T2["部门经理审批 lisi"]
    T2 --> T3["总经理审批 wangwu"]
    T3 --> E["结束"]
```

图上三个任务节点各挂一个负责人，节点名与 assignee 一一对应，这张对应关系就是后面任务查询的过滤依据。

## 四、保存之后得到的是什么

画完保存，磁盘上多出的是 `holiday.bpmn`。用文本方式看它的骨架，与画布一一对应：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL"
             xmlns:activiti="http://activiti.org/bpmn"
             targetNamespace="http://www.example.org/bpmn">
  <process id="holiday" name="请假流程" isExecutable="true">
    <startEvent id="startevent1" name="开始"/>
    <userTask id="usertask1" name="填写请假申请单" activiti:assignee="zhangsan"/>
    <userTask id="usertask2" name="部门经理审批" activiti:assignee="lisi"/>
    <userTask id="usertask3" name="总经理审批" activiti:assignee="wangwu"/>
    <endEvent id="endevent1" name="结束"/>
    <sequenceFlow id="flow1" sourceRef="startevent1" targetRef="usertask1"/>
    <sequenceFlow id="flow2" sourceRef="usertask1" targetRef="usertask2"/>
    <sequenceFlow id="flow3" sourceRef="usertask2" targetRef="usertask3"/>
    <sequenceFlow id="flow4" sourceRef="usertask3" targetRef="endevent1"/>
  </process>
</definitions>
```

三个属性要读明白。`process` 的 `id` 是流程定义的标识，等价于后面部署与启动时用的 key，`startProcessInstanceByKey("holiday")` 里的字符串就是它；`name` 只用于展示。`activiti:assignee` 是 Activiti 对 BPMN 标准的扩展属性，把任务钉到具体人身上，任务查询按它过滤。`isExecutable` 为 true 表示这份定义可被执行。

画布之外，文件里还有一节 BPMNDiagram 信息，记录每个图形的坐标和尺寸，插件就是靠它把 XML 还原成图。这也解释了为什么换一台没装插件的机器，同一个文件打开只剩一堆 XML。

## 常见误区

- **把 bpmn 当图片文件。** 双击用看图软件打不开就以为文件坏了，实际它是 XML，图形只是插件渲染的结果。
- **id 随手起或多流程共用。** id 是部署后的 key，两个不相关的流程定义共用一个 id，启动时按 key 会拿到高版本那份，行为和预期完全对不上。
- **任务节点漏设 assignee。** 画布上毫无异常，流程启动后任务查询永远查不到数据，回头补属性即可。
- **只摆节点不连线。** 没有 `sequenceFlow` 的节点之间没有流向，部署不报错，运行到该处直接停住。

## 面试可能被问到的问题

1. 面试官追问：「bpmn 文件是什么，Activiti 为什么选它？」
   答：bpmn 是业务流程模型与标记法的标准文件格式，本质是 XML。它是行业通用的流程建模标准，任何支持该标准的引擎和设计器都能读写，画好的流程图不绑定在某个产品上。

2. 面试官追问：「process 的 id 和 name 分别起什么作用？」
   答：id 是流程定义的 key，部署进库后启动流程实例要按它找定义，必须唯一且稳定；name 是显示名，给人看，不参与定位。

3. 面试官追问：「assignee 是什么，和候选人有什么区别？」
   答：assignee 是任务的唯一负责人，任务直接落到这个人名下；候选人是把任务放进一组人的候选池，由其中一人拾取后变成负责人。简单场景用 assignee，抢办场景用候选人组。

4. 面试官追问：「IDEA 和 Eclipse 里画流程定义差别大吗？」
   答：产物一样，都是 bpmn 文件。差别在工具体验：Eclipse 版设计器拖动时有对齐提示，保存即生成 png；IDEA 版没有自动对齐，导出 png 也要绕一步，所以常见做法是画图用 Eclipse，写代码用 IDEA。

5. 面试官追问：「画布上看到的图存在哪里？」
   答：存在 bpmn 文件末尾的 BPMNDiagram 一节，记录每个节点与连线的坐标和尺寸。设计器插件读取这节信息把 XML 渲染成图形，没有插件时看到的就是纯 XML。

## 配套资料

- 课程工程：`materials/code/02/Activiti7-day02-工作流使用/代码/代码/`
  （含 `ActivitiDeployment.java`、`ActivitiTest.java`、`activiti.cfg.xml` 等，文中包名已统一改为 `com.example`）
- 资料包中未包含 bpmn 源文件，文中的 bpmn 片段为按本课实录整理的示例，节点与属性设置和课程一致。
