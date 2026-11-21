# 06-IDEA中制作流程定义png文件的中文乱码问题

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day02-工作流使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day02-工作流使用\06-IDEA中制作流程定义png文件的中文乱码问题_【海量资源尽在 ubkz.com】.mp4
- 时长 3分40秒（音频 220s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们就给各位补充一下啊刚才我们在这里头说了如果你有中文的话你如果不去做任何的调整呢那这个时候你生成看见的这个图啊最终这个PNG图片啊它表现出来这里头肯定是乱码啊那我们怎么去调整呢这个给各位介绍一下啊那调整具体的这个操作步骤啊各位可以参考啊我们这个里头这个PNG图片生成啊
[00:29] 图片生成这是Eclipse工具底下的这是我们ideal里头的刚才这个步骤我其实给各位都演示了如果我们要真正生成可以看到没有乱码的情况下这个地方我们要这样做具体你也可以参考这个步骤这个步骤就这样了首先你去看一下你这个ideal工具你安装的位置在哪比如说我这个时候点它的属性对吧那这时候打开它的文件所在的位置
[00:57] 好那我是安装在这个目录下啊那在这个目录下这边就有一个64位的因为我是这个64位的机器啊然后我在我在这个时候呢就可以直接点打开打开打开这个文件啊那就打开了打开之后要注意这最后的一行是我自己添加的是我自己添加的那之前其实是没有这一行的我们只要把这一行给它加上就可以了前面不要不要有空格啊就是后面不要空格就这一段
[01:26] 那加完我们呢只要重新再去启动一下我们的这个idea工具然后呢你这个时候再进来那我们基本上就可以把这个乱码问题给它解决了当然我要说一下就是有些同学呢他在加的时候我告诉你他一会儿还会你这样做完之后他还有乱码我告诉你为什么产生的是因为他提前一上来把这个BPMMM这个文件呢他提前一上来了他就把这个文件啊给他
[01:56] 给它改成了.xml文件然后呢也用我们的这个前面的这个操作步骤啊它也是用这个xml文件去打开最后你会发现它的这个时候真正它在打开的时候我告诉你它打开的时候它的这个文件就不再是一个就不再是一个我们的这个正常的这个汉字明白是吧就是说它已经把这个东西搞成乱乱了它已经乱了
[02:23] 已经是乱码了然后呢你说我调一下Utl吧这个时候它还能变得回来吗就变不回来了这是这个原因啊所以我为什么开始说我们要把这个文件先提前怎么办呢给它备份一下你给它备份一下然后呢你这个时候再去用的时候那它肯定就是正常的明白意思吧你比如说这是一份正常的这个文件它里头汉字本来就还没有变成乱码我说的这个意思大概就是呢有些时候它已经搞成乱码了然后说
[02:53] 他去调一下Utl吧调完之后这个时候他希望调完之后回来回到这边呢然后又给他变回来了那是不可能的啊所以有同学来将来可能会出现这个问题啊就是他调完了还是有乱码那我的意见就是啥呢你先把好的这份文件先提前给他考考备一份一旦他我们完的时候相对于把他给他完成乱码了然后呢你将来再把这份好的文件放进来那这个过程呢你再去再去啊当这个参数一旦调完
[03:20] 重启我们的Ideal工具你再把这个文件放进来然后再去改XML再去导致PNG文件那这个过程呢就应该是通畅了不会有乱码问题好这是我们在这个地方呢就是生成我们PNG图片这个乱码的小问题怎么去解决

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

