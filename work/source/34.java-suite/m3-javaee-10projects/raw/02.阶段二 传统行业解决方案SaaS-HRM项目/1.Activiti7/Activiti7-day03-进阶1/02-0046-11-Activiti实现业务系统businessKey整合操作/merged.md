# 11-Activiti实现业务系统businessKey整合操作

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\11-Activiti实现业务系统businessKey整合操作_【海量资源尽在 ubkz.com】.mp4
- 时长 13分14秒（音频 795s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 各位通过我们对于activity如何跟我们的业务系统进行关联刚才做的分析我们主要就是通过在我们的activity中添加一个business key这个业务标识这个业务标识其实我们刚才说了就主要对应的是我们的请假单的ID
[00:27] 这样就相当于我们的请假单的ID将来就可以真正对应到具体的某一个值而怎么样去做可以使得我们的这个business key也就是我们请假单类似的这种业务表的这个组件对吧怎么样添加到我们的activity中去那这个部分我们主要是借助于我们流程实例在启动的时候有用到一个叫做runtime对吧这个runtime Service
[00:56] 点start process用词同时by key那我们除了添加我们的这个process definition key除了添加这个之外呢我们还要再去添加一个就是我们的business key那这个business key就是我们对应的比如说如果是一个请假单的话那我们就要把这个请假单的ID号直接放入进来这样我们就可以来观测到这个效果那好现在呢我们可以一起来看一下真正啊
[01:26] 我们在操作的时候首先呢第一个要去看你的这个流程是否已经部署进来各位可以看到我们的这个流程都已经部署进来那我们流程部署进来下一个我们就可以去观察一下对吧我们的这个流程对应的我们本身这个流程就是流程本身的这个key是叫做holiday对吧因为我们说了每一套流程都有自己的唯一编号对吧那我们的一个编号就是叫做holiday
[01:54] 那好我们还有一个要去看的就是我们的这个ru is quotient对吧因为这个里头才真正会关联到我们的这个business key对不对目前是没有值的那下面呢我们就可以直接来启动一个流程对吧启动一个流程实例那好现在我们回到我们的这个代码部分那现在比如说我这样做那假如说我直接在这个地方把我们的这个类重新复制一个出来比如说我就是叫做
[02:24] 我们的BusinessBusiness Key的添加我们业务组件的添加OK这样我就加了一个新的类型来它的主要作用就是在启动我们的流程实例启动流程实例时同时我们还要做一个事情就是要添加进要添加进我们的Business Key
[02:52] 这就是我们这一次想完成的这个目标要完成这个目标我们这一次在这边呢一起来看一下应该怎么样做可以达到我们想要的这个效果那第一个步骤Process Engine这个是我们都这样做就不用去关注了那第二个我们主要是得到一个我们的Runtime Service得到Runtime Service对象我们通过这个Runtime Service呢就可以进一步去
[03:21] 进一步去得到我们去开启我们的流程实例对吧所以我们在这里头可以通过我们的这个processengine.getRuntimeService对吧这样我们就可以得到一个RuntimeService的这个对象对吧好这样我们就拿到了一个RuntimeService那下一步我们就可以进一步在这边通过RuntimeService去第三个步骤
[03:50] 那就是通过Runtime Service去准备启动我们的这个流程实例对吧那就是通过那就是叫做启动我们的这个流程实例但是呢在启动这个流程实例的时候我们同时还要指定什么呢同时还要指定同时还要指定我们的这个业务标识对吧那我们这个业务标识其实就是我们所说的这个Business Key对吧
[04:19] 就是我们所说的business key好那这个business key对于我们而言本身又是什么本身它本身呢它本身啊就是我们的这个请加单的ID请加单的ID这就是这个意思啊好那下面我们就可以来做这个启动工作啊那就是通过我们的这个run time Service去调用它的start process
[04:49] Unsponsored by key对吧而我们的这个流程实例它本身的流程的ID应该是叫做Polity对不对那现在我们其实就可以用这个方法来做这里头第一个是时均第二个是时均我们可以用这个方法那其中的第一个常数我们给各位解释一下第一个常数指的是是指
[05:18] 我们的这个流程实例本身所对应的这个流程定义或者叫流程定义的key流程定义的key那本身它就是一个唯一的对吧而我们的第二个常数又代表什么呢我们的第二个常数代表的是这个部分
[05:45] 这个就是我们真正所对应的这个业务标识business key就是作为它的这个第二个参数那第一个参数对于我们而言比较好写那就是把我们的holiday直接写过来对吧而第二个参数我们刚才看了它其实代表的就是我们的这个叫做business key对吧business key要注意的就是我们之前在启动一个流程实例的时候我们没有带上第二个参数那时候我们就只是跟上了我们的这个流程第一的key
[06:15] 那现在我们可以带上第二个参数带上第二个参数的话第二个参数指的是我们的business key而我们business key又是一个什么样的值这个就要去看你真正关联的那个请假单的ID对吧假如说比如说在这个里头我又还有新的一张表这个表里头将来有一个有一个我们的这个专门的请假单的表对吧那这个请假单的表里头将来可能包含有很多记录
[06:44] 其中有一条记录它的ID假如说是1001可以吧有一条记录有一条请假单它的ID是1001如果是这样的话那我们这边就直接应该把这个请假单的ID1001直接放到这里头来是这个意思所以我这里头1001其实就是请假单某一条记录某一条请假单的ID是这个意思好那这样我们就可以得到一个
[07:12] 得到一个对象对吧就是叫做processing instance对吧好我们就完成了我们的这个processing instance这个获取那下一步呢我们就可以进一步去输出一下比如说我在这里头输出我们的这个processing instance相关的这个实例processing instance相关的一些属性对吧这个就看你输出多少值了那现在我就可以直接呢来输出我们的pro
[07:42] process.users.我们可以看一下它其中就可以再次将我们的这个business key进一步输出我们这个时候最终这个business key是否已经真正的添加成功我告诉各位我们将来还要观察谁呢还要观察ru-exclusion这个表格看business key是否有值如果它真的有值
[08:12] 那就证明我们通过这个start process用词同时by key在第二个参数中跟着这个1001如果真的进到这个位置来了那证明我们通过这种方式是加入我们business key的一个有效方法对不对而将来如果说我们加入了一个business key将来我们希望把这个business key真正取得这个值呢
[08:40] 通过程序拿回来那我们主要就是通过Process Use同时调用它的Get Business Key这样呢我们又可以将这个业务业务组件重新再次拿回来那你想想将来我们的这个流程实例执行比如说已经执行到部门经理审批了对不对那部门经理审批到底审批的是某具体的哪一个员工的这个请假单那这个时候是不是就要
[09:08] 就要去查看请加单的这个信息才知道那你要查看请加单的信息就必须要知道请加单的这个ID对吧如果这种方法能够把流程实例中的这个business key真正给我拿出来的话那将来是我们拿的这个business key的真正的值再去回查我们的请加单就又可以把请加单的信息查出来所以呢这里头啊我们基本上啊就可以来运行
[09:38] 看一下这个结果是否可以达成我们想要的目标好现在我们跑一下结果一起来关注一下好现在各位可以看到我们真正获取出来的这个值就是叫做1001对不对那为什么是1001主要是我们在这里头刚才给进去的这个业务标识business key的值就是1001所以在这个地方就告诉了各位
[10:08] 用这种方式我们可以实现我们的这个business key的存对不对而用processing instance里头的get business key的这个方法就可以实现什么business key的这个取是不是所以说取出我们的这个business keybusiness key使用我们的这个方法就可以了使用我们的这个流程实例点get process instance
[10:37] get business key这个方法就可以完成我们的取出工作那我们还要观察一个问题就是什么就是我们最终你说已经存进去了对不对你说已经取出来了那最关键是我们还要到我们的这个RU-EXCUSE表中我们还要来刷一下看看这个表中的记录是否真的已经加入了我们的这个business key对不对各位
[11:08] 这个时候你就可以看到啊我们目前呢已经看到了这个流程实例2501的这个实例与我们的business key是1001的这个请假单的ID完全关联在一起了对吧好所以呢我们通过刚才这一段的这个测试啊我们基本上啊各位同学应该要掌握啊我们如果说
[11:35] 业务系统又能够跟我们的activity这25张表真正关联到一起的将来一个最为关键的点就是我们的business key这个部分比如说你关联请假单将来这里头存的就是请假单的ID假如说我关联的是一个调薪对吧是一个调薪的申请单那我们这个地方应该放的就是调薪的这个调薪申请单的那一条记录的ID是这个意思
[12:04] 那目前我们已经测完完整的这个效果各位呢我们再总结一下其实这一段主要告诉各位我们真正如果要把business key添加进来主要就是靠启动一个流程实例的时候我们用了这个第二个参数给进来的如果要取出来的话我们通过process use要用它的这个get business key的这个方法就可以实现这个效果而真正本质呢
[12:31] 我们再说一下这个本质本质主要就是通过我们activity的这张表对吧copy一下本质就是这张表这个表中的叫做businessbusiness p的字段对吧这个字段要存入我们的这个业务标识要存入我们的业务标识这个就是我们所谓的这个本质
[13:02] 好那我们关于关于这个business key而我们的这个activity怎么样去存以及怎么样去取这个问题给各位就介绍到这里头

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Activiti 工作流引擎中如何通过 businessKey 启动流程实例，并演示了相关的 Java 代码和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Java 代码，用于查询正在运行的流程实例，获取其 ID、所属流程定义 ID 和是否执行完成状态。
画面2：展示 PPT 内容，说明开始一个任务时会向 act_ru_task 和 act_hi_actinst 表插入记录。
画面3：展示 PPT 内容，解释 businessKey 的概念及其在 Activiti 中的存储方式，并展示数据库表中 businessKey 的值。
画面4：展示 IntelliJ IDEA 中的项目结构，包含 src、resources 等目录，以及 BusinessKeyAdd.java 文件。
画面5：展示 BusinessKeyAdd.java 文件的初始状态，仅包含 package 和 class 声明。
画面6：展示在 BusinessKeyAdd.java 中调用 ProcessEngine 的 getRuntimeService() 方法，弹出方法签名提示。
画面7：展示在 BusinessKeyAdd.java 中调用 RuntimeService 的 startProcessInstanceByKey() 方法，准备启动流程实例。
画面8：展示 MySQL Workbench 中的 SQL 语句，用于删除 activiti 数据库并创建新数据库。
画面9：展示在 BusinessKeyAdd.java 中调用 startProcessInstanceByKey() 方法，第一个参数为流程定义 key "holiday"。
画面10：展示在 BusinessKeyAdd.java 中调用 startProcessInstanceByKey() 方法，第二个参数为 businessKey "1001"。
画面11：展示在 BusinessKeyAdd.java 中导入 Spring 相关的 XML Schema。
画面12：展示在 BusinessKeyAdd.java 中完成代码编写，包含启动流程实例和打印 businessKey 的逻辑。
画面13：展示在 BusinessKeyAdd.java 中运行成功，终端输出了流程实例的 businessKey 值。
画面14：展示 PPT 内容，再次强调 businessKey 的作用，并展示数据库表中 businessKey 的值。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void queryProcessInstance() {
    // 流程定义key
    String processDefinitionKey = "holiday";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    List<ProcessInstance> list = runtimeService
            .createProcessInstanceQuery()
            .processDefinitionKey(processDefinitionKey)
            .list();

    for (ProcessInstance processInstance : list) {
        System.out.println("------------------------");
        System.out.println("流程实例Id：" + processInstance.getProcessInstanceId());
        System.out.println("所属流程定义Id：" + processInstance.getProcessDefinitionId());
        System.out.println("是否执行完成：" + processInstance.isEnded());
    }
}
```

画面2：
```sql
SELECT * FROM act_ru_task;  # 任务历史表，记录所有任务
SELECT * FROM act_hi_actinst; # 活动历史表，记录所有活动
```

画面3：
```java
// 根据流程定义的key启动一个流程实例
ProcessInstance processInstance = runtimeService
        .startProcessInstanceByKey(processDefinitionKey,
        businessKey);
```

画面4：
```
src
├── main
│   └── java
│       └── com
│           └── ithema
│               └── day03
│                   └── activiti
│                       └── BusinessKeyAdd.java
└── resources
    ├── diagram
    │   ├── holiday.hpmn
    │   ├── holiday.png
    │   └── holiday.bpmn
```

画面6：
```java
RuntimeService runtimeService = processEngine.getRuntimeService();
```

画面7：
```java
runtimeService.startProcessInstanceByKey();
```

画面8：
```sql
1 drop database activiti;
3 create database activiti;
```

画面9：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", 
```

画面10：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", "1001");
```

画面11：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-3.0.xsd
        http://www.springframework.org/schema/tx
        http://www.springframework.org/schema/tx/spring-tx-3.0.xsd">
```

画面12：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday", "1001");
System.out.println(processInstance.getBusinessKey());
```

画面13：
```java
System.out.println(processInstance.getBusinessKey());
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
标题：开始一个任务，不仅在 act_ru_task 表插入记录，也会在历史任务表插入一条记录，任务历史表的主键就是任务 id，任务完成此表记录不删除。
表格数据：
| 表名 | 说明 |
|------|------|
| act_ru_task | 任务历史表，记录所有任务 |
| act_hi_actinst | 活动历史表，记录所有活动 |

画面3：
标题：Businesskey：业务标识，通常为业务表的主键，业务标识和流程实例一一对应。
表格数据：
| ID | REV | PROC_INST_ID | BUSINESS_KEY | PARENT_ID | PROC_DEF_ID |
|----|-----|--------------|---------------|-----------|-------------|
| 1401 | 1 | 1401 | 1001 | (NULL) | purchasingFlow:1.1:1 |
| 1501 | 1 | 1501 | 1001 | (NULL) | purchasingFlow:1.1:1 |

画面14：
标题：Businesskey：业务标识，通常为业务表的主键，业务标识和流程实例一一对应。
表格数据：
| ID | REV | PROC_INST_ID | BUSINESS_KEY | PARENT_ID | PROC_DEF_ID |
|----|-----|--------------|---------------|-----------|-------------|
| 1401 | 1 | 1401 | 1001 | (NULL) | purchasingFlow:1.1:1 |
| 1501 | 1 | 1501 | 1001 | (NULL) | purchasingFlow:1.1:1 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

