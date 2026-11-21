# 15-Activiti中单个流程实例的挂起与激活

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day03-进阶1
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day03-进阶1\15-Activiti中单个流程实例的挂起与激活_【海量资源尽在 ubkz.com】.mp4
- 时长 8分47秒（音频 528s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 也一起来编写一个代码来测试一下这个效果这个跟我们的这个全部挂起呢不太一样的是它这里头用到的是run time Service然后查到的是我们的这个process instance对吧而后面用这两个方法呢也用的是run time中的两个方法那这个大致也是比较简单对吧那我们可以一起再来测试一下这个效果那现在我们呢
[00:29] 就去把这个部分再去control v扔出一个比如说我在这后面跟上一个这跟上这是1这是2ok好现在我们这不是全部对吧叫做单个单个流程实例的挂取机合这个地方我们得到的就已经开始变成了叫做run time对吧run time Service变成它了
[00:56] 然后我们下面就可以把这个代码直接给它更新过来就可以通过我们的process engine.getRuntimeService这样我们就拿到一个RuntimeService对吧RuntimeService下一个我们就应该得到的是我们的流程实例的对象对不对流程实例对象那流程实例对象我们可以通过Runtime来进一步查比如说我们通过RuntimeService.query
[01:26] GreaterProcessInstanceQueue类然后进一步去调用它的方法比如说我们还是给一个ProcessInstanceByKey或者是你直接用ID都可以我们要是根据Key的话我们这个地方就可以叫做Holiday然后点是不是也可以通过它的SingleResult好这样查了我们就可以得到一个返回的结果
[01:55] 这个访费结果呢比如说我们这个地方就是叫做我们的process use times对吧当我们拿到这个process use times下一个我们就可以通过这个process use times对吧来调用来调用它的这个方法比如说这两个我都可以过于注意一下那现在我就可以通过我们的process use times点这时候我就可以得到它本身的这个get
[02:23] Process Instance的ID对吧或者是叫做Get ID对不对这就是我们的Process Instance ID这样我们就拿到了一个Strength叫做Process Instance ID对吧就拿到它了好当我们拿到这个之后还有一个就是这个System的状态我们还不知道对不对那这个状态我们可以怎么去得到呢一样的我们可以通过我们的这个
[02:51] 我们可以通过我们的这个run time Service点叫做age suspend对吧好我们可以通过我们来看一下这个时候我们可以通过process use我们来看一下process use去看一下它的这个点age suspend点age suspend对吧这样呢我们就可以拿到一个也是一个boolean
[03:19] 比如说叫做sourcepand对吧好那同样我们根据这个sourcepand以及我们的这个processingustosid就可以得到这个结果当然这里头的这个方法已经变了对吧我们这时候用的是runtimeservice里头的方法对不对那叫做叫做activeprocessingustosid对吧而我们的processingustosid上面已经有了对吧这个部分代表的是如果它已经是暂停状态
[03:49] 我们就把这个流程激活对吧但是这个地方激活的是具体的某一个流程对不对流程它已经被激活而这个ID也应该改成Process Instance ID对吧Process Instance ID当然这个地方这个ELL字里头的这个方法就也要变变成RuntimeService.叫做SuspenderProcess InstanceByID对吧那这条给定的也是我们的Process Instance
[04:19] Process Instance ID这样我们就完成了具体的某一个Process Instance那就是某一个流程实例真正将来它要挂起或者是要被激活对吧好我们也一起可以来看一下效果其实看一下我们这边有没有正在跑的一个实例各位可以看到其实我们有一个实例是叫做2501对不对我们再来运行看一下
[04:48] 我们挂起的是否为我们的2501的实例目前各位可以看到我们在执行完了这个易辅活标志之后我看一下这个地方有没有输出我们想要的这个结果呢这里头好像报了一个就是叫做long point exception好像是没有找到我们的这个记录似的
[05:26] 好我们看一下我们的这个实例啊是否已经启动好了啊比如说我可以执行一个一下这样的步骤啊比如说走对吧然后呢再把这个库整个创建出来对吧创建出来之后啊这样我们就相当于实例就没有了对吧我们可以呢再去把我们的这个再去把我们的这个早期的这个部署的工作啊对吧重新让它部署一次
[05:54] 我们做这个目标呢就是希望我们的这个实力啊我们的这个流程定义是不是再次部署对吧然后呢我们到这边再去启动一个我们的这个实力对吧好你们说这个是我们运行它其实就可以启动一个实力对不对那我们把这个实力启动之后其实我们就已经有实力了对吧在我们这是2501吧对吧那我们在有实力的情况下
[06:23] 然后再去执行这个实例的挂体与集合那这个部分我感觉应该就应该会有这个结果了它这边还是写的是long point exception那应该就是我这边这个查询这个是应该有问题的对吧process new stance这个地方这个是business key了是不是
[06:53] 这个条件对不起这个条件刚才我们在设置的时候没看清楚叫做process process instance他这边开头的就只有这几个process instance id这个地方我就干脆直接把我们的 id直接给进来对不对其实我这个地方刚才应该都有值我们可以看一下process instance id是2501对吧我这个应该是刚才写过了应该写成2501对不对
[07:23] 好我们这个时候再来看一下那2501看它是否会做我们的激活与挂起对不对那你看看目前它是激活状态所以它就被挂起了对吧好它现在已经是挂起的状态然后我再次运行它又会被重新激活对吧会看到这就是我们的激活与挂起的效果那激活将来才可以下一步下一步执行我们的流程这个时候才可以一步一步走
[07:52] 如果说你已经是暂停了那对不起这个时候你想部门经理整天去批那是肯定不允许的这是我们关于这个单个的流程实例的挂起与激活给各位演示到这里头其中整洁起来主要是这几个方法第一个就是我们应该将这个实例是否被挂起的这个状态要查询出来如果说已经被
[08:20] 挂起那我们就应该是想办法让它激活对吧如果说是已经被激活那我们就可以通过调用suspend的process instance by id来进一步开启它大概就是这样的如果是激活就应该是挂起如果是挂起了那我们就可以激活对吧调两个不同的方法就可以实现效果

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 代码操作 Activiti 工作流引擎，实现对流程实例的挂起与激活功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示一个名为 `suspendProcessInstance` 的测试方法，用于根据流程实例 ID 获取流程实例并判断其是否挂起，若挂起则激活，否则挂起。
画面2：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，用于获取流程引擎和运行时服务，查询流程定义并判断其是否挂起。
画面3：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，使用 `createProcessInstanceQuery` 查询流程实例。
画面4：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，调用 `runtimeService.createProcessInstanceQuery()` 方法并查看其方法签名。
画面5：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，判断流程定义是否挂起，并根据结果输出相应信息。
画面6：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，若流程实例挂起则激活，否则挂起。
画面7：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，执行后在控制台输出流程实例 ID 和流程定义 ID。
画面8：展示 MySQL 命令行工具中执行的 SQL 语句，用于创建名为 `activiti` 的数据库。
画面9：展示 `ActivitiDeployment.java` 文件的 `main` 方法，用于部署流程定义，通过 `repositoryService` 读取 `diagram` 文件夹下的 `holiday.bpmn` 文件并部署。
画面10：展示 `ActivitiStartInstance.java` 文件的 `main` 方法，用于启动流程实例，输出流程定义 ID、流程实例 ID 和活动 ID。
画面11：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，执行后在控制台输出异常信息，提示 `NullPointerException`。
画面12：展示 MySQL 命令行工具中执行的 SQL 语句，用于更新 `act_ru_execution` 表。
画面13：展示 `SuspendProcessInstance.java` 文件的 `main` 方法，使用 `runtimeService` 查询流程实例并判断其是否挂起。
画面14：展示 `suspendProcessInstance` 测试方法的完整代码，用于根据流程实例 ID 获取流程实例并判断其是否挂起，若挂起则激活，否则挂起。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例Id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例Id查询流程实例
    ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
            .processInstanceId(processInstanceId).singleResult();
    boolean suspend = processInstance.isSuspended();
    if(suspend){
        // 如果暂停则激活
        runtimeService.activateProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"激活");
    }else{
        // 如果激活则挂起
        runtimeService.suspendProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"挂起");
    }
}
```

画面2：
```java
public class SuspendProcessInstance2 {
    public static void main(String[] args) {
        // 获取流程引擎对象
        ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
        // 获取RuntimeService
        RuntimeService runtimeService = processEngine.getRuntimeService();
        // 查询流程定义对象
        ProcessDefinition processDefinition = repositoryService.createProcessDefinitionQuery()
                .processDefinitionKey("holiday").singleResult();
        // 判断当前流程定义的实例是否为暂停状态
        boolean suspended = processDefinition.isSuspended();
        String processDefinitionId = processDefinition.getId();
        if(suspended){
```

画面3：
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceBusinessKey("holiday").singleResult();
```

画面4：
```java
runtimeService.createProcessInstanceQuery()
```

画面5：
```java
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面6：
```java
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面7：
```java
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceBusinessKey("holiday").singleResult();
```

画面8：
```sql
drop database activiti;
create database activiti;
```

画面9：
```java
InputStream is = ActivitiDeployment.class.getClassLoader().getResourceAsStream("diagram");
ZipInputStream zipInputStream = new ZipInputStream(is);
```

画面10：
```java
ProcessInstance processInstance = runtimeService.startProcessInstanceByKey("holiday");
System.out.println("流程定义ID：" + processDefinition.getId());
System.out.println("流程实例ID：" + processInstance.getId());
System.out.println("活动ID：" + processInstance.getActivityId());
```

画面11：
```java
Exception in Thread "main" java.lang.NullPointerException
at line.15
```

画面12：
```sql
alter table act_ru_execution modify column id varchar(64) not null;
```

画面13：
```java
// 获取RuntimeService
RuntimeService runtimeService = processEngine.getRuntimeService();
// 查询流程实例
ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
        .processInstanceId("2501").singleResult();
// 判断当前流程定义的实例是否为暂停状态
boolean suspended = processInstance.isSuspended();
String processInstanceId = processInstance.getId();
if(suspended){
    // 如果暂停则激活
    runtimeService.activateProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"激活");
}else{
    // 如果激活则挂起
    runtimeService.suspendProcessInstanceById(processInstanceId);
    System.out.println("流程实例："+"processInstanceId"+"挂起");
}
```

画面14：
```java
@Test
public void suspendOrActiveProcessInstance() {
    // 流程实例Id
    String processInstanceId = "";
    // 获取RuntimeService
    RuntimeService runtimeService = processEngine.getRuntimeService();
    // 根据流程实例Id查询流程实例
    ProcessInstance processInstance = runtimeService.createProcessInstanceQuery()
            .processInstanceId(processInstanceId).singleResult();
    boolean suspend = processInstance.isSuspended();
    if(suspend){
        // 如果暂停则激活
        runtimeService.activateProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"激活");
    }else{
        // 如果激活则挂起
        runtimeService.suspendProcessInstanceById(processInstanceId);
        System.out.println("流程实例："+"processInstanceId"+"挂起");
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

