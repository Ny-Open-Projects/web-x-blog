# 05-IDEA中制作Activiti流程定义的png文件

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\05-IDEA中制作Activiti流程定义的png文件_【海量资源尽在 ubkz.com】.mp4
- 时长 8分39秒（音频 519s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们接着来把流程定义这一块结合我们第六章的流程定义给各位把这个问题一次性给它讲完了要注意的是我们这一次在实现流程定义的时候将来我们这个activity designer它给我们生成的它给我们在这边真正生成的是一个这样的图对吧那这个图其实它的扩展名是一个BPMN的文件对吧好
[00:28] 我们为了能够先把这个图片先给它存好那我们这一次打算直接进到我们的这个资料中就把这个图给各位先拷进来先给你拷到这来相当于做一个备份因为我们要去做后续的操作了后续的操作到底做些什么主要是我们的这个holody.bpmn它在这里表现的是一个这样的图
[00:56] 但其实它真正的本质呢并不是一个图比如说我直接放到这来完了我们在这里头直接打开你可以发现它不是一个图你打不开的然后我们直接用打开方式比如说用这个ID plus直接打开这个时候各位就可以看到它其实真正的本质是一个XML文件对吧那如果我们呢希望将来
[01:24] 把这个图也一下给它存起来这个地方我们就要想办法要不然的话将来它存储的时候真正存的文件并不是一个图片但是我们很多时候很多时候我们希望看到的是一个这样的图片对吧有些同学就想这不是个图吗对吧怎么会是XML文件你要注意这个地方是因为我们的这个idea工具
[01:50] 装了我们的这个activitydesigner这个插件所以说我们这个时候真正看到的这个是一个图其实是因为这个插件给我们把这个XML文件做了一个解析最后给它形成了一个这样的图展示出来让我们看的所以在我们如果不用activity这个工具的情况下你比如说你就是一个这东西对吧你考到任何一个地方它其实都不是一个图那如果你要看的话你只能看这个
[02:20] 所以这个时候呢我们就想着能不能有什么办法在这里头把这幅图片提前给它保存好对不对保存到什么样呢我今天给各位提供的这个资料中应该也有一个你看这就是我们提前给它存起来的一个图提前存好了那我们现在如果说也能够把刚才我们的这个流程图给它存起来那将来我们在很多时候用户想去看你这个请假流程到底有哪些步骤啊
[02:50] 那你不能说你去直接看这个BPMN文件对吧你直接打开这个文件看吧啥意思呢就直接你打开这个文件你看吧你看有几个流程就有几个节点啊对吧那这个很显然显然是不合理的啊因为对于普通的用户而言他看这一堆东西他是受不了的对吧所以呢我们这个时候就想办法要把我们的这个图提前给他存好那要把这个图存好呢各位啊要参考的是我们第六个部分啊
[03:20] 第六个部分给各位介绍的这里边呢首先第一个你可以把这个BPMN文件改成我们的XML文件啊各位只要按我这个步骤去做就可以啊那大致的步骤是这样的啊比如说我这样做啊我呢点右键啊我们在这里头提前呢把这个文件给它改个名啊叫refact relam然后呢把这个名字我改成叫做XML文件啊改成它
[03:49] 然后refact这样的我就相当于啊把这个holiday.xml这个文件就创建好了然后呢我呢然后呢我下一个就需要做的工作是啊要做的工作就是我可以这个时候你比如说我把它关了啊我把它关了这个时候你再去打开你看到吗它的真正的这个格式就是一个就是一个xml文件啊所以呢所以呢我们这个时候如果要接着往后走的话那我们这个地方
[04:20] 可以啊打开它的这个Digram然后呢有一个叫做Show BPMN 2.0 Designer那这个时候我们就可以看到我们就可以看到啊它真正给我们生成了一个这样的图各位看见了吗就有一个这样的图了这个图要注意啊这个图呢我们同学自己在做的时候呢其实呢这个图如果有中文的话它不会显示为中文啊
[04:49] 它会显示出来是一堆乱码所以呢我们这个地方就需要对乱码进行调整对吧具体对乱码怎么调啊现在各位先别着急啊假设我们乱码已经调好了对吧那就已经是如果你你在这点右键对吧你用这个Diggram用小BPMN2.0Designer这种方式你这个时候打开它已经就是这个XML文件它已经给你解析成一个这样的图了对吧
[05:17] 那下一步我们就是希望把这个图要存好对不对那这个图要存好我们又怎么做呢那在这边呢有一个叫做叫做export to fail那我们这个时候就可以啊直接给它导出来啊你比如说我就直接这么做吧我先呢给它导到导到我就直接导到我们的这个这个这个今天的这个第二天啊导到第二天我这里不有个资料吗对吧这个资料里头有一个holo的png
[05:46] 我这个地方比如说来一个holy holiday比如说叫01它的扩展名各位自己可以去选取我们就是叫做png然后点ok这样的话这个图就已经导出来了然后我们可以回到我们的02叫做资料对吧这个时候我们再看一下这边刚才这个位置没找对吗我们再看一下然后我这个时候重新再看一下
[06:16] 我刚才放的到这个位置去了我们应该是02资料对吧然后呢在这个资料里头直接是这个目录然后我起一个名字就是holidayholiday01对吧叫点编辑OK那这样这个图就应该已经存过来了我们这个时候就可以看到了对吧叫holiday01编辑我们来看一下对吧填写请价申请单部门经理省总经理省
[06:44] 最后是我们的结束节点对吧这就是我们在这边啊呃直接通过这种方式给他生成出来的一个图片那这个图片呢如果后续我们还需要这个图片啊当然这个图片我就可以不要了对吧我这个都删了啊然后我们留着这个图这样的话我就可以一样的给他起成也叫做也叫做holiday啊因为这个名字和这个名字一样嘛对吧都叫holiday啊copy然后呢我这个时候再次回到我们的这个digram给他contra v拿到再来
[07:14] 这样我们就相当于实现了我们的这个Digrim里头的这个Xml和png的生成那一旦我们这个图片生成好了这时候呢我们再可以去refact rename把它的这个扩展名又怎么办啊再次给它改回来叫BPMN所以呢你发现ideal里头要去做这个工作其实相对来说稍微麻烦一些稍微麻烦一些
[07:42] Eclips底下直接按一下Ctrl S自然就可以保存成功所以我前面说了我们如果要去做工作流的开发其实用Eclips这个工具其实相对来说很多工作我们会变得更加简洁这是我们在这里头给各位刚才补充了一下我们如何去做我们的流程定义的BPMN文件以及我们的PNG的
[08:11] 真正的这个图片因为有了这张图片之后将来就是不管你到哪对吧你去打开它都是这样的对吧只要这台机器它可以打开这个图片那我们打开的时候就可以很自然的看到我们的真正的这个流程对吧这是我们关于我们的这个png文件和我们的这个bpm文件这样我们就基本上已经给它讲的比较全面一些了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何使用 Activiti Designer 工具创建 BPMN 流程图，并展示其生成的 .bpmn 和 .png 文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 第 6.1.1 节“什么是流程定义”，说明流程定义是基于 BPMN 2.0 标准，使用 activiti-explorer 或 activiti-eclipse-designer 插件进行建模，生成 .bpmn 和 .png 文件。
画面 2: 展示文件夹，包含四个与 Activiti 开发相关的视频教程文件。
画面 3: 显示桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面 4: 在 IntelliJ IDEA 中打开项目，展示 BPMN 流程图编辑器，包含 StartEvent、用户任务、审批任务和 EndEvent 等节点。
画面 5: 显示桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面 6: 鼠标右键点击桌面图标，弹出菜单。
画面 7: 显示桌面，有“传智播客”和“黑马程序员”的联合出品标志。
画面 8: 在 IntelliJ IDEA 中，右键点击“holiday.bpmn”文件，弹出菜单，选择“Analyze”。
画面 9: 在 IntelliJ IDEA 中，显示“holiday.xml”文件内容，包含 BPMN 2.0 的 XML 结构。
画面 10: 展示文件夹，包含“holiday.bpmn”、“holiday.png”和“使用IDEA开发activiti的配置.docx”文件。
画面 11: 在 Windows 系统中，打开“holiday.png”文件，显示流程图。
画面 12: 在 IntelliJ IDEA 中，右键点击“holiday.xml”文件，弹出菜单。
画面 13: 展示文件夹，包含“holiday.bpmn”、“holiday.png”和“使用IDEA开发activiti的配置.docx”文件。
画面 14: 展示课程 PPT 第 5.1.1 节“Activiti-Designer 使用”，说明在 Eclipse 或 IDEA 中安装 activiti-designer 插件后，画板中包含的节点类型，以及新建流程的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 9 的 XML 内容：
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:activiti="http://activiti.org/bpmn" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.omg.org/spec/BPMN/20100524/MODEL BPMN20.xsd">
  <process id="holiday" isClosed="false" isExecutable="true" name="请假流程" processType="None">
    <startEvent id="1" name="请假申请" />
    <userTask id="2" name="部门经理审批" activiti:assignee="liush" activiti:exclusive="true" activiti:formRef="1" />
    <userTask id="3" name="总经理审批" activiti:assignee="wangwu" activiti:exclusive="true" activiti:formRef="2" />
    <endEvent id="4" name="结束" />
    <sequenceFlow sourceRef="1" targetRef="2" />
    <sequenceFlow sourceRef="2" targetRef="3" />
    <sequenceFlow sourceRef="3" targetRef="4" />
  </process>
  <bpmn:di:di>
    <bpmn:di:plane id="BPMNPlane_1" bpmn:di:bounds="32.0,32.0,32.0,45.0" bpmn:di:orientation="0" bpmn:di:horizontalCount="1" bpmn:di:verticalCount="1" bpmn:di:width="80.0" bpmn:di:height="80.0">
      <bpmn:di:shape id="Shape_1" bpmn:di:bounds="32.0,32.0,32.0,45.0" bpmn:di:label="请假申请" />
      <bpmn:di:shape id="Shape_2" bpmn:di:bounds="55.0,85.0,85.0,255.0" bpmn:di:label="部门经理审批" />
      <bpmn:di:shape id="Shape_3" bpmn:di:bounds="55.0,85.0,85.0,255.0" bpmn:di:label="总经理审批" />
      <bpmn:di:shape id="Shape_4" bpmn:di:bounds="55.0,85.0,85.0,255.0" bpmn:di:label="结束" />
    </bpmn:di:plane>
  </bpmn:di:di>
</definitions>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4: BPMN 流程图结构：
- StartEvent → “填写请假申请”
- “填写请假申请” → “部门经理审批”
- “部门经理审批” → “总经理审批”
- “总经理审批” → EndEvent

画面 14: PPT 标题“5.1.1 Activiti-Designer 使用”，子标题“5.1.1.1 Palette（画板）”，列出画板中包含的节点类型：
- Connection——连接
- Event——事件
- Task——任务
- Gateway——网关
- Container——容器
- Boundary event——边界事件
- Intermediate event——中间事件

5) 不要评价画面美观，不要输出与课程无关的内容。
（以上内容已按要求输出）

