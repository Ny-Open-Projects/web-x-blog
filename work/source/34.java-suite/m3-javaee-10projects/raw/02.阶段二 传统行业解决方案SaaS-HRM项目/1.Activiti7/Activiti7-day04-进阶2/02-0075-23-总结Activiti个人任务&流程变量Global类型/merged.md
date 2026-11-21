# 23-总结Activiti个人任务&流程变量Global类型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day04-进阶2
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day04-进阶2\23-总结Activiti个人任务&流程变量Global类型_【海量资源尽在 ubkz.com】.mp4
- 时长 7分16秒（音频 436s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 那下面我们一起对于我们这一次课程所介绍内容给各位简单做一个总结那这次课程主要是我们首先给各位讲了我们的这个任务分配对吧任务分配我们在这里面给他讲了有固定分配方式对吧而我们还有这个表达式对吧通过UEL表达式的方式来实现我们的这个实现我们的这个任务执行人的这个分配
[00:29] 除了这一点呢我们这边还有一种就是通过监听器的方式来实现我们的这个任务分配对吧这也是一种方式啊那如果用监听器的方式的话我们要注意啊我们要去实现的是task listen的这个接口对吧好我们当我们把这个任务分配完了我们就可以去查询当前用户的具体的任务对吧那这一点其实不是什么新的内容啊因为我们在前面
[00:56] 早期介绍的时候也给用户也给讲过如何去查询用户的任务对吧主要是通过Task Service里边去Create Task Query这样我们就可以查询去设置我们查询的一些条件最终来查询我们的任务那查询完任务之后我们就可以办理任务办理任务了也不是什么新的支点那我们可以通过Task Service的Complete方法
[01:24] 里头去写上我们的task任务的ID对吧就可以完成任务啊这是关于过程任务这一块内容的指点啊那后面我们又给各位介绍了就是我们的这个流程变量对吧什么是流程变量对吧那我们为什么要通过为什么要设置流程变量对吧流程变量就是我们在这个流程啊在执行过程中必须要用到的一个量啊这个量呢
[01:50] 这个流程变量呢将来不是说什么内容都都可以存放到我们的这个流程变量中是跟我们的跟我们的这个activity的这个流程定义啊完全相关联的这样的一些变量我们呢才有必要放到我们的这个流程变量中啊那如果说我们的业务系统将来有一些值要存放的话那很明显那样的一些值不适合放在我们的流程变量中来进行存储啊
[02:18] 所以说我们这边也给各位特别整洁了一下就是我们业务系统将来如果里头有数据的话我们应该保存的话由我们的业务系统来负责它的存储以及查询而我们activity只是设置流程变量只是为了我们的流程执行的需要而创建然后我们下一个就给各位讲到了流程变量既然有变量那变量的数据类型就应该介绍一下对吧有这样的一些数据类型
[02:48] 这些类型的其中我们特别关注的一点就是这个serisable对吧那它主要就是存放POJO的时候我们这个POJO要去实现一个serisable接口既然变量的类型说清楚了那下一步我们来介绍就是我们的变量的作用欲我们包括有global类型的变量和我们的local局部变量后面我们又介绍了这个变量具体怎么去用对不对第一种就是我们
[03:18] 要去设置我们的流程变量那设置的时候我们主要是通过我们的这个assign这个地方任务执行人你可以设置除了这一点呢我们在连线上面也可以进一步去设置我们的这个UEL表达式对吧像我们在这个地方就设置了一个取我们用UEL表达式去取holiday这个对象的Numbo属性对吧然后再去看它是否大于3对不对
[03:46] 如果大于商那这个条件这个线上的这个条件就是去是去那这个这个节点才会执行如果是force那这个节点就不会被执行是这个意思好这是我们变量的使用方法于是后面呢我们就给各位讲了具体到底怎么样来用对不对具体怎么样来用呢这就是刚才我们在这边给各位看到的这个流程这个流程呢在这里面它就允许有多过分支的结构了对吧好
[04:15] 这是我们的这个global类型的变量具体怎么去设置在这个连线上设置我们的条件主要就是去指定它的这个condition的去值对吧condition在里面去设置我们的条件当设置好条件之后下一步就是应该我们什么时候给这个连线上面的这个变量负值的问题对不对那要负值的话我们这边给各位介绍了四种方式一个就是通过我们的这个
[04:44] 启动流程实例的时候在这个地方关键点就在于这一行代码start process use by key的时候指定它的第二个参数第二个参数就是我们真正所对应的这个变量的key和value第二种方式就是我们也可以在实现我们任务办理的时候指定第二个参数这也是一种还有一种就是第三种方式通过我们的这个流程实例的ID
[05:13] 直接在runtime Service通过setValue的方式来设置当然如果要设置多过参数的话我们用setValue支这个方法第二个参数其中是一个卖户集国里头存多过keyValue建制队我们还有第四种方式来设置我们的流程变量这种方式就是通过我们当前的任务来执行来设置那就是通过我们的任务的
[05:43] 任务的ID第二个参数是我们任务就是我们的这个流程变量的名字第三个参数就是我们的这个value值这个方式也是只能设置一个key value对吧如果有多过流程变量要设置值的话那我们第二个参数用setValueBuds这个方法第二个参数给定一个map激活这种方式就可以了对吧这是我们基本上给各位讲过的这个全局变量将来我们
[06:12] 要去复制的话这四种方式都可以复制后面我们又给他介绍了一下我们的这个注意事项以及背后所操作的数据库表对吧那主要是SATRU variable表以及我们的这个SATHIVR instance这个表这是我们的流程变量的表这是历史记录对吧完了如果我们这个设置的变量是一个PUGO类型的话那我们对应的其实
[06:41] 这个表里要真正存储的是一个serivable类型的变量对应的变量的值就需要到我们的GE ACTGENERATEBITER RATE这个表中去找对吧就可以找到这个变量真正所对应的值总体上呢这是我们这次课程给各位所涉及到的主要的支点就是这样的主要包括一个是过程任务任务部分另外一个就是我们的流程变量部分对吧
[07:11] 主要后面给各位介绍的是我们的全局变量

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中任务分配、流程变量类型及使用方法，包括 UEL 表达式、流程变量设置与查询。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 标题：2.1.1 固定分配
- 内容：在进行业务流程建模时指定固定的任务负责人。
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 2:
- 标题：2.1.1.1 UEL 表达式
- 内容：Activiti 使用 UEL 表达式，UEL 是 Java EE6 规范的一部分，UEL (Unified Expression Language) 即统一表达式语言。
- 内容：Activiti 支持两个 UEL 表达式：UEL-value 和 UEL-method。
- 内容：UEL-value 定义如下。

画面 3:
- 内容：Create: 任务创建后触发
- 内容：Assignment: 任务分配后触发
- 内容：Delete: 任务完成后触发
- 内容：All: 所有事件发生都触发
- 内容：java 逻辑 或 表达式；表达式参考上边的介绍的 UFL 表达式，这里主要介绍监听使用。

画面 4:
- 代码：
```java
@Test
public void findPersonalTaskList() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 任务负责人
    String assignee = "张三丰";
    // 创建TaskService
    TaskService taskService = processEngine.getTaskService();
    List<Task> list = taskService.createTaskQuery()
        .processDefinitionKey(processDefinitionKey)
        .includeProcessVariables().taskAssignee(assignee).list();
    for (Task task : list) {
        System.out.println("-------------");
        System.out.println("流程实例Id: " + task.getProcessInstanceId());
        System.out.println("任务负责人: " + task.getAssignee());
        System.out.println("任务名称: " + task.getName());
    }
}
```

画面 5:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。

画面 6:
- 标题：3.2 流程变量类型
- 表格：Table 15.9. Variable Types
- 表格内容：
| Type | name | Description |
|---|---|---|
| string | Value is threaded as a java.lang.String. Raw JSON text. | Value is threaded as a java.lang.String. Raw JSON text. |
| integer | Value is threaded as a java.lang.Integer. When writing, text. | Value is threaded as a java.lang.Integer. When writing, text. |
| short | Value is threaded as a java.lang.Short. When writing, text. | Value is threaded as a java.lang.Short. When writing, text. |
| long | Value is threaded as a java.lang.Long. When writing, text. | Value is threaded as a java.lang.Long. When writing, text. |
| double | Value is threaded as a java.lang.Double. When writing, text. | Value is threaded as a java.lang.Double. When writing, text. |
| boolean | Value is threaded as a java.lang.Boolean. When writing, text. | Value is threaded as a java.lang.Boolean. When writing, text. |
| date | Value is threaded as a java.util.Date. When writing, the text. | Value is threaded as a java.util.Date. When writing, the text. |
| binary | Binary variable, threaded as an array of bytes. The value stream. | Binary variable, threaded as an array of bytes. The value stream. |
| serializable | Serializable representation of a Serializable Java-object. | Serializable representation of a Serializable Java-object. |

画面 7:
- 标题：3.4 流程变量的使用方法
- 内容：第一步：设置流程变量
- 内容：第二步：通过 UEL 表达式使用流程变量
- 内容：> 可以在 assignee 处设置 UEL 表达式，表达式的值为任务的负责人。比如：${assignee}，assignee 就是一个流程变量名称。
- 内容：Activiti 获取 UEL 表达式的值，将流程变量 assignee 的值，作为任务的负责人进行任务分配。
- 内容：> 可以在连线上设置 UEL 表达式，决定流程走向。
- 内容：比如：${price>=10000} 和 ${price<10000}；price 就是一个流程变量名称，uel 表达式结果类型为布尔类型。
- 内容：如果 UEL 表达式是 true，要决定 流程执行走向。

画面 8:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 9:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 10:
- 展示了流程图：StartEvent → 任务处理节点 → 任务处理节点 → EndEvent。
- 任务处理节点之间有连线，标注了条件表达式：${holiday.num==1}。
- 展示了属性面板：Name: 任务处理节点, Assignee: 张三丰, Multi Instance: false。

画面 11:
- 代码：
```java
Map<String, Object> variables = new HashMap<String, Object>();
// 变量名num，变量值是holiday.getNum()，变量名也可以是一个对象
variables.put("num", holiday.getNum());

RuntimeService runtimeService = processEngine.getRuntimeService();
ProcessInstance processInstance = runtimeService
    .startProcessInstanceByKey(processDefinitionKey, variables);

System.out.println("流程实例Id: " + processInstance.getProcessInstanceId());
```
- 说明：startProcessInstanceByKey(processDefinitionKey, variables) 流程变量作用域是一个流程实例，流程变量使用 Map 存储，同一个流程实例设置 map 中 key 相同，后者覆盖前者。

画面 12:
- 代码：
```java
public void setGlobalVariableByExecutionId() {
    // 当前流程实例执行 id，通常设置为当前执行的流程实例
    String executionId = "2681";

    RuntimeService runtimeService = processEngine.getRuntimeService();
    Holiday holiday = new Holiday();
    holiday.setNum(3);

    // 通过流程实例 id 设置流程变量
    runtimeService.setVariable(executionId, "holiday", holiday);

    // 一次设置多个值
    // runtimeService.setVariables(executionId, variables)
}
```

画面 13:
- 代码：
```java
TaskService taskService = processEngine.getTaskService();
Holiday holiday = new Holiday();

// 通过任务设置流程变量
taskService.setVariable(taskId, "holiday", holiday);
// 一次设置多个值
// taskService.setVariables(taskId, variables)
```
- 注意：任务必须是当前待办任务，如果任务已经结束，报错。

画面 14:
- 内容：设置流程变量会在当前执行流程变量表插入记录，同时也会在历史流程变量表也插入记录。
- 内容：SELECT * FROM act_ru_variable #当前流程变量表
- 内容：记录当前运行流程实例可使用的流程变量，包括 global 和 local 变量
- 内容：Id: 主键
- 内容：Type: 变量类型
- 内容：Name: 变量名称
- 内容：Execution_id: 所属流程实例执行 id，global 和 local 变量都存储
- 内容：Proc_inst_id: 所属流程实例 id，global 和 local 变量都存储
- 内容：Task_id: 所属任务 id，local 变量存储
- 内容：Bytearray_: serializable 类型变量存储对应 act_ge_bytearray 表的 id
- 内容：Double_: double 类型变量值
- 内容：Long_: long 类型变量值
- 内容：Text_: text 类型变量值
- 内容：SELECT * FROM act_hi_varinst #历史流程变量表
- 内容：记录所有已创建的流程变量，包括 global 和 local 变量
- 内容：字段意义参考当前流程变量表。

