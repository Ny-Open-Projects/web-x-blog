# bpmn 打开是 XML 不是图：IDEA 里导出流程 png 的土办法

画完 `holiday.bpmn`，想把这张请假流程图发给业务同事看，双击却打不开，换编辑器打开是一屏 XML。可课程资料里偏偏躺着一张 `holiday.png`，打开就是完整的流程图。图从哪来？这一步把 bpmn 与 png 的关系，以及 IDEA 里没有一键导出时的土办法讲清楚。

## 先给结论

- `.bpmn` 的本体是 XML，图形只是设计器插件解析后的展示；换台没装插件的机器，看到的永远是 XML。
- 引擎运行只认 bpmn；png 是给人看的流程图快照，价值在业务传阅和后续查询流程图资源。
- Eclipse 里保存即自动生成 png；IDEA 的设计器没有这个能力，只能绕：复制 bpmn 改后缀为 `.xml`，右键 Diagrams 选 Show BPMN 2.0 Designer 打开图形，Export to file 导出 png，再把后缀改回 `.bpmn`。
- 导出的 png 与 bpmn 同名成对（`holiday.bpmn` 与 `holiday.png`），后续部署时一起放进引擎。

## 一、为什么双击打不开

先做个实验验证 bpmn 的本质：把 `holiday.bpmn` 复制一份，通过 Refactor 的 Rename 把副本后缀改成 `.xml`，再打开，看到的就是一段段标签。节点、连线、属性全在 `process` 元素里：

```xml
<process id="holiday" isClosed="false" isExecutable="true"
         name="请假流程" processType="None">
  <startEvent id="1" name="开始"/>
  <userTask id="2" name="部门经理审批" activiti:assignee="lisi"/>
  <userTask id="3" name="总经理审批" activiti:assignee="wangwu"/>
  <endEvent id="4" name="结束"/>
</process>
```

文件末尾还有一节记录每个图形坐标尺寸的 BPMNDiagram 信息。装了设计器插件的 IDEA 读到这些内容后，按坐标把 XML 渲染成图展示出来，插件只负责视图，不负责生成图片文件。所以把 bpmn 拷到任何地方它都不是图，这是文件格式决定的，与机器无关。

## 二、土办法导出 png

思路一句话：借设计器的视图能力，把渲染结果另存为图片。完整动作五步：

```mermaid
flowchart LR
    A["复制 holiday.bpmn 备份"] --> B["副本改名 holiday.xml"]
    B --> C["Diagrams 菜单打开 Show BPMN 2.0 Designer"]
    C --> D["Export to file 另存 holiday.png"]
    D --> E["后缀改回 bpmn"]
```

这条链路的本质是借 xml 后缀让 IDEA 按图形方式渲染文件，再把渲染结果另存成图片。对应的操作要点：

1. 先复制一份 `holiday.bpmn` 留作备份，后面会解释为什么这一步不能省。
2. 对副本执行 Refactor 里的 Rename，改成 `holiday.xml`。改的只是名字，内容不变。
3. 右键 `holiday.xml`，在 Diagrams 菜单里选 Show BPMN 2.0 Designer，XML 被解析成流程图。节点名是中文时此时可能显示为乱码，处理方式见下一篇。
4. 设计器工具栏点 Export to file，在 Save diagram as image 对话框里选好目录，文件名 `holiday`，格式选 png，确认导出。
5. 把工作文件的后缀再改回 `.bpmn`，保持流程定义文件的原样。

几个操作细节值得留意：导出目录建议直接选 bpmn 所在的 diagram 目录，保证两个文件天然成对、路径一致；文件名必须与 bpmn 同名，只留后缀差异，部署与查询流程图资源都按名字对应，名字对不上后续就会扑空；格式在 png 与 jpg 之间选 png，无损且不失真，缩放查看时不发糊。备份的作用也在这一步之后体现：整条链路只在副本上操作，原件从头到尾没被动过，中途出了任何岔子，删掉副本重来即可，原件不会陪葬。

导出后目录里就是成对的 `holiday.bpmn` 与 `holiday.png`。png 放到任何一台能看图的机器上都直接可读，业务方想确认请假流程有哪几步，看图即可，不必逼他们读 XML。

## 三、png 与 bpmn 各自的角色

| 文件 | 内容 | 服务对象 | 引擎是否必需 |
|---|---|---|---|
| `holiday.bpmn` | XML 流程定义 | 引擎解析执行 | 必需 |
| `holiday.png` | 流程图图片 | 人查看、业务传阅 | 非必需 |

部署时两个文件成对进入引擎，代码里能看到它们的对应关系（部署细节下一篇展开）：

```java
Deployment deployment = repositoryService.createDeployment()
        .addClasspathResource("diagram/holiday.bpmn")  //添加 bpmn 资源
        .addClasspathResource("diagram/holiday.png")   //添加 png 资源
        .name("请假申请单流程")
        .deploy();
```

png 不部署引擎也能跑：查询流程图资源时，Activiti 可以按 bpmn 里的坐标信息现画一张。带上 png 的意义是让用户看到与设计器里一致的图，而不是引擎自动生成的简版。

要不要带 png，可以按展示要求倒推：只要求流程能跑，png 可以省；要求审批页面显示与设计器一致的图，或者后续要按流程实例查询流程图资源，就把 png 一起部署。两个文件加起来不过几十 KB，实际项目里基本都是成对带上，省一张图省不出收益，反而埋下线上展示与设计稿不一致的坑。

## 常见误区

- **以为改后缀就改了文件类型。** Rename 只动名字，`.xml` 副本的内容与 bpmn 完全相同，改回后缀也无损。
- **把 png 当部署必需品。** 缺 png 部署照常成功，流程照常运行，只是流程图展示退回引擎自动生成版。
- **不备份直接改后缀操作。** 中途一旦在乱码状态下保存或导出，文件里的中文可能被写坏，有备份才有退路。
- **在 Eclipse 里找同样的五步。** Eclipse 版设计器按 Ctrl+S 保存就自动生成同名 png，不需要这套绕行动作，两边的操作别混用。

## 面试可能被问到的问题

1. 面试官追问：「bpmn 和 png 是什么关系，部署时必须都给吗？」
   答：bpmn 是流程定义本体，引擎解析执行只靠它；png 是流程图的图片形式，供人查看。png 非必需，缺了引擎会按 bpmn 的图形坐标自动生成流程图，部署两个文件是为了展示效果与设计图一致。

2. 面试官追问：「为什么 IDEA 画的流程图导出 png 要改后缀绕一圈？」
   答：IDEA 的设计器插件只提供 XML 的可视化预览，没有像 Eclipse 那样保存即出图的功能。借 Diagrams 菜单把 bpmn 当 xml 渲染出来，再用 Export to file 存图，绕过能力缺口。

3. 面试官追问：「用户想看流程走到哪一步了，应该给他看什么？」
   答：运行中节点高亮的流程图。数据来自运行时表，图可以取部署时存入的 png 资源，或由引擎按坐标生成，再把当前活动节点标红后展示给前端。

4. 面试官追问：「bpmn 文件里的图形坐标信息有什么用？」
   答：它记录每个节点与连线在画布上的位置和尺寸，设计器靠它还原图形视图，引擎靠它自动生成流程图。删掉这节不影响流程执行，但图会乱或画不出来。

## 配套资料

- 部署代码所在工程：`materials/code/02/Activiti7-day02-工作流使用/代码/代码/`
  （`ActivitiDeployment.java` 中保留 bpmn 与 png 成对部署的真实写法，包名已改为 `com.example`）
- 资料包未含 `holiday.bpmn` 与 `holiday.png` 原件，导出步骤为按本课实录整理。
